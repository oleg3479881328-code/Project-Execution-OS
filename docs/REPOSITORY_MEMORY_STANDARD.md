# Repository Memory Standard — Project Execution OS

## Purpose

This standard defines how humans, ChatGPT, Codex, Claude, local models, and future agents should use repository memory in `Project-Execution-OS`.

Goal:
Prevent lost context, duplicated work, fake state claims, and blind repository navigation.

## Core Principle

The repository is the source of truth.

Chat messages, generated plans, and internal reasoning are not executed state unless they are backed by repository artifacts, commits, explicit tool output, or user-confirmed execution.

## Central Memory Layers

### 1. `START_HERE.md`

Purpose:
- universal entrypoint;
- first orientation for any human or AI agent;
- role clarification for this repository.

### 2. `PROJECT_INDEX.md`

Purpose:
- current central system map;
- canonical document list;
- current phase and next action.

### 3. `logs/WORKFLOW_LOG.md`

Purpose:
- executed history;
- major decisions;
- migration events;
- repository milestones;
- lessons and risks.

### 4. `docs/THREETESTAGENTS_MIGRATION_MAP.md`

Purpose:
- migration control artifact;
- source-to-target transfer plan;
- adoption status guidance for imported standards and skills.

### 5. `skills/registry.md`

Purpose:
- skill lifecycle memory;
- review state;
- status tracking;
- compatibility tracking.

### 6. `skills/PROJECT_INDEX.md`

Purpose:
- human navigation for the central skill layer;
- category map;
- migration priorities;
- growth boundaries.

### 7. `knowledge-library/`

Purpose:
- reusable cross-project knowledge;
- patterns;
- anti-patterns;
- architecture and workflow lessons.

### 8. `graphify-out/` when present

Purpose:
- graph-memory layer;
- repository cognition bootstrap;
- broad navigation aid for large repositories.

### 9. `projects/<project-id>/...`

Purpose:
- local project memory;
- project-specific state;
- local workflow history;
- project-only agents and project-only knowledge.

### 10. `projects/<project-id>/CONTEXT_PACK.md` when present

Purpose:
- fast re-entry brief;
- short handoff pack between sessions or agents;
- cache-like memory summary for projects with repeated continuation.

This file is optional.

It must not override canonical project artifacts.

## Required Read Order

### When entering the central system

Read in this order:

1. `START_HERE.md`
2. `PROJECT_INDEX.md`
3. `docs/GOVERNANCE.md`
4. `docs/WORKFLOW_CONTRACT.md`
5. `docs/KNOWLEDGE_SYSTEM.md`
6. `docs/REPOSITORY_MEMORY_STANDARD.md`
7. `skills/PROJECT_INDEX.md` when skills are relevant
8. `skills/registry.md` when skill status matters
9. `graphify-out/GRAPH_REPORT.md` when Graphify exists and broad navigation is needed
10. `logs/WORKFLOW_LOG.md`

If Graphify is justified by scope and `graphify-out/GRAPH_REPORT.md` is missing while supported files exist, the agent should build Graphify before broad exploration instead of pretending the graph layer exists.

### When continuing a specific project

After the central documents above, read:

1. `projects/<project-id>/PROJECT_ENTRYPOINT.md`
2. `projects/<project-id>/PROJECT_STATE.md`
3. `projects/<project-id>/PROJECT_RULES.md`
4. latest project log
5. latest workflow run
6. relevant project-library entries
7. relevant central knowledge-library entries

## Memory Responsibilities

### Central repository memory

Must store:
- central workflow rules;
- governance;
- central skill standards;
- central skill lifecycle state;
- cross-project reusable knowledge;
- migration decisions;
- central operating constraints.

### Project-local memory

Must store:
- project scope;
- project current state;
- project workflow outputs;
- project-specific decisions;
- local project knowledge;
- project execution history.

Do not collapse these layers into one.

## Update Rules

After any meaningful central repository change, consider updating:

- `logs/WORKFLOW_LOG.md`
- `PROJECT_INDEX.md`
- relevant `docs/` standards
- `skills/registry.md` if skills changed
- `skills/PROJECT_INDEX.md` if skill navigation changed
- `knowledge-library/` if reusable knowledge changed

After any meaningful project-level change, update the relevant project memory artifacts first.

When `PROJECT_STATE.md` uses machine-readable frontmatter, update that header whenever the effective project status, mode, current step, or next action changes.

When `CONTEXT_PACK.md` exists, refresh it only after the underlying canonical state has already been updated.

## State Labels

Always distinguish:

- `generated` = proposed but not committed
- `committed` = written to repository
- `reviewed` = checked through a review process
- `active` = approved for reuse
- `archived` = preserved but not operational

Do not use these labels loosely.

## Conflict Resolution

If repository artifacts disagree, use this priority:

1. explicit user instruction in the current task
2. `START_HERE.md`
3. `PROJECT_INDEX.md`
4. `docs/GOVERNANCE.md`
5. `docs/WORKFLOW_CONTRACT.md`
6. `docs/REPOSITORY_MEMORY_STANDARD.md`
7. `skills/registry.md`
8. `logs/WORKFLOW_LOG.md`
9. historical workflow artifacts
10. raw chat history

If conflict remains, record a decision before expanding the system further.
