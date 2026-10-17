# Repository Memory Standard — Project Execution OS

## Purpose

This standard defines repository memory (память репозитория) for:

1. the `Project-Execution-OS` repository itself; and
2. any project that has an active GitHub layer because it contains versioned execution, code, technical artifacts, documentation, or Codex implementation work.

It does **not** require every project in the wider system to have a repository.

Lifecycle and layer decisions are defined in `docs/PROJECT_LIFECYCLE_MODEL.md`.

## Goal

Prevent lost technical context, duplicated work, fake execution claims, and blind repository navigation where GitHub is actually part of the project.

## Scope Boundary

Apply this standard when:

- working on `Project Execution OS` itself;
- a project has a GitHub repository as an active layer;
- Codex changes files, runs implementation work, creates commits or pull requests;
- versioned technical evidence must be preserved.

Do not apply this standard as a reason to create GitHub for:

- a discussion that lives only in Chat;
- an idea preserved only in Notion;
- a non-technical project whose durable management layer is Notion;
- heavy source files stored only in Google Drive.

For projects without a GitHub layer, persistent project truth belongs in the verified canonical Google Drive project records. Notion can provide optional coordination views, linked to that truth.

## Core Principle

By owner decision of 2026-10-17, Google Drive is the central Project Execution OS storage and project-knowledge layer. This GitHub repository remains the committed source of truth for its currently repository-resident standards, templates, skills and technical artifacts until each is deliberately promoted to a verified canonical Drive record. This protects continuity while migrating and does not designate GitHub as the central project store.

For another GitHub-backed project, its repository is the committed source of truth only for the technical/versioned material assigned to its GitHub layer.

A repository does not override verified canonical Google Drive project status, decisions or management records. Notion coordination is optional and must not create competing truth.

Chat messages, generated plans and internal reasoning are not executed technical state unless supported by appropriate evidence: repository artifacts, commits, explicit tool output or user-confirmed execution.

## Central Repository Memory Layers

These layers describe this `Project-Execution-OS` repository, not every project in the system.

### 1. `START_HERE.md`

Purpose:
- stable top-level door;
- first orientation for a human or AI entering this system repository.

### 2. `docs/ROUTER.md`

Purpose:
- live internal router;
- current route catalogue for internal navigation.

### 3. `PROJECT_INDEX.md`

Purpose:
- current central system map;
- canonical document list;
- current phase and next action when maintained.

### 4. `logs/WORKFLOW_LOG.md`

Purpose:
- meaningful executed history;
- major decisions;
- migration events;
- repository milestones;
- lessons and risks.

Do not log trivial activity by ritual.

### 5. `skills/registry.md` and `skills/PROJECT_INDEX.md`

Purpose:
- reusable skill lifecycle and navigation when skills are involved.

### 6. `knowledge-library/`

Purpose:
- reviewed reusable cross-project knowledge;
- patterns and anti-patterns;
- architecture and workflow lessons;
- verified technical solutions worth reuse.

### 7. `graphify-out/` when present and justified

Purpose:
- optional graph-memory layer;
- navigation aid for a large GitHub-backed repository.

Do not require graph output for small repositories or simple tasks.

### 8. `projects/<project-id>/...` when a project is intentionally stored inside this repository

Purpose:
- internal project-specific state;
- local workflow history;
- project-only technical artifacts.

This is an exception model, not the default home for all projects.

### 9. `projects/<project-id>/CONTEXT_PACK.md` when present

Purpose:
- optional fast re-entry brief;
- short handoff pack between sessions or agents.

It must not override canonical project evidence.

### 10. `PROJECT_CHANGE_INDEX.md` when present

Purpose:
- short semantic change index — короткий смысловой индекс изменений;
- faster re-entry for agents that need recent delta only.

It must not replace Git commits as technical evidence.

### 11. `agent-checkpoints/<agent-id>.md` when present

Purpose:
- short per-agent checkpoint — короткая контрольная отметка конкретного агента;
- record of the last seen commit and next expected action.

It must not become project history or project truth.

## Required Read Order

### When entering `Project-Execution-OS` itself

Start at:

1. `START_HERE.md`
2. `docs/ROUTER.md`

Then follow only the relevant route.

Do not read every standard by default. The stable door must remain minimal. The live route catalogue belongs in `docs/ROUTER.md`.

Examples:

- lifecycle or storage-layer decision -> `docs/PROJECT_LIFECYCLE_MODEL.md`
- project workflow rule needed -> `docs/WORKFLOW_CONTRACT.md`
- GitHub-backed memory question -> `docs/REPOSITORY_MEMORY_STANDARD.md`
- Codex execution handoff -> `docs/CODEX_HANDOFF_STANDARD.md`
- research work -> `docs/RESEARCH_STANDARD.md`
- central knowledge work -> `docs/KNOWLEDGE_SYSTEM.md`

