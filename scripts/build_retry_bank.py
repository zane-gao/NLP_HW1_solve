from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import read_jsonl, write_jsonl


def latest_response_map(
    rows: Sequence[Dict[str, Any]],
    model_id: Optional[str] = None,
    prompt_id: Optional[str] = None,
) -> Dict[Tuple[str, str, str], Dict[str, Any]]:
    latest: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for row in rows:
        if model_id and row.get("model_id") != model_id:
            continue
        if prompt_id and row.get("prompt_id") != prompt_id:
            continue
        key = (row["qid"], row["model_id"], row["prompt_id"])
        latest[key] = row
    return latest


def collect_retry_qids(
    response_rows: Sequence[Dict[str, Any]],
    model_id: Optional[str] = None,
    prompt_id: Optional[str] = None,
) -> List[str]:
    latest = latest_response_map(response_rows, model_id=model_id, prompt_id=prompt_id)
    return sorted(
        {
            qid
            for (qid, _model_id, _prompt_id), row in latest.items()
            if row.get("status") != "ok"
        }
    )


def build_retry_rows(problem_rows: Sequence[Dict[str, Any]], retry_qids: Sequence[str]) -> List[Dict[str, Any]]:
    wanted = set(retry_qids)
    return [row for row in problem_rows if row["qid"] in wanted]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a minimal retry problem bank from failed response keys.")
    parser.add_argument("--problem-bank", required=True)
    parser.add_argument("--responses", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model-id", default="")
    parser.add_argument("--prompt-id", default="")
    args = parser.parse_args()

    problem_rows = read_jsonl(args.problem_bank)
    response_rows = read_jsonl(args.responses)
    retry_qids = collect_retry_qids(
        response_rows,
        model_id=args.model_id or None,
        prompt_id=args.prompt_id or None,
    )
    retry_rows = build_retry_rows(problem_rows, retry_qids)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.output, retry_rows)
    print(f"[done] retry_qids={len(retry_qids)} rows={len(retry_rows)} -> {args.output}")


if __name__ == "__main__":
    main()
