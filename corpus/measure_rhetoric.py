#!/usr/bin/env python3
"""Measure the rhetorical cues behind strategy cards S1-S5 across the ELIT corpus of ICLR and ICML 2026 oral, spotlight and outstanding papers."""
import argparse
import collections
import json
import re
import statistics
from pathlib import Path

ACHIEVEMENT_VERBS = r"\bwe (?:propose|introduce|present|develop|design|build|derive|establish|formalize|formalise)\b"
FINDING_VERBS = r"\bwe (?:show|find|observe|demonstrate|prove|reveal|identify|discover|uncover|report)\b"
NEGATION_STANCE = r"\b(?:does not|do not|without|no longer) (?:require|need|rely|depend|assume)\w*\b"
REMOVAL_STANCE = r"\b(?:removes?|eliminates?|avoids?|bypass(?:es)?|lifts?|drops?) (?:the )?(?:need|requirement|assumption|dependence|reliance)\b"
FIRST_CLAIM = r"\b(?:the first|first to|for the first time)\b"
NOVEL_CLAIM = r"\bnovel\b"
SOTA_CLAIM = r"\bstate[- ]of[- ]the[- ]art\b"
PERCENT_POINT = r"\b\d+(?:\.\d+)?\s*(?:percentage points?|pp|points?)\b"
RELATIVE_GAIN = r"\b(?:by|of)\s+(?:up to\s+|over\s+|around\s+|about\s+|nearly\s+)?\d+(?:\.\d+)?\s*(?:%|percent\b|×|x\b)"
FROM_TO = r"\bfrom\s+\d+(?:\.\d+)?%?\s+to\s+\d+(?:\.\d+)?%?\b"
COMPARATIVE_VERB = r"\b(?:outperforms?|improves?|reduces?|surpass(?:es)?|exceeds?|beats?|boosts?|accelerates?|speeds? up)\b"
HEDGES = r"\b(?:may|might|could|potentially|possibly|preliminary|suggests?|appears?|seems?|likely|arguably|tend to|tends to)\b"
BOOSTERS = r"\b(?:significantly|substantially|consistently|clearly|strongly|dramatically|remarkably|considerably|robustly)\b"
CONTRASTIVE = r"\b(?:however|but|although|though|whereas|despite|nevertheless|nonetheless|in contrast|on the other hand|yet)\b"
SCOPE_FRAME = r"\b(?:we (?:evaluate|focus|restrict|limit|consider) (?:only|on)|remains? (?:untested|unexplored|open)|beyond the scope|future work|not (?:yet )?(?:evaluated|tested|explored|addressed)|limited to)\b"
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")


def words(text):
    return len(WORD.findall(text))


def per_thousand(pattern, text):
    n = words(text)
    return 1000.0 * len(re.findall(pattern, text, flags=re.I)) / n if n else 0.0


def load_document(root, paper_id):
    doc = json.loads((root / "papers" / paper_id / "document.json").read_text())
    pages = [json.loads(line) for line in (root / "papers" / paper_id / "pages.jsonl").read_text().split("\n") if line.strip()]
    module_of = {s["id"]: s.get("module") for s in doc.get("document_sections", [])}
    titles = [s.get("title", "") for s in doc.get("document_sections", [])]
    module_text = collections.defaultdict(list)
    for page in pages:
        for block in page.get("blocks", []):
            if block.get("role") in ("running_header", "page_number"):
                continue
            for sid in block.get("section_ids", []):
                module_text[module_of.get(sid, "other")].append(block.get("text", ""))
    return doc, titles, {m: "\n".join(t) for m, t in module_text.items()}


def abstract_features(sentences):
    n = len(sentences)
    functions = [set(s.get("functions", [])) for s in sentences]
    def first_index(labels):
        for s, f in zip(sentences, functions):
            if f & labels:
                return s["index"]
        return None
    idea = first_index({"core_idea", "method"})
    result = first_index({"quantitative_result", "qualitative_result"})
    return {
        "sentence_count": n,
        "first_idea_index": idea,
        "first_idea_position": (idea - 1) / (n - 1) if idea and n > 1 else None,
        "first_result_index": result,
        "first_result_position": (result - 1) / (n - 1) if result and n > 1 else None,
        "quantitative_result": any("quantitative_result" in f for f in functions),
        "qualitative_result_only": any("qualitative_result" in f for f in functions) and not any("quantitative_result" in f for f in functions),
        "limitation_in_abstract": any("limitation" in f for f in functions),
        "theory_in_abstract": any("theory" in f for f in functions),
        "first_sentence_functions": sorted(functions[0]) if functions else [],
        "function_by_position": [[s["index"], sorted(f)] for s, f in zip(sentences, functions)],
    }


