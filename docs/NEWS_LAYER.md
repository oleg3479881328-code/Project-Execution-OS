# News Layer

## Purpose

The News Layer is the system node for turning current events into digestible understanding.

It is not a skill layer and not a project-only layer. It handles any news domain: politics, economy, law, immigration, technology, AI, wars, elections, markets, companies, platforms, local events, and other current topics.

The layer exists because raw news is noisy. The owner needs useful output, not a pile of headlines.

## Status

`candidate`

## Core Function

The News Layer converts incoming news into:

- quick briefs;
- digests;
- timelines;
- watchlists;
- source packs;
- analysis notes;
- decision memos;
- evidence trails.

## Core Rule

News must be processed before it is trusted.

Every important news item should be separated into:

1. what happened;
2. what is confirmed;
3. what is uncertain or disputed;
4. who is affected;
5. why it matters;
6. practical meaning;
7. confidence;
8. what to watch next;
9. whether to store or ignore.

## Layer Position

```text
Internet / Public Sources
        ↓
News Layer
        ↓
Processed News Outputs
        ↓
Reference Layer / Knowledge Layer / Project Layer / Personal Decisions
```

## Relation To Other Layers

### Reference Layer

Raw links, articles, videos, tweets, documents, and source packs belong here first.

They are references, not active knowledge.

### Knowledge Layer

Only stable lessons, reusable patterns, repeated signals, and reviewed conclusions can move into central knowledge.

A temporary news cycle must not become permanent system knowledge by default.

### Project Layer

If a news item affects an active project, store the implication inside that project layer.

Example: platform policy news affecting a content automation project belongs in that project context.

### Personal Decision Layer

If a news item affects the owner's life, money, legal position, immigration situation, tools, or timing, output a practical personal meaning and recommended next-watch point.

## Default Intake Flow

1. Identify the topic.
2. Identify the needed output type.
3. Search current sources.
4. Prefer official or primary sources when available.
5. Add reputable reporting for context.
6. Add specialist/community signals only as supporting or early indicators.
7. Deduplicate repeated copies of the same claim.
8. Group items by topic, actor, geography, timeline, and consequence.
9. Separate facts from claims, rumors, opinions, and analysis.
10. Produce a readable output.
11. Decide storage level.

## Source Priority

Use the strongest available sources for the domain:

1. official sources;
2. primary sources;
3. reputable reporting;
4. specialist sources;
5. community signals;
6. weak or unverified social signals.

Weak signals can be useful for early detection, but they must not be presented as confirmed facts.

## Output Types

### Quick Brief

Use when the owner asks what happened or wants a short explanation.

Required output:

- what happened;
- why it matters;
- confidence;
- what to watch next.

### Digest

Use when several items must be grouped into a readable summary.

Required output per item:

- short headline;
- 2-4 sentence explanation;
- confirmed/uncertain split when needed;
- practical meaning;
- confidence.

### Timeline

Use when sequence matters.

Required output:

- dated events;
- what changed at each step;
- unresolved questions;
- current state.

### Watchlist

Use when the topic must be monitored.

Required output:

- topic;
- key actors;
- keywords;
- reliable sources;
- trigger events;
- reason to watch.

### Source Pack

Use when the owner wants links for NotebookLM or deeper research.

Required output:

- clean URLs only when requested;
- no descriptions if the owner asks for NotebookLM export format.

### Decision Memo

Use when news affects an action.

Required output:

- decision context;
- relevant facts;
- uncertainty;
- options;
- recommended action;
- risk if wrong.

## Digestibility Rules

Readable output is the default.

Prefer:

- grouped summaries;
- plain language;
- short sections;
- clear labels;
- practical consequences;
- explicit uncertainty.

Avoid:

- headline dumps;
- long unstructured source lists;
- fake certainty;
- emotional framing without evidence;
- overloading the owner with irrelevant details;
- turning every news item into permanent knowledge.

## Storage Model

```text
Raw News
    ↓
Processed News
    ↓
Reusable Knowledge / Project Implication / Personal Decision / Ignore
```

### Raw News

Contains source material only:

- links;
- articles;
- screenshots;
- videos;
- transcripts;
- official documents.

### Processed News

Contains cleaned outputs:

- digests;
- timelines;
- watchlists;
- summaries;
- source packs;
- issue maps.

### Reusable Knowledge

Contains only reviewed durable lessons:

- repeated pattern;
- stable rule change;
- reusable workflow insight;
- durable risk;
- durable opportunity.

## Confidence Labels

Use simple labels:

- `high`: strong official/primary evidence or multiple independent reputable confirmations;
- `medium`: credible reporting but limited confirmation or incomplete details;
- `low`: early signal, community report, leak, rumor, or weak corroboration.

## Special Domains

For law, immigration, finance, medicine, elections, safety, war, and politics:

- use current sources;
- prefer official/primary sources;
- separate facts from interpretation;
- avoid overconfident conclusions;
- show what remains uncertain;
- give practical next-watch points instead of pretending certainty.

## Relation To News Intelligence Block

`blocks/news-intelligence/BLOCK.md` contains the reusable operating block for this layer.

This document defines the system-level layer. The block defines the reusable workflow inside the layer.

## Activation Boundary

This document is a candidate system node until reviewed.

Do not treat it as fully active central law until it is reviewed and promoted according to the Knowledge System lifecycle.

## Final Rule

The News Layer exists to make current events understandable and usable.

The correct output is not more news. The correct output is clearer meaning, cleaner sources, lower noise, and better decisions.
