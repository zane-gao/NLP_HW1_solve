from __future__ import annotations

import argparse
import csv
import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
import pandas as pd
import seaborn as sns

from scripts.common import read_jsonl


MODEL_ORDER = [
    "gpt-5.2",
    "gemini-3-flash",
    "DeepSeek-V3.2",
    "GLM-4.6",
    "Qwen3-235B-A22B-Instruct-2507",
]
MODEL_LABELS = {
    "gpt-5.2": "GPT-5.2",
    "gemini-3-flash": "Gemini",
    "DeepSeek-V3.2": "DeepSeek",
    "GLM-4.6": "GLM-4.6",
    "Qwen3-235B-A22B-Instruct-2507": "Qwen3-235B",
}
PROMPT_ORDER = ["P1", "P2", "P3", "P4"]
PROMPT_COLORS = {
    "P1": "#1F5A91",
    "P2": "#4C8DCB",
    "P3": "#C16A1B",
    "P4": "#A43B3B",
}
SUBTYPE_ORDER = ["simp_trad", "full_half_width", "ocr_confusable"]
SUBTYPE_LABELS = {
    "simp_trad": "Simp-Trad",
    "full_half_width": "Full/Half Width",
    "ocr_confusable": "OCR Confusable",
}
SUBTYPE_COLORS = {
    "simp_trad": "#1F5A91",
    "ocr_confusable": "#C16A1B",
    "full_half_width": "#A43B3B",
}
SUBTYPE_NOTES = {
    "simp_trad": "正式 C 成立",
    "ocr_confusable": "正式 C 成立",
    "full_half_width": "弱对照",
}
FIELD_LABELS = {"company": "公司", "date": "日期", "amount": "金额"}
DOMAIN_LABELS = {
    "announcement": "公告",
    "customer_service": "客服",
    "email": "邮件",
    "form_ocr": "表单 OCR",
    "im_chat": "即时聊天",
    "social_media": "社交媒体",
}
STYLE_LABELS = {
    "chat": "聊天",
    "doc": "文档",
    "form": "表单",
    "mail": "邮件",
    "social": "社媒",
}
INTENSITY_LABELS = {"light": "轻度", "medium": "中度", "hard": "重度"}
COMPOSITION_LABELS = {"single": "单扰动", "composite": "复合扰动"}


def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def setup_style() -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "font.family": "sans-serif",
            "font.sans-serif": ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "DejaVu Sans"],
            "axes.titlesize": 13,
            "axes.labelsize": 11,
            "axes.titleweight": "bold",
            "axes.edgecolor": "#444444",
            "axes.linewidth": 0.8,
            "axes.labelcolor": "#333333",
            "xtick.color": "#333333",
            "ytick.color": "#333333",
            "grid.color": "#D9D9D9",
            "grid.linewidth": 0.6,
            "legend.frameon": False,
            "legend.fontsize": 10,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.unicode_minus": False,
        }
    )


def read_csv_rows(path: str | Path) -> List[Dict[str, str]]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def savefig_multi(fig: plt.Figure, output_path: str | Path) -> None:
    base = Path(output_path)
    ensure_parent(base)
    stem = base.with_suffix("")
    for suffix in (".png", ".pdf"):
        fig.savefig(stem.with_suffix(suffix), bbox_inches="tight", facecolor="white")
    plt.close(fig)


def build_pair_scores(
    problem_bank: str,
    scores_path: str,
    subtype_filter: str = "simp_trad",
    task_type: str = "extraction",
) -> Dict[Tuple[str, str], List[Tuple[int, int]]]:
    problems = {row["qid"]: row for row in read_jsonl(problem_bank)}
    latest: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for row in read_jsonl(scores_path):
        latest[(row["qid"], row["model_id"], row["prompt_id"])] = row

    pair_bucket: Dict[Tuple[str, str, str], Dict[str, int]] = defaultdict(dict)
    for (qid, model_id, prompt_id), row in latest.items():
        problem = problems.get(qid)
        if not problem:
            continue
        if problem["subtype_id"] != subtype_filter or problem["task_type"] != task_type:
            continue
        if row.get("is_correct") not in [0, 1]:
            continue
        pair_bucket[(model_id, prompt_id, problem["pair_id"])][problem["variant"]] = int(row["is_correct"])

    grouped: Dict[Tuple[str, str], List[Tuple[int, int]]] = defaultdict(list)
    for (model_id, prompt_id, _pair_id), variants in pair_bucket.items():
        if "control" in variants and "perturbed" in variants:
            grouped[(model_id, prompt_id)].append((variants["control"], variants["perturbed"]))
    return grouped


