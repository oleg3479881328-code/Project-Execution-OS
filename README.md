# Project Execution OS

Universal repository-first operating system for starting, running, reviewing, and preserving project work.

This repository is the source of truth for a universal project workflow that can be used by humans, ChatGPT, Codex, Claude, local AI agents, research agents, coding agents, and future automation systems.

It is also the central repository for:

- reusable workflow and governance standards;
- reusable domain blocks;
- central reusable skills;
- central reusable agent templates;
- central reusable knowledge;
- integration rules for lightweight idea capture before project creation;
- migration of validated ideas from incubator repositories.

Default private AI coordination hub:

`oleg3479881328-code/AI-Coordination-Hub`

Default external idea intake library:

`oleg3479881328-code/Reference-Idea-Library`

Important coordination rule:

Use the central `ChatGPT <-> Codex <-> GitHub` collaboration protocol and skill whenever reasoning-model work must be handed to Codex through a durable reviewable surface.

For that workflow, `GitHub main` is the committed source of truth. Local folders are execution workspaces only.

## Start Here

Use one top-level entry:

`START_HERE.md`

Then route from there:

- new project -> `Start New Project.md`
- continue an existing project -> project memory inside that repository
- quick daily orientation -> `START_FAST.md`

Do not start by coding.
Do not start by creating agents.
Do not start by building runtime.
Do not start by designing a giant architecture.

First read the entrypoint, understand the project workflow, then create or continue a project through repository artifacts.

## Core Idea

Every new project should have:

- one dedicated private GitHub repository by default;
- one short clear bilingual repository description at creation time, with Russian first and English second;
- one clear project entrypoint;
- one local project memory;
- one workflow run folder;
- task-specific agents created only when needed;
- project knowledge extracted into the project library;
- reusable knowledge promoted into the central knowledge library after review.

## Repository Role

GitHub is the source of truth.

Chat messages, generated drafts, and uncommitted ideas are not final project state.

A project state becomes valid only when it is represented by a repository artifact.

## Current Mode

Document-first foundation.

No backend.
No frontend.
No runtime engine.
No orchestration engine.
No vector database.
No automation layer.
No mass agent creation.

Important future-system ideas that are intentionally deferred belong in:

`docs/DEFERRED_SYSTEM_IDEAS.md`

## Universal Workflow

INPUT
→ CLARIFICATION
→ RESEARCH
→ PLAN
→ EXECUTION SPEC
→ REVIEW
→ RESULT
→ KNOWLEDGE EXTRACT
→ LOG

## Main Documents

- `START_HERE.md`
- `Start New Project.md`
- `START_FAST.md`
- `PROJECT_INDEX.md`
- `blocks/README.md`
- `blocks/PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/WORKFLOW_DECISION_TABLE.md`
- `docs/MICRO_TASK_MODE.md`
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
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
- `agent-library/README.md`
- `agent-library/PROJECT_INDEX.md`
- `skills/PROJECT_INDEX.md`
- `skills/registry.md`
- `workflow-templates/universal-project-v1/README.md`
- `knowledge-library/README.md`
- `knowledge-library/PROJECT_INDEX.md`
- `CHANGELOG.md`
- `logs/WORKFLOW_LOG.md`

## First Operational Rule

When a new project begins, create a dedicated private GitHub repository by default.

`Start New Project.md` is the short boot-router.

The heavier operating logic lives in the linked standards under `docs/`.

Internal project folders under:

`projects/<project-id>/`

are exceptions for compact or intentionally internal work.

Then create the first workflow run from:

`workflow-templates/universal-project-v1/`
