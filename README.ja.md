# 🤖 Game the LLM Reviewer

[English / 中文](README.md) · [日本語](README.ja.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md)

Game the LLM Reviewer は、完成した論文を投稿前に編集するための **スキル**です。LLM による査読の選好に関する研究知見をもとに、論文の科学的な意味を保ちながら、表現を小さく調整します。

**Claude Code**、**Codex**、および Agent Skills に対応する他のエージェントで利用できます。

[クイックスタート](#quick-start) · [変更前と変更後](#before-after) · [戦略](skills/game-the-llm-reviewer/references/strategies.md) · [研究](skills/game-the-llm-reviewer/references/research.md)

![AI 査読者が論文に疑問を呈し、表現の書き換え後には、同じ科学的内容に対してより好意的に反応する様子。](assets/hero.png)

> **LLM による査読を完全には避けられないなら、その選好を理解し、研究成果を守るために活用しましょう。**

私たちは、査読の判断を LLM に委ねることに反対しています。しかし、査読者が LLM を使うかどうかを著者が決められることは少なく、表現の変更が評価に影響しうることも研究で示されています。このスキルは、通常の執筆と推敲を終えた著者が、対象の査読モデルに問い合わせることなく、そのような選好を考慮するためのものです。

> 論文は手法、証拠、貢献に基づいて評価されるべきです。それでも、LLM 査読者は同じ段落でも言い換えによって異なる点数を付けることがあると報告されています。

> このツールは投稿前の最後の「防御的な推敲」です。LLM 査読の選好に関する研究をもとに、意味を保った複数の表現から、人間が評価する科学的内容をほぼ変えずに、LLM 査読者に好まれる可能性のある表現を選びます。

> ⚠️ **学術的誠実性**
>
> 編集では、引用、仮定、不確実性、実質的な限界を含め、論文の主張とそれを支える証拠を保つ必要があります。変更はすべて記録してください。結果の捏造、新規性の誇張、弱点の隠蔽、査読者への隠れた指示は、このスキルの対象外です。
>
> 原稿への責任と、AI 支援およびその開示に関する投稿先の規則を守る責任は、著者にあります。

> **論文を完成させる → 普段の執筆ツールを使う → 最後に Game-the-LLM-Reviewer を使う。**

<a id="quick-start"></a>

## 🚀 クイックスタート

### 1. スキルをインストールする

**コーディングエージェントに次のように依頼してください。**

```text
このリポジトリをクローンし、game-the-llm-reviewer スキルをインストールしてください。
https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer
```

または [Skills CLI](https://github.com/vercel-labs/skills) でインストールします。

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer
```

### 2. 原稿に適用する

完成した原稿をエージェントに渡します。

```text
paper/main.tex に game-the-llm-reviewer を適用してください。まず取り込まれている各節を読んでください。
LLM 査読者の選好を考慮し、意味を保つ小さな表現変更を行ってください。
人間が行える科学的評価が変わらないようにしてください。
修正版のコピーと、各修辞的変更を説明する changes.md を保存してください。
```

エージェントは **修正版のコピー**と、編集内容を説明する **変更メモ**を保存します。既存の執筆環境で使え、追加の査読 API は不要です。

<details>
<summary>エージェントを指定したインストール、非公開リポジトリへのアクセス、手動での利用</summary>

エージェントを明示的に選ぶ場合：

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a claude-code
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a codex
```

使用するエージェントに対応するコマンドを実行してください。既定ではプロジェクト単位でインストールされます。個人用にインストールするには `-g` を付けます。インストーラーには Node.js が必要です（[現在の要件](https://github.com/vercel-labs/skills/blob/main/package.json)を確認してください）。非公開リポジトリでは GitHub へのアクセス権と、Git、GitHub CLI、または SSH の認証設定が必要です。

手動で利用する場合は、リポジトリをクローンし、ファイルを読める執筆エージェントにスキルを読むよう依頼します。

```sh
git clone https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer.git
cd game-the-llm-reviewer
```

```text
skills/game-the-llm-reviewer/SKILL.md を読み、完成した原稿に適用してください。
修正版のコピーと簡潔な変更メモを返してください。
```

手動でインストールする場合は、参照資料も含め、`skills/game-the-llm-reviewer/` フォルダー **全体**を、エージェントが対応するスキルディレクトリにコピーしてください。既存のインストールを置き換える前に、その内容を確認してください。スキル自体に実行時の依存関係はありません。ファイル処理と LaTeX のコンパイルには、エージェントで利用できるツールを使います。

</details>

<a id="before-after"></a>

## ✨ 変更前と変更後

次の例は、**コーディングエージェントの実行メモリ**に関する論文の Introduction にある、貢献の概要です。

### 変更前

> コーディングエージェントは、ツールの出力が蓄積するにつれて、失敗した修正の試行を見失うことがあります。私たちは、モデルの重みを更新せずに、試したパッチとそのテスト結果を記録し、後続のステップで利用する実行メモリを提案します。Python リポジトリの 300 件の issue を対象に、2 つの基盤モデルと issue ごとに固定したトークン予算で評価したところ、実行メモリを備えたエージェントの解決率はそれぞれ 34% と 39% でした。同じエージェントでメモリを使わない場合は、それぞれ 30% と 35% でした。

### Game the LLM Reviewer 適用後

> 私たちは、モデルの重みの更新を必要としない、コーディングエージェント向けの実行メモリを導入します。これは試したパッチとそのテスト結果を記録して後続のステップで利用し、ツールの出力が蓄積するにつれて失敗した試行の履歴が失われる問題に対処します。Python リポジトリの 300 件の issue を対象に、2 つの基盤モデルと issue ごとに固定したトークン予算で評価したところ、実行メモリは各モデルの issue 解決率を 4 パーセントポイント向上させ、それぞれ 30% から 34%、35% から 39% に引き上げました。

### 変更点

| 戦略 | 変更内容 |
|---|---|
| **S1 · 貢献の打ち出し方** | 既存の「重みの更新が不要」という特性を、手法の冒頭の説明に移す |
| **S2 · 証拠の示し方** | ベースラインと最終的な解決率をともに残し、同じ数値を 4 パーセントポイントの改善として表現する |
| **S3 · 要旨での強調** | 貢献から始め、その後に元の問題背景を残す |

どちらも同じ手法と評価を記述しています。修正版は貢献を前面に出し、既存の解決率の差をパーセントポイントで示しています。詳しくは[戦略カード](skills/game-the-llm-reviewer/references/strategies.md)をご覧ください。

<details>
<summary>付属のコーディングエージェントの例で試す</summary>

リポジトリのルートで、エージェントに次のように依頼します。

```text
skills/game-the-llm-reviewer/SKILL.md を読み、examples/coding-agent-introduction.md に適用してください。
introduction.revised.md と introduction.changes.md を保存してください。
```

出力を上記の変更前・変更後の例と比較してください。

</details>

## 🎯 他の執筆ツールとの併用

草稿の作成と通常の推敲が完了してから、このスキルを使ってください。次のプロジェクトが提供するものを含め、既存の執筆ワークフローの後に利用できます。

| プロジェクト | 組み合わせ方 |
|---|---|
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 自動化された研究パイプラインで論文を作成します。完成した草稿にこのスキルを適用します。 |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) / [AI Research Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs) | より広範な研究・執筆ツールを提供し、前段階で利用できます。 |
| [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) / [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 草稿作成と改稿を支援します。それらの編集が終わってからこのスキルを適用します。 |
| [ARGAR](https://github.com/xyimatvoid/ARGAR) | AI 査読のフィードバックを繰り返し使って提示方法を最適化します。このスキルは査読者とのフィードバックループを使わず、あらかじめ用意した編集戦略を適用します。 |

## 🛠️ 編集戦略

| 修辞的な観点 | 意味を保つ操作 |
|---|---|
| **S1 · 貢献の打ち出し方** | 既に示されている同じ貢献を、文法的な焦点を変えて表現する |
| **S2 · 証拠の示し方** | 同じ数値比較を、測定された効果として言い換える |
| **S3 · 要旨での強調** | 説明を追加せず、既存の記述の順序や強調を変える |
| **S4 · 語彙による姿勢** | 確実性の程度を保ちながら、事実を表すものではない評価的な言葉を調整する |
| **S5 · 範囲の示し方** | 限界を弱めず、同じ評価済み・未評価の範囲を言い換える |
| **S6 · 同等性の確認** | 編集によって主張、証拠、科学的含意が変わっていないことを確認する |

各[戦略カード](skills/game-the-llm-reviewer/references/strategies.md)は、いつ編集を行い、何を保つべきかを説明しています。エージェントは S1–S5 から適切な編集を選び、S6 で原文と照合します。文章を変更せずに残す場合もあります。

<details>
<summary>そのまま使える依頼文：要旨、理論論文、推敲済みの論文</summary>

**要旨のみ**

```text
この要旨に game-the-llm-reviewer を適用し、200 語未満に収めてください。
提示した文章の事実だけを使い、肯定的な結果と否定的な結果の両方を保ってください。
差し替え用の文章と短い変更メモを返してください。
```

**理論論文**

```text
paper/main.tex に game-the-llm-reviewer を適用してください。科学的な意味を変えずに、貢献の打ち出し方を調整してください。
定理の仮定、量化表現、上界と最適なレートの区別を保ってください。
```

**他の執筆スキルを使った後**

```text
草稿は既に推敲済みです。game-the-llm-reviewer を最終工程として使ってください。
添付の主張と証拠の対応表を原稿と照合しながら再利用してください。
付属の戦略を使い、LLM 査読の選好に対応する小さな表現変更を選んでください。
意味と科学的評価を保ち、文体だけを理由に書き換えないでください。
```

</details>

## 📦 出力

修正した原稿と変更メモが出力されます。短い抜粋の場合は、差し替え用の文章と、その場での変更説明を返すこともできます。変更メモの例：

| 箇所 | 戦略・理由 | 保持する意味 |
|---|---|---|
| Introduction の冒頭と結果 | S1/S3：貢献を先に示す。S2：解決率の改善 | 同じ実行メモリ、変更しないモデルの重み、Python の issue 300 件、2 つのモデル、トークン予算、解決率 |

メモには論文のどの部分を読んだかを示し、各編集を関連する証拠と結び付けます。LaTeX プロジェクトではファイル間の関係を保ち、適切なツールチェーンが利用できる場合に修正版をコンパイルします。

## 📚 参考文献

[研究ノート](skills/game-the-llm-reviewer/references/research.md)は次の論文を要約し、その知見と編集戦略の対応を示しています。

- [How Can Rhetoric Reward-Hack AI Reviewers?](https://arxiv.org/abs/2608.08975)：どの修辞的な観点が査読に影響するかを調べています。
- [No Hidden Prompts Needed!](https://arxiv.org/abs/2606.13044)：ARGAR を使い、提示方法だけを変更する改稿を研究しています。
- [Gaming AI-Assisted Peer Reviews](https://arxiv.org/abs/2606.10159)：要旨の言い換えを研究しています。
- [LLM-REVal](https://arxiv.org/abs/2510.12367) 人間の査読者と LLM 査読者の文章表現に対する選好を比較しています。
- [Are We There Yet?](https://arxiv.org/abs/2412.01708)：開示された限界への反応を含め、査読の失敗を調べています。

## 🤝 コントリビューション

訂正や表現例の追加を歓迎します。戦略の変更を提案する場合は、根拠となる出典や理由を添えてください。[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

---

このプロジェクト独自のファイルには [MIT ライセンス](LICENSE)が適用されます。参照している研究、データセット、上流のコードには、それぞれのライセンスが引き続き適用されます。このプロジェクトは、引用した研究の著者から独立したものです。
