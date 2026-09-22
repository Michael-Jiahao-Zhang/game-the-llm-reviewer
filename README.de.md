# 🤖 Game the LLM Reviewer

[English / 中文](README.md) · [日本語](README.ja.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md)

Game the LLM Reviewer ist ein **Skill** zur Überarbeitung fertiger wissenschaftlicher Manuskripte vor der Einreichung. Auf Grundlage von Studien zu den Präferenzen LLM-basierter Gutachter nimmt er kleine sprachliche Änderungen vor, ohne die wissenschaftliche Bedeutung zu verändern.

Funktioniert mit **Claude Code**, **Codex** und anderen Agenten, die Agent Skills unterstützen.

[Schnellstart](#quick-start) · [Vorher und nachher](#before-after) · [Strategien](skills/game-the-llm-reviewer/references/strategies.md) · [Forschung](skills/game-the-llm-reviewer/references/research.md)

![Ein KI-Gutachter hinterfragt eine Arbeit; nach einer sprachlichen Überarbeitung reagieren Gutachter positiver auf denselben wissenschaftlichen Inhalt.](assets/hero.png)

> **Wenn wir LLM-basierten Gutachten nicht vollständig ausweichen können, sollten wir ihre Präferenzen zum Schutz unserer Forschungsergebnisse berücksichtigen.**

Wir lehnen es ab, Entscheidungen im Peer Review an LLMs zu übertragen. Autoren haben jedoch häufig wenig Einfluss darauf, ob ein Gutachter ein solches Modell verwendet. Studien zeigen, dass sprachliche Änderungen die Bewertung beeinflussen können. Dieser Skill ermöglicht es, solche Präferenzen nach dem üblichen Schreiben und Überarbeiten zu berücksichtigen, ohne ein bestimmtes Gutachtermodell abzufragen.

> Wissenschaftliche Arbeiten sollten nach ihren Methoden, Belegen und Beiträgen beurteilt werden. Studien haben jedoch festgestellt, dass LLM-Gutachter denselben Absatz nach einer Umformulierung unterschiedlich bewerten können.

> Dieses Werkzeug dient als letzte „defensive Überarbeitung“ vor der Einreichung: Anhand von Forschung zu LLM-Präferenzen wählt es zwischen bedeutungsgleichen Formulierungen solche aus, die LLM-Gutachter möglicherweise bevorzugen, während die wissenschaftliche Beurteilungsgrundlage für Menschen nahezu unverändert bleibt.

> ⚠️ **Wissenschaftliche Integrität**
>
> Änderungen müssen die Aussagen und zugehörigen Belege der Arbeit erhalten, einschließlich Quellenangaben, Annahmen, Unsicherheiten und wesentlicher Einschränkungen. Dokumentieren Sie jede Änderung. Erfundenen Ergebnissen, übertriebener Neuartigkeit, verschwiegenen Schwächen und versteckten Anweisungen an Gutachter dient dieser Skill nicht.
>
> Die Autoren bleiben für das Manuskript und die Einhaltung der Vorgaben des jeweiligen Publikationsorts zu KI-Unterstützung und deren Offenlegung verantwortlich.

> **Arbeit fertigstellen → Gewohnte Schreibwerkzeuge einsetzen → Zum Schluss Game-the-LLM-Reviewer anwenden.**

<a id="quick-start"></a>

## 🚀 Schnellstart

### 1. Skill installieren

**Bitten Sie Ihren Coding-Agenten, den Skill zu installieren:**

```text
Klone dieses Repository und installiere den enthaltenen Skill game-the-llm-reviewer:
https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer
```

Oder installieren Sie ihn mit der [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer
```

### 2. Auf Ihr Manuskript anwenden

Übergeben Sie Ihrem Agenten ein fertiges Manuskript:

```text
Wende game-the-llm-reviewer auf paper/main.tex an. Lies zuerst die eingebundenen Abschnitte.
Nimm kleine, bedeutungserhaltende sprachliche Änderungen vor, die LLM-Gutachterpräferenzen berücksichtigen.
Lass die wissenschaftliche Beurteilung, die ein Mensch vornehmen könnte, unverändert.
Speichere eine überarbeitete Kopie und eine changes.md, die jede rhetorische Änderung erklärt.
```

Der Agent speichert eine **überarbeitete Kopie** und ein **Änderungsprotokoll** mit Erläuterungen. Der Skill passt in Ihre bestehende Schreibumgebung und benötigt keine zusätzliche Gutachter-API.

<details>
<summary>Installation für bestimmte Agenten, privater Zugriff und manuelle Nutzung</summary>

So wählen Sie einen Agenten ausdrücklich aus:

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a claude-code
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a codex
```

Führen Sie den Befehl für Ihren Agenten aus. Standardmäßig erfolgt die Installation nur für das jeweilige Projekt; mit `-g` installieren Sie den Skill für Ihr Benutzerkonto. Der Installer benötigt Node.js (siehe [aktuelle Anforderungen](https://github.com/vercel-labs/skills/blob/main/package.json)). Private Repositories erfordern GitHub-Zugriff und eine eingerichtete Authentifizierung über Git, GitHub CLI oder SSH.

Für die manuelle Nutzung klonen Sie das Repository und bitten einen Schreibagenten mit Dateizugriff, den Skill zu lesen:

```sh
git clone https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer.git
cd game-the-llm-reviewer
```

```text
Lies skills/game-the-llm-reviewer/SKILL.md und wende den Skill auf mein fertiges Manuskript an.
Gib eine überarbeitete Kopie und ein kurzes Änderungsprotokoll zurück.
```

Für eine manuelle Installation kopieren Sie den **gesamten** Ordner `skills/game-the-llm-reviewer/` einschließlich der Referenzdateien in das von Ihrem Agenten unterstützte Skill-Verzeichnis. Prüfen Sie eine vorhandene Installation, bevor Sie sie ersetzen. Der Skill selbst hat keine Laufzeitabhängigkeiten; Dateiverarbeitung und LaTeX-Kompilierung erfolgen mit den verfügbaren Werkzeugen Ihres Agenten.

</details>

<a id="before-after"></a>

## ✨ Vorher und nachher

Dieses Beispiel stammt aus einer Einleitung über einen **Ausführungsspeicher für Coding-Agenten** und fasst die Beiträge zusammen.

### Vorher

> Coding-Agenten können den Überblick über fehlgeschlagene Reparaturversuche verlieren, wenn sich Werkzeugausgaben ansammeln. Wir schlagen einen Ausführungsspeicher vor, der versuchte Patches und ihre Testergebnisse für spätere Schritte aufzeichnet, ohne die Modellgewichte zu aktualisieren. Bei 300 Issues aus Python-Repositories mit zwei Basismodellen und einem festen Tokenbudget pro Issue löst der Agent mit Speicher 34% beziehungsweise 39% der Issues, verglichen mit 30% beziehungsweise 35% bei denselben Agenten ohne Speicher.

### Nach Game the LLM Reviewer

> Wir stellen einen Ausführungsspeicher für Coding-Agenten vor, der keine Aktualisierung der Modellgewichte erfordert. Er zeichnet versuchte Patches und ihre Testergebnisse für spätere Schritte auf und wirkt damit dem Verlust der Historie fehlgeschlagener Versuche entgegen, wenn sich Werkzeugausgaben ansammeln. Bei 300 Issues aus Python-Repositories mit zwei Basismodellen und einem festen Tokenbudget pro Issue erhöht der Ausführungsspeicher die Lösungsquote für jedes Modell um 4 Prozentpunkte, von 30% auf 34% beziehungsweise von 35% auf 39%.

### Was wurde geändert?

| Strategie | Änderung |
|---|---|
| **S1 · Darstellung des Beitrags** | Die bereits vorhandene Eigenschaft, keine Gewichtsaktualisierung zu benötigen, in die einleitende Methodenbeschreibung verschieben |
| **S2 · Darstellung der Belege** | Dieselben Lösungsquoten als Verbesserung um 4 Prozentpunkte ausdrücken und dabei Ausgangs- und Endwerte beibehalten |
| **S3 · Gewichtung im Abstract** | Mit dem Beitrag beginnen und anschließend den vorhandenen Problemkontext beibehalten |

Beide Fassungen beschreiben dieselbe Methode und Evaluation. Die Überarbeitung rückt den Beitrag in den Vordergrund und drückt die vorhandenen Quotenunterschiede in Prozentpunkten aus. Weitere Einzelheiten finden Sie in den [Strategiekarten](skills/game-the-llm-reviewer/references/strategies.md).

<details>
<summary>Am mitgelieferten Coding-Agenten-Beispiel ausprobieren</summary>

Geben Sie Ihrem Agenten im Stammverzeichnis des Repositories folgende Anweisung:

```text
Lies skills/game-the-llm-reviewer/SKILL.md und wende den Skill auf examples/coding-agent-introduction.md an.
Speichere introduction.revised.md und introduction.changes.md.
```

Vergleichen Sie das Ergebnis mit dem obigen Vorher-Nachher-Beispiel.

</details>

## 🎯 Verwendung mit anderen Schreibwerkzeugen

Wenden Sie diesen Skill an, sobald der Entwurf und die übliche sprachliche Überarbeitung abgeschlossen sind. Er kann an bestehende Schreibabläufe anschließen, einschließlich der Abläufe dieser Projekte:

| Projekt | Einordnung |
|---|---|
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Erstellt eine Arbeit über einen automatisierten Forschungsablauf; wenden Sie diesen Skill auf den fertigen Entwurf an. |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) / [AI Research Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs) | Bieten umfassendere Forschungs- und Schreibwerkzeuge für frühere Arbeitsschritte. |
| [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) / [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar) | Decken Entwurf und Überarbeitung ab; wenden Sie diesen Skill nach Abschluss dieser Änderungen an. |
| [ARGAR](https://github.com/xyimatvoid/ARGAR) | Optimiert die Darstellung durch wiederholtes Feedback von KI-Gutachtern. Dieser Skill wendet vorbereitete Bearbeitungsstrategien ohne Gutachter-Feedbackschleife an. |

## 🛠️ Bearbeitungsstrategien

| Rhetorische Dimension | Bedeutungserhaltender Eingriff |
|---|---|
| **S1 · Darstellung des Beitrags** | Denselben belegten Beitrag mit einem anderen grammatischen Schwerpunkt ausdrücken |
| **S2 · Darstellung der Belege** | Denselben numerischen Vergleich als gemessenen Effekt umformulieren |
| **S3 · Gewichtung im Abstract** | Reihenfolge oder Gewichtung vorhandener Aussagen ändern, ohne eine Erklärung hinzuzufügen |
| **S4 · Wortwahl und Haltung** | Wertende Formulierungen ohne Tatsachengehalt anpassen und dabei den Grad der Gewissheit beibehalten |
| **S5 · Darstellung des Geltungsbereichs** | Denselben untersuchten und nicht untersuchten Bereich umformulieren, ohne die Einschränkung abzuschwächen |
| **S6 · Äquivalenzprüfung** | Prüfen, ob Aussagen, Belege und wissenschaftliche Implikationen erhalten bleiben |

Jede [Strategiekarte](skills/game-the-llm-reviewer/references/strategies.md) beschreibt, wann eine Änderung geeignet ist und was erhalten bleiben muss. Der Agent wählt passende Eingriffe aus S1–S5 aus und prüft sie mit S6 gegen das Original. Er kann eine Passage auch unverändert lassen.

<details>
<summary>Direkt verwendbare Prompts: Abstract, Theorie oder bereits überarbeitete Arbeit</summary>

**Nur das Abstract**

```text
Wende game-the-llm-reviewer auf dieses Abstract an und halte es unter 200 Wörtern.
Arbeite nur mit dem bereitgestellten Text und erhalte sowohl positive als auch negative Ergebnisse.
Gib einen Ersatztext und ein kurzes Änderungsprotokoll zurück.
```

**Theoretische Arbeit**

```text
Wende game-the-llm-reviewer auf paper/main.tex an. Passe die Darstellung des Beitrags an, ohne seine wissenschaftliche Bedeutung zu ändern.
Erhalte die Annahmen der Sätze, Quantoren und die Unterscheidung zwischen einer oberen Schranke und einer optimalen Rate.
```

**Nach einem anderen Schreib-Skill**

```text
Der Entwurf ist bereits überarbeitet. Nutze game-the-llm-reviewer als letzten Durchgang.
Verwende die beigefügte Zuordnung von Aussagen und Belegen erneut und gleiche sie mit dem Manuskript ab.
Wähle anhand der enthaltenen Strategien kleine sprachliche Änderungen aus, die LLM-Gutachterpräferenzen berücksichtigen.
Lass Bedeutung und wissenschaftliche Beurteilung unverändert; schreibe nicht allein aus Stilgründen um.
```

</details>

## 📦 Ausgabe

Die Ausgabe enthält ein überarbeitetes Manuskript und ein Änderungsprotokoll. Bei einem kurzen Auszug kann der Agent einen Ersatztext liefern und die Änderungen direkt erläutern. Beispiel für ein Änderungsprotokoll:

| Passage | Strategie / Begründung | Erhaltene Bedeutung |
|---|---|---|
| Beginn der Einleitung und Ergebnisse | S1/S3: Beitrag zuerst; S2: höhere Lösungsquoten | Derselbe Ausführungsspeicher, unveränderte Modellgewichte, 300 Python-Issues, zwei Modelle, Tokenbudget und Lösungsquoten |

Das Protokoll nennt die gelesenen Teile der Arbeit und verknüpft Änderungen mit den relevanten Belegen. Bei LaTeX-Projekten erhält der Agent die Beziehungen zwischen Dateien und kompiliert die überarbeitete Fassung, sofern geeignete Werkzeuge verfügbar sind.

## 📚 Referenzen

Die [Forschungsnotizen](skills/game-the-llm-reviewer/references/research.md) fassen diese Arbeiten zusammen und ordnen ihre Ergebnisse den Bearbeitungsstrategien zu:

- [How Can Rhetoric Reward-Hack AI Reviewers?](https://arxiv.org/abs/2608.08975) untersucht, welche rhetorischen Dimensionen Gutachten beeinflussen.
- [No Hidden Prompts Needed!](https://arxiv.org/abs/2606.13044) untersucht mit ARGAR Überarbeitungen, die nur die Darstellung verändern.
- [Gaming AI-Assisted Peer Reviews](https://arxiv.org/abs/2606.10159) untersucht die Umformulierung von Abstracts.
- [LLM-REVal](https://arxiv.org/abs/2510.12367) vergleicht die Schreibstilpräferenzen menschlicher und LLM-basierter Gutachter.
- [Are We There Yet?](https://arxiv.org/abs/2412.01708) untersucht Fehler bei der Begutachtung, einschließlich Reaktionen auf offengelegte Einschränkungen.

## 🤝 Mitwirken

Korrekturen und weitere Formulierungsbeispiele sind willkommen. Fügen Sie bei vorgeschlagenen Strategieänderungen die Quelle oder Begründung bei; siehe [CONTRIBUTING.md](CONTRIBUTING.md).

---

Für die ursprünglichen Dateien dieses Projekts gilt die [MIT-Lizenz](LICENSE). Referenzierte Forschungsarbeiten, Datensätze und Code anderer Projekte behalten ihre jeweiligen Lizenzen. Dieses Projekt ist von den zitierten Autoren unabhängig.