def text_features(text):
    return {
        "words": words(text),
        "achievement_verbs_per_1k": per_thousand(ACHIEVEMENT_VERBS, text),
        "finding_verbs_per_1k": per_thousand(FINDING_VERBS, text),
        "negation_stance": len(re.findall(NEGATION_STANCE, text, flags=re.I)),
        "removal_stance": len(re.findall(REMOVAL_STANCE, text, flags=re.I)),
        "first_claims": len(re.findall(FIRST_CLAIM, text, flags=re.I)),
        "novel_claims": len(re.findall(NOVEL_CLAIM, text, flags=re.I)),
        "sota_claims": len(re.findall(SOTA_CLAIM, text, flags=re.I)),
        "percentage_point_framing": len(re.findall(PERCENT_POINT, text, flags=re.I)),
        "relative_gain_framing": len(re.findall(RELATIVE_GAIN, text, flags=re.I)),
        "from_to_framing": len(re.findall(FROM_TO, text, flags=re.I)),
        "comparative_verbs_per_1k": per_thousand(COMPARATIVE_VERB, text),
        "hedges_per_1k": per_thousand(HEDGES, text),
        "boosters_per_1k": per_thousand(BOOSTERS, text),
        "contrastives_per_1k": per_thousand(CONTRASTIVE, text),
        "scope_frames": len(re.findall(SCOPE_FRAME, text, flags=re.I)),
    }


def measure(root):
    rows = []
    for reading_path in sorted((root / "readings").glob("*.json")):
        reading = json.loads(reading_path.read_text())
        paper_id = reading["paper_id"]
        doc, titles, module_text = load_document(root, paper_id)
        abstract = module_text.get("abstract", "")
        intro = module_text.get("introduction", "")
        conclusion = module_text.get("conclusion", "")
        body = "\n".join(t for m, t in module_text.items() if m not in ("other", "appendix"))
        rows.append({
            "paper_id": paper_id,
            "conference": paper_id.split("-")[0].upper(),
            "title": doc.get("title"),
            "has_limitations_section": any(re.search(r"limitation", t, flags=re.I) for t in titles),
            "abstract": abstract_features(reading.get("abstract_sentences", [])),
            "abstract_text": text_features(abstract),
            "introduction_text": text_features(intro),
            "conclusion_text": text_features(conclusion),
            "body_text": text_features(body),
        })
    return rows


def summarize(rows):
    def share(key, scope="abstract"):
        vals = [r[scope][key] for r in rows if r[scope][key] is not None]
        return sum(bool(v) for v in vals) / len(vals) if vals else None
    def median(key, scope):
        vals = [r[scope][key] for r in rows if r[scope][key] is not None]
        return statistics.median(vals) if vals else None
    def quartiles(key, scope):
        vals = sorted(r[scope][key] for r in rows if r[scope][key] is not None)
        if not vals:
            return None
        q = statistics.quantiles(vals, n=4)
        return {"q1": q[0], "median": q[1], "q3": q[2], "mean": statistics.fmean(vals)}
    position_counts = collections.Counter()
    for r in rows:
        for index, functions in r["abstract"]["function_by_position"]:
            for f in functions:
                position_counts[(min(index, 10), f)] += 1
    return {
        "papers": len(rows),
        "by_conference": dict(collections.Counter(r["conference"] for r in rows)),
        "abstract_sentence_count": quartiles("sentence_count", "abstract"),
        "first_idea_index": quartiles("first_idea_index", "abstract"),
        "first_idea_position": quartiles("first_idea_position", "abstract"),
        "first_result_position": quartiles("first_result_position", "abstract"),
        "share_quantitative_result_in_abstract": share("quantitative_result"),
        "share_qualitative_result_only_in_abstract": share("qualitative_result_only"),
        "share_limitation_in_abstract": share("limitation_in_abstract"),
        "share_theory_in_abstract": share("theory_in_abstract"),
        "share_limitations_section": sum(r["has_limitations_section"] for r in rows) / len(rows),
        "first_sentence_functions": dict(collections.Counter("+".join(r["abstract"]["first_sentence_functions"]) for r in rows).most_common(8)),
        "function_by_position": [[i, f, c] for (i, f), c in sorted(position_counts.items())],
        "share_first_claim_in_body": sum(r["body_text"]["first_claims"] > 0 for r in rows) / len(rows),
        "share_novel_in_body": sum(r["body_text"]["novel_claims"] > 0 for r in rows) / len(rows),
        "share_sota_in_body": sum(r["body_text"]["sota_claims"] > 0 for r in rows) / len(rows),
        "share_removal_stance_in_body": sum(r["body_text"]["removal_stance"] > 0 for r in rows) / len(rows),
        "share_negation_stance_in_body": sum(r["body_text"]["negation_stance"] > 0 for r in rows) / len(rows),
        "evidence_framing_in_abstract": {
            "percentage_point": sum(r["abstract_text"]["percentage_point_framing"] > 0 for r in rows) / len(rows),
            "relative_gain": sum(r["abstract_text"]["relative_gain_framing"] > 0 for r in rows) / len(rows),
            "from_to": sum(r["abstract_text"]["from_to_framing"] > 0 for r in rows) / len(rows),
            "comparative_verb": sum(r["abstract_text"]["comparative_verbs_per_1k"] > 0 for r in rows) / len(rows),
        },
        "density_per_1k": {
            scope: {
                key: quartiles(key, scope)
                for key in ("achievement_verbs_per_1k", "finding_verbs_per_1k", "hedges_per_1k", "boosters_per_1k", "contrastives_per_1k", "comparative_verbs_per_1k")
            }
            for scope in ("abstract_text", "introduction_text", "conclusion_text", "body_text")
        },
        "scope_frames_in_conclusion_share": sum(r["conclusion_text"]["scope_frames"] > 0 for r in rows) / len(rows),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = measure(args.corpus)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"corpus_revision": (args.corpus / ".git" / "HEAD").read_text().strip() if (args.corpus / ".git").exists() else None, "summary": summarize(rows), "papers": rows}, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(summarize(rows), indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
