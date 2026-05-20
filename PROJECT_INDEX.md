# Project Index — Project Execution OS

## Repository

`oleg3479881328-code/Project-Execution-OS`

## System Name

Project Execution OS

## Purpose

Create a universal repository-first operating system for starting, running, reviewing, and preserving projects.

The system must support humans, ChatGPT, Codex, Claude, local models, specialized agents, and future automation systems through one entrypoint and one stable project workflow.

For the canonical GitHub-based coordination loop between reasoning models and Codex, use:

`docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

It must also support:

- brainstorm-only work without forcing project creation;
- normalization of older repositories into the current standard.
- durable ChatGPT to Codex communication through GitHub.

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
  ├── Central Skill Layer
  ├── Central Knowledge Library
  └── Project Libraries
```

## Canonical Documents

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/GOVERNANCE.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/SKILL_SPEC.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/SKILL_REVIEW_STANDARD.md`
- `docs/COMPATIBILITY_MODEL.md`
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
- `docs/AI_COORDINATION_HUB_STANDARD.md`
- `docs/SKILL_UNIVERSE_INVENTORY.md`
- `docs/GRAPHIFY_STANDARD.md`
- `docs/DEFERRED_SYSTEM_IDEAS.md`
- `docs/AGENT_CREATION_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `skills/PROJECT_INDEX.md`
- `skills/registry.md`
- `workflow-templates/universal-project-v1/README.md`
- `knowledge-library/README.md`
- `knowledge-library/PROJECT_INDEX.md`
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

Default model:

Every project should live in its own dedicated private GitHub repository by default.

Every new repository should also have a short clear GitHub description from the start.

Internal project folders under:

`projects/<project-id>/`

are allowed as an exception for compact or intentionally internal work.

Public repositories should be treated as an explicit user choice, not the default.

Internal full-mode projects must contain:

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

Research and design work should prefer publicly verifiable external sources, including official documentation, GitHub repositories, open-source examples, and other public evidence sources appropriate to the domain.

## Agent Architecture

Agents are created per project when needed.

Agents are task-specific modules, not the root system.

Required agent artifact:

`projects/<project-id>/agents/<agent-name>/AGENT.md`

Central reusable skills live under:

`skills/<category>/<skill-name>/`

Key coordination skill:

`skills/coordination/chatgpt-codex-github-communication/SKILL.md`

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

Deferred future-system ideas that are worth preserving without building yet belong in:

`docs/DEFERRED_SYSTEM_IDEAS.md`

## Current Status

Foundation initialized as committed repository artifacts.

Committed artifacts:

- `README.md`
- `START_HERE.md`
- `PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/GOVERNANCE.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/SKILL_SPEC.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/SKILL_REVIEW_STANDARD.md`
- `docs/COMPATIBILITY_MODEL.md`
- `docs/SKILL_UNIVERSE_INVENTORY.md`
- `docs/GRAPHIFY_STANDARD.md`
- `docs/AGENT_CREATION_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `skills/PROJECT_INDEX.md`
- `skills/registry.md`
- `workflow-templates/universal-project-v1/`
- `knowledge-library/README.md`
- `knowledge-library/PROJECT_INDEX.md`
- `logs/WORKFLOW_LOG.md`

## Next Required Action

Run the first real project using this OS with the default repository-per-project model:

`projects/0001-project-execution-os-foundation-review/`

Purpose:

Run Project Execution OS on itself and review the foundation through the universal workflow.
