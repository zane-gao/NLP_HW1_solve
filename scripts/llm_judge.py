from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import (
    extract_json_object,
    load_config,
    read_jsonl,
    retry_chat_completion,
    utc_now_iso,
    write_jsonl,
)


def build_judge_prompt(case: Dict[str, Any]) -> List[Dict[str, str]]:
    system = (
        "你是严格评测裁判。请判断候选模型输出是否与标准答案等价正确。"
        "如果无法确定，也必须给出最保守判断。只输出 JSON。"
    )
    user = (
        "请根据以下信息判定 is_correct。\n"
        f"任务类型: {case['task_type']}\n"
        f"输入:\n{case['input']}\n\n"
        f"标准答案(gold): {case['gold']}\n"
        f"候选模型输出(raw): {case.get('raw_output', '')}\n"
        "输出格式: {\"is_correct\": 0或1, \"reason\": \"不超过30字\"}"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def parse_judge_vote(raw: str) -> Optional[int]:
    parsed = extract_json_object(raw)
    if not parsed:
        return None
    value = parsed.get("is_correct")
    if value in [0, 1]:
        return int(value)
    if isinstance(value, str):
        v = value.strip()
        if v in {"0", "1"}:
            return int(v)
    return None


def find_model(model_cfg: Dict[str, Any], model_id: str) -> Optional[Dict[str, Any]]:
    for model in model_cfg["models"]:
        if model["model_id"] == model_id and model.get("enabled", True):
            return model
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="双 LLM 裁判复核")
    parser.add_argument("--model-registry", default="configs/model_registry.yaml")
    parser.add_argument("--scores", default="runs/scores.jsonl")
    parser.add_argument("--hard-cases", default="runs/hard_cases.jsonl")
    parser.add_argument("--output", default="runs/scores_merged.jsonl")
    parser.add_argument("--votes", default="runs/judge_votes.jsonl")
    parser.add_argument("--judge-a", default="gpt5.3-xhigh")
    parser.add_argument("--judge-b", default="claude-4.6-opus")
    parser.add_argument("--timeout-sec", type=int, default=120)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--max-cases", type=int, default=0)
    args = parser.parse_args()

    model_cfg = load_config(args.model_registry)
    judge_a = find_model(model_cfg, args.judge_a)
    judge_b = find_model(model_cfg, args.judge_b)
    if judge_a is None or judge_b is None:
        raise RuntimeError("裁判模型未在 model_registry.yaml 中找到或未启用。")

    hard_cases = read_jsonl(args.hard_cases)
    if args.max_cases > 0:
        hard_cases = hard_cases[: args.max_cases]
    base_scores = read_jsonl(args.scores)
    score_map: Dict[Tuple[str, str, str], Dict[str, Any]] = {
        (row["qid"], row["model_id"], row["prompt_id"]): row for row in base_scores
    }

    votes: List[Dict[str, Any]] = []
    consensus_map: Dict[Tuple[str, str, str], int] = {}

    for case in hard_cases:
        key = (case["qid"], case["model_id"], case["prompt_id"])
        messages = build_judge_prompt(case)
        vote_bundle: Dict[str, Any] = {
            "qid": case["qid"],
            "model_id": case["model_id"],
            "prompt_id": case["prompt_id"],
            "created_at": utc_now_iso(),
            "votes": {},
            "consensus": None,
        }

        judge_votes: List[Optional[int]] = []
        for judge in [judge_a, judge_b]:
            model_id = judge["model_id"]
            api_key = os.getenv(judge.get("api_key_env", ""))
            if not api_key:
                vote_bundle["votes"][model_id] = {"is_correct": None, "error": "missing_api_key"}
                judge_votes.append(None)
                continue
            ok, content, _, err = retry_chat_completion(
                api_base=judge["api_base"],
                api_key=api_key,
                model=judge.get("api_model", model_id),
                messages=messages,
                temperature=float(judge.get("temperature", 0.0)),
                max_tokens=int(judge.get("max_tokens", 256)),
                timeout_sec=args.timeout_sec,
                max_retries=args.max_retries,
            )
            if not ok:
                vote_bundle["votes"][model_id] = {"is_correct": None, "error": err}
                judge_votes.append(None)
                continue
            vote = parse_judge_vote(content)
            vote_bundle["votes"][model_id] = {"is_correct": vote, "raw_output": content}
            judge_votes.append(vote)

        if len(judge_votes) == 2 and judge_votes[0] is not None and judge_votes[0] == judge_votes[1]:
            vote_bundle["consensus"] = int(judge_votes[0])
            consensus_map[key] = int(judge_votes[0])
        votes.append(vote_bundle)

    merged_scores: List[Dict[str, Any]] = []
    for row in base_scores:
        key = (row["qid"], row["model_id"], row["prompt_id"])
        if key in consensus_map:
            row = dict(row)
            row["is_correct"] = consensus_map[key]
            row["error_type"] = "llm_consensus"
            row["score_source"] = "llm"
        elif row.get("is_correct") is None:
            row = dict(row)
            row["score_source"] = "human"
        merged_scores.append(row)

    write_jsonl(args.votes, votes)
    write_jsonl(args.output, merged_scores)
    print(f"[done] votes={len(votes)} -> {args.votes}")
    print(f"[done] merged_scores={len(merged_scores)} -> {args.output}")


if __name__ == "__main__":
    main()
