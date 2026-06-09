from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import mcnemar_exact_p_value, read_jsonl


def parse_csv_arg(raw: str) -> List[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(path: str | Path, rows: Iterable[Dict[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def deduplicate_scores(paths: Sequence[str]) -> Dict[Tuple[str, str, str], Dict[str, Any]]:
    latest: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for path in paths:
        for row in read_jsonl(path):
            latest[(row["qid"], row["model_id"], row["prompt_id"])] = row
    return latest


def build_pair_bucket(
    problem_rows: List[Dict[str, Any]],
    score_rows: Dict[Tuple[str, str, str], Dict[str, Any]],
    task_type: str,
) -> Dict[Tuple[str, str, str, str], Dict[str, Any]]:
    problems = {row["qid"]: row for row in problem_rows}
    bucket: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    for (qid, model_id, prompt_id), score in score_rows.items():
        problem = problems.get(qid)
        if not problem:
            continue
        if task_type != "all" and problem["task_type"] != task_type:
            continue
        key = (model_id, prompt_id, problem["subtype_id"], problem["pair_id"])
        bundle = bucket.setdefault(
            key,
            {
                "meta": {
                    "subtype_id": problem["subtype_id"],
                    "domain": problem.get("domain", ""),
                    "source_style": problem.get("source_style", ""),
                    "target_field": problem.get("target_field", ""),
                    "intensity": problem.get("intensity", ""),
                    "composition": "composite" if problem.get("is_composite") else "single",
                },
                "control": None,
                "perturbed": None,
            },
        )
        bundle[problem["variant"]] = score.get("is_correct")
    return bucket


def summarize_group(rows: List[Tuple[Optional[int], Optional[int]]]) -> Dict[str, Any]:
    paired = [(control, perturbed) for control, perturbed in rows if control in [0, 1] and perturbed in [0, 1]]
    pair_count = len(paired)
    if pair_count == 0:
        return {
            "pair_count": 0,
            "flip_pairs": 0,
            "reverse_flip_pairs": 0,
            "FR_control": 0.0,
            "FR_trigger": 0.0,
            "delta_pp": 0.0,
            "p_value": 1.0,
            "n01": 0,
            "n10": 0,
        }
    control_err = sum(1 for control, _ in paired if control == 0)
    perturbed_err = sum(1 for _, perturbed in paired if perturbed == 0)
    n01 = sum(1 for control, perturbed in paired if control == 1 and perturbed == 0)
    n10 = sum(1 for control, perturbed in paired if control == 0 and perturbed == 1)
    return {
        "pair_count": pair_count,
        "flip_pairs": n01,
        "reverse_flip_pairs": n10,
        "FR_control": 100.0 * control_err / pair_count,
        "FR_trigger": 100.0 * perturbed_err / pair_count,
        "delta_pp": 100.0 * (perturbed_err - control_err) / pair_count,
        "p_value": mcnemar_exact_p_value(n01=n01, n10=n10),
        "n01": n01,
        "n10": n10,
    }


def build_rows(pair_bucket: Dict[Tuple[str, str, str, str], Dict[str, Any]]) -> List[Dict[str, Any]]:
    group_bucket: Dict[Tuple[str, str, str, str, str], List[Tuple[Optional[int], Optional[int]]]] = defaultdict(list)
    for (model_id, prompt_id, subtype_id, _pair_id), bundle in pair_bucket.items():
        meta = bundle["meta"]
        control = bundle.get("control")
        perturbed = bundle.get("perturbed")
        for group_type in ["target_field", "domain", "source_style", "intensity", "composition"]:
            group_value = meta.get(group_type, "")
            key = (model_id, prompt_id, subtype_id, group_type, group_value)
            group_bucket[key].append((control, perturbed))

    summary_rows: List[Dict[str, Any]] = []
    for (model_id, prompt_id, subtype_id, group_type, group_value), pairs in sorted(group_bucket.items()):
        stats = summarize_group(pairs)
        summary_rows.append(
            {
                "model_id": model_id,
                "prompt_id": prompt_id,
                "subtype_id": subtype_id,
                "group_type": group_type,
                "group_value": group_value,
                "pair_count": stats["pair_count"],
                "flip_pairs": stats["flip_pairs"],
                "reverse_flip_pairs": stats["reverse_flip_pairs"],
                "FR_control": f"{stats['FR_control']:.4f}",
                "FR_trigger": f"{stats['FR_trigger']:.4f}",
                "delta_pp": f"{stats['delta_pp']:.4f}",
                "p_value": f"{stats['p_value']:.6f}",
                "n01": stats["n01"],
                "n10": stats["n10"],
            }
        )
    return summary_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="输出 focus3 分层统计汇总")
    parser.add_argument("--problem-bank", required=True)
    parser.add_argument("--scores", required=True, help="Comma-separated jsonl files.")
    parser.add_argument("--task-type", choices=["all", "extraction", "classification"], default="extraction")
    parser.add_argument("--all-output", default="runs/focus3_layer_summary.csv")
    parser.add_argument("--field-output", default="runs/focus3_field_summary.csv")
    parser.add_argument("--domain-output", default="runs/focus3_domain_summary.csv")
    parser.add_argument("--style-output", default="runs/focus3_source_style_summary.csv")
    parser.add_argument("--intensity-output", default="runs/focus3_intensity_summary.csv")
    parser.add_argument("--composition-output", default="runs/focus3_composition_summary.csv")
    args = parser.parse_args()

    problem_rows = read_jsonl(args.problem_bank)
    score_rows = deduplicate_scores(parse_csv_arg(args.scores))
    pair_bucket = build_pair_bucket(problem_rows, score_rows, args.task_type)
    rows = build_rows(pair_bucket)

    fieldnames = [
        "model_id",
        "prompt_id",
        "subtype_id",
        "group_type",
        "group_value",
        "pair_count",
        "flip_pairs",
        "reverse_flip_pairs",
        "FR_control",
        "FR_trigger",
        "delta_pp",
        "p_value",
        "n01",
        "n10",
    ]
    write_csv(args.all_output, rows, fieldnames)
    write_csv(args.field_output, [row for row in rows if row["group_type"] == "target_field"], fieldnames)
    write_csv(args.domain_output, [row for row in rows if row["group_type"] == "domain"], fieldnames)
    write_csv(args.style_output, [row for row in rows if row["group_type"] == "source_style"], fieldnames)
    write_csv(args.intensity_output, [row for row in rows if row["group_type"] == "intensity"], fieldnames)
    write_csv(args.composition_output, [row for row in rows if row["group_type"] == "composition"], fieldnames)
    print(f"[done] layer rows={len(rows)} -> {args.all_output}")


if __name__ == "__main__":
    main()
