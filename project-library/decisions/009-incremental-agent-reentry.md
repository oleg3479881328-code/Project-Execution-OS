# Decision 009 — Incremental Agent Re-entry

## Date

`2026-05-30`

## Decision

Adopt incremental re-entry as the default MVP pattern for agent continuation in GitHub-backed projects when rereading the whole repository is unnecessary.

## Core Rule

```text
PROJECT_ENTRYPOINT.md
→ agent checkpoint
→ last_seen_commit..HEAD
→ PROJECT_CHANGE_INDEX.md
→ changed and directly related files only
→ continue work
→ update checkpoint
```

## Reason

Reuse existing project entrypoints, optional context packs, Git commits, repository-memory rules, and bounded context loading. Add only a lightweight delta-based re-entry layer.

## Boundary

Do not build heavy automation, backend, runtime engine, vector database, semantic index, embeddings, or dashboard for this MVP.

## Status

`accepted — reviewed and merged into main; ready for project adoption`

## Implementation Evidence

- `docs/INCREMENTAL_REENTRY_STANDARD.md`
- `workflow-templates/incremental-reentry/`
- merge commit: `3d9aae42af66c205fa2efa2106c3bf37002e10a1`

## Final Rule

Use Git for technical evidence and lightweight project files for re-entry speed.