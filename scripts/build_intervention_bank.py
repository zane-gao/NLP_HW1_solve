from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import read_jsonl, write_jsonl
from scripts.normalization_repair import load_trad_to_simp, repair_problem_bank_text


def parse_csv_arg(raw: str) -> List[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def select_pairs(rows: List[Dict[str, Any]], subtypes: List[str], pairs_per_subtype: int) -> List[str]:
    by_subtype: Dict[str, List[str]] = defaultdict(list)
    for row in rows:
        if row.get("variant") != "control":
            continue
        subtype = row.get("subtype_id")
        if subtype not in subtypes:
            continue
        pair_id = row["pair_id"]
        if pair_id not in by_subtype[subtype]:
            by_subtype[subtype].append(pair_id)
    selected: List[str] = []
    for subtype in subtypes:
        selected.extend(sorted(by_subtype[subtype])[:pairs_per_subtype])
    return selected


def build_condition_rows(rows: List[Dict[str, Any]], selected_pairs: List[str], condition: str) -> List[Dict[str, Any]]:
    script_map = load_trad_to_simp()
    selected = set(selected_pairs)
    out: List[Dict[str, Any]] = []
    for row in rows:
        if row.get("pair_id") not in selected:
            continue
        new_row = dict(row)
        new_row["condition"] = condition
        new_row["original_qid"] = row["qid"]
        new_row["qid"] = f"{row['qid']}__{condition}"
        if condition in {"preprocess", "harness"}:
            new_row = repair_problem_bank_text(new_row, script_map=script_map)
            new_row["condition"] = condition
        out.append(new_row)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="构造在线精选消融问题库")
    parser.add_argument("--problem-bank", default="data/problem_bank_focus3_main_extraction.jsonl")
    parser.add_argument("--subtypes", default="simp_trad,ocr_confusable,full_half_width")
    parser.add_argument("--pairs-per-subtype", type=int, default=6)
    parser.add_argument("--output-dir", default="data/intervention")
    args = parser.parse_args()

    rows = read_jsonl(args.problem_bank)
    subtypes = parse_csv_arg(args.subtypes)
    selected_pairs = select_pairs(rows, subtypes, args.pairs_per_subtype)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "source_problem_bank": args.problem_bank,
        "subtypes": subtypes,
        "pairs_per_subtype": args.pairs_per_subtype,
        "selected_pairs": selected_pairs,
        "conditions": ["base", "preprocess", "harness"],
        "models": ["gpt-5.2", "GLM-4.6"],
        "prompts": ["P1", "P4"],
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    all_rows: List[Dict[str, Any]] = []
    for condition in ["base", "preprocess", "harness"]:
        condition_rows = build_condition_rows(rows, selected_pairs, condition)
        write_jsonl(output_dir / f"problem_bank_{condition}.jsonl", condition_rows)
        all_rows.extend(condition_rows)
    write_jsonl(output_dir / "problem_bank_all_conditions.jsonl", all_rows)
    print(f"[done] selected_pairs={len(selected_pairs)} rows={len(all_rows)} -> {output_dir}")


if __name__ == "__main__":
    main()
