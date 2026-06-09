from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import extract_json_object, read_jsonl, to_half_width


SCRIPT_VARIANT_MAP = {
    "數": "数",
    "據": "据",
    "資": "资",
    "轉": "转",
    "發": "发",
    "於": "于",
    "長": "长",
    "風": "风",
    "網": "网",
    "銀": "银",
    "電": "电",
    "視": "视",
    "體": "体",
    "訊": "讯",
    "國": "国",
    "雲": "云",
    "漢": "汉",
    "臺": "台",
    "廣": "广",
    "華": "华",
    "龍": "龙",
    "藍": "蓝",
    "數": "数",
}

FULL_WIDTH_ALNUM_REPLACEMENTS = str.maketrans(
    {
        "０": "0",
        "１": "1",
        "２": "2",
        "３": "3",
        "４": "4",
        "５": "5",
        "６": "6",
        "７": "7",
        "８": "8",
        "９": "9",
        "Ａ": "A",
        "Ｂ": "B",
        "Ｃ": "C",
        "Ｄ": "D",
        "Ｅ": "E",
        "Ｆ": "F",
        "Ｇ": "G",
        "Ｈ": "H",
        "Ｉ": "I",
        "Ｊ": "J",
        "Ｋ": "K",
        "Ｌ": "L",
        "Ｍ": "M",
        "Ｎ": "N",
        "Ｏ": "O",
        "Ｐ": "P",
        "Ｑ": "Q",
        "Ｒ": "R",
        "Ｓ": "S",
        "Ｔ": "T",
        "Ｕ": "U",
        "Ｖ": "V",
        "Ｗ": "W",
        "Ｘ": "X",
        "Ｙ": "Y",
        "Ｚ": "Z",
        "ａ": "a",
        "ｂ": "b",
        "ｃ": "c",
        "ｄ": "d",
        "ｅ": "e",
        "ｆ": "f",
        "ｇ": "g",
        "ｈ": "h",
        "ｉ": "i",
        "ｊ": "j",
        "ｋ": "k",
        "ｌ": "l",
        "ｍ": "m",
        "ｎ": "n",
        "ｏ": "o",
        "ｐ": "p",
        "ｑ": "q",
        "ｒ": "r",
        "ｓ": "s",
        "ｔ": "t",
        "ｕ": "u",
        "ｖ": "v",
        "ｗ": "w",
        "ｘ": "x",
        "ｙ": "y",
        "ｚ": "z",
    }
)


