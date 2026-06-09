from __future__ import annotations

import argparse
import csv
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import load_config, write_jsonl
from scripts.generate_problem_bank import build_problem_bank_with_counts


def parse_float(value: str, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return default


def load_pilot_stats(summary_csv: str, pilot_delta_threshold: float) -> Dict[str, Dict]:
    per_subtype_model_max = defaultdict(lambda: defaultdict(float))
    with open(summary_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subtype = row["subtype_id"]
            model = row["model_id"]
            delta = parse_float(row.get("delta_pp", "0"))
            per_subtype_model_max[subtype][model] = max(per_subtype_model_max[subtype][model], delta)

    stats: Dict[str, Dict] = {}
    for subtype, model_map in per_subtype_model_max.items():
        deltas = list(model_map.values())
        pass_models = sum(1 for d in deltas if d >= pilot_delta_threshold)
        stats[subtype] = {
            "pass_models": pass_models,
            "mean_delta": (sum(deltas) / len(deltas)) if deltas else 0.0,
        }
    return stats


def load_semantic_pass_rate(path: str) -> Dict[str, float]:
    rates: Dict[str, float] = {}
    if not path or not Path(path).exists():
        return rates
    bucket = defaultdict(list)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subtype = row.get("subtype_id", "")
            if not subtype:
                continue
            flag = str(row.get("semantic_equivalent(1/0)", "")).strip()
            if flag in {"0", "1"}:
                bucket[subtype].append(int(flag))
    for subtype, flags in bucket.items():
        if flags:
            rates[subtype] = sum(flags) / len(flags)
    return rates


def allocate_integer(total: int, weights: Dict[str, float]) -> Dict[str, int]:
    keys = sorted(weights.keys())
    total_weight = sum(weights[k] for k in keys)
    if total_weight <= 0:
        equal = total // len(keys)
        out = {k: equal for k in keys}
        for k in keys[: total - equal * len(keys)]:
            out[k] += 1
        return out
    raw = {k: (total * weights[k] / total_weight) for k in keys}
    floored = {k: int(math.floor(raw[k])) for k in keys}
    remain = total - sum(floored.values())
    fractions = sorted(((raw[k] - floored[k], k) for k in keys), reverse=True)
    for _, k in fractions[:remain]:
        floored[k] += 1
    return floored


def split_task_counts(total_pairs: Dict[str, int], extraction_target: int) -> Dict[str, Dict[str, int]]:
    subtypes = sorted(total_pairs.keys())
    expected = {s: total_pairs[s] * 2 / 3 for s in subtypes}
    extraction = {s: int(math.floor(expected[s])) for s in subtypes}
    diff = extraction_target - sum(extraction.values())
    if diff > 0:
        order = sorted(subtypes, key=lambda s: (expected[s] - extraction[s]), reverse=True)
        for subtype in order:
            if diff == 0:
                break
            extraction[subtype] += 1
            diff -= 1
    elif diff < 0:
        order = sorted(subtypes, key=lambda s: (expected[s] - extraction[s]))
        for subtype in order:
            if diff == 0:
                break
            if extraction[subtype] > 0:
                extraction[subtype] -= 1
                diff += 1
    out = {}
    for subtype in subtypes:
        out[subtype] = {
            "extraction": extraction[subtype],
            "classification": total_pairs[subtype] - extraction[subtype],
        }
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="根据 Pilot 结果重分配主实验样本")
    parser.add_argument("--phenomenon", default="configs/phenomenon_bank.yaml")
    parser.add_argument("--experiment", default="configs/experiment.yaml")
    parser.add_argument("--domain-template", default="configs/domain_template_bank.yaml")
    parser.add_argument("--perturb-profile", default="configs/perturb_profile.yaml")
    parser.add_argument("--pilot-summary", default="runs/summary_pilot.csv")
    parser.add_argument("--semantic-review", default="")
    parser.add_argument("--output", default="data/problem_bank.jsonl")
    parser.add_argument("--allocation-csv", default="data/subtype_allocation.csv")
    args = parser.parse_args()

    phenomenon_cfg = load_config(args.phenomenon)
    experiment_cfg = load_config(args.experiment)
    domain_cfg = load_config(args.domain_template)
    perturb_cfg = load_config(args.perturb_profile)
    thresholds = experiment_cfg["thresholds"]
    dataset_cfg = experiment_cfg["dataset"]

    subtypes = [item["subtype_id"] for item in phenomenon_cfg["subtypes"]]
    total_pairs = int(dataset_cfg["pair_count_total"])
    min_pairs = int(dataset_cfg["min_pairs_per_subtype"])
    extraction_target = int(dataset_cfg["task_ratio"]["extraction_pairs"])
    semantic_threshold = float(thresholds["pilot_semantic_pass_rate"])
    pilot_delta = float(thresholds["pilot_delta_err_pp"])

    pilot_stats = load_pilot_stats(args.pilot_summary, pilot_delta_threshold=pilot_delta)
    semantic_rates = load_semantic_pass_rate(args.semantic_review)

    model_pass_need = 2  # Pilot 3 模型时对应“至少 2/3”
    qualified = {}
    weights = {}
    for subtype in subtypes:
        stats = pilot_stats.get(subtype, {"pass_models": 0, "mean_delta": 0.0})
        semantic_ok = True
        if subtype in semantic_rates:
            semantic_ok = semantic_rates[subtype] >= semantic_threshold
        is_qualified = stats["pass_models"] >= model_pass_need and semantic_ok
        qualified[subtype] = is_qualified
        weights[subtype] = max(0.0, stats["mean_delta"]) if is_qualified else 0.0

    base = {subtype: min_pairs for subtype in subtypes}
    extra_budget = total_pairs - min_pairs * len(subtypes)
    extra_alloc = allocate_integer(extra_budget, weights)
    pair_total = {subtype: base[subtype] + extra_alloc[subtype] for subtype in subtypes}

    subtype_task_counts = split_task_counts(pair_total, extraction_target=extraction_target)
    rows, _ = build_problem_bank_with_counts(
        phenomenon_cfg=phenomenon_cfg,
        subtype_task_counts=subtype_task_counts,
        domain_cfg=domain_cfg,
        perturb_cfg=perturb_cfg,
        pilot_cfg=experiment_cfg.get("pipeline"),
        seed=42,
    )
    write_jsonl(args.output, rows)

    allocation_rows: List[Dict[str, str]] = []
    for subtype in sorted(subtypes):
        stats = pilot_stats.get(subtype, {"pass_models": 0, "mean_delta": 0.0})
        allocation_rows.append(
            {
                "subtype_id": subtype,
                "pair_total": str(pair_total[subtype]),
                "extraction_pairs": str(subtype_task_counts[subtype]["extraction"]),
                "classification_pairs": str(subtype_task_counts[subtype]["classification"]),
                "pilot_pass_models": str(stats["pass_models"]),
                "pilot_mean_delta": f"{stats['mean_delta']:.4f}",
                "semantic_pass_rate": (
                    f"{semantic_rates[subtype]:.4f}" if subtype in semantic_rates else "NA"
                ),
                "qualified": "1" if qualified[subtype] else "0",
            }
        )

    Path(args.allocation_csv).parent.mkdir(parents=True, exist_ok=True)
    with open(args.allocation_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "subtype_id",
                "pair_total",
                "extraction_pairs",
                "classification_pairs",
                "pilot_pass_models",
                "pilot_mean_delta",
                "semantic_pass_rate",
                "qualified",
            ],
        )
        writer.writeheader()
        for row in allocation_rows:
            writer.writerow(row)

    pair_cnt = len({row["pair_id"] for row in rows})
    ex_cnt = len({row["pair_id"] for row in rows if row["task_type"] == "extraction"})
    cls_cnt = len({row["pair_id"] for row in rows if row["task_type"] == "classification"})
    print(f"[done] main rows={len(rows)} pairs={pair_cnt} ex_pairs={ex_cnt} cls_pairs={cls_cnt} -> {args.output}")
    print(f"[done] allocation -> {args.allocation_csv}")


if __name__ == "__main__":
    main()
