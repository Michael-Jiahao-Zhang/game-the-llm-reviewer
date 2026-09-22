"""figures4papers house style (ChenLiu-1996/figures4papers): PALETTE, FigureStyle, apply_publication_style, create_subplots, grouped bars, heatmaps and reproducible pdf plus png export."""
import os
from dataclasses import dataclass
from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

PALETTE = {
    "blue_main": "#0F4D92",
    "blue_secondary": "#3775BA",
    "green_1": "#DDF3DE",
    "green_2": "#AADCA9",
    "green_3": "#8BCF8B",
    "red_1": "#F6CFCB",
    "red_2": "#E9A6A1",
    "red_strong": "#B64342",
    "neutral": "#CFCECE",
    "highlight": "#FFD700",
    "teal": "#42949E",
    "violet": "#9A4D8E",
}
DEFAULT_COLORS = [PALETTE["blue_main"], PALETTE["green_3"], PALETTE["red_strong"], PALETTE["teal"], PALETTE["violet"], PALETTE["neutral"]]
INK = "#272727"
FRAME = "#4D4D4D"
REPRODUCIBLE_BUILD_EPOCH = 1600000000


@dataclass(frozen=True)
class FigureStyle:
    font_size: int = 16
    axes_linewidth: float = 2.5
    use_tex: bool = False
    font_family: tuple = ("Helvetica", "Arial", "DejaVu Sans", "sans-serif")


def apply_publication_style(style=None):
    style = style or FigureStyle()
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": list(style.font_family),
        "font.size": style.font_size,
        "axes.titlesize": style.font_size,
        "axes.titleweight": "bold",
        "axes.labelsize": style.font_size,
        "xtick.labelsize": style.font_size * 0.94,
        "ytick.labelsize": style.font_size * 0.94,
        "legend.fontsize": style.font_size * 0.94,
        "text.usetex": style.use_tex,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": FRAME,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": style.axes_linewidth,
        "axes.axisbelow": True,
        "axes.prop_cycle": mpl.cycler(color=DEFAULT_COLORS),
        "legend.frameon": False,
        "xtick.major.width": style.axes_linewidth,
        "ytick.major.width": style.axes_linewidth,
        "xtick.major.size": style.axes_linewidth * 2.2,
        "ytick.major.size": style.axes_linewidth * 2.2,
        "pdf.fonttype": 42,
        "svg.fonttype": "none",
        "figure.facecolor": "#FFFFFF",
        "axes.facecolor": "#FFFFFF",
        "savefig.facecolor": "#FFFFFF",
    })


def create_subplots(nrows=1, ncols=1, figsize=None, **kwargs):
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, **kwargs)
    return fig, np.atleast_1d(axes).ravel()


def finalize_figure(fig, out_path, formats=("png", "pdf"), dpi=300, close=True, pad=0.05):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("SOURCE_DATE_EPOCH", str(REPRODUCIBLE_BUILD_EPOCH))
    written = []
    for fmt in formats:
        target = out_path.with_suffix(f".{fmt}")
        fig.savefig(target, format=fmt, dpi=dpi, bbox_inches="tight", pad_inches=pad, metadata={"CreationDate": None} if fmt == "pdf" else None)
        written.append(target)
    if close:
        plt.close(fig)
    return written


def make_grouped_bar(ax, categories, series, labels, ylabel="Value", colors=None, annotate=False, fmt="{:.0f}", width=0.72, orientation="vertical"):
    colors = list(colors or DEFAULT_COLORS)
    positions = np.arange(len(categories))
    span = width / len(series)
    containers = []
    for index, values in enumerate(series):
        values = np.asarray(values, dtype=float)
        if len(values) != len(categories):
            raise ValueError("series length must match categories")
        offset = (index - (len(series) - 1) / 2) * span
        colour = colors[index % len(colors)]
        if orientation == "horizontal":
            container = ax.barh(positions + offset, values, height=span * 0.92, color=colour, edgecolor="black", linewidth=1.2, label=labels[index])
        else:
            container = ax.bar(positions + offset, values, width=span * 0.92, color=colour, edgecolor="black", linewidth=1.2, label=labels[index])
        containers.append(container)
        if annotate:
            annotate_bars(ax, container, fmt=fmt, orientation=orientation)
    if orientation == "horizontal":
        ax.set_yticks(positions)
        ax.set_yticklabels(categories)
        ax.set_xlabel(ylabel)
    else:
        ax.set_xticks(positions)
        ax.set_xticklabels(categories)
        ax.set_ylabel(ylabel)
    return containers[-1]


def annotate_bars(ax, bars, fmt="{:.0f}", fontsize=None, padding=3, orientation="vertical"):
    fontsize = fontsize or mpl.rcParams["font.size"] * 0.82
    for patch in bars:
        if orientation == "horizontal":
            value = patch.get_width()
            ax.annotate(fmt.format(value), (value, patch.get_y() + patch.get_height() / 2), xytext=(padding, 0), textcoords="offset points", ha="left", va="center", fontsize=fontsize, color=INK)
        else:
            value = patch.get_height()
            ax.annotate(fmt.format(value), (patch.get_x() + patch.get_width() / 2, value), xytext=(0, padding), textcoords="offset points", ha="center", va="bottom", fontsize=fontsize, color=INK)


def make_heatmap(ax, matrix, x_labels=None, y_labels=None, cmap="magma", cbar_label=None, annotate=False, fmt="{:.2f}"):
    matrix = np.asarray(matrix, dtype=float)
    image = ax.imshow(matrix, cmap=cmap, aspect="auto")
    if x_labels is not None:
        ax.set_xticks(range(len(x_labels)))
        ax.set_xticklabels(x_labels)
    if y_labels is not None:
        ax.set_yticks(range(len(y_labels)))
        ax.set_yticklabels(y_labels)
    if cbar_label:
        ax.figure.colorbar(image, ax=ax, label=cbar_label)
    if annotate:
        limit = matrix.max() * 0.55
        for row in range(matrix.shape[0]):
            for column in range(matrix.shape[1]):
                ax.text(column, row, fmt.format(matrix[row, column]), ha="center", va="center", fontsize=mpl.rcParams["font.size"] * 0.72, color="white" if matrix[row, column] > limit else INK)
    return image
