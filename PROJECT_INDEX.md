# Project Index — Project Execution OS

## Repository

`oleg3479881328-code/Project-Execution-OS`

## System Name

Project Execution OS

## Purpose

Create a universal repository-first operating system for starting, running, reviewing, and preserving projects.

The system must support humans, ChatGPT, Codex, Claude, local models, specialized agents, and future automation systems through one entrypoint and one stable project workflow.

For the canonical GitHub-based coordination loop between reasoning models and Codex, use:

`docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`

It must also support:

- brainstorm-only work without forcing project creation;
- idea capture without forcing project creation;
- normalization of older repositories into the current standard;
- durable ChatGPT to Codex communication through GitHub.

## Primary Entrypoint

`START_HERE.md`

Every user, assistant, agent, or automation session must start there.

`START_HERE.md` is intentionally minimal and durable. It points to the live internal router:

`docs/ROUTER.md`

Internal route growth belongs in `docs/ROUTER.md`, not in `START_HERE.md`.

## Current Phase

Foundation phase.

Mode:

`document-first`

Status:

`foundation_candidate`

## Core System Model

```text
Project Execution OS
  ├── Stable Universal Entrypoint
  ├── Live Internal Router
  ├── Project Workspace Standard
  ├── Universal Workflow Contract
  ├── Context Assembly Standard
  ├── System Context Versioning
  ├── API Runtime Cost And Cache Logging
  ├── Domain Blocks Layer
  ├── Agent Creation Standard
  ├── Agent Library Standard
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
- `docs/ROUTER.md`
- `Start New Project.md`
- `START_FAST.md`
- `PROJECT_INDEX.md`
- `SYSTEM_CONTEXT_MANIFEST.md`
- `project-library/DECISION_REGISTRY.md`
- `project-library/decisions/006-stable-start-here-live-router.md`
- `blocks/README.md`
- `blocks/PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/WORKFLOW_DECISION_TABLE.md`
- `docs/MICRO_TASK_MODE.md`
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `docs/DECISION_REGISTRY_STANDARD.md`
- `docs/GOVERNANCE.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/SKILL_SPEC.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/SKILL_REVIEW_STANDARD.md`
- `docs/COMPATIBILITY_MODEL.md`
- `docs/integrations/README.md`
- `docs/integrations/chatgpt/CODEX_GITHUB_PROTOCOL.md`
- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
- `docs/integrations/notion/README.md`
- `docs/AI_COORDINATION_HUB_STANDARD.md`
- `docs/SKILL_UNIVERSE_INVENTORY.md`
- `docs/GRAPHIFY_STANDARD.md`
- `docs/DEFERRED_SYSTEM_IDEAS.md`
- `docs/AGENT_CREATION_STANDARD.md`
- `docs/AGENT_LIBRARY_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `agent-library/README.md`
- `agent-library/PROJECT_INDEX.md`
- `skills/PROJECT_INDEX.md`
- `skills/registry.md`
- `workflow-templates/universal-project-v1/README.md`
- `workflow-templates/project-entrypoint/GITHUB_PROJECT_ENTRYPOINT_TEMPLATE.md`
- `workflow-templates/project-entrypoint/NOTION_PROJECT_ENTRYPOINT_TEMPLATE.md`
- `knowledge-library/README.md`
- `knowledge-library/PROJECT_INDEX.md`
- `CHANGELOG.md`
- `logs/WORKFLOW_LOG.md`
- `logs/2026-05-29-context-cache-implementation.md`
- `logs/2026-05-29-stable-start-here-router-split.md`

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

Every new repository should also have a short clear bilingual GitHub description from the start, with Russian first and English second.

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

## Context Assembly Architecture

Stable entry and routing:

```text
START_HERE.md
→ docs/ROUTER.md
→ smallest relevant internal node
```

Minimum sufficient context is assembled through:

`docs/CONTEXT_ASSEMBLY_STANDARD.md`

Stable reusable context identity is recorded in:

`SYSTEM_CONTEXT_MANIFEST.md`

Context-profile versioning rules live in:

`docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`

API token usage, provider-side cache behavior and cost evidence are measured through:

`docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`

Do not load the entire system, project, knowledge library or skill layer by default.

## Knowledge Architecture

Local project knowledge:

`projects/<project-id>/project-library/`

Central reusable knowledge:

`knowledge-library/`

Promotion rule:

Project knowledge becomes central knowledge only after review.

Research and design work should prefer publicly verifiable external sources, including official documentation, GitHub repositories, open-source examples, and other public evidence sources appropriate to the domain.

Central knowledge must be loaded selectively when relevant to the active task rather than injected wholesale into every AI context.

## Agent Architecture

Agents are created per project when needed.

Agents are task-specific modules, not the root system.

Required agent artifact:

`projects/<project-id>/agents/<agent-name>/AGENT.md`

Central reusable skills live under:

`skills/<category>/<skill-name>/`

Central reusable agent templates live under:

`agent-library/templates/`

Central reusable domain blocks live under:

`blocks/`

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

Committed artifacts include:

- `README.md`
- `START_HERE.md`
- `docs/ROUTER.md`
- `PROJECT_INDEX.md`
- `SYSTEM_CONTEXT_MANIFEST.md`
- `project-library/DECISION_REGISTRY.md`
- `project-library/decisions/006-stable-start-here-live-router.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/GOVERNANCE.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/SYSTEM_CONTEXT_VERSION_STANDARD.md`
- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
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
- `logs/2026-05-29-context-cache-implementation.md`
- `logs/2026-05-29-stable-start-here-router-split.md`

## Next Required Action

Run a bounded review for stale references that still treat `START_HERE.md` as the live route catalogue, then validate the new context-assembly and API-economics artifacts before building any runtime orchestrator.

## v2 Direction

`Start New Project.md` is now intended to stay short and act only as a startup router.

Heavier operating logic belongs in linked standards under `docs/`.