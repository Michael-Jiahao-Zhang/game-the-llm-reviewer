#!/usr/bin/env python3
"""Mechanical support for strategy S6: compare an original manuscript with its revision and report every number, citation, qualifier, and LaTeX reference whose change a human equivalence check must confirm."""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

NUMBER = re.compile(r"(?<![A-Za-z\d.])\d[\d,]*(?:\.\d+)?(?![\d,]*[A-Za-z])")
LATEX_CITATION = re.compile(r"\\cite[A-Za-z*]*(?:\[[^\]]*\])*\{([^}]*)\}")
MARKDOWN_CITATION = re.compile(r"(?<![\w.])@([A-Za-z][\w:-]*\w)")
LATEX_REFERENCES = {
    "label": re.compile(r"\\label\{([^}]*)\}"),
    "ref": re.compile(r"\\(?:auto|c|C|page)?ref\{([^}]*)\}"),
    "eqref": re.compile(r"\\eqref\{([^}]*)\}"),
    "input": re.compile(r"\\(?:input|include)\{([^}]*)\}"),
    "includegraphics": re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}"),
}
STRENGTHENING_PHRASES = ("first", "novel", "state of the art", "state-of-the-art", "significant", "significantly", "optimal", "outperforms all", "unprecedented", "breakthrough")
QUALIFIER_WORDS = ("may", "might", "could", "preliminary", "suggest", "suggests", "only", "limited", "limitation", "untested", "not", "no", "without", "fails", "cannot")
SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+")
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")
TOLERANCE = 1e-9


def phrase_pattern(phrase):
    return re.compile(r"(?<![\w-])" + re.escape(phrase) + r"(?![\w-])", re.IGNORECASE)


def sentences(text):
    return [s.strip() for s in SENTENCE_BOUNDARY.split(text.replace("\n", " ")) if s.strip()]


def number_values(text):
    values = []
    for token in NUMBER.findall(text):
        values.append((token, float(token.replace(",", ""))))
    return values


def close(a, b):
    return abs(a - b) <= TOLERANCE * max(1.0, abs(a), abs(b))


def derivations(value, original_values):
    formulas = []
    for i, a in enumerate(original_values):
        for j, b in enumerate(original_values):
            if i == j:
                continue
            if a >= b and close(a - b, value):
                formulas.append(f"{a:g} - {b:g} = {value:g} (difference or percentage-point difference)")
            if b and close(a / b, value):
                formulas.append(f"{a:g} / {b:g} = {value:g} (ratio)")
    seen = []
    for formula in formulas:
        if formula not in seen:
            seen.append(formula)
    return seen


def number_findings(original, revised):
    original_numbers = number_values(original)
    revised_numbers = number_values(revised)
    original_distinct = []
    for _, value in original_numbers:
        if not any(close(value, seen) for seen in original_distinct):
            original_distinct.append(value)
    derived, unsupported = [], []
    for token, value in revised_numbers:
        if any(close(value, seen) for seen in original_distinct):
            continue
        formulas = derivations(value, original_distinct)
        entry = {"number": token, "value": value, "formulas": formulas}
        (derived if formulas else unsupported).append(entry)
    revised_values = [value for _, value in revised_numbers]
    dropped = [{"number": token, "value": value} for token, value in original_numbers if not any(close(value, seen) for seen in revised_values)]
    return {"derived": derived, "unsupported": unsupported, "dropped": dropped}


def citation_keys(text):
    keys = set()
    for group in LATEX_CITATION.findall(text):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    keys.update(MARKDOWN_CITATION.findall(text))
    return keys


def set_difference(name, original_keys, revised_keys):
    return {"missing_in_revision": sorted(original_keys - revised_keys), "added_in_revision": sorted(revised_keys - original_keys)}


