# News Intelligence Block

## Purpose

This block gives `Project Execution OS` a reusable workflow for collecting, filtering, analyzing, scoring, and packaging news into a readable personal and project intelligence format.

The goal is not to collect random headlines. The goal is to turn current external signals into a usable view of the world: what happened, what is confirmed, what is uncertain, why it matters, what may change, and what the owner may need to do or watch.

This block is not limited to skills, software, or projects. It can be used for politics, economy, law, immigration, technology, platforms, markets, wars, elections, regulations, business trends, competitors, scientific developments, local events, and any other current-news domain.

## Status

`candidate`

## Core Position

News is not knowledge by default.

News is unstable incoming signal. It becomes useful only after it is cleaned, grouped, checked, interpreted, and packaged into a form the owner can actually read and use.

The default user value is digestibility: less noise, more structure, clear meaning, clear uncertainty, and clear practical relevance.

## When To Use

Use this block when the owner or an agent asks to:

- understand what is happening in a current news area;
- create a daily, weekly, or event-driven digest;
- monitor politics, economy, law, immigration, technology, platforms, markets, local events, or any other news field;
- compare multiple sources and detect narrative conflicts;
- separate confirmed facts from claims, rumors, opinions, and analysis;
- build a watchlist for continuing developments;
- preserve important source packs or evidence for later review;
- convert recurring monitoring into an automation, agent routine, or narrower skill only if needed later.

## When Not To Use

Do not use this block for:

- evergreen research that does not depend on current events;
- casual questions that only need a direct answer;
- dumping headlines without synthesis;
- treating one article as truth;
- storing unverified rumors as accepted facts;
- creating permanent system rules from a temporary news cycle;
- legal, immigration, financial, medical, or political conclusions without source-backed caution.

## Core Rule

Every important news item must be separated into:

1. source claim;
2. confirmed fact;
3. uncertain or disputed claim;
4. context;
5. analysis or inference;
6. possible consequence;
7. practical relevance for the owner or project;
8. storage decision.

Do not promote news into central reusable knowledge unless it has reviewed cross-domain or cross-project value.

## Workflow

1. Define the news area or question.
2. Define the needed output: quick answer, digest, alert, watchlist, source pack, or decision memo.
3. Collect recent sources from multiple source classes.
4. Deduplicate repeated wire copies, reposts, and derivative summaries.
5. Group items by topic, event, actor, geography, and consequence.
6. Separate facts, claims, rumors, opinions, and analysis.
7. Compare agreement and disagreement between sources.
8. Score freshness, source quality, corroboration, relevance, impact, actionability, and confidence.
9. Explain the meaning in plain language.
10. Produce the smallest useful output.
11. Decide whether anything should be stored as a raw reference, project-specific note, watchlist item, or central reusable lesson.

## Source Classes

Use a mix of sources when reliability matters:

- official sources: government pages, courts, agencies, legislation, regulators, company blogs, platform documentation, filings;
- primary sources: original announcements, transcripts, speeches, changelogs, repositories, papers, datasets;
- reputable reporting: established media with editorial standards;
- specialist sources: industry newsletters, analysts, trade publications, legal blogs, economic research, think tanks;
- community signals: GitHub issues, Reddit, forums, X posts, Telegram, Discord, local groups. Treat these as weak early signals unless independently confirmed.

## Scoring Model

Each important news item should be scored when the answer affects understanding, planning, money, legal position, safety, or a project decision:

- `freshness`: how recent the item is relative to the topic speed;
- `source_quality`: official, primary, reputable, specialist, community, weak;
- `corroboration`: whether independent sources agree;
- `relevance`: whether it matters to the owner, a project, a market, a location, or a decision;
- `impact`: possible upside, downside, risk, cost, opportunity, restriction, or required change;
- `actionability`: whether the owner can act now, watch only, or ignore;
- `confidence`: high, medium, low.

## Output Types

Use the smallest output that fits:

- `quick_brief`: short answer to what happened and why it matters;
- `digest`: grouped summary of several news items;
- `alert`: one urgent item with reason and action;
- `source_pack`: clean URL list for NotebookLM or deeper review;
- `timeline`: chronological sequence of events;
- `watchlist`: topics, keywords, sources, actors, and triggers to monitor;
- `decision_memo`: recommendation tied to a personal or project decision;
- `evidence_entry`: stored source-backed record with interpretation limits.

## Default Output Contract

For general news analysis, output:

1. `What happened`;
2. `What is confirmed`;
3. `What is uncertain or disputed`;
4. `Why it matters`;
5. `Who is affected`;
6. `Practical meaning`;
7. `Confidence`;
8. `What to watch next`;
9. `Store or ignore`.

For project news analysis, add:

1. `Impact on our project`;
2. `Recommended action`.

## Digest Style

Default digest must be readable, not academic.

Preferred structure:

- short headline;
- 2-4 sentence explanation;
- clear separation of fact and interpretation;
- confidence label;
- practical consequence;
- one next-watch point.

Avoid:

- long article dumps;
- vague summaries;
- false balance when one side has stronger evidence;
- emotional framing without evidence;
- treating headlines as facts;
- burying the practical meaning.

## Storage Rules

- Store raw links and source packs as references, not active knowledge.
- Store personal or project implications in the relevant personal/project layer.
- Store watchlists separately from permanent knowledge.
- Promote to `knowledge-library/` only when the lesson is reusable beyond one event and has been reviewed.
- Never store secrets, private customer data, or unstable rumors as central knowledge.

## Risks

- news decay: old articles become misleading;
- source laundering: many outlets repeat one original weak claim;
- narrative bias: sources may frame facts selectively;
- algorithmic amplification: noisy topics may look more important than they are;
- hallucinated certainty: AI may overstate weak signals;
- context bloat: dumping news into memory can poison future work;
- legal, financial, medical, immigration, political, and safety sensitivity: use extra source discipline.

## Related Nodes

- `docs/RESEARCH_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`

## Optional Future Split-Outs

These are optional. They are not required for this block to be useful:

- `news-digest-builder`: creates concise digest outputs from current sources;
- `source-pack-builder`: exports clean URL lists for NotebookLM;
- `news-impact-analyzer`: turns news into risk, opportunity, consequence, and action;
- `watchlist-maintainer`: maintains monitored topics, sources, actors, and trigger conditions;
- `timeline-builder`: reconstructs event chronology.

## Review Checklist

Before activation, check:

- no duplicate block or standard already covers this;
- source quality rules are compatible with `RESEARCH_STANDARD.md`;
- storage rules are compatible with `KNOWLEDGE_SYSTEM.md`;
- outputs are readable enough for non-technical use;
- the block is not limited to skills or software projects;
- optional split-outs are not prematurely registered as active;
- the block does not create a giant uncontrolled news memory dump.

## Boundary

This block does not automatically run monitoring.

This block defines how news collection and analysis should be structured when requested or when an approved automation/agent invokes it.

## Final Rule

News becomes useful only when it improves understanding, changes a decision, updates a risk, reveals an opportunity, or creates a reliable source trail.

Do not collect news for noise.
