from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np


SUBTYPES = ["simp_trad", "ocr_confusable", "full_half_width"]
SUBTYPE_LABELS = ["简繁变体", "OCR 易混字符", "全半角混排"]
PROMPTS = ["P1", "P2", "P3", "P4"]
METHODS = ["none", "script_numeric", "sccp_strict"]
METHOD_LABELS = ["模型原始输出", "字符与数值算子", "SCCP（严格）"]
METHOD_COLORS = ["#8C564B", "#E69F00", "#0072B2"]
BLUE = "#0072B2"
ORANGE = "#E69F00"
GREEN = "#009E73"
VERMILLION = "#D55E00"
GRAY = "#6B7280"


def read_csv(path: str | Path) -> List[Dict[str, str]]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def setup_style() -> None:
    preferred_font = "DejaVu Sans"
    for font_path in [
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
    ]:
        path = Path(font_path)
        if path.exists():
            font_manager.fontManager.addfont(str(path))
            preferred_font = font_manager.FontProperties(fname=str(path)).get_name()
            break
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "font.family": preferred_font,
            "font.sans-serif": [preferred_font, "Hiragino Sans GB", "Arial Unicode MS", "DejaVu Sans"],
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.edgecolor": "#333333",
            "axes.labelcolor": "#222222",
            "xtick.color": "#222222",
            "ytick.color": "#222222",
            "axes.unicode_minus": False,
        }
    )


def savefig_multi(fig: plt.Figure, output_path: str | Path) -> None:
    base = Path(output_path)
    base.parent.mkdir(parents=True, exist_ok=True)
    stem = base.with_suffix("")
    for suffix in [".png", ".pdf"]:
        fig.savefig(stem.with_suffix(suffix), bbox_inches="tight", facecolor="white")
    plt.close(fig)


def add_box(ax: plt.Axes, center: Tuple[float, float], text: str, color: str, width: float = 1.8, height: float = 0.56) -> None:
    x, y = center
    rect = plt.Rectangle(
        (x - width / 2, y - height / 2),
        width,
        height,
        facecolor=color,
        alpha=0.12,
        edgecolor=color,
        linewidth=1.2,
    )
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center", fontsize=9.2, color="#1F2937")


def add_arrow(ax: plt.Axes, start: Tuple[float, float], end: Tuple[float, float], color: str = "#4B5563") -> None:
    ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "lw": 1.25, "color": color})


def plot_canonical_gap(output: str) -> None:
    setup_style()
    fig, ax = plt.subplots(figsize=(7.6, 3.15))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    add_box(ax, (1.25, 3.0), "clean text\nentity-A1", BLUE)
    add_box(ax, (1.25, 1.05), "noisy text\nentity-AI", ORANGE)
    add_box(ax, (4.05, 2.0), "same latent fact\n(company,date,amount)", GRAY, width=2.3)
    add_box(ax, (6.95, 2.95), "surface field\nentity-AI", VERMILLION)
    add_box(ax, (6.95, 1.05), "canonical field\nentity-A1", BLUE)
    add_box(ax, (8.95, 2.0), "schema space\nΩ", GREEN, width=1.35)
    add_arrow(ax, (2.15, 3.0), (3.0, 2.25))
    add_arrow(ax, (2.15, 1.05), (3.0, 1.75))
    add_arrow(ax, (5.2, 2.1), (6.05, 2.75), VERMILLION)
    add_arrow(ax, (5.2, 1.9), (6.05, 1.25), BLUE)
    add_arrow(ax, (7.9, 1.05), (8.25, 1.8), GREEN)
    add_arrow(ax, (7.9, 2.95), (8.25, 2.2), VERMILLION)
    ax.text(4.05, 0.35, "Semantic invariance holds", ha="center", fontsize=9, color="#4B5563")
    ax.text(7.0, 3.68, "canonicalization gap", ha="center", fontsize=10, fontweight="semibold", color=VERMILLION)
    ax.text(8.95, 0.35, "SCCP intervenes at projection time", ha="center", fontsize=9, color="#374151")
    savefig_multi(fig, output)


