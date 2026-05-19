# START HERE — Project Execution OS

## 1. Purpose

This file is the universal entrypoint for every human, AI assistant, AI agent, coding agent, research agent, automation agent, or future runtime system that enters this repository.

If you are pointed to this repository, start here.

Repository:

`oleg3479881328-code/Project-Execution-OS`

System:

`Project Execution OS`

## 2. What This System Is

Project Execution OS is a repository-first operating system for running projects through a repeatable workflow.

It is designed so that project work does not disappear inside temporary chats.

Instead:

- projects become repository folders;
- decisions become artifacts;
- agents become task-specific modules;
- central reusable skills live in the central system;
- reviews become governance;
- knowledge becomes reusable library entries;
- central knowledge accumulates across projects.

## 3. Who Can Use This

This system must be understandable by:

- a human user;
- ChatGPT;
- Codex;
- Claude;
- local AI models;
- research agents;
- coding agents;
- review agents;
- future orchestration systems.

## 4. Core Rule

Do not start with code.
Do not start with runtime.
Do not start with automation.
Do not create agents before the task requires them.
Do not create architecture before the project has an input and first workflow run.

Start by identifying whether you are:

1. starting a new project;
2. continuing an existing project;
3. reviewing a project;
4. extracting reusable knowledge;
5. brainstorming without creating a project yet;
6. normalizing an older project into the current standard;
7. updating the operating system itself.

## 5. If Starting A New Project

Default rule:

Create a dedicated private GitHub repository for the new project.

Use an internal folder inside `Project Execution OS` only as an explicit exception for compact or temporary work.

New repositories should be private by default unless the user explicitly chooses public visibility.

If using an internal folder, create:

`projects/<project-id>/`

Inside it, create:

```text
PROJECT_ENTRYPOINT.md
PROJECT_STATE.md
PROJECT_RULES.md
agents/
project-library/
workflow-runs/
logs/
```

Then create the first workflow run:

`projects/<project-id>/workflow-runs/0001-initial-definition/`

Use the template:

`workflow-templates/universal-project-v1/`

Start with:

`00_INPUT.md`

If the project is small, low-risk, or intentionally compact, use compact mode with fewer files but the same core rules:

- repository artifacts are the source of truth;
- research is evidence-backed;
- review happens before stable acceptance;
- reusable knowledge is extracted when it appears;
- the next action is logged explicitly.

If the repository is broad enough that future navigation or architecture understanding will matter, build Graphify and use `graphify-out/GRAPH_REPORT.md` as a graph-memory layer for later sessions.

## 6. If Continuing An Existing Project

Read in this order:

1. `projects/<project-id>/PROJECT_ENTRYPOINT.md`
2. `projects/<project-id>/PROJECT_STATE.md`
3. `projects/<project-id>/PROJECT_RULES.md`
4. latest file in `projects/<project-id>/logs/`
5. latest workflow run in `projects/<project-id>/workflow-runs/`
6. relevant entries in `projects/<project-id>/project-library/`
7. relevant entries in root `knowledge-library/`

If central reusable skills are relevant to the task, also read:

8. `skills/PROJECT_INDEX.md`
9. `skills/registry.md`

If the work will move from a reasoning model to Codex through GitHub, also read:

10. `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
11. `skills/coordination/chatgpt-codex-github-communication/SKILL.md`

In that mode, treat `GitHub main` as the source of truth and the local Codex folder as an execution workspace only.

## 7. Universal Project Workflow

Every meaningful project run follows this chain:

```text
00_INPUT.md
01_CLARIFICATION.md
02_RESEARCH.md
03_PLAN.md
04_AGENT_DESIGN.md
05_EXECUTION_SPEC.md
06_REVIEW.md
07_RESULT.md
08_KNOWLEDGE_EXTRACT.md
09_LOG.md
```

## 8. Agent Creation Rule

Agents are created under the project only when a workflow stage requires a specialized role.

Agents are not the root system.
Agents are replaceable execution modules.
The workflow is the stable system.

Every project agent must define:

- purpose;
- when to use;
- inputs;
- outputs;
- constraints;
- evidence rules;
- failure modes;
- review requirements.

## 9. Knowledge Rule

Each project has a local project library:

`projects/<project-id>/project-library/`

The root repository has a central knowledge library:

`knowledge-library/`

The root repository also has a central reusable skill layer:

`skills/`

The wider external skill universe is inventoried in:

`docs/SKILL_UNIVERSE_INVENTORY.md`

Local project knowledge stays inside the project first.

Reusable knowledge may be promoted into the central knowledge library only after review.

Reusable skills may be promoted into the central skill layer only after review.

For the canonical GitHub-based collaboration loop between reasoning models and Codex, read:

`docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

## 10. State Separation

Always distinguish:

- generated state: proposed but not committed;
- committed state: written to the repository;
- reviewed state: checked by review;
- active state: approved for reuse.

Do not claim that something is saved, applied, executed, reviewed, active, or complete unless there is evidence.

## 11. Default Next Action

If the user says they want to start a new project, create the project folder structure and begin `00_INPUT.md`.

If the user only gives a project idea, preserve it in `00_INPUT.md` and ask only the minimum clarification needed for the first useful run.

## 12. Current Foundation Boundary

Current phase:

`document-first foundation`

Forbidden until the workflow is proven:

- backend;
- frontend;
- runtime engine;
- orchestration engine;
- vector database;
- semantic search;
- marketplace;
- mass agent creation;
- autonomous execution layer.
