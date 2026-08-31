# Indexing Layer Standard

## Purpose

This standard defines the structural indexing layer for `Project Execution OS`.

Its goal is to keep navigation current, make repository knowledge machine-readable, prepare a semantic-search corpus, prevent agents from repeatedly scanning the entire repository, and expose structural hygiene problems before they silently accumulate.

## Core Rule

Use layered indexing:

```text
stable door
  -> live router
  -> curated section indexes
  -> generated machine index
  -> semantic-ready chunk corpus
  -> system hygiene audit
  -> hygiene trend / persistence telemetry
  -> optional embeddings runtime
  -> optional graph-memory layer
```

No generated index, hygiene report, trend, or usage signal replaces canonical source files.

## Required Artifacts

### Curated navigation

- `START_HERE.md`
- `docs/ROUTER.md`
- `PROJECT_INDEX.md`
- `blocks/PROJECT_INDEX.md`
- `knowledge-library/PROJECT_INDEX.md`
- `skills/PROJECT_INDEX.md`
- `agent-library/PROJECT_INDEX.md`

### Generated indexing artifacts

- `indexes/system-index.json`
- `indexes/semantic-documents.jsonl`
- `indexes/BLOCK_CATALOG.generated.md`
- `indexes/KNOWLEDGE_CATALOG.generated.md`

### Hygiene evidence

- `logs/hygiene-history.jsonl` when scheduled history has begun accumulating
- GitHub Actions job summary for each integrity run

### Automation

- `scripts/build_system_index.py`
- `scripts/audit_system_hygiene.py`
- `.github/workflows/system-index.yml`
- `.github/workflows/validate-project-structure.yml`

## Structural Indexing Rule

After a meaningful structural change:

1. update the relevant curated index when human-readable navigation changed;
2. regenerate machine-readable artifacts;
3. verify that new blocks contain `BLOCK.md`;
4. verify that paths remain valid;
5. verify statuses and dated snapshots where applicable;
6. run or rely on the system hygiene audit;
7. preserve canonical files as the source of truth.

## Generated Index Scope

The generated index may include:

- path;
- title;
- artifact type;
- domain;
- lifecycle status when detected;
- updated or captured date when detected;
- content hash;
- related repository paths;
- source URLs;
- headings;
- search text;
- chunk identifiers for semantic ingestion.

Do not place secrets, tokens, personal data, or confidential case material in generated public indexes.

## System Hygiene Audit Rule

System hygiene is the maintenance counterpart to knowledge accumulation.

The system must be able to detect when its growing body of standards, blocks, skills, projects and knowledge starts becoming difficult to navigate, duplicated, stale, orphaned or misleading.

Use `scripts/audit_system_hygiene.py` as the lightweight automated audit.

The audit must distinguish **hard structural contradictions** from **review signals**.

Hard failures may include:

- a required canonical navigation artifact is missing;
- an internal project entrypoint exists but is not registered in the project router;
- a domain `BLOCK.md` entrypoint cannot be discovered from the curated block index or live router.

Review signals may include:

- candidate artifacts that have remained unreviewed for a long period;
- skills that exist but are not visible in the curated skill index;
- exact or near-obvious duplicate canonical Markdown artifacts;
- top-level standards that appear to have no inbound references;
- a long gap in the curated changelog.

A review signal is not permission to delete, merge, promote or deprecate automatically.

The executor must inspect the artifact and preserve rare but valuable knowledge when it still has a legitimate route or use.

## Hygiene Trend Rule

A one-time clean snapshot is not enough to prove system health.

Scheduled hygiene runs should preserve a compact trend record in `logs/hygiene-history.jsonl` containing the current metrics, warning identifiers, persistence state, and per-block activity signals.

Use trends to answer questions such as:

- are undated candidates shrinking or growing;
- are warnings resolving or persisting;
- are candidate counts growing faster than review capacity;
- which blocks show ongoing maintenance activity;
- which signals repeatedly survive multiple scheduled reviews.

Do not treat the history file as a second source of truth. It is evidence about system maintenance behavior.

## Persistent Warning Rule

Each repeatable warning class should have a stable warning identifier.

When the same warning identifier appears in consecutive recorded hygiene runs, increment its persistence count.

Default interpretation:

```text
1-2 consecutive runs -> warning
3+ consecutive runs -> ACTION_REQUIRED review signal
```

`ACTION_REQUIRED` does **not** automatically become a hard CI failure.

Escalate a warning class into a blocking error only when a separate explicit rule establishes that continuing with the condition is unsafe or structurally invalid.

This prevents a green CI badge from hiding long-lived hygiene debt without allowing harmless review signals to stop normal execution.

## GitHub Actions Visibility Rule

