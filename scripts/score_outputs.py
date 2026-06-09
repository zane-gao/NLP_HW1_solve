from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import (
    extract_json_object,
    normalize_amount,
    normalize_company,
    normalize_date,
    normalize_label,
    read_jsonl,
    write_jsonl,
)


def parse_label(parsed: Optional[Dict[str, Any]], raw_output: str) -> Optional[str]:
    if parsed:
        for key in ["label", "result", "answer"]:
            if key in parsed:
                label = normalize_label(str(parsed[key]))
                if label:
                    return label
    return normalize_label(raw_output)


def score_extraction(parsed: Optional[Dict[str, Any]], gold: Dict[str, Any]) -> Tuple[Optional[int], str]:
    if not parsed:
        return None, "parse_error"
    needed = ["company", "date", "amount"]
    for field in needed:
        if field not in parsed:
            return None, f"missing_field_{field}"
    mismatches = []
    if normalize_company(str(parsed["company"])) != normalize_company(str(gold["company"])):
        mismatches.append("company")
    if normalize_date(str(parsed["date"])) != normalize_date(str(gold["date"])):
        mismatches.append("date")
    if normalize_amount(str(parsed["amount"])) != normalize_amount(str(gold["amount"])):
        mismatches.append("amount")
    if mismatches:
        return 0, "mismatch_" + "_".join(mismatches)
    return 1, "ok"


def score_classification(parsed: Optional[Dict[str, Any]], raw_output: str, gold: Dict[str, Any]) -> Tuple[Optional[int], str]:
    pred = parse_label(parsed, raw_output)
    if pred is None:
        return None, "parse_error_label"
    gold_label = normalize_label(str(gold["label"]))
    if pred == gold_label:
        return 1, "ok"
    return 0, "label_mismatch"


def deduplicate_responses(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    latest: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for row in rows:
        key = (row["qid"], row["model_id"], row["prompt_id"])
        latest[key] = row
    return list(latest.values())


def main() -> None:
    parser = argparse.ArgumentParser(description="规则判分")
    parser.add_argument("--problem-bank", default="data/problem_bank.jsonl")
    parser.add_argument("--responses", default="runs/responses.jsonl")
    parser.add_argument("--scores", default="runs/scores.jsonl")
    parser.add_argument("--hard-cases", default="runs/hard_cases.jsonl")
    args = parser.parse_args()

    problems = {row["qid"]: row for row in read_jsonl(args.problem_bank)}
    responses = deduplicate_responses(read_jsonl(args.responses))

    scores: List[Dict[str, Any]] = []
    hard_cases: List[Dict[str, Any]] = []

    for resp in responses:
        qid = resp["qid"]
        sample = problems.get(qid)
        if sample is None:
            continue

        base = {
            "qid": qid,
            "model_id": resp["model_id"],
            "prompt_id": resp["prompt_id"],
            "is_correct": None,
            "error_type": "unknown",
            "score_source": "rule",
        }

        status = resp.get("status", "ok")
        if status != "ok":
            base["error_type"] = "call_error"
            scores.append(base)
            hard_cases.append(
                {
                    **base,
                    "task_type": sample["task_type"],
                    "input": sample["input"],
                    "gold": sample["gold"],
                    "raw_output": resp.get("raw_output", ""),
                    "call_error": resp.get("error", ""),
                }
            )
            continue

        parsed = resp.get("parsed_output")
        if not isinstance(parsed, dict):
            parsed = extract_json_object(resp.get("raw_output", ""))

        if sample["task_type"] == "extraction":
            is_correct, err = score_extraction(parsed, sample["gold"])
        else:
            is_correct, err = score_classification(parsed, resp.get("raw_output", ""), sample["gold"])

        base["is_correct"] = is_correct
        base["error_type"] = err
        scores.append(base)

        if is_correct is None:
            hard_cases.append(
                {
                    **base,
                    "task_type": sample["task_type"],
                    "input": sample["input"],
                    "gold": sample["gold"],
                    "raw_output": resp.get("raw_output", ""),
                    "parsed_output": parsed,
                }
            )

    write_jsonl(args.scores, scores)
    write_jsonl(args.hard_cases, hard_cases)
    print(f"[done] scores={len(scores)} -> {args.scores}")
    print(f"[done] hard_cases={len(hard_cases)} -> {args.hard_cases}")


if __name__ == "__main__":
    main()
