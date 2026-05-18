# Project Execution OS

Universal repository-first operating system for starting, running, reviewing, and preserving project work.

This repository is the source of truth for a universal project workflow that can be used by humans, ChatGPT, Codex, Claude, local AI agents, research agents, coding agents, and future automation systems.

It is also the central repository for:

- reusable workflow and governance standards;
- central reusable skills;
- central reusable knowledge;
- migration of validated ideas from incubator repositories.

## Start Here

Every human or AI agent must start with:

`START_HERE.md`

Do not start by coding.
Do not start by creating agents.
Do not start by building runtime.
Do not start by designing a giant architecture.

First read the entrypoint, understand the project workflow, then create or continue a project through repository artifacts.

## Core Idea

Every new project should have:

- one dedicated private GitHub repository by default;
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
- `PROJECT_INDEX.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/GOVERNANCE.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/SKILL_SPEC.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/SKILL_REVIEW_STANDARD.md`
- `docs/COMPATIBILITY_MODEL.md`
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`
- `docs/SKILL_UNIVERSE_INVENTORY.md`
- `docs/GRAPHIFY_STANDARD.md`
- `docs/AGENT_CREATION_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `skills/PROJECT_INDEX.md`
- `skills/registry.md`
- `workflow-templates/universal-project-v1/README.md`
- `knowledge-library/README.md`
- `knowledge-library/PROJECT_INDEX.md`
- `logs/WORKFLOW_LOG.md`

## First Operational Rule

When a new project begins, create a dedicated private GitHub repository by default.

Internal project folders under:

`projects/<project-id>/`

are exceptions for compact or intentionally internal work.

Then create the first workflow run from:

`workflow-templates/universal-project-v1/`
