from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import extract_json_object


BODY_CASE_SELECTION = [
    ("full_half_width", "gpt-5.2", "P1", "pair_cls_full_half_width_001"),
    ("minor_typo", "gpt-5.2", "P1", "pair_ex_minor_typo_002"),
    ("simp_trad", "gpt-5.2", "P1", "pair_ex_simp_trad_003"),
]


def read_csv_rows(path: str | Path) -> List[Dict[str, str]]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv_rows(path: str | Path, rows: Iterable[Dict[str, str]], fieldnames: Sequence[str]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def compact_json_like(text: str) -> str:
    parsed = extract_json_object(text)
    if isinstance(parsed, dict):
        return json.dumps(parsed, ensure_ascii=False, separators=(",", ":"))
    return text


def clean_text(text: str, newline_token: str) -> str:
    text = compact_json_like(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    cleaned = newline_token.join(lines)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def markdown_cell(text: str) -> str:
    return clean_text(text, "<br>").replace("|", "\\|")


def csv_cell(text: str) -> str:
    return clean_text(text, " / ")


def select_body_rows(case_rows: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    keyed = {
        (row["subtype_id"], row["model_id"], row["prompt_id"], row["pair_id"]): row
        for row in case_rows
    }
    selected: List[Dict[str, str]] = []
    for key in BODY_CASE_SELECTION:
        row = keyed.get(key)
        if row is None:
            raise ValueError(f"missing body case row: {key}")
        selected.append(row)
    return selected


def build_conclusion_lines(summary_rows: Sequence[Dict[str, str]]) -> List[str]:
    def has_flip(model_id: str, subtype_id: str) -> bool:
        return any(
            row["model_id"] == model_id and row["subtype_id"] == subtype_id and int(row["flip_pairs"]) > 0
            for row in summary_rows
        )

    simp_models = ["gpt-5.2", "gemini-3-flash", "DeepSeek-V3.2"]
    simp_all = all(has_flip(model_id, "simp_trad") for model_id in simp_models)
    if simp_all:
        line1 = (
            "在当前 `GPT-5.2`、`gemini-3-flash`、`DeepSeek-V3.2` 三模型对照下，`simp_trad` 继续稳定复现，"
            "说明简繁混排导致的字段规范化缺失具有跨模型一致性。"
        )
    else:
        line1 = (
            "在当前三模型对照下，`simp_trad` 尚未在全部模型继续复现，暂时只能认定它在部分模型上稳定存在。"
        )

    fhw_non_gpt = has_flip("gemini-3-flash", "full_half_width") or has_flip("DeepSeek-V3.2", "full_half_width")
    typo_non_gpt = has_flip("gemini-3-flash", "minor_typo") or has_flip("DeepSeek-V3.2", "minor_typo")
    if not fhw_non_gpt and not typo_non_gpt:
        line2 = (
            "`minor_typo` 与 `full_half_width` 目前仍停留在 `gpt-5.2` 单模型现象，"
            "还不足以作为稳定跨模型机制下结论。"
        )
    else:
        line2 = (
            "`minor_typo` 与 `full_half_width` 已开始在非 GPT 模型上出现翻转，"
            "但当前证据仍弱于 `simp_trad`。"
        )
    return [line1, line2]


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def build_body_markdown(summary_rows: Sequence[Dict[str, str]], body_rows: Sequence[Dict[str, str]]) -> str:
    overview_headers = [
        "subtype_id",
        "model_id",
        "prompt_id",
        "total_pairs",
        "flip_pairs",
        "delta_pp",
        "representative_pair_id",
    ]
    overview_rows = [[row[header] for header in overview_headers] for row in summary_rows]

    case_headers = ["subtype_id", "pair_id", "控制句", "扰动句", "模型输出", "机制解释"]
    case_rows = [
        [
            row["subtype_id"],
            row["pair_id"],
            markdown_cell(row["control_input"]),
            markdown_cell(row["perturbed_input"]),
            markdown_cell(row["perturbed_raw_output"]),
            markdown_cell(row["trigger_explanation"]),
        ]
        for row in body_rows
    ]

    line1, line2 = build_conclusion_lines(summary_rows)
    return "\n".join(
        [
            "### 3.4 Focus3 跨模型初筛结果",
            "",
            markdown_table(overview_headers, overview_rows),
            "",
            f"- {line1}",
            f"- {line2}",
            "",
            "### 4.1 代表性翻转样例",
            "",
            markdown_table(case_headers, case_rows),
            "",
            "- 固定 8 条案例完整表放入附录。",
            "",
        ]
    )


def build_appendix_markdown(case_rows: Sequence[Dict[str, str]]) -> str:
    headers = ["subtype_id", "model_id", "prompt_id", "pair_id", "task_type", "控制句", "扰动句", "模型输出", "机制解释"]
    rows = [
        [
            row["subtype_id"],
            row["model_id"],
            row["prompt_id"],
            row["pair_id"],
            row["task_type"],
            markdown_cell(row["control_input"]),
            markdown_cell(row["perturbed_input"]),
            markdown_cell(row["perturbed_raw_output"]),
            markdown_cell(row["trigger_explanation"]),
        ]
        for row in case_rows
    ]
    return "\n".join(
        [
            "### A.1 Focus3 八条翻转案例总表",
            "",
            markdown_table(headers, rows),
            "",
        ]
    )


def build_paper_rows(case_rows: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    output_rows: List[Dict[str, str]] = []
    for row in case_rows:
        output_rows.append(
            {
                "subtype_id": row["subtype_id"],
                "model_id": row["model_id"],
                "prompt_id": row["prompt_id"],
                "pair_id": row["pair_id"],
                "task_type": row["task_type"],
                "控制句": csv_cell(row["control_input"]),
                "扰动句": csv_cell(row["perturbed_input"]),
                "模型输出": csv_cell(row["perturbed_raw_output"]),
                "机制解释": csv_cell(row["trigger_explanation"]),
            }
        )
    return output_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Export body and appendix tables for the fixed Focus3 paper cases.")
    parser.add_argument("--case-csv", required=True)
    parser.add_argument("--summary-csv", required=True)
    parser.add_argument("--out-body-md", required=True)
    parser.add_argument("--out-appendix-md", required=True)
    parser.add_argument("--out-paper-csv", required=True)
    args = parser.parse_args()

    case_rows = read_csv_rows(args.case_csv)
    summary_rows = read_csv_rows(args.summary_csv)
    body_rows = select_body_rows(case_rows)
    paper_rows = build_paper_rows(case_rows)

    Path(args.out_body_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_body_md).write_text(build_body_markdown(summary_rows, body_rows), encoding="utf-8")
    Path(args.out_appendix_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_appendix_md).write_text(build_appendix_markdown(case_rows), encoding="utf-8")
    write_csv_rows(
        args.out_paper_csv,
        paper_rows,
        ["subtype_id", "model_id", "prompt_id", "pair_id", "task_type", "控制句", "扰动句", "模型输出", "机制解释"],
    )

    print(f"[done] body_md -> {args.out_body_md}")
    print(f"[done] appendix_md -> {args.out_appendix_md}")
    print(f"[done] paper_csv={len(paper_rows)} -> {args.out_paper_csv}")


if __name__ == "__main__":
    main()