def plot_sccp_architecture(output: str) -> None:
    setup_style()
    fig, ax = plt.subplots(figsize=(8.5, 3.45))
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 4.7)
    ax.axis("off")

    add_box(ax, (0.95, 2.35), "表面字段\n模型输出", VERMILLION)
    add_box(ax, (2.95, 2.35), "模式路由器", BLUE, width=1.55)
    add_box(ax, (5.0, 3.55), "字形/宽度\n规范算子", ORANGE)
    add_box(ax, (5.0, 2.35), "数值 OCR\n恢复算子", ORANGE)
    add_box(ax, (5.0, 1.15), "实体注册表\n投影算子", GREEN)
    add_box(ax, (7.25, 2.35), "规范候选集\n与字段约束", GRAY)
    add_box(ax, (9.35, 2.35), "规范字段\n验证输出", BLUE)

    add_arrow(ax, (1.85, 2.35), (2.18, 2.35))
    add_arrow(ax, (3.72, 2.35), (4.1, 3.35), ORANGE)
    add_arrow(ax, (3.72, 2.35), (4.1, 2.35), ORANGE)
    add_arrow(ax, (3.72, 2.35), (4.1, 1.35), GREEN)
    add_arrow(ax, (5.9, 3.55), (6.35, 2.62), GRAY)
    add_arrow(ax, (5.9, 2.35), (6.35, 2.35), GRAY)
    add_arrow(ax, (5.9, 1.15), (6.35, 2.08), GRAY)
    add_arrow(ax, (8.15, 2.35), (8.45, 2.35), BLUE)
    ax.plot([9.35, 9.35, 2.95, 2.95], [2.02, 0.45, 0.45, 2.02], color="#9CA3AF", linestyle="--", lw=1.0)
    ax.text(6.15, 0.22, "可追踪的一致性验证回路", ha="center", fontsize=8.8, color="#4B5563")
    ax.text(5.05, 4.35, "字段类型化规范算子", ha="center", fontsize=10, fontweight="semibold")
    savefig_multi(fig, output)


def plot_prompt_failure(cell_summary: str, output: str) -> None:
    rows = [r for r in read_csv(cell_summary) if r["repair_mode"] == "none" and r["subtype_id"] in SUBTYPES]
    matrix: List[List[float]] = []
    for subtype in SUBTYPES:
        subtype_values = []
        for prompt in PROMPTS:
            vals = [float(r["delta_pp"]) for r in rows if r["subtype_id"] == subtype and r["prompt_id"] == prompt]
            subtype_values.append(sum(vals) / len(vals) if vals else 0.0)
        matrix.append(subtype_values)

    setup_style()
    fig, ax = plt.subplots(figsize=(6.8, 3.2))
    data = np.array(matrix)
    image = ax.imshow(data, cmap="YlOrRd", vmin=0, vmax=max(75.0, float(data.max())))
    ax.set_xticks(range(len(PROMPTS)))
    ax.set_xticklabels(PROMPTS)
    ax.set_yticks(range(len(SUBTYPE_LABELS)))
    ax.set_yticklabels(SUBTYPE_LABELS)
    ax.set_xlabel("提示模板")
    ax.set_ylabel("")
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            color = "white" if data[i, j] > 45 else "#222222"
            ax.text(j, i, f"{data[i, j]:.1f}", ha="center", va="center", fontsize=9, color=color)
    cbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.03)
    cbar.set_label("不变性差距（百分点）")
    ax.set_title("更强提示未消除规范不变性断裂", fontsize=11)
    savefig_multi(fig, output)


