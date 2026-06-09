from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import read_jsonl, write_jsonl


MODE_SUBTYPE_BALANCED_40 = "subtype_balanced_40"
MODE_FOCUS_SUBTYPES = "focus_subtypes"
SUPPORTED_MODES = [MODE_SUBTYPE_BALANCED_40, MODE_FOCUS_SUBTYPES]


def parse_subtypes(raw: str) -> List[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def select_subtype_balanced_pairs(rows: Sequence[Dict]) -> List[str]:
    pair_ids_by_bucket: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
    for row in rows:
        pair_ids_by_bucket[row["subtype_id"]][row["task_type"]].add(row["pair_id"])

    selected_pair_ids: List[str] = []
    for subtype_id in sorted(pair_ids_by_bucket):
        extraction_pairs = sorted(pair_ids_by_bucket[subtype_id].get("extraction", set()))
        classification_pairs = sorted(pair_ids_by_bucket[subtype_id].get("classification", set()))
        if not extraction_pairs or not classification_pairs:
            raise ValueError(
                f"subtype={subtype_id} is missing required task pairs: "
                f"extraction={len(extraction_pairs)} classification={len(classification_pairs)}"
            )
        selected_pair_ids.extend([extraction_pairs[0], classification_pairs[0]])
    return selected_pair_ids


def filter_rows_by_pair_order(rows: Sequence[Dict], selected_pair_ids: Iterable[str]) -> List[Dict]:
    selected_set = set(selected_pair_ids)
    return [row for row in rows if row["pair_id"] in selected_set]


def filter_rows_by_subtypes(rows: Sequence[Dict], subtypes: Sequence[str]) -> List[Dict]:
    selected = set(subtypes)
    return [row for row in rows if row["subtype_id"] in selected]


def validate_complete_pairs(rows: Sequence[Dict]) -> None:
    pair_variants: Dict[str, Set[str]] = defaultdict(set)
    for row in rows:
        pair_variants[row["pair_id"]].add(row["variant"])
    broken_pairs = sorted(pair_id for pair_id, variants in pair_variants.items() if variants != {"control", "perturbed"})
    if broken_pairs:
        raise ValueError(f"incomplete pairs found: {broken_pairs[:5]}")


def build_subset(rows: Sequence[Dict], mode: str, subtypes: Sequence[str] | None = None) -> List[Dict]:
    if mode == MODE_SUBTYPE_BALANCED_40:
        selected_pair_ids = select_subtype_balanced_pairs(rows)
        subset = filter_rows_by_pair_order(rows, selected_pair_ids)
    elif mode == MODE_FOCUS_SUBTYPES:
        if not subtypes:
            raise ValueError("subtypes are required when mode=focus_subtypes")
        subset = filter_rows_by_subtypes(rows, subtypes)
        if not subset:
            raise ValueError(f"no rows found for subtypes={list(subtypes)}")
        found_subtypes = {row["subtype_id"] for row in subset}
        missing = [subtype for subtype in subtypes if subtype not in found_subtypes]
        if missing:
            raise ValueError(f"missing requested subtypes: {missing}")
    else:
        raise ValueError(f"unsupported mode: {mode}")

    validate_complete_pairs(subset)
    return subset


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a pilot subset from the problem bank.")
    parser.add_argument("--input", default="data/pilot_problem_bank.jsonl")
    parser.add_argument("--output", default="data/pilot_problem_bank_balanced40.jsonl")
    parser.add_argument("--mode", default=MODE_SUBTYPE_BALANCED_40, choices=SUPPORTED_MODES)
    parser.add_argument("--subtypes", default="", help="Comma-separated subtype ids for focus_subtypes mode.")
    args = parser.parse_args()

    rows = read_jsonl(args.input)
    if not rows:
        raise RuntimeError(f"empty problem bank: {args.input}")

    subtypes = parse_subtypes(args.subtypes)
    subset = build_subset(rows, mode=args.mode, subtypes=subtypes)
    write_jsonl(args.output, subset)

    pair_count = len({row["pair_id"] for row in subset})
    subtype_count = len({row["subtype_id"] for row in subset})
    print(f"[done] subset rows={len(subset)} pairs={pair_count} subtypes={subtype_count} -> {args.output}")


if __name__ == "__main__":
    main()
