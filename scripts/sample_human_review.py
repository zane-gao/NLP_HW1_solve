from __future__ import annotations

import argparse
import csv
import random
import sys
from pathlib import Path
from typing import Any, Dict, List

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import read_jsonl


def write_csv(path: str, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def build_pair_map(problem_rows: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    pair_map: Dict[str, Dict[str, Any]] = {}
    for row in problem_rows:
        pair_id = row["pair_id"]
        if pair_id not in pair_map:
            pair_map[pair_id] = {
                "pair_id": pair_id,
                "subtype_id": row["subtype_id"],
                "task_type": row["task_type"],
                "control_input": "",
                "perturbed_input": "",
            }
        if row["variant"] == "control":
            pair_map[pair_id]["control_input"] = row["input"]
        else:
            pair_map[pair_id]["perturbed_input"] = row["input"]
    return pair_map


def main() -> None:
    parser = argparse.ArgumentParser(description="导出人工复核样本")
    parser.add_argument("--problem-bank", default="data/problem_bank.jsonl")
    parser.add_argument("--output", default="runs/human_semantic_review.csv")
    parser.add_argument("--ratio", type=float, default=0.15)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--unresolved-scores", default="")
    parser.add_argument("--unresolved-output", default="runs/human_unresolved_review.csv")
    args = parser.parse_args()

    random.seed(args.seed)
    problem_rows = read_jsonl(args.problem_bank)
    pair_map = build_pair_map(problem_rows)
    pair_ids = sorted(pair_map.keys())
    sample_size = max(1, int(round(len(pair_ids) * args.ratio)))
    sampled_ids = random.sample(pair_ids, sample_size) if sample_size < len(pair_ids) else pair_ids

    semantic_rows: List[Dict[str, Any]] = []
    for pair_id in sampled_ids:
        item = pair_map[pair_id]
        semantic_rows.append(
            {
                "pair_id": pair_id,
                "subtype_id": item["subtype_id"],
                "task_type": item["task_type"],
                "control_input": item["control_input"],
                "perturbed_input": item["perturbed_input"],
                "semantic_equivalent(1/0)": "",
                "review_notes": "",
            }
        )

    write_csv(
        args.output,
        semantic_rows,
        [
            "pair_id",
            "subtype_id",
            "task_type",
            "control_input",
            "perturbed_input",
            "semantic_equivalent(1/0)",
            "review_notes",
        ],
    )
    print(f"[done] semantic review sample={len(semantic_rows)} -> {args.output}")

    if args.unresolved_scores:
        unresolved_rows = [row for row in read_jsonl(args.unresolved_scores) if row.get("is_correct") is None]
        human_rows: List[Dict[str, Any]] = []
        for row in unresolved_rows:
            human_rows.append(
                {
                    "qid": row["qid"],
                    "model_id": row["model_id"],
                    "prompt_id": row["prompt_id"],
                    "error_type": row.get("error_type", ""),
                    "human_is_correct(1/0)": "",
                    "review_notes": "",
                }
            )
        write_csv(
            args.unresolved_output,
            human_rows,
            ["qid", "model_id", "prompt_id", "error_type", "human_is_correct(1/0)", "review_notes"],
        )
        print(f"[done] unresolved sample={len(human_rows)} -> {args.unresolved_output}")


if __name__ == "__main__":
    main()
