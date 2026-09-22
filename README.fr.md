# 🤖 Game the LLM Reviewer

[English / 中文](README.md) · [日本語](README.ja.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md)

Game the LLM Reviewer est une **compétence (skill)** permettant de réviser un article terminé avant sa soumission. Elle s'appuie sur les résultats d'études consacrées aux préférences des LLM en matière d'évaluation pour apporter de légères modifications de formulation tout en préservant le sens scientifique de l'article.

Compatible avec **Claude Code**, **Codex** et les autres agents prenant en charge Agent Skills.

[Démarrage rapide](#quick-start) · [Avant et après](#before-after) · [Stratégies](skills/game-the-llm-reviewer/references/strategies.md) · [Recherche](skills/game-the-llm-reviewer/references/research.md)

![Un évaluateur IA remet en question un article ; après une reformulation, les évaluateurs réagissent plus favorablement au même contenu scientifique.](assets/hero.png)

> **Si nous ne pouvons pas éviter entièrement l'évaluation par des LLM, tenons compte de leurs préférences pour protéger nos travaux de recherche.**

Nous nous opposons au fait de confier aux LLM les décisions de l'évaluation par les pairs. Les auteurs ont toutefois souvent peu de prise sur le choix d'un évaluateur d'en utiliser un, et des études ont montré que des changements de formulation peuvent influencer l'évaluation. Cette compétence permet de tenir compte de ces préférences après le travail habituel de rédaction et de révision, sans interroger un modèle évaluateur cible.

> Un article devrait être jugé sur ses méthodes, ses éléments probants et ses contributions. Pourtant, des travaux ont montré que des évaluateurs LLM peuvent attribuer des notes différentes à un même paragraphe lorsqu'il est reformulé.

> Cet outil constitue une dernière révision « défensive » avant la soumission : il s'appuie sur les recherches concernant les préférences des évaluateurs LLM pour choisir, parmi des formulations de sens équivalent, celles susceptibles de leur convenir davantage, tout en laissant pratiquement inchangé le contenu scientifique qu'une personne peut évaluer.

> ⚠️ **Intégrité scientifique**
>
> Les modifications doivent préserver les affirmations de l'article et les éléments qui les étayent, notamment les citations, les hypothèses, les incertitudes et les limites substantielles. Consignez chaque modification. Les résultats inventés, la nouveauté exagérée, les faiblesses dissimulées et les instructions cachées adressées aux évaluateurs sont exclus du champ de cette compétence.
>
> Les auteurs restent responsables du manuscrit et du respect des règles de la revue ou de la conférence concernant l'assistance de l'IA et sa déclaration.

> **Terminez l'article → Utilisez vos outils de rédaction habituels → Appliquez Game-the-LLM-Reviewer en dernier.**

<a id="quick-start"></a>

## 🚀 Démarrage rapide

### 1. Installer la compétence

**Demandez à votre agent de programmation de l'installer :**

```text
Clone ce dépôt et installe sa compétence game-the-llm-reviewer :
https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer
```

Ou installez-la avec [Skills CLI](https://github.com/vercel-labs/skills) :

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer
```

### 2. L'appliquer à votre manuscrit

Fournissez un manuscrit terminé à votre agent :

```text
Applique game-the-llm-reviewer à paper/main.tex. Lis d'abord les sections incluses.
Apporte de légères modifications de formulation tenant compte des préférences des évaluateurs LLM, tout en préservant le sens.
Laisse inchangée l'évaluation scientifique qu'une personne pourrait faire.
Enregistre une copie révisée et un fichier changes.md expliquant chaque modification rhétorique.
```

L'agent enregistre une **copie révisée** et une **note de modifications** expliquant les changements. La compétence fonctionne avec votre environnement de rédaction existant et ne nécessite aucune API d'évaluation supplémentaire.

<details>
<summary>Installation pour un agent précis, accès privé et utilisation manuelle</summary>

Pour sélectionner explicitement un agent :

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a claude-code
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a codex
```

Exécutez la commande correspondant à votre agent. Par défaut, l'installation est locale au projet ; ajoutez `-g` pour une installation personnelle. Le programme d'installation nécessite Node.js (consultez les [prérequis actuels](https://github.com/vercel-labs/skills/blob/main/package.json)). Les dépôts privés nécessitent un accès à GitHub et une authentification configurée avec Git, GitHub CLI ou SSH.

Pour une utilisation manuelle, clonez le dépôt et demandez à un agent de rédaction capable de lire des fichiers de consulter la compétence :

```sh
git clone https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer.git
cd game-the-llm-reviewer
```

```text
Lis skills/game-the-llm-reviewer/SKILL.md et applique la compétence à mon manuscrit terminé.
Renvoie une copie révisée et une brève note de modifications.
```

Pour une installation manuelle, copiez le dossier **entier** `skills/game-the-llm-reviewer/`, références comprises, dans le répertoire de compétences pris en charge par votre agent. Examinez toute installation existante avant de la remplacer. La compétence elle-même n'a pas de dépendances d'exécution ; la gestion des fichiers et la compilation LaTeX utilisent les outils disponibles dans votre agent.

</details>

<a id="before-after"></a>

## ✨ Avant et après

Cet exemple présente un aperçu des contributions dans l'introduction d'un article sur la **mémoire d'exécution pour les agents de programmation**.

### Avant

> Les agents de programmation peuvent perdre la trace des tentatives de réparation infructueuses à mesure que les sorties des outils s'accumulent. Nous proposons une mémoire d'exécution qui enregistre les correctifs tentés et les résultats de leurs tests pour les utiliser aux étapes suivantes, sans mettre à jour les poids du modèle. Sur 300 tickets de dépôts Python, avec deux modèles de base et un budget de tokens fixe par ticket, l'agent doté de mémoire résout respectivement 34% et 39% des tickets, contre 30% et 35% pour les mêmes agents sans mémoire.

### Après Game the LLM Reviewer

> Nous présentons une mémoire d'exécution pour les agents de programmation qui ne nécessite aucune mise à jour des poids du modèle. Elle enregistre les correctifs tentés et les résultats de leurs tests pour les utiliser aux étapes suivantes, afin de remédier à la perte de l'historique des tentatives infructueuses lorsque les sorties des outils s'accumulent. Sur 300 tickets de dépôts Python, avec deux modèles de base et un budget de tokens fixe par ticket, la mémoire d'exécution augmente le taux de résolution de 4 points de pourcentage pour chaque modèle, de 30% à 34% et de 35% à 39%, respectivement.

### Ce qui a changé

| Stratégie | Modification |
|---|---|
| **S1 · Présentation de la contribution** | Déplacer la propriété déjà présente d'absence de mise à jour des poids dans la description initiale de la méthode |
| **S2 · Présentation des éléments probants** | Exprimer les mêmes taux de résolution comme des gains de 4 points de pourcentage, en conservant les taux de référence et les taux finaux |
| **S3 · Mise en avant dans le résumé** | Commencer par la contribution, puis conserver le contexte initial du problème |

Les deux versions décrivent la même méthode et la même évaluation. La révision met la contribution en avant et exprime les écarts de taux existants en points de pourcentage. Consultez les [fiches de stratégies](skills/game-the-llm-reviewer/references/strategies.md) pour plus de détails.

<details>
<summary>Essayer avec l'exemple d'agent de programmation fourni</summary>

Depuis la racine du dépôt, demandez à votre agent :

```text
Lis skills/game-the-llm-reviewer/SKILL.md et applique la compétence à examples/coding-agent-introduction.md.
Enregistre introduction.revised.md et introduction.changes.md.
```

Comparez le résultat à l'exemple avant/après ci-dessus.

</details>

## 🎯 Utilisation avec d'autres outils de rédaction

Utilisez cette compétence une fois la rédaction et la révision habituelle terminées. Elle peut intervenir à la fin d'un processus de rédaction existant, notamment ceux proposés par les projets suivants :

| Projet | Place dans le processus |
|---|---|
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Produit un article au moyen d'un processus de recherche automatisé ; appliquez cette compétence au manuscrit terminé. |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) / [AI Research Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs) | Proposent des outils de recherche et de rédaction plus larges, utilisables plus tôt dans le processus. |
| [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) / [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar) | Couvrent la rédaction et la révision ; appliquez cette compétence une fois ces modifications terminées. |
| [ARGAR](https://github.com/xyimatvoid/ARGAR) | Optimise la présentation à partir de retours répétés d'évaluateurs IA. Cette compétence applique un ensemble prédéfini de stratégies d'édition sans boucle de retour d'un évaluateur. |

## 🛠️ Stratégies d'édition

| Dimension rhétorique | Opération préservant le sens |
|---|---|
| **S1 · Présentation de la contribution** | Exprimer la même contribution établie avec une mise en relief grammaticale différente |
| **S2 · Présentation des éléments probants** | Reformuler la même comparaison numérique sous la forme d'un effet mesuré |
| **S3 · Mise en avant dans le résumé** | Modifier l'ordre ou l'accentuation d'énoncés existants sans ajouter d'explication |
| **S4 · Choix lexicaux** | Ajuster les formulations appréciatives sans contenu factuel, tout en conservant le degré de certitude |
| **S5 · Présentation de la portée** | Reformuler la même portée évaluée et non évaluée sans atténuer la limitation |
| **S6 · Vérification de l'équivalence** | Vérifier que les modifications préservent les affirmations, les éléments probants et les implications scientifiques |

Chaque [fiche de stratégie](skills/game-the-llm-reviewer/references/strategies.md) précise quand appliquer une modification et ce qu'il faut préserver. L'agent choisit les changements pertinents parmi S1–S5, puis utilise S6 pour les comparer à l'original. Il peut laisser un passage inchangé.

<details>
<summary>Instructions prêtes à l'emploi : résumé, théorie ou article déjà révisé</summary>

**Le résumé uniquement**

```text
Applique game-the-llm-reviewer à ce résumé en restant sous 200 mots.
Travaille uniquement à partir du texte fourni et conserve les résultats positifs comme négatifs.
Renvoie un texte de remplacement et une brève note de modifications.
```

**Article théorique**

```text
Applique game-the-llm-reviewer à paper/main.tex. Ajuste la présentation de la contribution sans modifier son sens scientifique.
Préserve les hypothèses des théorèmes, les quantificateurs et la distinction entre une borne supérieure et un taux optimal.
```

**Après une autre compétence de rédaction**

```text
Le manuscrit est déjà révisé. Utilise game-the-llm-reviewer comme dernière étape.
Réutilise la correspondance entre affirmations et éléments probants jointe, en la vérifiant dans le manuscrit.
Utilise les stratégies fournies pour sélectionner de légères modifications de formulation tenant compte des préférences des évaluateurs LLM.
Préserve le sens et l'évaluation scientifique ; ne reformule pas uniquement pour le style.
```

</details>

## 📦 Résultat

Le résultat comprend un manuscrit révisé et une note de modifications. Pour un court extrait, l'agent peut renvoyer un texte de remplacement et expliquer les changements directement à côté. Exemple de note :

| Passage | Stratégie / justification | Sens préservé |
|---|---|---|
| Début de l'introduction et résultats | S1/S3 : contribution en premier ; S2 : gains de résolution | Même mémoire d'exécution, poids du modèle inchangés, 300 tickets Python, deux modèles, budget de tokens et taux de résolution |

La note précise les parties de l'article qui ont été lues et relie les modifications aux éléments probants pertinents. Pour les projets LaTeX, l'agent préserve les relations entre fichiers et compile la version révisée lorsque les outils nécessaires sont disponibles.

## 📚 Références

Les [notes de recherche](skills/game-the-llm-reviewer/references/research.md) résument ces articles et relient leurs résultats aux stratégies d'édition :

- [How Can Rhetoric Reward-Hack AI Reviewers?](https://arxiv.org/abs/2608.08975) examine quelles dimensions rhétoriques influencent les évaluations.
- [No Hidden Prompts Needed!](https://arxiv.org/abs/2606.13044) étudie, avec ARGAR, des révisions portant uniquement sur la présentation.
- [Gaming AI-Assisted Peer Reviews](https://arxiv.org/abs/2606.10159) étudie la reformulation des résumés.
- [LLM-REVal](https://arxiv.org/abs/2510.12367) compare les préférences pour les textes humains et ceux produits par des LLM.
- [Are We There Yet?](https://arxiv.org/abs/2412.01708) examine les défaillances de l'évaluation, notamment les réactions aux limites déclarées.

## 🤝 Contribuer

Les corrections et les exemples de formulation supplémentaires sont les bienvenus. Joignez la source ou le raisonnement qui justifie toute proposition de modification d'une stratégie ; consultez [CONTRIBUTING.md](CONTRIBUTING.md).

---

Les fichiers originaux de ce projet sont distribués sous [licence MIT](LICENSE). Les recherches, jeux de données et codes tiers cités conservent leurs licences respectives. Ce projet est indépendant des auteurs cités.