def parse_csv_arg(raw: str) -> List[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(path: str | Path, rows: List[Dict[str, Any]], fieldnames: Sequence[str]) -> None:
    ensure_parent(path)
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def load_latest_jsonl(paths: Sequence[str], key_fields: Sequence[str]) -> Dict[Tuple[str, ...], Dict[str, Any]]:
    latest: Dict[Tuple[str, ...], Dict[str, Any]] = {}
    for path in paths:
        for row in read_jsonl(path):
            key = tuple(str(row[field]) for field in key_fields)
            latest[key] = row
    return latest


def normalize_script_variants(text: str) -> str:
    text = to_half_width(text).replace(" ", "")
    return "".join(SCRIPT_VARIANT_MAP.get(ch, ch) for ch in text)


def stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def pair_outcome(control_score: Optional[int], perturbed_score: Optional[int]) -> str:
    if control_score not in [0, 1] or perturbed_score not in [0, 1]:
        return "incomplete"
    if control_score == 1 and perturbed_score == 0:
        return "flip_case"
    if control_score == 0 and perturbed_score == 1:
        return "reverse_flip"
    if control_score == 1 and perturbed_score == 1:
        return "stable_ok"
    return "stable_err"


def has_full_width_alnum(text: str) -> bool:
    return any(ord(ch) > 127 and ch.translate(FULL_WIDTH_ALNUM_REPLACEMENTS) != ch for ch in text)


def contains_numeric_like_segment(text: str) -> bool:
    return any(ch.isdigit() for ch in to_half_width(text)) or "AX" in to_half_width(text).upper()


def classify_full_half_width(bundle: Dict[str, Any]) -> Tuple[str, str]:
    perturbed_input = bundle["perturbed"]["sample"]["input"]
    if has_full_width_alnum(perturbed_input) and contains_numeric_like_segment(perturbed_input):
        return (
            "mixed_width_numeric_field",
            "数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。",
        )
    return ("manual_review_needed", "无法由当前规则稳定归因")


def classify_minor_typo(bundle: Dict[str, Any]) -> Tuple[str, str]:
    gold = bundle["control"]["sample"]["gold"]
    perturbed_parsed = bundle["perturbed"]["response"].get("parsed_output") or {}
    pred_company = stringify(perturbed_parsed.get("company", ""))
    gold_company = stringify(gold.get("company", ""))
    if pred_company and gold_company and pred_company != gold_company and gold_company in pred_company:
        return (
            "entity_boundary_overattach",
            "轻微错别字触发了实体边界扩张，业务词被模型并入 company 字段。",
        )
    return ("manual_review_needed", "无法由当前规则稳定归因")


def classify_simp_trad(bundle: Dict[str, Any]) -> Tuple[str, str]:
    gold = bundle["control"]["sample"]["gold"]
    perturbed_parsed = bundle["perturbed"]["response"].get("parsed_output") or {}
    pred_company = stringify(perturbed_parsed.get("company", ""))
    gold_company = stringify(gold.get("company", ""))
    if pred_company and gold_company and pred_company != gold_company:
        if normalize_script_variants(pred_company) == normalize_script_variants(gold_company):
            return (
                "script_variant_preserved",
                "模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。",
            )
    return ("manual_review_needed", "无法由当前规则稳定归因")


def classify_ocr_confusable(bundle: Dict[str, Any]) -> Tuple[str, str]:
    control_input = bundle["control"]["sample"]["input"]
    perturbed_input = bundle["perturbed"]["sample"]["input"]
    if control_input != perturbed_input:
        normalized_control = to_half_width(control_input).upper()
        normalized_perturbed = to_half_width(perturbed_input).upper()
        if normalized_control != normalized_perturbed:
            return (
                "ocr_confusion_near_key_slot",
                "OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。",
            )
    return ("manual_review_needed", "无法由当前规则稳定归因")


def classify_trigger_shape(subtype_id: str, bundle: Dict[str, Any]) -> Tuple[str, str]:
    if subtype_id == "full_half_width":
        return classify_full_half_width(bundle)
    if subtype_id == "minor_typo":
        return classify_minor_typo(bundle)
    if subtype_id == "simp_trad":
        return classify_simp_trad(bundle)
    if subtype_id == "ocr_confusable":
        return classify_ocr_confusable(bundle)
    hint = bundle["perturbed"]["sample"].get("trigger_shape_hint")
    if hint:
        return str(hint), "根据数据集元数据回填触发形态，当前规则未单独覆盖该子类。"
    return ("manual_review_needed", "无法由当前规则稳定归因")


def parse_response_row(row: Dict[str, Any]) -> Dict[str, Any]:
    parsed = row.get("parsed_output")
    if not isinstance(parsed, dict):
        parsed = extract_json_object(row.get("raw_output", ""))
    return {**row, "parsed_output": parsed}


def build_analysis(
    problem_rows: Sequence[Dict[str, Any]],
    response_rows: Sequence[Dict[str, Any]],
    score_rows: Sequence[Dict[str, Any]],
    subtypes: Sequence[str],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    subtype_set = set(subtypes)
    problems_by_qid = {row["qid"]: row for row in problem_rows if row["subtype_id"] in subtype_set}
    pair_ids_by_subtype: Dict[str, List[str]] = defaultdict(list)
    for row in problem_rows:
        if row["subtype_id"] not in subtype_set:
            continue
        if row["pair_id"] not in pair_ids_by_subtype[row["subtype_id"]]:
            pair_ids_by_subtype[row["subtype_id"]].append(row["pair_id"])

    responses = {
        (row["qid"], row["model_id"], row["prompt_id"]): parse_response_row(row)
        for row in response_rows
        if row["qid"] in problems_by_qid
    }
    scores = {
        (row["qid"], row["model_id"], row["prompt_id"]): row
        for row in score_rows
        if row["qid"] in problems_by_qid
    }

    model_prompt_keys = sorted({(row["model_id"], row["prompt_id"]) for row in score_rows if row["qid"] in problems_by_qid})

    bucket: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    for qid, sample in problems_by_qid.items():
        for model_id, prompt_id in model_prompt_keys:
            score = scores.get((qid, model_id, prompt_id))
            response = responses.get((qid, model_id, prompt_id), {"raw_output": "", "parsed_output": None, "status": "missing"})
            pair_key = (model_id, prompt_id, sample["subtype_id"], sample["pair_id"])
            pair_bundle = bucket.setdefault(
                pair_key,
                {
                    "model_id": model_id,
                    "prompt_id": prompt_id,
                    "subtype_id": sample["subtype_id"],
                    "pair_id": sample["pair_id"],
                },
            )
            pair_bundle[sample["variant"]] = {
                "sample": sample,
                "score": score or {},
                "response": response,
            }

    case_rows: List[Dict[str, Any]] = []
    summary_rows: List[Dict[str, Any]] = []

    for model_id, prompt_id in model_prompt_keys:
        for subtype_id in subtypes:
            pair_keys = [
                (model_id, prompt_id, subtype_id, pair_id)
                for pair_id in pair_ids_by_subtype.get(subtype_id, [])
            ]
            pair_bundles = [bucket[pair_key] for pair_key in pair_keys if pair_key in bucket]

            complete_pairs = 0
            control_errors = 0
            trigger_errors = 0
            flip_pairs = 0
            reverse_flip_pairs = 0
            trigger_shapes: Counter[str] = Counter()
            representative_pair_id = ""

            for pair_bundle in pair_bundles:
                control = pair_bundle.get("control")
                perturbed = pair_bundle.get("perturbed")
                if not control or not perturbed:
                    continue

                control_score = control["score"].get("is_correct")
                perturbed_score = perturbed["score"].get("is_correct")
                outcome = pair_outcome(control_score, perturbed_score)

                if control_score in [0, 1] and perturbed_score in [0, 1]:
                    complete_pairs += 1
                    control_errors += int(control_score == 0)
                    trigger_errors += int(perturbed_score == 0)

                if outcome == "flip_case":
                    flip_pairs += 1
                    trigger_shape, trigger_explanation = classify_trigger_shape(subtype_id, pair_bundle)
                    trigger_shapes[trigger_shape] += 1
                    if not representative_pair_id:
                        representative_pair_id = pair_bundle["pair_id"]
                    case_rows.append(
                        {
                            "model_id": model_id,
                            "prompt_id": prompt_id,
                            "subtype_id": subtype_id,
                            "pair_id": pair_bundle["pair_id"],
                            "task_type": control["sample"]["task_type"],
                            "pair_outcome": outcome,
                            "control_qid": control["sample"]["qid"],
                            "perturbed_qid": perturbed["sample"]["qid"],
                            "control_input": control["sample"]["input"],
                            "perturbed_input": perturbed["sample"]["input"],
                            "gold": stringify(control["sample"]["gold"]),
                            "control_raw_output": stringify(control["response"].get("raw_output", "")),
                            "perturbed_raw_output": stringify(perturbed["response"].get("raw_output", "")),
                            "control_parsed_output": stringify(control["response"].get("parsed_output")),
                            "perturbed_parsed_output": stringify(perturbed["response"].get("parsed_output")),
                            "control_error_type": stringify(control["score"].get("error_type", "")),
                            "perturbed_error_type": stringify(perturbed["score"].get("error_type", "")),
                            "trigger_shape": trigger_shape,
                            "trigger_explanation": trigger_explanation,
                        }
                    )
                elif outcome == "reverse_flip":
                    reverse_flip_pairs += 1

            fr_control = 100.0 * control_errors / complete_pairs if complete_pairs else 0.0
            fr_trigger = 100.0 * trigger_errors / complete_pairs if complete_pairs else 0.0
            delta_pp = fr_trigger - fr_control
            top_trigger_shape = ""
            if trigger_shapes:
                top_trigger_shape = sorted(trigger_shapes.items(), key=lambda item: (-item[1], item[0]))[0][0]

            summary_rows.append(
                {
                    "model_id": model_id,
                    "prompt_id": prompt_id,
                    "subtype_id": subtype_id,
                    "total_pairs": str(complete_pairs),
                    "flip_pairs": str(flip_pairs),
                    "reverse_flip_pairs": str(reverse_flip_pairs),
                    "FR_control": f"{fr_control:.4f}",
                    "FR_trigger": f"{fr_trigger:.4f}",
                    "delta_pp": f"{delta_pp:.4f}",
                    "top_trigger_shape": top_trigger_shape,
                    "representative_pair_id": representative_pair_id,
                }
            )

    case_rows.sort(key=lambda row: (row["subtype_id"], row["model_id"], row["prompt_id"], row["pair_id"]))
    summary_rows.sort(key=lambda row: (row["subtype_id"], row["model_id"], row["prompt_id"]))
    return case_rows, summary_rows


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def build_markdown(summary_rows: Sequence[Dict[str, Any]], case_rows: Sequence[Dict[str, Any]]) -> str:
    overview_headers = [
        "subtype_id",
        "model_id",
        "prompt_id",
        "total_pairs",
        "flip_pairs",
        "delta_pp",
        "representative_pair_id",
    ]
    overview_rows = [
        [row[header] for header in overview_headers]
        for row in summary_rows
    ]

    case_headers = [
        "subtype_id",
        "model_id",
        "prompt_id",
        "pair_id",
        "task_type",
        "trigger_shape",
        "perturbed_error_type",
        "trigger_explanation",
    ]
    case_table_rows = [
        [row[header] for header in case_headers]
        for row in case_rows
    ]

    sections = [
        "# Focus3 翻转分析表",
        "",
        "## 表 1：跨模型触发概览",
        markdown_table(overview_headers, overview_rows),
        "",
        "## 表 2：代表性错误个案",
        markdown_table(case_headers, case_table_rows),
        "",
    ]
    return "\n".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export flip-case analysis tables for selected subtypes.")
    parser.add_argument("--problem-bank", required=True)
    parser.add_argument("--responses", nargs="+", required=True)
    parser.add_argument("--scores", nargs="+", required=True)
    parser.add_argument("--subtypes", required=True, help="Comma-separated subtype ids.")
    parser.add_argument("--out-cases", required=True)
    parser.add_argument("--out-summary", required=True)
    parser.add_argument("--out-markdown", required=True)
    args = parser.parse_args()

    subtypes = parse_csv_arg(args.subtypes)
    problem_rows = read_jsonl(args.problem_bank)
    response_rows = list(load_latest_jsonl(args.responses, ["qid", "model_id", "prompt_id"]).values())
    score_rows = list(load_latest_jsonl(args.scores, ["qid", "model_id", "prompt_id"]).values())

    case_rows, summary_rows = build_analysis(problem_rows, response_rows, score_rows, subtypes)

    write_csv(
        args.out_cases,
        case_rows,
        [
            "model_id",
            "prompt_id",
            "subtype_id",
            "pair_id",
            "task_type",
            "pair_outcome",
            "control_qid",
            "perturbed_qid",
            "control_input",
            "perturbed_input",
            "gold",
            "control_raw_output",
            "perturbed_raw_output",
            "control_parsed_output",
            "perturbed_parsed_output",
            "control_error_type",
            "perturbed_error_type",
            "trigger_shape",
            "trigger_explanation",
        ],
    )
    write_csv(
        args.out_summary,
        summary_rows,
        [
            "model_id",
            "prompt_id",
            "subtype_id",
            "total_pairs",
            "flip_pairs",
            "reverse_flip_pairs",
            "FR_control",
            "FR_trigger",
            "delta_pp",
            "top_trigger_shape",
            "representative_pair_id",
        ],
    )
    ensure_parent(args.out_markdown)
    Path(args.out_markdown).write_text(build_markdown(summary_rows, case_rows), encoding="utf-8")

    print(f"[done] cases={len(case_rows)} -> {args.out_cases}")
    print(f"[done] summary={len(summary_rows)} -> {args.out_summary}")
    print(f"[done] markdown -> {args.out_markdown}")


if __name__ == "__main__":
    main()