def bootstrap_delta_ci(
    pairs: Sequence[Tuple[int, int]],
    num_bootstrap: int = 2000,
    seed: int = 42,
) -> Tuple[float, float, float]:
    if not pairs:
        return 0.0, 0.0, 0.0
    rng = random.Random(seed)
    deltas: List[float] = []
    n = len(pairs)
    for _ in range(num_bootstrap):
        sample = [pairs[rng.randrange(n)] for _ in range(n)]
        control_err = sum(1 for control, _ in sample if control == 0)
        perturbed_err = sum(1 for _, perturbed in sample if perturbed == 0)
        deltas.append(100.0 * (perturbed_err - control_err) / n)
    deltas.sort()
    low = deltas[int(0.025 * len(deltas))]
    high = deltas[int(0.975 * len(deltas))]
    mean = sum(deltas) / len(deltas)
    return mean, low, high


def aggregate_mean_delta(rows: List[Dict[str, str]]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    df["delta_pp"] = df["delta_pp"].astype(float)
    return df.groupby(["subtype_id", "group_value"], as_index=False)["delta_pp"].mean()


def ordered_categories(df: pd.DataFrame) -> List[str]:
    score = df.groupby("group_value")["delta_pp"].max().sort_values(ascending=False)
    return score.index.tolist()


def heatmap_cmap() -> LinearSegmentedColormap:
    return LinearSegmentedColormap.from_list(
        "focus3_heat",
        ["#EEF4FB", "#B7D0E8", "#F1D49B", "#D47D57", "#8E2F2F"],
    )


def plot_delta_heatmap(summary_csv: str, output_path: str) -> None:
    rows = read_csv_rows(summary_csv)
    df = pd.DataFrame(rows)
    df["delta_pp"] = df["delta_pp"].astype(float)
    df["A_flag"] = df["A_flag"].astype(int)
    fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.8), sharey=True, constrained_layout=True)
    vmax = max(80.0, float(df["delta_pp"].max()) + 5.0)
    cmap = heatmap_cmap()
    cbar_ax = fig.add_axes([0.92, 0.16, 0.015, 0.7])

    for idx, (ax, subtype) in enumerate(zip(axes, SUBTYPE_ORDER)):
        sub = df[df["subtype_id"] == subtype].copy()
        pivot = sub.pivot(index="model_id", columns="prompt_id", values="delta_pp").reindex(index=MODEL_ORDER, columns=PROMPT_ORDER)
        a_pivot = sub.pivot(index="model_id", columns="prompt_id", values="A_flag").reindex(index=MODEL_ORDER, columns=PROMPT_ORDER)
        annot = pivot.copy().astype(object)
        for r in pivot.index:
            for c in pivot.columns:
                value = pivot.loc[r, c]
                if pd.isna(value):
                    annot.loc[r, c] = ""
                else:
                    suffix = "\nA" if int(a_pivot.loc[r, c]) == 1 else ""
                    annot.loc[r, c] = f"{value:.1f}{suffix}"
        sns.heatmap(
            pivot,
            ax=ax,
            cmap=cmap,
            vmin=0,
            vmax=vmax,
            annot=annot.values,
            fmt="",
            linewidths=0.8,
            linecolor="white",
            cbar=idx == 2,
            cbar_ax=cbar_ax if idx == 2 else None,
            annot_kws={"fontsize": 9, "color": "#202020"},
        )
        ax.set_title(SUBTYPE_LABELS[subtype], pad=12)
        ax.set_xlabel("提示模板")
        ax.set_xticklabels(PROMPT_ORDER, rotation=0)
        if idx == 0:
            ax.set_ylabel("模型")
            ax.set_yticklabels([MODEL_LABELS[m] for m in MODEL_ORDER], rotation=0)
        else:
            ax.set_ylabel("")
            ax.set_yticklabels([])
        ax.text(0.02, 1.03, SUBTYPE_NOTES[subtype], transform=ax.transAxes, fontsize=9.5, color="#6B6B6B")

    cbar_ax.set_ylabel(r"$\Delta_{pp}$", rotation=270, labelpad=14)
    fig.suptitle("五模型四提示在三类机制上的 extraction 效应", y=1.03, fontsize=14, fontweight="bold")
    savefig_multi(fig, output_path)


