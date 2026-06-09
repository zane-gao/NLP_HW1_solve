from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import load_config, mcnemar_exact_p_value, read_jsonl


def load_thresholds(config_path: str) -> Dict[str, float]:
    cfg = load_config(config_path)
    return cfg["thresholds"]


def to_bool_str(flag: bool) -> str:
    return "1" if flag else "0"


def write_csv(path: str, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="聚合 A/B/C 指标")
    parser.add_argument("--experiment-config", default="configs/experiment.yaml")
    parser.add_argument("--problem-bank", default="data/problem_bank.jsonl")
    parser.add_argument("--scores", default="runs/scores_merged.jsonl")
    parser.add_argument("--summary", default="runs/summary.csv")
    parser.add_argument("--c-summary", default="runs/c_summary.csv")
    parser.add_argument("--task-type", choices=["all", "extraction", "classification"], default="all")
    args = parser.parse_args()

    thresholds = load_thresholds(args.experiment_config)
    problems = {row["qid"]: row for row in read_jsonl(args.problem_bank)}
    scores = read_jsonl(args.scores)

    pair_bucket: Dict[Tuple[str, str, str], Dict[str, Dict[str, int]]] = defaultdict(dict)
    models_set = set()

    for row in scores:
        is_correct = row.get("is_correct")
        if is_correct not in [0, 1]:
            continue
        qid = row["qid"]
        problem = problems.get(qid)
        if not problem:
            continue
        if args.task_type != "all" and problem.get("task_type") != args.task_type:
            continue
        model_id = row["model_id"]
        prompt_id = row["prompt_id"]
        subtype_id = problem["subtype_id"]
        pair_id = problem["pair_id"]
        variant = problem["variant"]

        key = (model_id, prompt_id, subtype_id)
        if pair_id not in pair_bucket[key]:
            pair_bucket[key][pair_id] = {}
        pair_bucket[key][pair_id][variant] = int(is_correct)
        models_set.add(model_id)

    summary_rows: List[Dict[str, Any]] = []
    b_count: Dict[Tuple[str, str], int] = defaultdict(int)

    for (model_id, prompt_id, subtype_id), pair_map in sorted(pair_bucket.items()):
        paired = [(v["control"], v["perturbed"]) for _, v in pair_map.items() if "control" in v and "perturbed" in v]
        n = len(paired)
        if n == 0:
            continue
        control_err = sum(1 for c, _ in paired if c == 0)
        trigger_err = sum(1 for _, p in paired if p == 0)
        fr_control = 100.0 * control_err / n
        fr_trigger = 100.0 * trigger_err / n
        delta_pp = fr_trigger - fr_control
        n01 = sum(1 for c, p in paired if c == 1 and p == 0)
        n10 = sum(1 for c, p in paired if c == 0 and p == 1)
        p_value = mcnemar_exact_p_value(n01=n01, n10=n10)
        a_flag = (delta_pp >= float(thresholds["A_delta_err_pp"])) and (p_value < float(thresholds["A_p_value"]))
        if a_flag:
            b_count[(model_id, subtype_id)] += 1

        summary_rows.append(
            {
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
    for row in summary_rows:
        model_id = row["model_id"]
        subtype_id = row["subtype_id"]
        b_flag = b_count[(model_id, subtype_id)] >= min_prompt_count
        row["B_flag"] = to_bool_str(b_flag)

    fieldnames = [
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
    ]
    write_csv(args.summary, summary_rows, fieldnames)

    subtype_model_b: Dict[str, set] = defaultdict(set)
    for row in summary_rows:
        if row["B_flag"] == "1":
            subtype_model_b[row["subtype_id"]].add(row["model_id"])

    min_model_count = int(thresholds["C_min_model_count"])
    all_subtypes = sorted({row["subtype_id"] for row in summary_rows})
    c_rows: List[Dict[str, Any]] = []
    for subtype in all_subtypes:
        model_cnt = len(subtype_model_b[subtype])
        c_rows.append(
            {
                "subtype_id": subtype,
                "models_with_B": model_cnt,
                "total_models": len(models_set),
                "C_flag": to_bool_str(model_cnt >= min_model_count),
            }
        )

    write_csv(args.c_summary, c_rows, ["subtype_id", "models_with_B", "total_models", "C_flag"])
    print(f"[done] summary={len(summary_rows)} rows -> {args.summary}")
    print(f"[done] c_summary={len(c_rows)} rows -> {args.c_summary}")


if __name__ == "__main__":
    main()
