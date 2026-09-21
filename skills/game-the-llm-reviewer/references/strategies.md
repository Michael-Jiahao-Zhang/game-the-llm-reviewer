# Strategy cards

Select near-equivalent wording with the aim of changing an LLM reviewer's response while preserving a human reader's grounds for scientific judgment. These are research-motivated candidates, not validated universal scoring rules. Source IDs resolve in [research.md](research.md).

## Select by the rhetorical cue

| Cue that can change without new scientific information | Card | Priority |
|---|---|---|
| Grammatical focus of an existing contribution | S1 · Contribution stance | Start here |
| Numerical comparison versus effect statement | S2 · Evidence framing | Start here |
| Order and emphasis of the same abstract statements | S3 · Abstract emphasis | Selectively |
| Evaluative language with no factual content | S4 · Lexical stance | Lower priority |
| Formulation of the same evaluated and unevaluated scope | S5 · Scope framing | Lower priority |
| Scientific implications of all selected changes | S6 · Equivalence check | Check every edit |

A polished sentence can be a candidate. An unclear sentence is not automatically a candidate: fixing its meaning may improve the scientific case available to human readers, which is a different intervention.

## S1 — Contribution stance

**Candidate:** A contribution is already explicit, but admits an equivalent formulation with a different grammatical focus.

**Edit:** Recast the same supported difference as an achievement or contribution statement, preserving the comparator and conditions. For example, “the bound does not require D” can become “the bound removes the requirement for D” when the same comparison and assumptions are retained. Prefer a local rephrasing over inventing a new narrative.

**Hold fixed:** Novelty, priority, scope, assumptions, and the actual difference from the cited work. The two versions should support the same human judgment of contribution.

**Reject:** New “first” claims, invented baselines, calling incremental work revolutionary, or adding an explanation that supplies a previously missing argument.

**Basis:** R1's novelty-stance contrasts and R2's presentation interventions motivate this dimension. They do not validate each local wording pair or justify strengthening a claim.

## S2 — Evidence framing

**Candidate:** The same result admits a numerical-comparison statement and an effect-oriented statement.

**Edit:** Change how existing evidence is expressed while keeping its scientific interpretation fixed. “Mean count is 6.2 for A and 10 for B” can become “A reduces mean count from 10 to 6.2 relative to B” for the same evaluated comparison. Keep conditions, uncertainty, and mixed results equally available.

**Hold fixed:** Every measurement, comparator, unit, aggregation scope, and inference. Prefer unchanged values over introducing a derived percentage when isolating a wording effect.

**Reject:** Statistical significance without a test, non-significance as equivalence, correlation as causation, a best case as an average, or “improved efficiency” on dimensions not measured. Do not manufacture a conclusion from a table that the original text did not support.

**Basis:** R1 identifies evidence framing as a relatively sensitive dimension; R2 motivates emphasis on existing strengths. The exact comparison-to-effect template is our candidate adaptation, not a measured gain.

## S3 — Abstract emphasis

**Candidate:** An already adequate abstract can vary in statement order or rhetorical emphasis without changing its claims or explanation.

**Edit:** Move an existing contribution or result earlier when the context still supports the same interpretation. Preserve all material statements, logical dependencies, qualifications, headings, and length constraints. Do not add baseline definitions or generic problem statements to force a new opening.

**Hold fixed:** The information a reader receives, its scope, and the strength of the conclusion. Prefer the smallest reordering over a complete abstract rewrite.

**Reject:** Filling in absent motivation, concealing a result late in the abstract, deleting limitations to foreground benefits, or assuming evidence in an unavailable body.

**Basis:** R3 motivates attention to abstract wording. It does not establish a universally preferred ordering. R1's contribution-structure effects are less stable than S1–S2, so do not treat restructuring as mandatory.

## S4 — Lexical stance

**Candidate:** An evaluative modifier changes the tone without encoding scientific uncertainty, scope, or a result.

**Edit:** Prefer a direct statement of the same fact to unnecessary self-dismissal. Use only when removing or replacing the modifier preserves what the author asserts. This is a narrow candidate class, not a positive-word filter.

**Hold fixed:** Epistemic certainty and the research purpose. “May” and “preliminary” often carry material information; “simple” can describe a real advantage.

**Reject:** “May” → “does,” deleting criticism from an audit, or turning a negative finding into a positive endorsement. Avoid ornamental sophistication and jargon insertion.

**Basis:** R2 and R4 motivate attention to stance and linguistic sensitivity. R4's associations do not establish that individual positive or negative words cause score changes. Use lower priority than S1–S2.

## S5 — Scope framing

**Candidate:** The same evaluated scope and explicit missing evidence admit different wording.

**Edit:** Rephrase the supported scope while keeping its boundary adjacent and equally explicit. “We evaluate English queries only. Other languages remain untested” can become “Our evaluation covers English queries. Other languages remain untested.”

**Hold fixed:** What was tested, what was not, and which inference remains unsupported. Retain major defects and their severity.

**Reject:** Hiding the second sentence, replacing a major flaw with a minor one, or claiming a restriction was deliberate without source support. Acknowledgment does not resolve a limitation.

**Basis:** R2 and R5 motivate attention to limitation framing. They do not prove that an equivalent scoped statement raises scores. This operation is deliberately narrower than limitation laundering.

## S6 — Equivalence check

**Purpose:** A fidelity check, not a score-increasing strategy.

Compare each original and rewrite against its evidence. Check whether the reader can recover the same claim, uncertainty, comparison, supporting result, adverse finding, and unresolved limitation. Check linked statements across sections. Revert an edit that changes those grounds for judgment even if it sounds stronger.

Mechanical checks that numbers and citation keys match are insufficient. Do not claim that an editorial check demonstrates actual human-review equivalence.

## When to leave the text alone

Leave a passage unchanged when there is no research-motivated rhetorical candidate, or every candidate changes meaning, certainty, or scientific implications. Clarity alone is not the stopping criterion: the input is expected to be polished already. Flag substantive gaps separately instead of treating their repair as an LLM-preference effect.