def plot_main_result(c_summary: str, output: str) -> None:
    rows = read_csv(c_summary)
    values: Dict[Tuple[str, str], float] = {
        (r["repair_mode"], r["subtype_id"]): float(r["mean_delta_pp"]) for r in rows
    }
    setup_style()
    fig, ax = plt.subplots(figsize=(7.4, 3.9))
    x = np.arange(len(SUBTYPES))
    width = 0.18
    hatches = ["", "//", "", ".."]
    for idx, method in enumerate(METHODS):
        offsets = x + (idx - 1.0) * width
        ys = [values.get((method, subtype), 0.0) for subtype in SUBTYPES]
        bars = ax.bar(
            offsets,
            ys,
            width=width,
            color=METHOD_COLORS[idx],
            edgecolor="#222222",
            linewidth=0.5,
            hatch=hatches[idx],
            label=METHOD_LABELS[idx],
        )
        for bar, y in zip(bars, ys):
            ax.text(bar.get_x() + bar.get_width() / 2, y + 1.0, f"{y:.1f}", ha="center", va="bottom", fontsize=8)
    ax.axhline(15, color="#555555", linewidth=1.0, linestyle="--")
    ax.text(2.32, 16.2, "15 pp", ha="right", va="bottom", fontsize=8, color="#444444")
    ax.set_xticks(x)
    ax.set_xticklabels(SUBTYPE_LABELS)
    ax.set_ylabel("不变性差距（百分点）")
    ax.set_ylim(0, 76)
    ax.grid(axis="y", color="#E0E0E0", linewidth=0.6)
    ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.18), frameon=False)
    savefig_multi(fig, output)


def plot_coverage_boundary(coverage_summary: str, output: str) -> None:
    rows = [r for r in read_csv(coverage_summary) if r["score_set"] == "sccp_strict" and r["subtype_id"] == "ocr_confusable"]
    by_cov = {r["coverage"]: float(r["mean_delta_pp"]) for r in rows}
    setup_style()
    fig, ax = plt.subplots(figsize=(5.4, 3.5))
    labels = ["全部", "已登录", "未登录"]
    values = [by_cov.get("all", 0.0), by_cov.get("seen", 0.0), by_cov.get("unseen", 0.0)]
    colors = ["#0072B2", "#009E73", "#D55E00"]
    bars = ax.bar(labels, values, color=colors, edgecolor="#222222", linewidth=0.5)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 1.0, f"{value:.1f}", ha="center", va="bottom", fontsize=9)
    ax.axhline(15, color="#555555", linewidth=1.0, linestyle="--")
    ax.set_ylabel("SCCP 后 OCR 差距（百分点）")
    ax.set_ylim(0, 42)
    ax.grid(axis="y", color="#E0E0E0", linewidth=0.6)
    ax.set_title("实体覆盖率是剩余开放边界", fontsize=11)
    savefig_multi(fig, output)


def main() -> None:
    parser = argparse.ArgumentParser(description="绘制 SCCP 正式论文图表。")
    parser.add_argument("--cell-summary", default="runs/sccp_summary_cells.csv")
    parser.add_argument("--c-summary", default="runs/sccp_c_summary.csv")
    parser.add_argument("--coverage-summary", default="runs/registry_coverage_summary.csv")
    parser.add_argument("--output-dir", default="paper/figures")
    args = parser.parse_args()

    out = Path(args.output_dir)
    plot_canonical_gap(out / "sccp_canonical_gap.pdf")
    plot_sccp_architecture(out / "sccp_architecture.pdf")
    # 两组别名同时刷新，避免论文正文和历史文档引用到过期图。
    plot_prompt_failure(args.cell_summary, out / "prompt_failure_heatmap.pdf")
    plot_prompt_failure(args.cell_summary, out / "sccp_prompt_invariance.pdf")
    plot_main_result(args.c_summary, out / "sccp_main_result.pdf")
    plot_main_result(args.c_summary, out / "sccp_main_results.pdf")
    plot_coverage_boundary(args.coverage_summary, out / "sccp_coverage_boundary.pdf")
    print(f"[done] SCCP figures -> {out}")


if __name__ == "__main__":
    main()
