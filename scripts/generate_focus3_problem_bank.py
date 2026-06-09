from __future__ import annotations

import argparse
import csv
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import load_config, write_jsonl


COMPANIES = [
    "蓝海数据A1",
    "远景智能Lab",
    "新纪元物流X2",
    "华澄资讯B8",
    "华星科技I3",
    "北辰网络I研",
    "长风教育2部",
    "启真资讯B端",
    "万象云服AI",
    "银联实验室5组",
    "沐川健康S3",
    "青石出行M1",
    "深蓝能源E8",
    "瑞光芯片B8",
    "华策文旅D2",
    "智元科技Z9",
    "凌云航科A2",
    "青穗农业T5",
]

PURPOSES = [
    "算法研发",
    "产品迭代",
    "算力采购",
    "市场扩张",
    "渠道建设",
    "合规改造",
    "供应链升级",
    "海外试点",
]

AMOUNTS = [
    "800万元",
    "900万元",
    "1000万元",
    "1200万元",
    "1500万元",
    "1800万元",
    "2000万元",
    "2600万元",
]

CHANNELS = ["项目群", "产品群", "投研群", "运营群", "客服群", "销售群"]
PLATFORMS = ["创投观察", "科技速递", "行业风向", "企业动态", "投融资圈", "热点追踪"]


@dataclass
class Record:
    company: str
    date_iso: str
    date_cn: str
    amount: str
    code: str
    purpose: str
    channel: str
    platform: str