def plot_simp_trad_effect(summary_csv: str, scores_path: str, problem_bank: str, output_path: str) -> None:
    summary_rows = read_csv_rows(summary_csv)
    pair_scores = build_pair_scores(problem_bank, scores_path, subtype_filter="simp_trad", task_type="extraction")

    plot_rows: List[Dict[str, Any]] = []
    for row in summary_rows:
        if row["subtype_id"] != "simp_trad":
            continue
        model_id = row["model_id"]
        prompt_id = row["prompt_id"]
        seed = MODEL_ORDER.index(model_id) * 100 + PROMPT_ORDER.index(prompt_id)
        _mean, low, high = bootstrap_delta_ci(pair_scores.get((model_id, prompt_id), []), seed=seed)
        plot_rows.append(
            {
                "model_id": model_id,
                "prompt_id": prompt_id,
                "delta_pp": float(row["delta_pp"]),
                "low": low,
                "high": high,
                "label": f"{MODEL_LABELS[model_id]}  {prompt_id}",
            }
        )
    df = pd.DataFrame(plot_rows)
    df["order"] = [MODEL_ORDER.index(m) * 10 + PROMPT_ORDER.index(p) for m, p in zip(df["model_id"], df["prompt_id"])]
    df = df.sort_values("order", ascending=False).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(10.6, 7.2), constrained_layout=True)
    ax.axvspan(15, max(85.0, df["high"].max() + 4), color="#FBE8D2", alpha=0.45, zorder=0)
    ax.axvline(15, linestyle="--", color="#7A3E00", linewidth=1.2)
    ax.axvline(0, color="#999999", linewidth=0.8)

    y_positions = list(range(len(df)))
    for y, row in zip(y_positions, df.itertuples(index=False)):
        color = PROMPT_COLORS[row.prompt_id]
        ax.hlines(y, row.low, row.high, color=color, linewidth=2.2, alpha=0.95)
        ax.plot(row.delta_pp, y, "o", color=color, markersize=6.5)
        ax.text(row.high + 1.2, y, f"{row.delta_pp:.1f}", va="center", fontsize=8.8, color="#333333")

    ax.set_yticks(y_positions)
    ax.set_yticklabels(df["label"])
    ax.set_xlabel(r"$\Delta_{pp}$（extraction）")
    ax.set_ylabel("")
    ax.set_title("simp_trad 的效应量与 bootstrap 置信区间")
    ax.text(15.5, len(df) - 0.2, "A 阈值", fontsize=9, color="#7A3E00", va="bottom")
    legend = [Line2D([0], [0], marker="o", color=c, linestyle="", label=p) for p, c in PROMPT_COLORS.items()]
    ax.legend(handles=legend, title="提示", loc="lower right")
    savefig_multi(fig, output_path)


def plot_field_delta(field_csv: str, output_path: str) -> None:
    rows = read_csv_rows(field_csv)
    df = aggregate_mean_delta(rows)
    fig, axes = plt.subplots(1, 3, figsize=(12.8, 4.3), sharex=True, constrained_layout=True)
    xmax = max(100.0, float(df["delta_pp"].max()) + 8.0)

    for ax, subtype in zip(axes, SUBTYPE_ORDER):
        sub = df[df["subtype_id"] == subtype].copy()
        sub["label"] = sub["group_value"].map(FIELD_LABELS).fillna(sub["group_value"])
        sub = sub.sort_values("delta_pp", ascending=True)
        color = SUBTYPE_COLORS[subtype]
        ax.hlines(sub["label"], 0, sub["delta_pp"], color=color, linewidth=2.2, alpha=0.8)
        ax.plot(sub["delta_pp"], sub["label"], "o", color=color, markersize=6.5)
        for row in sub.itertuples(index=False):
            ax.text(row.delta_pp + 1.5, row.label, f"{row.delta_pp:.1f}", va="center", fontsize=8.8)
        ax.set_title(SUBTYPE_LABELS[subtype])
        ax.set_xlim(0, xmax)
        ax.set_xlabel(r"平均 $\Delta_{pp}$")
        ax.set_ylabel("")
        ax.grid(True, axis="x")
        ax.grid(False, axis="y")
    fig.suptitle("字段级脆弱性分布", y=1.03, fontsize=14, fontweight="bold")
    savefig_multi(fig, output_path)


