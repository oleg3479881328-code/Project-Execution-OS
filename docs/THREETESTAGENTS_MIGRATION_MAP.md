# 3TestAgents Migration Map

## Purpose

This document defines how ideas, standards, and reusable artifacts from `3TestAgents` should be migrated into `Project-Execution-OS`.

The goal is not to copy repository history blindly.

The goal is to preserve the best validated ideas from the experimental repository and adopt them into the canonical central system.

## Canonical Role Decision

`Project-Execution-OS` is the canonical central system.

It is the:

- central brain;
- central governance layer;
- central knowledge library;
- central skill registry;
- central workflow standard;
- central entrypoint for project-oriented AI work.

`3TestAgents` is the historical experimental incubator.

It may be archived or deleted after migration is completed and the adopted artifacts are committed into `Project-Execution-OS`.

## Migration Principle

Migrate:

- stable standards;
- durable governance;
- reusable skills;
- reusable knowledge patterns;
- entrypoint and memory conventions that improve continuity.

Do not migrate blindly:

- stale status claims;
- duplicate workflow history;
- ChatGPT-only framing;
- temporary MVP boundaries that no longer fit the central system;
- contradictory or outdated next-step artifacts.

## Repository Role Split

### 3TestAgents

Role:
- experimental sandbox;
- early skill/governance prototype;
- source of ideas to curate.

### Project-Execution-OS

Role:
- canonical operating system;
- central source of truth for cross-project workflow;
- central home for reusable skills and knowledge;
- central onboarding system for humans and AI agents.

## Migration Actions

| Source in `3TestAgents` | Target in `Project-Execution-OS` | Action | Notes |
|---|---|---|---|
| `docs/MIGRATION_SNAPSHOT.md` | new central memory-entry standard document | adapt | Keep the idea of a fast restart artifact, but generalize beyond the old repo phase. |
| `docs/REPO_MEMORY_STANDARD.md` | `docs/` central repository-memory standard | adapt | Strong candidate for adoption because it defines agent read order and memory layers clearly. |
| `docs/SKILL_SPEC.md` | `docs/` skill standard | adapt | Keep only the tool-neutral stable parts. |
| `docs/LIFECYCLE.md` | `docs/` skill lifecycle standard | adapt | Useful for candidate/reviewed/active progression. |
| `docs/REVIEW_PROCESS.md` | `docs/` review standard | adapt | Move only the reusable review process. |
| `docs/COMPATIBILITY_MODEL.md` | `docs/` compatibility/adapters standard | adapt | Strong fit for central tool-neutral architecture. |
| `skills/registry.md` | central `skills/registry.md` or equivalent | merge | Needed if `Project-Execution-OS` becomes the central skill hub. |
| `skills/PROJECT_INDEX.md` | central `skills/PROJECT_INDEX.md` or equivalent | merge | Keep as navigation index for the central skill layer. |
| `skills/research/github-repository-research/` | central `skills/` candidate skill set | adapt | Keep as candidate until re-reviewed under the new system. |
| `skills/review/multi-agent-design-review/` | central `skills/review/` | adapt | Migrate only if the role still fits the universal workflow. |
| `skills/review/codex-execution-review/` | central `skills/review/` | adapt | Strong candidate for central execution-quality review. |
| `skills/orchestration/workflow-state-machine/` | central `skills/orchestration/` or governance docs | adapt | Keep the state logic minimal; do not turn the OS into a BPM engine. |
| `skills/orchestration/skill-runtime-router/` | central `skills/orchestration/` | review-first | Migrate only if it remains tool-neutral and does not imply premature runtime. |
| `skills/design/pre-architecture-brainstorming/` | central `skills/design/` | adapt | Fits the workflow if kept lightweight. |
| `skills/memory/repository-memory-update/` | central `skills/memory/` | adapt | Strong fit with central memory discipline. |
| `skills/implementation/implementation-handoff-packet/` | central `skills/implementation/` | adapt | Fits execution handoff use cases. |
| `knowledge-library/patterns/document-first-mvp.md` | `knowledge-library/patterns/` | merge | Strong reusable pattern. |
| `knowledge-library/patterns/tool-neutral-core.md` | `knowledge-library/patterns/` | merge | Strong reusable pattern. |
| `knowledge-library/patterns/state-separation-in-ai-systems.md` | `knowledge-library/patterns/` | merge | Strong reusable pattern. |
| `workflow-runs/001-first-run-template.md` | none | archive | Historical artifact, not central state. |
| `workflow-runs/002-ai-skill-system-run.md` | optional migration reference under `docs/` | reference-only | Useful as provenance, not as active operating artifact. |
| `workflow-runs/003-workflow-artifact-standard-validation/` | optional migration reference under `docs/` | reference-only | Keep only if needed as validation evidence. |
| `logs/WORKFLOW_LOG.md` | `logs/WORKFLOW_LOG.md` | selective extract | Copy lessons and decisions, not the full old log. |
| `README.md` | none | do not copy | The old README is superseded by the central OS README. |
| `PROJECT_INDEX.md` | none | do not copy | The old repo index describes the incubator, not the canonical system. |

## Adoption Labels

Use these labels during migration:

- `adopted` = transferred with minimal change and accepted as central standard
- `adapted` = transferred but rewritten for the central system
- `candidate` = promising but still requires review
- `reference_only` = kept only as historical evidence
- `archived` = intentionally not active
- `dropped` = intentionally not migrated

## Recommended Migration Order

1. Adopt memory and governance standards.
2. Adopt skill lifecycle, review, and compatibility standards.
3. Create the central skill registry and central skill index.
4. Migrate reusable knowledge patterns.
5. Re-review each migrated skill under `Project-Execution-OS`.
6. Mark `3TestAgents` as archived only after the central repo contains the adopted artifacts.

## What Must Exist Before Deleting 3TestAgents

Before deleting `3TestAgents`, confirm that `Project-Execution-OS` contains:

- a central repository-memory standard;
- a central skill registry;
- a central skill index;
- adopted or adapted lifecycle and review standards;
- migrated reusable knowledge patterns;
- explicit status for each migrated skill;
- a migration log entry proving what was adopted and what was dropped.

## Deletion Rule

`3TestAgents` should be deleted only after:

1. all desired reusable artifacts are migrated or intentionally dropped;
2. the adopted artifacts are committed in `Project-Execution-OS`;
3. the migration status is documented in repository artifacts;
4. no active workflow depends on the old repository.
