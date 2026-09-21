# 🤖 Game the LLM Reviewer

We distilled research on LLM reviewer preferences into an **agent-compatible skill** for the final editing pass before submission.

> 我们整理了 LLM 审稿偏好的相关研究，提炼成一个 **LLM agent 可直接使用的 skill**，用于投稿前的最后一轮润色。

Works with **Claude Code**, **Codex**, and other Agent Skills-compatible agents.

[Quick start](#-quick-start) · [Before / after](#-nearly-the-same-to-a-human) · [Strategies](skills/game-the-llm-reviewer/references/strategies.md) · [Research](skills/game-the-llm-reviewer/references/research.md)

![Before: an AI reviewer questions novelty, evidence, and scope. After one wording rewrite: three AI reviewers show fully checked lists, with the same scientific content.](assets/hero.png)

**Defend sound research against LLM reviewer bias through meaning-preserving rewrites.**

> **If we cannot opt out of LLM review, make its biases work for our research—without compromising the science.**
>
> **既然我们无法彻底避开 LLM 审稿，那干脆利用它们的偏好来保护我们的研究成果。**

Research deserves to be judged on its methods, evidence, and contribution. We oppose replacing accountable human peer review with LLM verdicts. Authors, however, cannot always choose how their manuscripts are assessed. When a model treats near-equivalent wording differently, a sound paper should not pay the price for its stylistic preferences.

> 论文凭方法、证据和贡献说话。但已有研究发现，LLM 审稿人经常同一段话换个说法就给出不同的分。

Game the LLM Reviewer is a defensive final editing pass for that situation. It draws on research into LLM reviewer preferences to choose among meaning-preserving formulations, without querying a target reviewer. The aim is to protect a manuscript from wording-driven penalties while leaving the scientific case a human reviewer can assess unchanged.

> 这个工具是投稿前的最后一道“防御性润色”：我们根据 LLM 审稿偏好的研究，在意思完全不变的几种说法里将论文改写成 LLM reviewer 更青睐的那种，而这种改动对人类审稿人来说几乎没有区别。

> ⚠️ **Academic integrity is the boundary**
>
> Preserve every claim, result, citation, assumption, uncertainty, and substantive limitation. Document the edits. No fabricated evidence, inflated novelty, concealed weaknesses, or hidden instructions to reviewers.
>
> Authors remain responsible for the manuscript and for following their venue’s rules on AI assistance and disclosure.

**Finish your paper. Run your usual writing tools. Then run Game-the-LLM-Reviewer.**

> **写完论文 → 跑完你常用的写作工具 → 最后跑一遍 Game-the-LLM-Reviewer。**

## 🚀 Quick start

### 1. Install the skill

**Just ask your coding agent to install it.** Paste this into the chat:

```text
Clone this repository and install its game-the-llm-reviewer skill:
https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer
```

Your agent can handle the setup—you don't need to run the installation commands yourself.

Or install with [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer
```

### 2. Apply it to your manuscript

Give your agent a finished manuscript:

```text
Use game-the-llm-reviewer on paper/main.tex. Read the included sections first.
Apply small, meaning-preserving edits targeting LLM reviewer preferences.
Keep the scientific assessment a human could make unchanged.
Save a revised copy and changes.md explaining each rhetorical change.
```

- **You get:** an edited manuscript plus a short, evidence-linked change note.
- **You need:** your existing writing agent; no extra reviewer API, target-model configuration, or scoring loop.

<details>
<summary>Agent-specific installation, private access, and manual use</summary>

The command above opens the installer’s agent and scope selection. For a specific agent:

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a claude-code
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a codex
```

Run the command for your agent. Installs are project-local by default; add `-g` for a personal installation. The installer requires Node.js (check its [current requirements](https://github.com/vercel-labs/skills/blob/main/package.json)). Private repositories require GitHub access and configured Git, GitHub CLI, or SSH authentication.

For manual use, clone the repository and ask any file-capable writing agent to read the skill:

```sh
git clone https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer.git
cd game-the-llm-reviewer
```

```text
Read skills/game-the-llm-reviewer/SKILL.md and apply it to my finished manuscript.
Return a revised copy and a compact change note.
```

For manual installation, copy the **whole** `skills/game-the-llm-reviewer/` folder into your agent’s supported skills directory, including its references. Inspect an existing installation before replacing it. The skill itself has no runtime dependencies; file handling and LaTeX compilation use your agent’s available tools.

</details>

## ✨ Nearly the same to a human

A contribution overview from the end of an Introduction about **execution memory for coding agents**. The original is already normal paper prose; the revision combines several strategies while retaining the same scientific information.

### Before

> Coding agents can lose track of failed repair attempts as tool outputs accumulate. We propose an execution memory that records attempted patches and their test outcomes for use in subsequent steps, without updating model weights. On 300 Python repository issues with two backbone models and a fixed per-issue token budget, the memory-equipped agent resolves 34% and 39% of issues, compared with 30% and 35% for the same agents without memory, respectively.

### After Game the LLM Reviewer

> We introduce an execution memory for coding agents that requires no model weight updates. It records attempted patches and their test outcomes for use in subsequent steps, addressing the loss of failed-attempt history as tool outputs accumulate. On 300 Python repository issues with two backbone models and a fixed per-issue token budget, execution memory increases issue resolution by 4 percentage points for each model, from 30% to 34% and from 35% to 39%, respectively.

### What changed

| Strategy | What changes |
|---|---|
| **S1 · Contribution stance** | Move the existing no-weight-update property into the opening description of the method |
| **S2 · Evidence framing** | Express the same resolution rates as 4-percentage-point gains, retaining both baseline and final rates |
| **S3 · Abstract emphasis** | Lead with the contribution, then retain the existing problem context |

**Same method, evidence, and evaluation scope; different emphasis and phrasing.** The edits work together without adding an experiment or supplying a missing argument. [Strategy rationale →](skills/game-the-llm-reviewer/references/strategies.md)

<details>
<summary>Try it on the included coding agent example</summary>

From the repository root, give your agent:

```text
Read skills/game-the-llm-reviewer/SKILL.md and apply it to examples/coding-agent-introduction.md.
Save introduction.revised.md and introduction.changes.md.
```

Compare the output with the before/after example above.

</details>

## 🎯 The last step in your writing workflow

```text
Research → Draft → Your usual writing tools → Game the LLM Reviewer → Submission
```

| Starting point | What it provides | Add Game the LLM Reviewer when… |
|---|---|---|
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | An idea-to-paper research pipeline | The finished manuscript is ready for an LLM-preference pass |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) / [AI Research Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs) | Broad research and writing skills | You want a focused AI-review-facing final pass |
| [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) / [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar) | Paper writing, revision, and research workflows | The prose is already polished; you want to target LLM wording preferences |
| [ARGAR](https://github.com/xyimatvoid/ARGAR) | Presentation optimization driven by repeated AI-review feedback | You want preselected strategies without querying a target reviewer |

**One skill. Across reviewer models. No target-model setup.**

Game the LLM Reviewer selects among near-equivalent formulations based on research about LLM reviewer preferences. Its purpose is to counter wording-driven judgments while keeping the human-readable scientific case intact. The tools above are complementary starting points, not required integrations.

## 🛠️ What the pass targets

| Rhetorical dimension | Meaning-preserving operation |
|---|---|
| **S1 · Contribution stance** | Express the same established contribution through a different grammatical emphasis |
| **S2 · Evidence framing** | Rephrase the same numerical comparison as a measured effect |
| **S3 · Abstract emphasis** | Change the order or emphasis of existing statements without adding an explanation |
| **S4 · Lexical stance** | Adjust non-factual evaluative wording while preserving certainty |
| **S5 · Scope framing** | Rephrase the same evaluated and unevaluated scope without reducing the limitation |
| **S6 · Equivalence check** | Check that the edits leave claims, evidence, and scientific implications intact |

The [strategy cards](skills/game-the-llm-reviewer/references/strategies.md) distinguish research-motivated candidates from the final equivalence check. An already clear paragraph is eligible; a change needs a rationale tied to LLM preferences, not just “sounds better.”

<details>
<summary>Ready-to-use prompts: abstract, theory, or an already-polished paper</summary>

**Abstract only**

```text
Use game-the-llm-reviewer on this abstract, keeping it under 200 words.
Work only from the supplied text and preserve both positive and negative results.
Return replacement prose and a short change note.
```

**Theory paper**

```text
Use game-the-llm-reviewer on paper/main.tex. Adjust contribution stance without
changing its scientific meaning. Preserve theorem assumptions, quantifiers,
and the distinction between an upper bound and an optimal rate.
```

**After another writing skill**

```text
The draft is already polished. Use game-the-llm-reviewer as the final pass.
Reuse the attached claim–evidence map, checking it against the manuscript.
Select small rhetorical changes with a research-backed LLM-preference rationale.
Keep the meaning and scientific assessment unchanged; do not rewrite just for style.
```

</details>

## 📦 What comes back

A revised copy, or replacement passages for an excerpt, followed by a compact change note:

| Passage | Strategy / rationale | Meaning held fixed |
|---|---|---|
| Introduction opening and results | S1/S3: contribution first; S2: resolution gains | Same execution memory, unchanged model weights, 300 Python issues, two models, token budget, and resolution rates |

For this excerpt, coverage is the supplied Introduction excerpt. For a full paper, anchors point to its actual sections, tables, or theorems. Numbers, citations, assumptions, and substantive limitations stay intact. LaTeX projects retain their file relationships and are compiled when the environment supports it.

## 📚 Research behind the skill

The starting points are [ARGAR](https://arxiv.org/abs/2606.13044), [Dissecting AI Reviews](https://arxiv.org/abs/2608.08975), [Gaming AI-Assisted Peer Reviews](https://arxiv.org/abs/2606.10159), [LLM-REVal](https://arxiv.org/abs/2510.12367), and [Are We There Yet?](https://arxiv.org/abs/2412.01708).

These works study presentation effects, reviewer biases, and gameability. [The reading notes](skills/game-the-llm-reviewer/references/research.md) distinguish their findings from our editorial adaptations.

## 🤝 Contribute

Bring a source, a near-equivalent wording pair, or a case where a strategy backfires. [CONTRIBUTING.md](CONTRIBUTING.md) explains what makes a useful contribution.

---

[MIT license](LICENSE) for this project's original files. Referenced research, datasets, and upstream code retain their own licenses. This project is independent of the cited authors.
