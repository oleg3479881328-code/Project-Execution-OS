# Project Execution OS

Layer-aware operating system for starting, managing, executing, reviewing and preserving project work without forcing every idea into the same storage model.

This repository contains the reusable rules, standards, skills, templates and knowledge for the system itself.

## Start Here

Use the single top-level entrypoint:

`START_HERE.md`

That entrypoint is navigation only. It routes into the relevant internal system node rather than carrying operational logic itself.

For a possible new initiative, it routes to:

`Start New Project.md`

## Core Operating Model

Projects use only the layers they actually need:

| Layer | Role |
| --- | --- |
| Chat | discussion, analysis, decisions and commands |
| Local Git | minimal version-control bootstrap for a real project folder |
| GitHub | versioned execution, code, durable technical artifacts and Codex work when required |
| Notion | readable memory, status, project catalogue and coordination when durable context is needed |
| Google Drive | optional heavy files and source assets when required |

Read the internal lifecycle node for the full rule:

`docs/PROJECT_LIFECYCLE_MODEL.md`

Key principle:

- not every thought becomes a project;
- not every project needs GitHub;
- not every project needs Notion;
- not every project needs Google Drive;
- every persistent project must state which layer stores which kind of truth.

## System Repository Role

For **Project Execution OS itself**, this GitHub repository is the committed source of truth for its standards and reusable artifacts.

This rule does not mean that GitHub is mandatory for every project managed by the system.

## Coordination And Execution

Default private AI coordination hub:

`oleg3479881328-code/AI-Coordination-Hub`

Default external idea intake library:

`oleg3479881328-code/Reference-Idea-Library`

Use the `ChatGPT <-> Codex <-> GitHub` collaboration protocol only when bounded execution work must be handed to Codex through a durable reviewable surface.

Working division:

- ChatGPT handles research, comparison, classification, architecture reasoning and decision preparation when it has adequate access;
- Codex handles bounded technical execution after the decision is clear: scripts, bulk updates, file changes, commits, pull requests, verification and logs.

## Current Mode

Document-first foundation.

No backend.
No frontend.
No runtime engine.
No orchestration engine.
No vector database.
No broad automation layer.
No mass agent creation.

## Main Internal Nodes

- `START_HERE.md` — system front door and router only
- `Start New Project.md` — new-initiative router only
- `docs/PROJECT_LIFECYCLE_MODEL.md` — layer and source-of-truth decisions
- `docs/MODE_CLASSIFIER.md` — choose the lightest correct mode
- `docs/PROJECT_ENTRYPOINT_STANDARD.md` — standard for a specific project's front door, using `PROJECT.md` for repository and file-executed projects
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md` — keep useful ideas without creating projects prematurely
- `docs/WORKFLOW_CONTRACT.md` — workflow rules when work actually needs them
- `docs/MICRO_TASK_MODE.md` — bounded small tasks
- `docs/RESEARCH_STANDARD.md` — research work
- `docs/REVIEW_STANDARD.md` — review work
- `docs/CODEX_HANDOFF_STANDARD.md` — approved execution transfer
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` — continuity and durable state maintenance
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md` — GitHub-based ChatGPT/Codex coordination
- `docs/integrations/notion/README.md` — Notion integration guidance
- `docs/KNOWLEDGE_SYSTEM.md` — reusable knowledge layer
- `knowledge-library/README.md` — central knowledge library
- `skills/PROJECT_INDEX.md` — reusable skills
- `agent-library/PROJECT_INDEX.md` — reusable agents
- `CHANGELOG.md` — accepted repository changes
- `logs/WORKFLOW_LOG.md` — workflow log

## Guiding Rule

Start at the front door.
Route to the smallest necessary internal node.
Expand only when real work proves that another layer or standard is needed.
