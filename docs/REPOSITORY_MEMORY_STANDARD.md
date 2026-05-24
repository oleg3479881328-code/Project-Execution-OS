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

For projects without a GitHub layer, persistent truth belongs to the active layer defined by the project, usually Notion and, for heavy assets, optionally Google Drive.

## Core Principle

For `Project-Execution-OS` itself, this repository is the committed source of truth for its standards, templates, skills and reusable technical artifacts.

For another GitHub-backed project, its repository is the committed source of truth only for the technical/versioned material assigned to its GitHub layer.

A repository does not override Notion for project status or management decisions unless the project's own entrypoint explicitly says so.

Chat messages, generated plans and internal reasoning are not executed technical state unless supported by appropriate evidence: repository artifacts, commits, explicit tool output or user-confirmed execution.

## Central Repository Memory Layers

These layers describe this `Project-Execution-OS` repository, not every project in the system.

### 1. `START_HERE.md`

Purpose:
- top-level router only;
- first orientation for a human or AI entering this system repository.

### 2. `PROJECT_INDEX.md`

Purpose:
- current central system map;
- canonical document list;
- current phase and next action when maintained.

### 3. `logs/WORKFLOW_LOG.md`

Purpose:
- meaningful executed history;
- major decisions;
- migration events;
- repository milestones;
- lessons and risks.

Do not log trivial activity by ritual.

### 4. `skills/registry.md` and `skills/PROJECT_INDEX.md`

Purpose:
- reusable skill lifecycle and navigation when skills are involved.

### 5. `knowledge-library/`

Purpose:
- reviewed reusable cross-project knowledge;
- patterns and anti-patterns;
- architecture and workflow lessons;
- verified technical solutions worth reuse.

### 6. `graphify-out/` when present and justified

Purpose:
- optional graph-memory layer;
- navigation aid for a large GitHub-backed repository.

Do not require graph output for small repositories or simple tasks.

### 7. `projects/<project-id>/...` when a project is intentionally stored inside this repository

Purpose:
- internal project-specific state;
- local workflow history;
- project-only technical artifacts.

This is an exception model, not the default home for all projects.

### 8. `projects/<project-id>/CONTEXT_PACK.md` when present

Purpose:
- optional fast re-entry brief;
- short handoff pack between sessions or agents.

It must not override canonical project evidence.

## Required Read Order

### When entering `Project-Execution-OS` itself

Start at:

1. `START_HERE.md`

Then follow only the route relevant to the current work.

Do not read every standard by default. The front door must remain a router, and internal documents should be opened only when their branch is active.

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
3. relevant active issue, pull request or execution report;
4. recent logs or workflow artifact only when required for continuation;
5. relevant reusable knowledge when it applies.

Do not impose this repository's full internal structure on every GitHub-backed project.

### When continuing a project without GitHub

Do not use repository memory as the default path.

Use the project's active durable layer defined by `docs/PROJECT_LIFECYCLE_MODEL.md`, normally its Notion project state and linked files/assets when present.

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

### Notion-managed project memory

For a project using Notion as its durable management layer, Notion stores:
- readable project status;
- high-level decisions;
- project catalogue entry;
- next action and coordination.

Do not force those management functions into GitHub just because a technical repository also exists.

### Google Drive asset storage

For a project using Google Drive as an optional assets layer, Google Drive stores heavy or non-versioned source files.

Do not treat Google Drive as the project brain or as the source of operational decisions.

## Update Rules

After a meaningful change to `Project-Execution-OS`, update only the central artifacts actually affected, such as:

- the relevant `docs/` standard;
- `PROJECT_INDEX.md` when the system map changes;
- `logs/WORKFLOW_LOG.md` when durable executed history is useful;
- `skills/registry.md` or `skills/PROJECT_INDEX.md` when skills changed;
- `knowledge-library/` when reviewed reusable knowledge was produced.

After a meaningful change to a separate GitHub-backed project, update that project's necessary technical evidence first.

After a meaningful change to a Notion-managed project without GitHub, update Notion rather than inventing repository artifacts.

When a context pack exists, refresh it only after the underlying canonical state has already been updated.

## State Labels

Always distinguish the state appropriate to the active layer:

- `generated` = proposed but not written into a durable layer;
- `recorded` = written into Notion or another appropriate durable management layer;
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
5. the relevant layer evidence: Notion status, GitHub commit/issue/PR, or Google Drive asset reference.

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

Repository memory is a tool for projects that actually have a GitHub layer.

It is not a requirement that turns every thought, Notion-managed project or files/assets collection into a repository.