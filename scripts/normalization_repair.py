from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import (
    load_config,
    normalize_amount,
    normalize_company,
    normalize_date,
    read_jsonl,
    to_half_width,
)


# 这里显式维护常见繁简映射，是为了让修复模块不依赖系统级 opencc。
# 课程实验关注的是可复现机制，而不是最大覆盖的中文转换器。
DEFAULT_TRAD_TO_SIMP: Dict[str, str] = {
    "藍": "蓝",
    "數": "数",
    "據": "据",
    "遠": "远",
    "紀": "纪",
    "華": "华",
    "網": "网",
    "絡": "络",
    "長": "长",
    "風": "风",
    "啟": "启",
    "訊": "讯",
    "資": "资",
    "雲": "云",
    "銀": "银",
    "聯": "联",
    "實": "实",
    "驗": "验",
    "記": "记",
    "錄": "录",
    "獲": "获",
    "輪": "轮",
    "後": "后",
    "續": "续",
    "將": "将",
    "於": "于",
    "這": "这",
    "筆": "笔",
    "轉": "转",
    "寫": "写",
    "單": "单",
    "號": "号",
    "總": "总",
    "結": "结",
    "發": "发",
    "貼": "贴",
    "話": "话",
    "員": "员",
    "術": "术",
    "觀": "观",
    "測": "测",
    "電": "电",
    "視": "视",
    "體": "体",
    "國": "国",
    "漢": "汉",
    "臺": "台",
    "廣": "广",
    "龍": "龙",
}

OCR_TO_DIGIT: Dict[str, str] = {
    "O": "0",
    "o": "0",
    "I": "1",
    "l": "1",
    "Z": "2",
    "z": "2",
    "S": "5",
    "s": "5",
    "G": "6",
    "g": "6",
    "B": "8",
}


@dataclass
class RepairResult:
    output: Optional[Dict[str, Any]]
    actions: List[Dict[str, str]] = field(default_factory=list)


@dataclass(frozen=True)
class CompanyRegistry:
    """实体规范表。显式记录来源，避免误把测试集 gold 当成默认知识。"""

    companies: Tuple[str, ...]
    source: str

    def __iter__(self):
        return iter(self.companies)

    def __len__(self) -> int:
        return len(self.companies)


def load_trad_to_simp(config_path: str | Path = "configs/focus3_study.yaml") -> Dict[str, str]:
    mapping = dict(DEFAULT_TRAD_TO_SIMP)
    path = Path(config_path)
    if path.exists():
        try:
            cfg = load_config(path)
            for simp, trad in cfg.get("noise_profile", {}).get("script_variant_map", {}).items():
                if isinstance(simp, str) and isinstance(trad, str) and trad:
                    mapping[trad] = simp
        except Exception:
            pass
    return mapping


def simplify_script(text: Any, mapping: Optional[Dict[str, str]] = None) -> str:
    mapping = mapping or DEFAULT_TRAD_TO_SIMP
    return "".join(mapping.get(ch, ch) for ch in str(text))


def replace_ocr_confusables(text: Any) -> str:
    return "".join(OCR_TO_DIGIT.get(ch, ch) for ch in str(text))


def compact_key(text: Any, *, script_map: Optional[Dict[str, str]] = None, ocr: bool = False) -> str:
    s = normalize_company(simplify_script(to_half_width(str(text)), script_map))
    if ocr:
        s = replace_ocr_confusables(s)
    return re.sub(r"[\s\W_]+", "", s, flags=re.U).lower()


def normalize_company_script(text: Any, *, script_map: Optional[Dict[str, str]] = None) -> str:
    return normalize_company(simplify_script(to_half_width(str(text)), script_map))


def repair_date_value(text: Any) -> str:
    return normalize_date(replace_ocr_confusables(to_half_width(str(text))))


def repair_amount_value(text: Any) -> str:
    return normalize_amount(replace_ocr_confusables(to_half_width(str(text))))


def build_company_registry(problem_rows: Iterable[Dict[str, Any]]) -> List[str]:
    companies = []
    seen = set()
    for row in problem_rows:
        if row.get("task_type") != "extraction":
            continue
        gold = row.get("gold") or {}
        company = gold.get("company")
        if not company:
            continue
        norm = normalize_company(str(company))
        if norm and norm not in seen:
            seen.add(norm)
            companies.append(norm)
    return sorted(companies)


def build_company_registry_object(problem_rows: Iterable[Dict[str, Any]], *, source: str) -> CompanyRegistry:
    return CompanyRegistry(companies=tuple(build_company_registry(problem_rows)), source=source)


