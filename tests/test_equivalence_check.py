import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "equivalence_check.py"


def readme_example(heading):
    readme = (ROOT / "README.md").read_text()
    section = readme.split(f"### {heading}", 1)[1].split("###", 1)[0]
    quote = next(line for line in section.splitlines() if line.startswith("> "))
    return re.sub(r"\*\*", "", quote[2:]).strip()


BEFORE = readme_example("Before")
AFTER = readme_example("After Game the LLM Reviewer")
LATEX_ORIGINAL = "REAP \\citep{lasby2025reap} prunes experts. Table~\\ref{tab:published} lists it. \\label{sec:reap} \\input{tables/published-comparison.tex} Equation~\\eqref{eq:bound} bounds the gap. \\includegraphics{figures/frontier.pdf}"
LATEX_REVISED_MATCHING = "REAP \\citep{lasby2025reap} prunes experts and Table~\\ref{tab:published} lists it. \\label{sec:reap} \\input{tables/published-comparison.tex} Equation~\\eqref{eq:bound} bounds the gap. \\includegraphics{figures/frontier.pdf}"
LATEX_REVISED_MISSING_CITATION = LATEX_REVISED_MATCHING.replace(" \\citep{lasby2025reap}", "")


def run(tmp_path, original, revised, fmt="json"):
    original_path, revised_path = tmp_path / "original.md", tmp_path / "revised.md"
    original_path.write_text(original)
    revised_path.write_text(revised)
    completed = subprocess.run([sys.executable, str(SCRIPT), str(original_path), str(revised_path), "--format", fmt], capture_output=True, text=True)
    payload = json.loads(completed.stdout) if fmt == "json" else completed.stdout
    return completed.returncode, payload


def test_readme_example_passes_with_derived_percentage_points(tmp_path):
    code, report = run(tmp_path, BEFORE, AFTER)
    assert code == 0
    assert report["numbers"]["unsupported"] == []
    assert report["strengthening"] == []
    derived = {entry["number"]: entry["formulas"] for entry in report["numbers"]["derived"]}
    assert list(derived) == ["4"]
    assert any(formula.startswith("34 - 30 = 4") for formula in derived["4"])
    assert any(formula.startswith("39 - 35 = 4") for formula in derived["4"])
    assert report["word_count"]["original"] > 0 and report["word_count"]["revised"] > 0


def test_added_first_claim_blocks(tmp_path):
    code, report = run(tmp_path, BEFORE, AFTER.replace("We introduce an execution memory", "We introduce the first execution memory"))
    assert code == 1
    assert [entry["phrase"] for entry in report["strengthening"]] == ["first"]
    assert "the first execution memory" in report["strengthening"][0]["sentences"][0]


def test_changed_result_number_blocks(tmp_path):
    code, report = run(tmp_path, BEFORE, AFTER.replace("from 30% to 34%", "from 30% to 36%"))
    assert code == 1
    assert [entry["number"] for entry in report["numbers"]["unsupported"]] == ["36"]
    assert [entry["number"] for entry in report["numbers"]["dropped"]] == ["34"]


def test_dropped_scope_clause_is_a_review_warning(tmp_path):
    revised = BEFORE.replace(", without updating model weights", "")
    code, report = run(tmp_path, BEFORE, revised)
    assert code == 0
    weakened = {entry["word"]: entry for entry in report["weakened_qualification"]}
    assert "without" in weakened
    assert weakened["without"]["removed_occurrences"] == 1
    assert any("without updating model weights" in sentence for sentence in weakened["without"]["sentences"])
    assert report["numbers"]["unsupported"] == [] and report["strengthening"] == []


def test_latex_missing_citation_blocks(tmp_path):
    code, report = run(tmp_path, LATEX_ORIGINAL, LATEX_REVISED_MISSING_CITATION)
    assert code == 1
    assert report["citations"]["missing_in_revision"] == ["lasby2025reap"]
    assert report["structure"] == {}


def test_latex_matching_structure_passes(tmp_path):
    code, report = run(tmp_path, LATEX_ORIGINAL, LATEX_REVISED_MATCHING)
    assert code == 0
    assert report["citations"] == {"missing_in_revision": [], "added_in_revision": []}
    assert report["structure"] == {}
    assert report["numbers"]["derived"] == [] and report["numbers"]["unsupported"] == []


def test_latex_dropped_label_blocks(tmp_path):
    code, report = run(tmp_path, LATEX_ORIGINAL, LATEX_REVISED_MATCHING.replace(" \\label{sec:reap}", ""))
    assert code == 1
    assert report["structure"]["label"]["missing_in_revision"] == ["sec:reap"]


@pytest.mark.parametrize("revised", [AFTER, AFTER.replace("from 30% to 34%", "from 30% to 36%")])
def test_text_and_json_formats_agree_on_counts(tmp_path, revised):
    json_code, report = run(tmp_path, BEFORE, revised)
    text_code, text = run(tmp_path, BEFORE, revised, fmt="text")
    assert json_code == text_code
    counts_line = next(line for line in text.splitlines() if line.startswith("counts "))
    text_counts = dict(item.split("=") for item in counts_line.split()[1:])
    assert {key: str(value) for key, value in report["counts"].items()} == text_counts
    assert ("derived number 4" in text) == bool(report["numbers"]["derived"])
    assert text.splitlines()[0] == "findings" and "review" in text.splitlines()