def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(path: str | Path, rows: Iterable[Dict[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def allocate_counts(total: int, ratios: Dict[str, float]) -> Dict[str, int]:
    keys = list(ratios.keys())
    raw = {key: total * float(ratios[key]) for key in keys}
    base = {key: int(raw[key]) for key in keys}
    remain = total - sum(base.values())
    order = sorted(keys, key=lambda key: (raw[key] - base[key]), reverse=True)
    for key in order[:remain]:
        base[key] += 1
    return base


def repeated_labels(total: int, ratio_map: Dict[str, float], seed: int) -> List[str]:
    counts = allocate_counts(total, ratio_map)
    labels: List[str] = []
    for key, count in counts.items():
        labels.extend([key] * count)
    rng = random.Random(seed)
    rng.shuffle(labels)
    return labels


def build_records(total_pairs: int) -> List[Record]:
    records: List[Record] = []
    for idx in range(total_pairs):
        year = 2026
        month = (idx % 12) + 1
        day = (idx * 3 % 27) + 1
        records.append(
            Record(
                company=COMPANIES[idx % len(COMPANIES)],
                date_iso=f"{year:04d}-{month:02d}-{day:02d}",
                date_cn=f"{year}年{month:02d}月{day:02d}日",
                amount=AMOUNTS[idx % len(AMOUNTS)],
                code=f"AX{1400 + idx * 17}",
                purpose=PURPOSES[idx % len(PURPOSES)],
                channel=CHANNELS[idx % len(CHANNELS)],
                platform=PLATFORMS[idx % len(PLATFORMS)],
            )
        )
    return records


def to_context(record: Record) -> Dict[str, str]:
    return {
        "company": record.company,
        "date_iso": record.date_iso,
        "date_cn": record.date_cn,
        "amount": record.amount,
        "code": record.code,
        "purpose": record.purpose,
        "channel": record.channel,
        "platform": record.platform,
    }


def select_domain(template_cfg: Dict[str, Any], domain_name: str) -> Dict[str, Any]:
    for domain in template_cfg["domains"]:
        if domain["domain"] == domain_name:
            return domain
    raise KeyError(f"unknown domain: {domain_name}")


def render_extraction_text(domain_entry: Dict[str, Any], template_index: int, record: Record) -> Tuple[str, str]:
    template = domain_entry["extraction_templates"][template_index % len(domain_entry["extraction_templates"])]
    return template.format(**to_context(record)), f"{domain_entry['domain']}.ex.{template_index % len(domain_entry['extraction_templates'])}"


def render_classification_text(
    domain_entry: Dict[str, Any],
    template_index: int,
    record: Record,
    supported: bool,
) -> Tuple[str, Dict[str, str], str]:
    evidence, _ = render_extraction_text(domain_entry, template_index, record)
    claim_amount = record.amount if supported else bump_amount(record.amount, 100)
    claim = f"{record.company}在{record.date_iso}完成{claim_amount}融资。"
    wrapper = domain_entry["classification_wrappers"][template_index % len(domain_entry["classification_wrappers"])]
    gold = {"label": "支持" if supported else "不支持"}
    return wrapper.format(text=evidence, claim=claim, **to_context(record)), gold, f"{domain_entry['domain']}.cls.{template_index % len(domain_entry['classification_wrappers'])}"


def bump_amount(amount: str, step: int) -> str:
    digits = "".join(ch for ch in amount if ch.isdigit())
    unit = amount[len(digits) :]
    if not digits:
        return amount
    return f"{int(digits) + step}{unit}"


def to_full_width_char(ch: str) -> str:
    code = ord(ch)
    if ch == " ":
        return "\u3000"
    if 33 <= code <= 126:
        return chr(code + 65248)
    return ch


def eligible_positions(text: str, predicate) -> List[int]:
    return [idx for idx, ch in enumerate(text) if predicate(ch)]


def pick_positions(positions: List[int], intensity: str) -> List[int]:
    if not positions:
        return []
    if intensity == "light":
        count = 1
    elif intensity == "medium":
        count = min(2, len(positions))
    else:
        count = min(max(3, len(positions) // 2), len(positions))
    return positions[:count]


def replace_positions(text: str, positions: List[int], mapper) -> str:
    chars = list(text)
    for idx in positions:
        chars[idx] = mapper(chars[idx])
    return "".join(chars)


def replace_all(text: str, old: str, new: str) -> str:
    if old and old in text:
        return text.replace(old, new)
    return text


def perturb_window(
    text: str,
    anchor: str,
    predicate,
    mapper,
    intensity: str,
    pad: int = 12,
) -> str:
    if not anchor or anchor not in text:
        return text
    start = text.index(anchor)
    left = max(0, start - pad)
    right = min(len(text), start + len(anchor) + pad)
    window = text[left:right]
    positions = pick_positions(eligible_positions(window, predicate), intensity)
    if not positions:
        return text
    new_window = replace_positions(window, positions, mapper)
    return text[:left] + new_window + text[right:]


def perturb_globally(text: str, predicate, mapper, intensity: str) -> str:
    positions = pick_positions(eligible_positions(text, predicate), intensity)
    if not positions:
        return text
    return replace_positions(text, positions, mapper)


def perturb_simp_trad(
    text: str,
    record: Record,
    target_field: str,
    intensity: str,
    mapping: Dict[str, str],
) -> Tuple[str, str]:
    can_map = lambda ch: ch in mapping and mapping.get(ch) != ch
    anchor = {
        "company": record.company,
        "date": record.date_cn,
        "amount": record.amount,
    }[target_field]
    if target_field == "company":
        positions = pick_positions(eligible_positions(anchor, can_map), intensity)
        if positions:
            new_anchor = replace_positions(anchor, positions, lambda ch: mapping.get(ch, ch))
            return replace_all(text, anchor, new_anchor), "script_variant_preserved"
    new_text = perturb_window(
        text,
        anchor,
        predicate=can_map,
        mapper=lambda ch: mapping.get(ch, ch),
        intensity=intensity,
        pad=16,
    )
    if new_text != text:
        return new_text, "script_variant_preserved"
    global_text = perturb_globally(
        text,
        predicate=can_map,
        mapper=lambda ch: mapping.get(ch, ch),
        intensity=intensity,
    )
    return global_text, "script_variant_preserved"


def perturb_full_half_width(
    text: str,
    record: Record,
    target_field: str,
    intensity: str,
) -> Tuple[str, str]:
    anchor = {
        "company": record.company,
        "date": record.date_iso if record.date_iso in text else record.date_cn,
        "amount": record.amount,
    }[target_field]
    if anchor in text:
        positions = pick_positions(eligible_positions(anchor, lambda ch: ch.isdigit() or ch.isascii() and ch.isalpha()), intensity)
        if positions:
            new_anchor = replace_positions(anchor, positions, to_full_width_char)
            return replace_all(text, anchor, new_anchor), "mixed_width_numeric_field"
    new_text = perturb_window(
        text,
        anchor,
        predicate=lambda ch: ch.isdigit() or ch.isascii() and ch.isalpha(),
        mapper=to_full_width_char,
        intensity=intensity,
        pad=8,
    )
    if new_text != text:
        return new_text, "mixed_width_numeric_field"
    global_text = perturb_globally(
        text,
        predicate=lambda ch: ch.isdigit() or ch.isascii() and ch.isalpha(),
        mapper=to_full_width_char,
        intensity=intensity,
    )
    return global_text, "mixed_width_numeric_field"


def perturb_ocr_confusable(
    text: str,
    record: Record,
    target_field: str,
    intensity: str,
    mapping: Dict[str, str],
) -> Tuple[str, str]:
    anchor = {
        "company": record.company,
        "date": record.date_iso if record.date_iso in text else record.date_cn,
        "amount": record.amount,
    }[target_field]
    if anchor in text:
        positions = pick_positions(eligible_positions(anchor, lambda ch: ch in mapping), intensity)
        if positions:
            new_anchor = replace_positions(anchor, positions, lambda ch: mapping.get(ch, ch))
            return replace_all(text, anchor, new_anchor), "ocr_confusion_near_key_slot"
    new_text = perturb_window(
        text,
        anchor,
        predicate=lambda ch: ch in mapping,
        mapper=lambda ch: mapping.get(ch, ch),
        intensity=intensity,
        pad=8,
    )
    if new_text != text:
        return new_text, "ocr_confusion_near_key_slot"
    global_text = perturb_globally(
        text,
        predicate=lambda ch: ch in mapping,
        mapper=lambda ch: mapping.get(ch, ch),
        intensity=intensity,
    )
    return global_text, "ocr_confusion_near_key_slot"


def apply_primary_perturbation(
    text: str,
    subtype_id: str,
    record: Record,
    target_field: str,
    intensity: str,
    study_cfg: Dict[str, Any],
) -> Tuple[str, str, str]:
    profile = study_cfg["noise_profile"]
    if subtype_id == "simp_trad":
        new_text, shape = perturb_simp_trad(text, record, target_field, intensity, profile["script_variant_map"])
    elif subtype_id == "full_half_width":
        new_text, shape = perturb_full_half_width(text, record, target_field, intensity)
    elif subtype_id == "ocr_confusable":
        new_text, shape = perturb_ocr_confusable(text, record, target_field, intensity, profile["ocr_confusable_map"])
    else:
        raise ValueError(f"unsupported subtype: {subtype_id}")
    return new_text, f"{subtype_id}:{target_field}:{intensity}", shape


def apply_secondary_perturbation(
    text: str,
    primary_subtype: str,
    record: Record,
    target_field: str,
    study_cfg: Dict[str, Any],
) -> Tuple[str, str]:
    secondaries = [item for item in ["simp_trad", "full_half_width", "ocr_confusable"] if item != primary_subtype]
    secondary = secondaries[0]
    new_text, op, _ = apply_primary_perturbation(text, secondary, record, target_field, "light", study_cfg)
    return new_text, op


def split_domain_tasks(pair_total: int, extraction_pairs: int, domains: List[str]) -> Dict[str, Dict[str, int]]:
    pair_per_domain = pair_total // len(domains)
    extraction_per_domain = extraction_pairs // len(domains)
    out: Dict[str, Dict[str, int]] = {}
    ex_remainder = extraction_pairs - extraction_per_domain * len(domains)
    total_remainder = pair_total - pair_per_domain * len(domains)
    for idx, domain in enumerate(domains):
        total = pair_per_domain + (1 if idx < total_remainder else 0)
        extraction = extraction_per_domain + (1 if idx < ex_remainder else 0)
        out[domain] = {"total": total, "extraction": extraction, "classification": total - extraction}
    return out


def make_pair_specs(section_cfg: Dict[str, Any], study_cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    domains = list(study_cfg["domains"])
    rng_seed = int(study_cfg["seed"])
    specs: List[Dict[str, Any]] = []
    for subtype_index, subtype_cfg in enumerate(section_cfg["subtypes"]):
        subtype_id = subtype_cfg["subtype_id"]
        pair_total = int(subtype_cfg["pair_total"])
        extraction_pairs = int(subtype_cfg["extraction_pairs"])
        domain_split = split_domain_tasks(pair_total, extraction_pairs, domains)
        target_fields = repeated_labels(pair_total, subtype_cfg["target_field_ratio"], rng_seed + subtype_index * 13)
        intensities = repeated_labels(pair_total, study_cfg["intensity_ratio"], rng_seed + subtype_index * 29)
        composite_count = int(round(pair_total * float(study_cfg["composite_ratio"])))
        composite_flags = [False] * pair_total
        for idx in range(composite_count):
            composite_flags[pair_total - 1 - idx] = True

        cursor = 0
        for domain in domains:
            split = domain_split[domain]
            for task_type in ["extraction", "classification"]:
                for _ in range(split[task_type]):
                    specs.append(
                        {
                            "subtype_id": subtype_id,
                            "task_type": task_type,
                            "domain": domain,
                            "target_field": target_fields[cursor],
                            "intensity": intensities[cursor],
                            "is_composite": composite_flags[cursor],
                        }
                    )
                    cursor += 1
    return specs


def build_rows(section_name: str, study_cfg: Dict[str, Any], template_cfg: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    section_cfg = study_cfg[section_name]
    specs = make_pair_specs(section_cfg, study_cfg)
    records = build_records(len(specs))
    rows: List[Dict[str, Any]] = []
    allocation_rows: List[Dict[str, Any]] = []

    for idx, (spec, record) in enumerate(zip(specs, records), start=1):
        domain_entry = select_domain(template_cfg, spec["domain"])
        template_index = idx % 2
        source_style = domain_entry["source_style"]
        pair_id = f"pair_{section_name}_{spec['task_type'][:3]}_{spec['subtype_id']}_{idx:03d}"
        if spec["task_type"] == "extraction":
            control_text, template_id = render_extraction_text(domain_entry, template_index, record)
            gold = {"company": record.company, "date": record.date_iso, "amount": record.amount}
        else:
            control_text, gold, template_id = render_classification_text(
                domain_entry,
                template_index,
                record,
                supported=(idx % 2 == 0),
            )

        perturbed_text, primary_op, trigger_shape = apply_primary_perturbation(
            control_text,
            spec["subtype_id"],
            record,
            spec["target_field"],
            spec["intensity"],
            study_cfg,
        )
        perturb_ops = [primary_op]
        secondary_subtype = ""
        if spec["is_composite"]:
            perturbed_text, secondary_op = apply_secondary_perturbation(
                perturbed_text,
                spec["subtype_id"],
                record,
                spec["target_field"],
                study_cfg,
            )
            secondary_subtype = secondary_op.split(":", 1)[0]
            perturb_ops.append(secondary_op)

        rows.append(
            {
                "qid": f"{pair_id}_control",
                "pair_id": pair_id,
                "task_type": spec["task_type"],
                "subtype_id": spec["subtype_id"],
                "variant": "control",
                "input": control_text,
                "gold": gold,
                "domain": spec["domain"],
                "template_id": template_id,
                "source_style": source_style,
                "target_field": spec["target_field"],
                "intensity": spec["intensity"],
                "perturb_ops": [],
                "is_composite": False,
                "trigger_shape_hint": "",
                "secondary_subtype": "",
            }
        )
        rows.append(
            {
                "qid": f"{pair_id}_perturbed",
                "pair_id": pair_id,
                "task_type": spec["task_type"],
                "subtype_id": spec["subtype_id"],
                "variant": "perturbed",
                "input": perturbed_text,
                "gold": gold,
                "domain": spec["domain"],
                "template_id": template_id,
                "source_style": source_style,
                "target_field": spec["target_field"],
                "intensity": spec["intensity"],
                "perturb_ops": perturb_ops,
                "is_composite": spec["is_composite"],
                "trigger_shape_hint": trigger_shape,
                "secondary_subtype": secondary_subtype,
            }
        )
        allocation_rows.append(
            {
                "pair_id": pair_id,
                "subtype_id": spec["subtype_id"],
                "task_type": spec["task_type"],
                "domain": spec["domain"],
                "source_style": source_style,
                "target_field": spec["target_field"],
                "intensity": spec["intensity"],
                "is_composite": "1" if spec["is_composite"] else "0",
                "secondary_subtype": secondary_subtype,
                "trigger_shape_hint": trigger_shape,
            }
        )

    return rows, allocation_rows


def filter_rows(rows: List[Dict[str, Any]], *, task_type: str) -> List[Dict[str, Any]]:
    return [row for row in rows if row["task_type"] == task_type]


def quality_report(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    pair_bucket: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for row in rows:
        pair_bucket.setdefault(row["pair_id"], {})[row["variant"]] = row
    perturbed_rows = [row for row in rows if row["variant"] == "perturbed"]
    single_ratio = sum(1 for row in perturbed_rows if not row["is_composite"]) / max(1, len(perturbed_rows))
    intensity_count: Dict[str, int] = {}
    for row in perturbed_rows:
        intensity_count[row["intensity"]] = intensity_count.get(row["intensity"], 0) + 1
    subtype_hit = {
        subtype: any(row["subtype_id"] == subtype and row["input"] != pair_bucket[row["pair_id"]]["control"]["input"] for row in perturbed_rows)
        for subtype in sorted({row["subtype_id"] for row in rows})
    }
    return {
        "rows_total": len(rows),
        "pair_total": len(pair_bucket),
        "single_ratio": single_ratio,
        "composite_ratio": 1 - single_ratio,
        "intensity_count": intensity_count,
        "subtype_hit": subtype_hit,
    }


def write_quality(path: str | Path, report: Dict[str, Any]) -> None:
    ensure_parent(path)
    lines = [f"{key}: {value}" for key, value in report.items()]
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="生成 focus3 三件套补强数据集")
    parser.add_argument("--study-config", default="configs/focus3_study.yaml")
    parser.add_argument("--template-bank", default="configs/focus3_template_bank.yaml")
    parser.add_argument("--main-output", default="data/problem_bank_focus3_main.jsonl")
    parser.add_argument("--main-extraction-output", default="data/problem_bank_focus3_main_extraction.jsonl")
    parser.add_argument("--main-classification-output", default="data/problem_bank_focus3_main_classification.jsonl")
    parser.add_argument("--main-allocation", default="data/focus3_main_allocation.csv")
    parser.add_argument("--main-quality", default="runs/data_quality_focus3_main.txt")
    parser.add_argument("--calibration-output", default="data/problem_bank_focus3_calibration.jsonl")
    parser.add_argument("--calibration-extraction-output", default="data/problem_bank_focus3_calibration_extraction.jsonl")
    parser.add_argument("--calibration-classification-output", default="data/problem_bank_focus3_calibration_classification.jsonl")
    parser.add_argument("--calibration-allocation", default="data/focus3_calibration_allocation.csv")
    parser.add_argument("--calibration-quality", default="runs/data_quality_focus3_calibration.txt")
    args = parser.parse_args()

    study_cfg = load_config(args.study_config)
    template_cfg = load_config(args.template_bank)

    main_rows, main_alloc = build_rows("main", study_cfg, template_cfg)
    calibration_rows, calibration_alloc = build_rows("calibration", study_cfg, template_cfg)

    write_jsonl(args.main_output, main_rows)
    write_jsonl(args.main_extraction_output, filter_rows(main_rows, task_type="extraction"))
    write_jsonl(args.main_classification_output, filter_rows(main_rows, task_type="classification"))
    write_jsonl(args.calibration_output, calibration_rows)
    write_jsonl(args.calibration_extraction_output, filter_rows(calibration_rows, task_type="extraction"))
    write_jsonl(args.calibration_classification_output, filter_rows(calibration_rows, task_type="classification"))

    write_csv(
        args.main_allocation,
        main_alloc,
        ["pair_id", "subtype_id", "task_type", "domain", "source_style", "target_field", "intensity", "is_composite", "secondary_subtype", "trigger_shape_hint"],
    )
    write_csv(
        args.calibration_allocation,
        calibration_alloc,
        ["pair_id", "subtype_id", "task_type", "domain", "source_style", "target_field", "intensity", "is_composite", "secondary_subtype", "trigger_shape_hint"],
    )
    write_quality(args.main_quality, quality_report(main_rows))
    write_quality(args.calibration_quality, quality_report(calibration_rows))

    print(f"[done] main rows={len(main_rows)} pairs={len(main_rows) // 2} -> {args.main_output}")
    print(f"[done] calibration rows={len(calibration_rows)} pairs={len(calibration_rows) // 2} -> {args.calibration_output}")


if __name__ == "__main__":
    main()
