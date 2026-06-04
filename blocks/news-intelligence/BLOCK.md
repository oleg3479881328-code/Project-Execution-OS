# News Intelligence Block

## Purpose

This block gives `Project Execution OS` a reusable workflow for collecting, filtering, analyzing, scoring, and packaging news into useful project intelligence.

The goal is not to collect random news. The goal is to turn current external signals into decisions, risks, opportunities, source packs, briefs, and reusable project evidence.

## Status

`candidate`

## When To Use

Use this block when the owner or an agent asks to:

- monitor news for a project, market, technology, company, law, platform, competitor, product category, or monetization niche;
- create a daily, weekly, or event-driven digest;
- analyze current events for business impact;
- compare multiple news sources and detect narrative conflicts;
- preserve important news as project evidence;
- convert repeated news monitoring into a narrower skill or automation.

## When Not To Use

Do not use this block for:

- evergreen research that does not depend on current events;
- casual questions that only need a direct answer;
- legal, immigration, financial, or medical conclusions without source-backed caution;
- storing unverified rumors as accepted facts;
- dumping large article lists without synthesis;
- creating a permanent rule from one news cycle.

## Core Rule

News is unstable input, not knowledge by default.

A news item must be separated into:

1. source claim;
2. confirmed fact;
3. uncertain claim;
4. analysis or inference;
5. project impact;
6. recommended action;
7. storage decision.

Do not promote news into central reusable knowledge unless it has reviewed cross-project value.

## Workflow

1. Define the monitoring target.
2. Define the decision the news should support.
3. Collect recent sources from multiple source classes.
4. Deduplicate repeated wire copies and reposts.
5. Separate facts, claims, rumors, opinions, and analysis.
6. Compare source agreement and disagreement.
7. Score relevance, freshness, credibility, impact, and actionability.
8. Extract project implications.
9. Produce the smallest useful output: alert, brief, digest, source pack, decision memo, or watchlist update.
10. Decide whether anything should be captured into the project layer or central knowledge layer.

## Source Classes

Use a mix of sources when the task requires reliability:

- official sources: government pages, company blogs, platform documentation, regulatory notices, court records, filings;
- primary sources: original announcements, changelogs, repositories, papers, transcripts, datasets;
- reputable reporting: established media with editorial standards;
- specialist sources: industry newsletters, analysts, trade publications;
- community signals: GitHub issues, Reddit, forums, X posts, Discord/Telegram only as weak early signals unless independently confirmed.

## Scoring Model

Each useful news item should be scored when the answer affects a project decision:

- `freshness`: how recent the item is relative to the topic speed;
- `source_quality`: official/primary/reputable/weak;
- `corroboration`: whether independent sources agree;
- `project_relevance`: whether it affects the active project;
- `impact`: possible upside, downside, risk, or required change;
- `actionability`: whether the owner can act on it now;
- `confidence`: high, medium, low.

## Output Types

Use the smallest output that fits:

- `alert`: one urgent item with reason and action;
- `digest`: short grouped summary of several items;
- `source_pack`: clean URL list for NotebookLM or deeper review;
- `decision_memo`: recommendation tied to a project decision;
- `watchlist`: topics, keywords, sources, and triggers to monitor;
- `evidence_entry`: project-level record with source links and interpretation limits.

## Default Output Contract

For project news analysis, output:

1. `What happened`;
2. `Why it matters`;
3. `Evidence`;
4. `Confidence`;
5. `Impact on our project`;
6. `Recommended action`;
7. `Store or ignore`.

## Storage Rules

- Store raw links and source packs as references, not active knowledge.
- Store project-specific implications in the active project layer.
- Promote to `knowledge-library/` only when the lesson is reusable beyond one project and has been reviewed.
- Never store secrets, private customer data, or unstable rumors as central knowledge.

## Risks

- news decay: old articles become misleading;
- source laundering: many outlets repeat one original weak claim;
- narrative bias: sources may frame facts selectively;
- hallucinated certainty: AI may overstate weak signals;
- context bloat: dumping news into memory can poison future work;
- legal/financial/medical/political sensitivity: use extra source discipline.

## Related Nodes

- `docs/RESEARCH_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `blocks/skill-creator/BLOCK.md`

## Candidate Skills That May Later Be Split Out

- `news-digest-builder`: creates concise project digests from current sources;
- `source-pack-builder`: exports clean URL lists for NotebookLM;
- `news-impact-analyzer`: turns news into project risk/opportunity/action;
- `watchlist-maintainer`: maintains monitored topics, sources, and trigger conditions.

## Review Checklist

Before activation, check:

- no duplicate block or standard already covers this;
- source quality rules are compatible with `RESEARCH_STANDARD.md`;
- storage rules are compatible with `KNOWLEDGE_SYSTEM.md`;
- outputs are narrow enough for execution;
- candidate skills are not prematurely registered as active;
- the block does not create a giant catch-all news agent.

## Boundary

This block does not automatically run monitoring.

This block defines how news collection and analysis should be structured when requested or when an approved automation/agent invokes it.

## Final Rule

News becomes useful only when it changes a decision, updates a risk, reveals an opportunity, or produces reusable evidence.

Do not collect news for noise.
