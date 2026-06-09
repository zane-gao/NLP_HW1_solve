from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.aggregate_summary import load_thresholds, to_bool_str
from scripts.common import mcnemar_exact_p_value, read_jsonl


def parse_score_sets(raw_items: Sequence[str]) -> Dict[str, str]:
    score_sets: Dict[str, str] = {}
    for item in raw_items:
        if "=" not in item:
            raise ValueError(f"score set must be mode=path, got: {item}")
        mode, path = item.split("=", 1)
        score_sets[mode.strip()] = path.strip()
    return score_sets


def write_csv(path: str | Path, rows: Iterable[Dict[str, Any]], fieldnames: Sequence[str]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def summarize_mode(
    *,
    repair_mode: str,
    problem_rows: Dict[str, Dict[str, Any]],
    score_rows: List[Dict[str, Any]],
    thresholds: Dict[str, float],
    task_type: str,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    pair_bucket: Dict[Tuple[str, str, str], Dict[str, Dict[str, int]]] = defaultdict(dict)
    models_set = set()
    for row in score_rows:
        is_correct = row.get("is_correct")
        if is_correct not in [0, 1]:
            continue
        problem = problem_rows.get(row["qid"])
        if not problem:
            continue
        if task_type != "all" and problem.get("task_type") != task_type:
            continue
        key = (row["model_id"], row["prompt_id"], problem["subtype_id"])
        pair_bucket[key].setdefault(problem["pair_id"], {})[problem["variant"]] = int(is_correct)
        models_set.add(row["model_id"])

    cell_rows: List[Dict[str, Any]] = []
    b_count: Dict[Tuple[str, str], int] = defaultdict(int)
    for (model_id, prompt_id, subtype_id), pair_map in sorted(pair_bucket.items()):
        paired = [(v["control"], v["perturbed"]) for v in pair_map.values() if "control" in v and "perturbed" in v]
        if not paired:
            continue
        n = len(paired)
        control_err = sum(1 for c, _ in paired if c == 0)
        trigger_err = sum(1 for _, p in paired if p == 0)
        fr_control = 100.0 * control_err / n
        fr_trigger = 100.0 * trigger_err / n
        delta_pp = fr_trigger - fr_control
        n01 = sum(1 for c, p in paired if c == 1 and p == 0)
        n10 = sum(1 for c, p in paired if c == 0 and p == 1)
        p_value = mcnemar_exact_p_value(n01=n01, n10=n10)
        a_flag = delta_pp >= float(thresholds["A_delta_err_pp"]) and p_value < float(thresholds["A_p_value"])
        if a_flag:
            b_count[(model_id, subtype_id)] += 1
        cell_rows.append(
            {
                "repair_mode": repair_mode,
                "model_id": model_id,
                "prompt_id": prompt_id,
                "subtype_id": subtype_id,
                "FR_control": f"{fr_control:.4f}",
                "FR_trigger": f"{fr_trigger:.4f}",
                "delta_pp": f"{delta_pp:.4f}",
                "A_flag": to_bool_str(a_flag),
                "B_flag": "0",
                "p_value": f"{p_value:.6f}",
                "pair_count": str(n),
                "n01": str(n01),
                "n10": str(n10),
            }
        )

    min_prompt_count = int(thresholds["B_min_prompt_count"])
    subtype_model_b: Dict[str, set] = defaultdict(set)
    for row in cell_rows:
        b_flag = b_count[(row["model_id"], row["subtype_id"])] >= min_prompt_count
        row["B_flag"] = to_bool_str(b_flag)
        if b_flag:
            subtype_model_b[row["subtype_id"]].add(row["model_id"])

    min_model_count = int(thresholds["C_min_model_count"])
    subtype_to_deltas: Dict[str, List[float]] = defaultdict(list)
    for row in cell_rows:
        subtype_to_deltas[row["subtype_id"]].append(float(row["delta_pp"]))

    c_rows: List[Dict[str, Any]] = []
    for subtype_id in sorted(subtype_to_deltas):
        deltas = subtype_to_deltas[subtype_id]
        model_cnt = len(subtype_model_b[subtype_id])
        c_rows.append(
            {
                "repair_mode": repair_mode,
                "subtype_id": subtype_id,
                "mean_delta_pp": f"{sum(deltas) / len(deltas):.4f}",
                "models_with_B": str(model_cnt),
                "total_models": str(len(models_set)),
                "C_flag": to_bool_str(model_cnt >= min_model_count),
            }
        )
    return cell_rows, c_rows


def build_acceptance_rows(c_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    by_mode_subtype = {(row["repair_mode"], row["subtype_id"]): row for row in c_rows}
    checks: List[Tuple[Sequence[str], str, float, str]] = [
        (["script_numeric"], "simp_trad", 5.0, "simp_trad 修复后平均 delta_pp < 5 且 C 消失"),
        (["sccp_strict", "field_aware"], "simp_trad", 5.0, "SCCP 保持 simp_trad 消解"),
        (["sccp_strict", "field_aware"], "ocr_confusable", 15.0, "ocr_confusable 在严格 SCCP 后平均 delta_pp < 15 且 C 消失"),
    ]
    for modes, subtype, threshold, description in checks:
        row = next((by_mode_subtype.get((mode, subtype)) for mode in modes if by_mode_subtype.get((mode, subtype))), None)
        if not row:
            rows.append({"check": description, "actual_delta_pp": "", "C_flag": "", "pass": "0"})
            continue
        actual = float(row["mean_delta_pp"])
        passed = actual < threshold and row["C_flag"] == "0"
        rows.append(
            {
                "check": description,
                "actual_delta_pp": f"{actual:.4f}",
                "C_flag": row["C_flag"],
                "pass": to_bool_str(passed),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="比较 baseline 与 HDR 修复后的 A/B/C 效应")
    parser.add_argument("--problem-bank", default="data/problem_bank_focus3_main.jsonl")
    parser.add_argument("--experiment-config", default="configs/experiment.yaml")
    parser.add_argument("--task-type", choices=["all", "extraction", "classification"], default="extraction")
    parser.add_argument("--score-set", action="append", required=True, help="mode=score_jsonl_path，可重复")
    parser.add_argument("--cell-output", default="runs/repair_summary_cells.csv")
    parser.add_argument("--c-output", default="runs/repair_c_summary.csv")
    parser.add_argument("--acceptance-output", default="runs/repair_acceptance.csv")
    args = parser.parse_args()

    thresholds = load_thresholds(args.experiment_config)
    problem_rows = {row["qid"]: row for row in read_jsonl(args.problem_bank)}
    all_cell_rows: List[Dict[str, Any]] = []
    all_c_rows: List[Dict[str, Any]] = []

    for repair_mode, path in parse_score_sets(args.score_set).items():
        cell_rows, c_rows = summarize_mode(
            repair_mode=repair_mode,
            problem_rows=problem_rows,
            score_rows=read_jsonl(path),
            thresholds=thresholds,
            task_type=args.task_type,
        )
        all_cell_rows.extend(cell_rows)
        all_c_rows.extend(c_rows)

    write_csv(
        args.cell_output,
        all_cell_rows,
        [
            "repair_mode",
            "model_id",
            "prompt_id",
            "subtype_id",
            "FR_control",
            "FR_trigger",
            "delta_pp",
            "A_flag",
            "B_flag",
            "p_value",
            "pair_count",
            "n01",
            "n10",
        ],
    )
    write_csv(
        args.c_output,
        all_c_rows,
        ["repair_mode", "subtype_id", "mean_delta_pp", "models_with_B", "total_models", "C_flag"],
    )
    acceptance_rows = build_acceptance_rows(all_c_rows)
    write_csv(args.acceptance_output, acceptance_rows, ["check", "actual_delta_pp", "C_flag", "pass"])
    print(f"[done] cells={len(all_cell_rows)} -> {args.cell_output}")
    print(f"[done] c_rows={len(all_c_rows)} -> {args.c_output}")
    print(f"[done] acceptance={len(acceptance_rows)} -> {args.acceptance_output}")


if __name__ == "__main__":
    main()
