from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import extract_json_object, read_jsonl, write_jsonl
from scripts.normalization_repair import (
    build_company_registry,
    load_trad_to_simp,
    repair_extraction_output,
)
from scripts.score_outputs import score_classification, score_extraction


def deduplicate_responses(rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    latest: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for row in rows:
        latest[(row["qid"], row["model_id"], row["prompt_id"])] = row
    return list(latest.values())


def parse_csv_arg(raw: str) -> List[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def load_response_rows(paths: Sequence[str]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for path in paths:
        rows.extend(read_jsonl(path))
    return rows


def resolve_registry_rows(
    *,
    repair_mode: str,
    registry_scope: str,
    registry_problem_bank: str,
    main_problem_rows: Sequence[Dict[str, Any]],
) -> Tuple[List[Dict[str, Any]], str]:
    if repair_mode != "field_aware":
        return [], "none"
    if registry_scope == "strict":
        if not registry_problem_bank:
            raise RuntimeError("field_aware strict 模式必须通过 --registry-problem-bank 指定独立 calibration bank。")
        rows = read_jsonl(registry_problem_bank)
        if not rows:
            raise RuntimeError(f"registry problem bank 为空或不存在：{registry_problem_bank}")
        return rows, f"strict:{registry_problem_bank}"
    if registry_scope == "oracle":
        return list(main_problem_rows), "oracle:test_gold"
    raise RuntimeError(f"unsupported registry_scope: {registry_scope}")


def main() -> None:
    parser = argparse.ArgumentParser(description="对旧模型输出执行 HDR 修复后重评分")
    parser.add_argument("--problem-bank", default="data/problem_bank_focus3_main.jsonl")
    parser.add_argument(
        "--registry-problem-bank",
        default="data/problem_bank_focus3_calibration.jsonl",
        help="strict field_aware 使用的独立实体规范表来源。",
    )
    parser.add_argument(
        "--registry-scope",
        choices=["strict", "oracle"],
        default="strict",
        help="strict 使用独立 calibration registry；oracle 显式使用测试集 gold，仅作上界。",
    )
    parser.add_argument("--responses", required=True, help="Comma-separated response jsonl files.")
    parser.add_argument("--scores", required=True)
    parser.add_argument("--hard-cases", required=True)
    parser.add_argument("--repair-actions", default="")
    parser.add_argument("--repair-mode", choices=["none", "script_numeric", "field_aware"], default="field_aware")
    parser.add_argument("--focus-task", choices=["all", "extraction", "classification"], default="all")
    args = parser.parse_args()

    problems = {row["qid"]: row for row in read_jsonl(args.problem_bank)}
    problem_rows = list(problems.values())
    registry_rows, registry_source = resolve_registry_rows(
        repair_mode=args.repair_mode,
        registry_scope=args.registry_scope,
        registry_problem_bank=args.registry_problem_bank,
        main_problem_rows=problem_rows,
    )
    registry = build_company_registry(registry_rows)
    script_map = load_trad_to_simp()
    responses = deduplicate_responses(load_response_rows(parse_csv_arg(args.responses)))

    scores: List[Dict[str, Any]] = []
    hard_cases: List[Dict[str, Any]] = []
    repair_actions: List[Dict[str, Any]] = []

    for resp in responses:
        qid = resp["qid"]
        sample = problems.get(qid)
        if sample is None:
            continue
        if args.focus_task != "all" and sample.get("task_type") != args.focus_task:
            continue

        base = {
            "qid": qid,
            "model_id": resp["model_id"],
            "prompt_id": resp["prompt_id"],
            "repair_mode": args.repair_mode,
            "registry_scope": args.registry_scope if args.repair_mode == "field_aware" else "none",
            "is_correct": None,
            "error_type": "unknown",
            "score_source": "rule_repaired",
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
            repair = repair_extraction_output(
                parsed,
                sample,
                repair_mode=args.repair_mode,
                registry=registry,
                script_map=script_map,
            )
            is_correct, err = score_extraction(repair.output, sample["gold"])
            if repair.actions:
                repair_actions.append(
                    {
                        "qid": qid,
                        "model_id": resp["model_id"],
                        "prompt_id": resp["prompt_id"],
                        "repair_mode": args.repair_mode,
                        "registry_scope": args.registry_scope,
                        "registry_source": registry_source,
                        "original_output": parsed,
                        "repaired_output": repair.output,
                        "actions": repair.actions,
                    }
                )
        else:
            repair = None
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
                    "repaired_output": repair.output if repair else parsed,
                }
            )

    write_jsonl(args.scores, scores)
    write_jsonl(args.hard_cases, hard_cases)
    if args.repair_actions:
        write_jsonl(args.repair_actions, repair_actions)

    print(f"[done] repair_mode={args.repair_mode} registry={registry_source} companies={len(registry)} scores={len(scores)} -> {args.scores}")
    print(f"[done] hard_cases={len(hard_cases)} -> {args.hard_cases}")
    if args.repair_actions:
        print(f"[done] repair_actions={len(repair_actions)} -> {args.repair_actions}")


if __name__ == "__main__":
    main()