The hygiene audit should write a readable GitHub Actions job summary when running inside GitHub Actions.

The summary should expose at least:

- error count;
- warning count;
- persistent/action-required warning count;
- candidate count;
- undated candidate count;
- current block/project counts;
- warning IDs and consecutive-run counts when warnings exist;
- a compact low-activity block view.

Important hygiene signals must not exist only in stdout that requires opening raw job logs.

## Git History Completeness Rule

Never interpret Git-history-derived hygiene telemetry from a shallow repository as complete repository activity evidence.

Before relying on `last_touched`, commit counts, change frequency, age-by-history, or similar metrics, check whether the repository has complete history with:

```text
git rev-parse --is-shallow-repository
```

If the result is `true`:

- structural checks that depend only on the current tree may still be valid;
- Git-history-derived activity metrics must be explicitly marked incomplete or unreliable;
- do not compare shallow-derived activity numbers against full-history baselines as if they were equivalent;
- fetch full history or use a full clone before making maintenance, lifecycle, deprecation, or prioritization decisions from activity telemetry.

The system hygiene auditor must surface shallow-history state rather than silently emitting plausible-looking activity numbers.

This rule applies to CI, local human runs, Codex/agent checkouts, temporary worktrees, external reviewers, and any future repository analytics that use Git history as evidence.

## Block Activity Signal Rule

For each domain block, hygiene may record lightweight Git-derived activity signals such as:

- date of the most recent commit touching the block;
- commit count touching the block over the last 30 days;
- commit count touching the block over the last 90 days.

These are **maintenance/activity signals**, not proof of user value or real-world usage.

Low activity alone must never auto-delete, auto-deprecate, or auto-demote a block. A rarely changed mature block may be more useful than a frequently edited unstable block.

Use activity signals to select review targets and ask better questions, not to make autonomous lifecycle decisions.

## Candidate Hygiene Rule

`candidate` is a lifecycle state, not permanent storage.

Candidates should periodically be reviewed for one of these outcomes:

```text
keep candidate
-> promote / activate when evidence supports it
-> merge into an existing canonical artifact
-> deprecate / replace when superseded
-> archive or remove only when safe and evidence shows no continuing value
```

Age alone does not decide the outcome. A rarely used candidate may still be valuable; a young candidate may already be obsolete.

## Changelog Boundary

`CHANGELOG.md` is a curated milestone log for significant system-level changes.

It is not the authoritative per-commit history and must not duplicate Git history or `logs/latest.md`.

Use it to record major architectural, governance, routing, enforcement and system-capability milestones that materially change how PEOS operates.

A stale changelog is a hygiene review signal when major system changes have occurred without a corresponding milestone entry; ordinary implementation commits do not require changelog entries.

## Anti-Bloat Rule

The purpose of hygiene is to reduce ambiguity and maintenance cost, not to create more documentation ceremony.

Do not create a new hygiene document for every warning.

Prefer this order:

```text
repair an existing canonical artifact
-> update an existing router/index
-> merge or deprecate duplicate knowledge when verified
-> create a new artifact only when responsibility is genuinely distinct
```

Do not auto-delete knowledge merely because it has low usage, old dates, few references or candidate status.

## Semantic-Ready Corpus

`indexes/semantic-documents.jsonl` is a preparation layer for future semantic search.

Each record should contain:

- stable chunk ID;
- source path;
- heading path;
- artifact type;
- domain;
- lifecycle status where available;
- text;
- content hash.

The corpus is not an embeddings database by itself.

## Semantic Search Boundary

Embeddings search is optional and requires an approved runtime and storage layer.

Before enabling embeddings:

1. choose the storage system;
2. define access boundaries;
3. exclude confidential data;
4. define refresh behavior;
5. define stale-index handling;
6. define retrieval limits;
7. validate that retrieved chunks improve context quality and cost.

## Graphify Boundary

Graphify remains an optional graph-memory layer under `docs/GRAPHIFY_STANDARD.md`.

Use it only for broad repositories or document corpora where cross-file navigation benefit justifies maintenance cost.

## Context Assembly Rule

Use generated indexes to locate the smallest sufficient context package.

Do not load the entire repository, the entire knowledge library, or the entire semantic corpus into routine work.

## Freshness Rule

Generated artifacts must record the repository commit they reflect when practical.

If an index is stale:

- report that limitation;
- verify important conclusions against canonical source files;
- refresh the index before relying on broad navigation.

## Final Rule

Index for navigation and selective loading, audit for structural hygiene, and trend only what helps reveal maintenance direction. Never treat an index, audit signal, activity metric, or trend as a substitute for the underlying source of truth or reviewed lifecycle judgment.