# Decision 009 — Incremental Agent Re-entry

## Date

`2026-05-30`

## Decision

Adopt incremental re-entry — инкрементальный повторный вход — as the default MVP pattern for agent continuation in GitHub-backed projects where rereading the whole repository is unnecessary.

## Core Rule

Use:

```text
PROJECT_ENTRYPOINT.md
→ agent checkpoint
→ last_seen_commit..HEAD
→ PROJECT_CHANGE_INDEX.md
→ changed files and directly related files only
→ continue work
→ update checkpoint
```

## Reason

The repository already has adjacent mechanisms that should be reused instead of replaced:

- `PROJECT_ENTRYPOINT.md` for entry;
- `CONTEXT_PACK.md` for optional fast briefing;
- Git commits for technical truth;
- repository-memory and context-assembly standards for bounded loading.

The missing piece was a light central rule for delta-based re-entry between agents.

## Boundary

Do not build:

- backend;
- runtime engine;
- vector database;
- semantic index;
- embeddings;
- dashboard;
- heavy automation.

This is a document-first MVP — документный MVP.

## Status

`accepted — bounded MVP standard added`

## Implementation Evidence

- `docs/INCREMENTAL_REENTRY_STANDARD.md`
- `workflow-templates/incremental-reentry/`

## Final Rule

Use Git for technical evidence and lightweight project files for re-entry speed.
