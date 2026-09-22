#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["matplotlib>=3.9", "numpy>=2"]
# ///
"""Render the elite-corpus rhetoric figures that calibrate strategy cards S1-S5."""
import argparse
import json
from pathlib import Path

import numpy as np

from figure_style import PALETTE, FigureStyle, apply_publication_style, create_subplots, finalize_figure, make_grouped_bar, make_heatmap

FUNCTIONS = ["object_scope", "problem_gap", "core_idea", "method", "theory", "experimental_setup", "quantitative_result", "qualitative_result", "impact_claim", "limitation"]
FUNCTION_LABELS = ["Object and scope", "Problem gap", "Core idea", "Method", "Theory", "Experimental setup", "Quantitative result", "Qualitative result", "Impact claim", "Limitation"]


def abstract_position_heatmap(summary, out):
    papers = summary["papers"]
    matrix = np.zeros((len(FUNCTIONS), 10))
    for index, function, count in summary["function_by_position"]:
        if function in FUNCTIONS:
            matrix[FUNCTIONS.index(function), index - 1] = 100.0 * count / papers
    fig, axes = create_subplots(1, 1, figsize=(13, 7.5))
    make_heatmap(axes[0], matrix, x_labels=[str(i) for i in range(1, 10)] + ["10+"], y_labels=FUNCTION_LABELS, cmap="Blues", cbar_label="Papers whose sentence carries the function (%)", annotate=True, fmt="{:.0f}")
    axes[0].set_xlabel("Abstract sentence position")
    axes[0].set_title(f"Abstract sentence functions across {papers} elite papers")
    finalize_figure(fig, out / "abstract_function_by_position")


def stance_claims(summary, out):
    categories = ["“first” claim", "“novel”", "“state of the art”", "Negation stance\n(does not require)", "Removal stance\n(removes the need)"]
    values = [100 * summary[k] for k in ("share_first_claim_in_body", "share_novel_in_body", "share_sota_in_body", "share_negation_stance_in_body", "share_removal_stance_in_body")]
    fig, axes = create_subplots(1, 1, figsize=(13, 6))
    colors = [PALETTE["blue_main"], PALETTE["blue_secondary"], PALETTE["teal"], PALETTE["red_2"], PALETTE["green_3"]]
    bars = axes[0].bar(range(len(categories)), values, color=colors, edgecolor="black", linewidth=1.2)
    for patch, value in zip(bars, values):
        axes[0].annotate(f"{value:.0f}%", (patch.get_x() + patch.get_width() / 2, value), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom")
    axes[0].set_xticks(range(len(categories)))
    axes[0].set_xticklabels(categories)
    axes[0].set_ylabel("Papers using the form in the main body (%)")
    axes[0].set_ylim(0, 100)
    axes[0].set_title("Contribution stance forms (S1) in elite main bodies")
    finalize_figure(fig, out / "stance_claims")


def abstract_evidence_and_scope(summary, out):
    ef = summary["evidence_framing_in_abstract"]
    categories = ["Quantitative\nresult", "Qualitative\nresult only", "Comparative\nverb", "Relative gain\n(by N%)", "Percentage\npoints", "From X\nto Y", "Limitation\nin abstract", "Theory\nin abstract"]
    values = [100 * summary["share_quantitative_result_in_abstract"], 100 * summary["share_qualitative_result_only_in_abstract"], 100 * ef["comparative_verb"], 100 * ef["relative_gain"], 100 * ef["percentage_point"], 100 * ef["from_to"], 100 * summary["share_limitation_in_abstract"], 100 * summary["share_theory_in_abstract"]]
    colors = [PALETTE["blue_main"], PALETTE["neutral"], PALETTE["blue_secondary"], PALETTE["green_3"], PALETTE["green_2"], PALETTE["green_1"], PALETTE["red_2"], PALETTE["violet"]]
    fig, axes = create_subplots(1, 1, figsize=(15, 6))
    bars = axes[0].bar(range(len(categories)), values, color=colors, edgecolor="black", linewidth=1.2)
    for patch, value in zip(bars, values):
        axes[0].annotate(f"{value:.0f}%", (patch.get_x() + patch.get_width() / 2, value), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom")
    axes[0].set_xticks(range(len(categories)))
    axes[0].set_xticklabels(categories)
    axes[0].set_ylabel("Elite abstracts (%)")
    axes[0].set_ylim(0, 100)
    axes[0].set_title("Evidence framing (S2), abstract emphasis (S3) and scope (S5) in elite abstracts")
    finalize_figure(fig, out / "abstract_evidence_and_scope")


def lexical_density(summary, out):
    scopes = [("abstract_text", "Abstract"), ("introduction_text", "Introduction"), ("conclusion_text", "Conclusion"), ("body_text", "Main body")]
    keys = [("achievement_verbs_per_1k", "Achievement verbs (we propose, introduce)"), ("finding_verbs_per_1k", "Finding verbs (we show, find)"), ("hedges_per_1k", "Hedges (may, suggest, preliminary)"), ("boosters_per_1k", "Boosters (significantly, consistently)"), ("contrastives_per_1k", "Contrastive connectives (however, but)")]
    series = [[summary["density_per_1k"][scope][key]["mean"] for scope, _ in scopes] for key, _ in keys]
    fig, axes = create_subplots(1, 1, figsize=(15, 6.5))
    make_grouped_bar(axes[0], [label for _, label in scopes], series, [label for _, label in keys], ylabel="Mean occurrences per 1,000 words", colors=[PALETTE["blue_main"], PALETTE["blue_secondary"], PALETTE["red_2"], PALETTE["green_3"], PALETTE["neutral"]], annotate=True, fmt="{:.1f}")
    axes[0].set_ylim(0, 8.5)
    axes[0].legend(loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.0))
    axes[0].set_title("Lexical stance (S4) across sections of elite papers")
    finalize_figure(fig, out / "lexical_density")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, default=Path(__file__).with_name("elite-corpus-rhetoric.json"))
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent.parent / "assets" / "corpus")
    args = parser.parse_args()
    summary = json.loads(args.record.read_text())["summary"]
    apply_publication_style(FigureStyle())
    abstract_position_heatmap(summary, args.out)
    stance_claims(summary, args.out)
    abstract_evidence_and_scope(summary, args.out)
    lexical_density(summary, args.out)
    skill_figures = Path(__file__).resolve().parent.parent / "skills" / "game-the-llm-reviewer" / "references" / "figures"
    skill_figures.mkdir(parents=True, exist_ok=True)
    for png in args.out.glob("*.png"):
        (skill_figures / png.name).write_bytes(png.read_bytes())


if __name__ == "__main__":
    main()
