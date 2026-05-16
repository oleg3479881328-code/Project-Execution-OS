# Project Index — Project Execution OS

## Repository

`oleg3479881328-code/Project-Execution-OS`

## System Name

Project Execution OS

## Purpose

Create a universal repository-first operating system for starting, running, reviewing, and preserving projects.

The system must support humans, ChatGPT, Codex, Claude, local models, specialized agents, and future automation systems through one entrypoint and one stable project workflow.

## Primary Entrypoint

`START_HERE.md`

Every user, assistant, agent, or automation session must start there.

## Current Phase

Foundation phase.

Mode:

`document-first`

Status:

`foundation_candidate`

## Core System Model

```text
Project Execution OS
  ├── Universal Entrypoint
  ├── Project Workspace Standard
  ├── Universal Workflow Contract
  ├── Agent Creation Standard
  ├── Knowledge System
  ├── Governance Layer
  ├── Review Layer
  ├── Logging Layer
  ├── Central Knowledge Library
  └── Project Libraries
```

## Canonical Documents

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/GOVERNANCE.md`
- `docs/AGENT_CREATION_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `workflow-templates/universal-project-v1/README.md`
- `knowledge-library/README.md`
- `logs/WORKFLOW_LOG.md`

## Universal Workflow Chain

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

## Project Folder Standard

Every project must live under:

`projects/<project-id>/`

Each project must contain:

```text
PROJECT_ENTRYPOINT.md
PROJECT_STATE.md
PROJECT_RULES.md
agents/
project-library/
workflow-runs/
logs/
```

## Knowledge Architecture

Local project knowledge:

`projects/<project-id>/project-library/`

Central reusable knowledge:

`knowledge-library/`

Promotion rule:

Project knowledge becomes central knowledge only after review.

## Agent Architecture

Agents are created per project when needed.

Agents are task-specific modules, not the root system.

Required agent artifact:

`projects/<project-id>/agents/<agent-name>/AGENT.md`

## Current Forbidden Priorities

Do not build yet:

- backend;
- frontend;
- runtime engine;
- orchestration engine;
- vector database;
- semantic search;
- automation framework;
- marketplace;
- mass agent creation;
- autonomous execution layer.

## Current Status

Foundation initialized as committed repository artifacts.

Committed artifacts:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/GOVERNANCE.md`
- `docs/AGENT_CREATION_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `workflow-templates/universal-project-v1/`
- `knowledge-library/README.md`
- `logs/WORKFLOW_LOG.md`

## Next Required Action

Create the first real project using this OS:

`projects/0001-project-execution-os-foundation-review/`

Purpose:

Run Project Execution OS on itself and review the foundation through the universal workflow.