def registry_match_company(
    company: Any,
    source_text: str,
    registry: Sequence[str],
    *,
    script_map: Optional[Dict[str, str]] = None,
) -> Tuple[str, Optional[str]]:
    base = normalize_company_script(company, script_map=script_map)
    if not base or not registry:
        return base, None

    base_key = compact_key(base, script_map=script_map, ocr=True)
    source_key = compact_key(source_text, script_map=script_map, ocr=True)
    base_plain_key = compact_key(base, script_map=script_map, ocr=False)
    best: Tuple[int, int, str, str] = (-1, -1, base, "")

    for candidate in registry:
        candidate_key = compact_key(candidate, script_map=script_map, ocr=True)
        candidate_plain_key = compact_key(candidate, script_map=script_map, ocr=False)
        score = 0
        reason = ""

        if candidate_plain_key == base_plain_key:
            score = 120
            reason = "script_exact_registry"
        elif candidate_key == base_key:
            score = 110
            reason = "ocr_equivalent_registry"
        elif candidate_key and candidate_key in source_key and (
            base_key in candidate_key or candidate_key in base_key
        ):
            score = 95
            reason = "source_anchored_registry"
        elif candidate_key and base_key and base_key in candidate_key and len(candidate_key) - len(base_key) <= 3:
            score = 70
            reason = "prefix_completion_registry"

        # 候选越长通常信息越完整，用作 tie-breaker，避免把带编号实体截短。
        if score > best[0] or (score == best[0] and len(candidate_key) > best[1]):
            best = (score, len(candidate_key), candidate, reason)

    if best[0] >= 90 and normalize_company(best[2]) != base:
        return normalize_company(best[2]), best[3]
    return base, None


def repair_extraction_output(
    parsed: Optional[Dict[str, Any]],
    sample: Dict[str, Any],
    *,
    repair_mode: str,
    registry: Sequence[str] = (),
    script_map: Optional[Dict[str, str]] = None,
) -> RepairResult:
    if not isinstance(parsed, dict):
        return RepairResult(output=None, actions=[])

    if repair_mode == "none":
        return RepairResult(output=dict(parsed), actions=[])

    repaired = dict(parsed)
    actions: List[Dict[str, str]] = []
    source_text = str(sample.get("input", ""))

    if "company" in repaired:
        old_company = str(repaired["company"])
        if repair_mode == "field_aware":
            new_company, reason = registry_match_company(
                old_company,
                source_text,
                registry,
                script_map=script_map,
            )
        else:
            new_company = normalize_company_script(old_company, script_map=script_map)
            reason = "script_normalize" if new_company != old_company else None
        repaired["company"] = new_company
        if new_company != old_company:
            actions.append({"field": "company", "before": old_company, "after": new_company, "reason": reason or "company_repair"})

    if "date" in repaired:
        old_date = str(repaired["date"])
        new_date = repair_date_value(old_date) if repair_mode in {"script_numeric", "field_aware"} else old_date
        repaired["date"] = new_date
        if new_date != old_date:
            actions.append({"field": "date", "before": old_date, "after": new_date, "reason": "ocr_numeric_date"})

    if "amount" in repaired:
        old_amount = str(repaired["amount"])
        new_amount = repair_amount_value(old_amount) if repair_mode in {"script_numeric", "field_aware"} else old_amount
        repaired["amount"] = new_amount
        if new_amount != old_amount:
            actions.append({"field": "amount", "before": old_amount, "after": new_amount, "reason": "ocr_numeric_amount"})

    return RepairResult(output=repaired, actions=actions)


def repair_problem_bank_text(sample: Dict[str, Any], *, script_map: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    row = dict(sample)
    text = simplify_script(to_half_width(str(row.get("input", ""))), script_map)
    text = replace_ocr_confusables(text)
    row["input"] = text
    row["preprocess_mode"] = "script_width_ocr_numeric"
    return row


def main() -> None:
    parser = argparse.ArgumentParser(description="HDR-Harness 字段级规范化修复工具")
    parser.add_argument("--problem-bank", default="data/problem_bank_focus3_main.jsonl")
    parser.add_argument("--text", default="", help="调试：直接规范化一段文本")
    args = parser.parse_args()

    script_map = load_trad_to_simp()
    if args.text:
        print(replace_ocr_confusables(simplify_script(to_half_width(args.text), script_map)))
        return

    rows = read_jsonl(args.problem_bank)
    registry = build_company_registry(rows)
    print(json.dumps({"companies": registry}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
