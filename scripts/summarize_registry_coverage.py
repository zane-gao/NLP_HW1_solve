from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import read_jsonl
from scripts.normalization_repair import build_company_registry, normalize_company_script


def write_csv(path: str | Path, rows: Iterable[Dict[str, Any]], fieldnames: Sequence[str]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def registry_keys(rows: Sequence[Dict[str, Any]]) -> set[str]:
    return {normalize_company_script(company) for company in build_company_registry(rows)}


def gold_company_key(row: Dict[str, Any]) -> str:
    return normalize_company_script((row.get("gold") or {}).get("company", ""))


def summarize_scores(
    *,
    problem_rows: Dict[str, Dict[str, Any]],
    score_rows: Sequence[Dict[str, Any]],
    registry: set[str],
    label: str,
) -> List[Dict[str, str]]:
    pair_bucket: Dict[Tuple[str, str, str, str], Dict[str, int]] = defaultdict(dict)
    coverage_pairs: Dict[Tuple[str, str], str] = {}

    for qid, row in problem_rows.items():
        if row.get("task_type") != "extraction":
            continue
        coverage_pairs[(row["pair_id"], row["subtype_id"])] = "seen" if gold_company_key(row) in registry else "unseen"

    for score in score_rows:
        if score.get("is_correct") not in [0, 1]:
            continue
        problem = problem_rows.get(score["qid"])
        if not problem or problem.get("task_type") != "extraction":
            continue
        coverage = coverage_pairs.get((problem["pair_id"], problem["subtype_id"]), "unknown")
        for bucket_coverage in ["all", coverage]:
            key = (problem["subtype_id"], bucket_coverage, score["model_id"], score["prompt_id"])
            pair_bucket[key][problem["pair_id"] + "::" + problem["variant"]] = int(score["is_correct"])

    subtype_coverage_deltas: Dict[Tuple[str, str], List[float]] = defaultdict(list)
    subtype_coverage_pairs: Dict[Tuple[str, str], int] = defaultdict(int)
    subtype_coverage_flips: Dict[Tuple[str, str], Tuple[int, int]] = defaultdict(lambda: (0, 0))

    for (subtype, coverage, _model_id, _prompt_id), keyed_scores in pair_bucket.items():
        pair_ids = sorted({item.rsplit("::", 1)[0] for item in keyed_scores})
        paired = []
        for pair_id in pair_ids:
            control_key = pair_id + "::control"
            perturbed_key = pair_id + "::perturbed"
            if control_key in keyed_scores and perturbed_key in keyed_scores:
                paired.append((keyed_scores[control_key], keyed_scores[perturbed_key]))
        if not paired:
            continue
        control_err = sum(1 for c, _ in paired if c == 0)
        trigger_err = sum(1 for _, p in paired if p == 0)
        delta_pp = 100.0 * (trigger_err - control_err) / len(paired)
        bucket = (subtype, coverage)
        subtype_coverage_deltas[bucket].append(delta_pp)
        subtype_coverage_pairs[bucket] += len(paired)
        old_n01, old_n10 = subtype_coverage_flips[bucket]
        n01 = sum(1 for c, p in paired if c == 1 and p == 0)
        n10 = sum(1 for c, p in paired if c == 0 and p == 1)
        subtype_coverage_flips[bucket] = (old_n01 + n01, old_n10 + n10)

    rows: List[Dict[str, str]] = []
    for subtype in ["simp_trad", "ocr_confusable", "full_half_width"]:
        for coverage in ["all", "seen", "unseen"]:
            deltas = subtype_coverage_deltas.get((subtype, coverage), [])
            pair_count = subtype_coverage_pairs.get((subtype, coverage), 0)
            n01, n10 = subtype_coverage_flips.get((subtype, coverage), (0, 0))
            if not deltas:
                continue
            rows.append(
                {
                    "score_set": label,
                    "subtype_id": subtype,
                    "coverage": coverage,
                    "mean_delta_pp": f"{sum(deltas) / len(deltas):.4f}",
                    "cell_count": str(len(deltas)),
                    "paired_observations": str(pair_count),
                    "n01": str(n01),
                    "n10": str(n10),
                }
            )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="汇总 strict registry 的 seen/unseen 覆盖边界。")
    parser.add_argument("--problem-bank", default="data/problem_bank_focus3_main.jsonl")
    parser.add_argument("--registry-problem-bank", default="data/problem_bank_focus3_calibration.jsonl")
    parser.add_argument("--score-set", action="append", required=True, help="label=score_jsonl，可重复。")
    parser.add_argument("--summary-output", default="runs/registry_coverage_summary.csv")
    parser.add_argument("--manifest-output", default="runs/registry_manifest.csv")
    args = parser.parse_args()

    problem_rows_list = read_jsonl(args.problem_bank)
    problem_rows = {row["qid"]: row for row in problem_rows_list}
    registry_rows = read_jsonl(args.registry_problem_bank)
    registry = registry_keys(registry_rows)

    seen_companies = sorted({gold_company_key(row) for row in problem_rows_list if gold_company_key(row) in registry})
    unseen_companies = sorted({gold_company_key(row) for row in problem_rows_list if gold_company_key(row) and gold_company_key(row) not in registry})

    all_rows: List[Dict[str, str]] = []
    for item in args.score_set:
        if "=" not in item:
            raise RuntimeError(f"score-set must be label=path, got {item}")
        label, path = item.split("=", 1)
        all_rows.extend(
            summarize_scores(
                problem_rows=problem_rows,
                score_rows=read_jsonl(path),
                registry=registry,
                label=label,
            )
        )

    write_csv(
        args.summary_output,
        all_rows,
        ["score_set", "subtype_id", "coverage", "mean_delta_pp", "cell_count", "paired_observations", "n01", "n10"],
    )
    write_csv(
        args.manifest_output,
        [
            {"split": "calibration_registry", "company_count": str(len(registry)), "companies": "；".join(sorted(registry))},
            {"split": "main_seen", "company_count": str(len(seen_companies)), "companies": "；".join(seen_companies)},
            {"split": "main_unseen", "company_count": str(len(unseen_companies)), "companies": "；".join(unseen_companies)},
        ],
        ["split", "company_count", "companies"],
    )
    print(f"[done] registry={len(registry)} summary={len(all_rows)} -> {args.summary_output}")
    print(f"[done] seen={len(seen_companies)} unseen={len(unseen_companies)} -> {args.manifest_output}")


if __name__ == "__main__":
    main()