### When continuing a separate GitHub-backed project

Read that project's own entrypoint and current evidence first.

A GitHub-backed project should define only the memory artifacts it actually needs, for example:

1. project entrypoint, when present;
2. current project state or decision artifact, when present;
3. `PROJECT_CHANGE_INDEX.md` and `agent-checkpoints/` when incremental re-entry is needed;
4. relevant active issue, pull request or execution report;
5. recent logs or workflow artifact only when required for continuation;
6. relevant reusable knowledge when it applies.

For incremental re-entry — инкрементальный повторный вход — use:

`docs/INCREMENTAL_REENTRY_STANDARD.md`

That standard defines how `PROJECT.md`, legacy `PROJECT_ENTRYPOINT.md` when still being migrated, Git diff, `PROJECT_CHANGE_INDEX.md`, `CONTEXT_PACK.md`, and `agent-checkpoints/` work together without replacing Git as technical truth.

Do not impose this repository's full internal structure on every GitHub-backed project.

### When continuing a project without GitHub

Do not use repository memory as the default path.

Use the canonical Google Drive project entrypoint, state and linked knowledge as defined by `docs/PROJECT_LIFECYCLE_MODEL.md`.

## Memory Responsibilities

### `Project-Execution-OS` repository memory

May store:
- central workflow and lifecycle standards;
- governance of the system itself;
- reusable skill and agent standards;
- reviewed cross-project knowledge;
- migration decisions relating to this system repository;
- technical coordination and execution rules.

### Separate GitHub-backed project memory

Store only what is needed for that project's GitHub layer:
- technical scope and versioned artifacts;
- code and technical documentation;
- implementation decisions;
- execution reports and validation evidence;
- project-local technical lessons worth keeping near the code.

### Google Drive — central project storage and memory

Google Drive is the central store for the project catalogue, entrypoints, current state, operational decisions, reviewed reusable project knowledge, documents and assets. Each record needs one verified canonical location. Do not infer authority from one of several copies or mirrors.

### Notion — optional coordination layer

When used, Notion supplies task views and collaboration, linked to canonical Google Drive project knowledge and GitHub engineering evidence. It must not silently create a second authoritative project catalogue or decision history.

## Update Rules

After a meaningful change to `Project-Execution-OS`, update only the central artifacts actually affected, such as:

- the relevant `docs/` standard;
- `PROJECT_INDEX.md` when the system map changes;
- `logs/WORKFLOW_LOG.md` when durable executed history is useful;
- `skills/registry.md` or `skills/PROJECT_INDEX.md` when skills changed;
- `knowledge-library/` when reviewed reusable knowledge was produced.

After a meaningful change to a separate GitHub-backed project, update that project's necessary technical evidence first.

When a project uses `PROJECT_CHANGE_INDEX.md` or `agent-checkpoints/`, update them only after meaningful completed work that improves future re-entry.

After a meaningful change to a project without GitHub, update its canonical Google Drive project records; update any optional Notion views only as needed, without duplicating truth.

When a context pack exists, refresh it only after the underlying canonical state has already been updated.

## State Labels

Always distinguish the state appropriate to the active layer:

- `generated` = proposed but not written into a durable layer;
- `recorded` = written into the canonical Google Drive project/system record or another specifically verified durable source;
- `committed` = written to GitHub in a commit when a GitHub layer exists;
- `reviewed` = checked through a review process;
- `active` = approved for reuse;
- `archived` = preserved but not operational.

Do not use `committed` for Notion-only work, and do not claim execution without evidence appropriate to the active layer.

## Conflict Resolution

For lifecycle or storage-layer conflicts, use:

1. explicit user instruction in the current task;
2. `START_HERE.md` as the routing entrypoint;
3. `docs/PROJECT_LIFECYCLE_MODEL.md` for layer roles and source-of-truth boundaries;
4. the specific project's own entrypoint or recorded decision;
5. the relevant layer evidence: canonical Google Drive project state/decision, GitHub commit/issue/PR for engineering, or linked Notion coordination view.

For conflicts inside `Project-Execution-OS` technical repository artifacts, use:

1. explicit user instruction in the current task;
2. `START_HERE.md`;
3. `docs/PROJECT_LIFECYCLE_MODEL.md`;
4. `docs/WORKFLOW_CONTRACT.md`;
5. the relevant specialized standard;
6. `PROJECT_INDEX.md` and logs as supporting history;
7. historical workflow artifacts;
8. raw chat history.

If conflict remains, record a decision before expanding the system further.

## Final Rule

Repository memory supports projects that actually have a GitHub engineering layer. Google Drive remains the central durable project storage and knowledge home.

This standard does not turn every thought, non-code project or file collection into a repository.
