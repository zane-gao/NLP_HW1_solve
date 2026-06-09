from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, List

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


SUBTYPE_ORDER = ["simp_trad", "ocr_confusable", "full_half_width"]
SUBTYPE_LABELS = {
    "simp_trad": "Simp-Trad",
    "ocr_confusable": "OCR Confusable",
    "full_half_width": "Full/Half Width",
}
MODE_ORDER = ["none", "script_numeric", "field_aware"]
MODE_LABELS = {
    "none": "Baseline",
    "script_numeric": "Script+Numeric",
    "field_aware": "HDR/FND",
}
MODE_COLORS = {
    "none": "#A43B3B",
    "script_numeric": "#C16A1B",
    "field_aware": "#1F5A91",
}


def read_csv_rows(path: str | Path) -> List[Dict[str, str]]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def savefig_multi(fig: plt.Figure, output_path: str | Path) -> None:
    base = Path(output_path)
    base.parent.mkdir(parents=True, exist_ok=True)
    stem = base.with_suffix("")
    for suffix in [".png", ".pdf"]:
        fig.savefig(stem.with_suffix(suffix), bbox_inches="tight", facecolor="white")
    plt.close(fig)


def setup_style() -> None:
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "font.family": "sans-serif",
            "font.sans-serif": ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS", "DejaVu Sans"],
            "axes.unicode_minus": False,
            "axes.edgecolor": "#444444",
            "axes.labelcolor": "#333333",
            "xtick.color": "#333333",
            "ytick.color": "#333333",
        }
    )


def plot_delta_by_mode(c_summary: str, output_path: str) -> None:
    rows = read_csv_rows(c_summary)
    values = {(row["repair_mode"], row["subtype_id"]): float(row["mean_delta_pp"]) for row in rows}
    setup_style()
    fig, ax = plt.subplots(figsize=(9.6, 5.0))
    width = 0.24
    x_positions = list(range(len(SUBTYPE_ORDER)))
    for idx, mode in enumerate(MODE_ORDER):
        offsets = [x + (idx - 1) * width for x in x_positions]
        ys = [values.get((mode, subtype), 0.0) for subtype in SUBTYPE_ORDER]
        bars = ax.bar(offsets, ys, width=width, color=MODE_COLORS[mode], label=MODE_LABELS[mode])
        for bar, value in zip(bars, ys):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.0, f"{value:.1f}", ha="center", va="bottom", fontsize=9)
    ax.axhline(15, color="#777777", linewidth=1.0, linestyle="--")
    ax.text(len(SUBTYPE_ORDER) - 0.2, 15.8, "A threshold", ha="right", va="bottom", fontsize=9, color="#555555")
    ax.set_xticks(x_positions)
    ax.set_xticklabels([SUBTYPE_LABELS[s] for s in SUBTYPE_ORDER])
    ax.set_ylabel(r"Mean $\Delta_{pp}$")
    ax.set_title("HDR-Harness offline repair effect")
    ax.legend(loc="upper right")
    ax.set_ylim(0, max(75, max(values.values()) + 10))
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.6)
    savefig_multi(fig, output_path)


def plot_c_flag(c_summary: str, output_path: str) -> None:
    rows = read_csv_rows(c_summary)
    values = {(row["repair_mode"], row["subtype_id"]): int(row["models_with_B"]) for row in rows}
    setup_style()
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    width = 0.24
    x_positions = list(range(len(SUBTYPE_ORDER)))
    for idx, mode in enumerate(MODE_ORDER):
        offsets = [x + (idx - 1) * width for x in x_positions]
        ys = [values.get((mode, subtype), 0) for subtype in SUBTYPE_ORDER]
        bars = ax.bar(offsets, ys, width=width, color=MODE_COLORS[mode], label=MODE_LABELS[mode])
        for bar, value in zip(bars, ys):
            ax.text(bar.get_x() + bar.get_width() / 2, value + 0.08, str(value), ha="center", va="bottom", fontsize=9)
    ax.axhline(5, color="#777777", linewidth=1.0, linestyle="--")
    ax.set_xticks(x_positions)
    ax.set_xticklabels([SUBTYPE_LABELS[s] for s in SUBTYPE_ORDER])
    ax.set_ylabel("Models satisfying B")
    ax.set_title("C-level evidence disappears after HDR/FND repair")
    ax.set_ylim(0, 5.8)
    ax.legend(loc="upper right")
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.6)
    savefig_multi(fig, output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="绘制 HDR 修复效果图")
    parser.add_argument("--c-summary", default="runs/repair_c_summary.csv")
    parser.add_argument("--delta-output", default="paper/figures/repair_delta_by_mode.pdf")
    parser.add_argument("--c-output", default="paper/figures/repair_c_by_mode.pdf")
    args = parser.parse_args()

    plot_delta_by_mode(args.c_summary, args.delta_output)
    plot_c_flag(args.c_summary, args.c_output)
    print(f"[done] figures -> {Path(args.delta_output).with_suffix('.png')}, {Path(args.c_output).with_suffix('.png')}")


if __name__ == "__main__":
    main()