def add_group_panel(ax: plt.Axes, df: pd.DataFrame, title: str, label_map: Dict[str, str]) -> None:
    order = ordered_categories(df)
    display_order = [label_map.get(v, v) for v in order]
    base_positions = {name: idx for idx, name in enumerate(display_order)}
    offsets = {"simp_trad": -0.22, "ocr_confusable": 0.0, "full_half_width": 0.22}

    for subtype in SUBTYPE_ORDER:
        sub = df[df["subtype_id"] == subtype].copy()
        if sub.empty:
            continue
        sub["label"] = sub["group_value"].map(label_map).fillna(sub["group_value"])
        sub = sub.set_index("label").reindex(display_order).dropna(how="all").reset_index()
        y = [base_positions[label] + offsets[subtype] for label in sub["label"]]
        ax.hlines(y, 0, sub["delta_pp"], color=SUBTYPE_COLORS[subtype], linewidth=1.7, alpha=0.75)
        ax.plot(sub["delta_pp"], y, "o", color=SUBTYPE_COLORS[subtype], markersize=5.5, label=SUBTYPE_LABELS[subtype])

    ax.axvline(0, color="#999999", linewidth=0.8)
    ax.set_yticks(list(base_positions.values()))
    ax.set_yticklabels(display_order)
    ax.set_title(title)
    ax.set_xlabel(r"平均 $\Delta_{pp}$")
    ax.grid(True, axis="x")
    ax.grid(False, axis="y")


def plot_domain_intensity(domain_csv: str, style_csv: str, intensity_csv: str, composition_csv: str, output_path: str) -> None:
    domain_df = aggregate_mean_delta(read_csv_rows(domain_csv))
    style_df = aggregate_mean_delta(read_csv_rows(style_csv))
    intensity_df = aggregate_mean_delta(read_csv_rows(intensity_csv))
    composition_df = aggregate_mean_delta(read_csv_rows(composition_csv))

    fig, axes = plt.subplots(2, 2, figsize=(13.4, 9.4), constrained_layout=True)
    add_group_panel(axes[0, 0], domain_df, "场景", DOMAIN_LABELS)
    add_group_panel(axes[0, 1], style_df, "文本体裁", STYLE_LABELS)
    add_group_panel(axes[1, 0], intensity_df, "扰动强度", INTENSITY_LABELS)
    add_group_panel(axes[1, 1], composition_df, "扰动组合", COMPOSITION_LABELS)

    handles = [Line2D([0], [0], marker="o", color=SUBTYPE_COLORS[s], linestyle="", label=SUBTYPE_LABELS[s]) for s in SUBTYPE_ORDER]
    fig.legend(handles=handles, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.02))
    fig.suptitle("场景、体裁与扰动强度的分层效应", y=1.05, fontsize=14, fontweight="bold")
    savefig_multi(fig, output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Focus3 paper figures.")
    parser.add_argument("--summary-extraction", required=True)
    parser.add_argument("--scores-merged", required=True)
    parser.add_argument("--problem-bank", required=True)
    parser.add_argument("--field-summary", required=True)
    parser.add_argument("--domain-summary", required=True)
    parser.add_argument("--style-summary", required=True)
    parser.add_argument("--intensity-summary", required=True)
    parser.add_argument("--composition-summary", required=True)
    parser.add_argument("--out-dir", default="paper/figures")
    args = parser.parse_args()

    setup_style()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    plot_delta_heatmap(args.summary_extraction, out_dir / "delta_heatmap.png")
    plot_simp_trad_effect(
        args.summary_extraction,
        args.scores_merged,
        args.problem_bank,
        out_dir / "simp_trad_effect_ci.png",
    )
    plot_field_delta(args.field_summary, out_dir / "field_delta.png")
    plot_domain_intensity(
        args.domain_summary,
        args.style_summary,
        args.intensity_summary,
        args.composition_summary,
        out_dir / "domain_intensity.png",
    )
    print(f"[done] figures -> {out_dir}")


if __name__ == "__main__":
    main()