def strengthening_findings(original, revised):
    findings = []
    for phrase in STRENGTHENING_PHRASES:
        pattern = phrase_pattern(phrase)
        added = len(pattern.findall(revised)) - len(pattern.findall(original))
        if added > 0:
            findings.append({"phrase": phrase, "added_occurrences": added, "sentences": [s for s in sentences(revised) if pattern.search(s)]})
    return findings


def weakened_qualification_findings(original, revised):
    findings = []
    for word in QUALIFIER_WORDS:
        pattern = phrase_pattern(word)
        removed = len(pattern.findall(original)) - len(pattern.findall(revised))
        if removed > 0:
            findings.append({"word": word, "removed_occurrences": removed, "sentences": [s for s in sentences(original) if pattern.search(s)]})
    return findings


def structure_findings(original, revised):
    findings = {}
    for name, pattern in LATEX_REFERENCES.items():
        original_set, revised_set = set(pattern.findall(original)), set(pattern.findall(revised))
        if original_set != revised_set:
            findings[name] = set_difference(name, original_set, revised_set)
    return findings


def compare(original, revised):
    numbers = number_findings(original, revised)
    citations = set_difference("citations", citation_keys(original), citation_keys(revised))
    strengthening = strengthening_findings(original, revised)
    weakened = weakened_qualification_findings(original, revised)
    structure = structure_findings(original, revised)
    original_words, revised_words = len(WORD.findall(original)), len(WORD.findall(revised))
    blocking = bool(numbers["unsupported"] or strengthening or citations["missing_in_revision"] or citations["added_in_revision"] or structure)
    return {
        "numbers": numbers,
        "citations": citations,
        "strengthening": strengthening,
        "weakened_qualification": weakened,
        "structure": structure,
        "word_count": {"original": original_words, "revised": revised_words, "delta": revised_words - original_words},
        "counts": {"derived": len(numbers["derived"]), "unsupported": len(numbers["unsupported"]), "dropped": len(numbers["dropped"]), "strengthening": len(strengthening), "weakened_qualification": len(weakened), "citation_differences": len(citations["missing_in_revision"]) + len(citations["added_in_revision"]), "structure_differences": len(structure)},
        "equivalent_on_mechanical_invariants": not blocking,
    }


def render_text(report):
    lines = ["findings"]
    for entry in report["numbers"]["unsupported"]:
        lines.append(f"  unsupported number {entry['number']}")
    for entry in report["strengthening"]:
        lines.append(f"  strengthening '{entry['phrase']}' added {entry['added_occurrences']} time(s)")
    for key in report["citations"]["missing_in_revision"]:
        lines.append(f"  citation missing in revision: {key}")
    for key in report["citations"]["added_in_revision"]:
        lines.append(f"  citation added in revision: {key}")
    for name, difference in report["structure"].items():
        lines.append(f"  {name} differs: missing {difference['missing_in_revision']} added {difference['added_in_revision']}")
    lines.append("review")
    for entry in report["numbers"]["derived"]:
        lines.append(f"  derived number {entry['number']}: " + "; ".join(entry["formulas"]))
    for entry in report["numbers"]["dropped"]:
        lines.append(f"  dropped number {entry['number']}")
    for entry in report["weakened_qualification"]:
        lines.append(f"  weakened qualification '{entry['word']}' removed {entry['removed_occurrences']} time(s): " + " | ".join(entry["sentences"]))
    counts = report["counts"]
    lines.append("counts " + " ".join(f"{key}={value}" for key, value in counts.items()))
    words = report["word_count"]
    lines.append(f"words original={words['original']} revised={words['revised']} delta={words['delta']}")
    lines.append("equivalent_on_mechanical_invariants " + str(report["equivalent_on_mechanical_invariants"]).lower())
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("revised", type=Path)
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args()
    report = compare(args.original.read_text(), args.revised.read_text())
    print(json.dumps(report, indent=1, ensure_ascii=False) if args.format == "json" else render_text(report))
    return 0 if report["equivalent_on_mechanical_invariants"] else 1


if __name__ == "__main__":
    sys.exit(main())
