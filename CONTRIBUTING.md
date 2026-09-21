# Contributing

Game the LLM Reviewer opposes replacing accountable human peer review with LLM verdicts. It helps authors respond to wording bias when they cannot opt out of automated assessment. Academic integrity governs every contribution: preserve evidence and limitations, and never inflate the scientific case to obtain a favorable score. Contributions should isolate rhetorical changes in an already-polished manuscript while preserving the scientific assessment a human reader could make.

For a strategy change, include:

- The changed rhetorical cue and why LLM-preference research motivates it. A generic clarity improvement is not enough.
- A source link and the relevant section, if the claim comes from research.
- The distinction between a reported finding and your proposed editorial adaptation.
- A near-equivalent before/after pair, preferably isolating one cue, with the scientific meaning and evidence held fixed.
- Why the versions leave a human reader the same grounds for judgment; do not present this rationale as a measured human evaluation.
- A case where the strategy should not be applied or would backfire.

Fictional examples are welcome when labeled. No benchmark run is required for a documentation or strategy contribution. If reporting a measured gain, give enough context to interpret it: model/version, review instructions, sample size, selection process, and whether the reviewer participated in optimization. Do not present a selected high score as a typical result.

Keep the skill self-contained inside `skills/game-the-llm-reviewer/`. Avoid adding provider dependencies or reviewer-query loops to the default path. Update the README if the user-facing behavior changes. Do not include private manuscripts, credentials, or text you lack permission to redistribute.

Simple fixes can be simple pull requests. Source corrections and negative examples are especially useful.
