# Project Structure Standard v1

## Purpose

This standard defines the folder structure for every project inside Project Execution OS.

Any human or AI agent must be able to open a project folder and understand the goal, current state, rules, agents, knowledge, workflow history, and next action.

For the exact contract of the first-project-read artifact, use:

`docs/PROJECT_ENTRYPOINT_STANDARD.md`

## Project Root

Default rule:

Every project should live in its own dedicated private GitHub repository by default.

Every new repository should also receive a short clear bilingual GitHub description at creation time so the repository remains identifiable in GitHub lists, search, and navigation.

Description order rule:

- Russian first
- English second

The root `projects/` folder inside `Project Execution OS` is for internal or compact exceptions, not the primary default.

Recommended project id format:

YYYYMMDD-short-kebab-name

Example:

projects/20260516-news-telegram-bot/

## Required Project Files And Folders

Every full-mode project must contain:

- PROJECT_ENTRYPOINT.md
- PROJECT_STATE.md
- PROJECT_RULES.md
- agents/
- project-library/
- workflow-runs/
- logs/

Optional but recommended when handoff speed matters:

- CONTEXT_PACK.md

## Compact Project Mode

Compact mode is allowed for small or low-risk projects.

Compact mode may use a smaller structure, for example:

```text
PROJECT_ENTRYPOINT.md
PROJECT_STATE.md
workflow-runs/
logs/
```

or another minimal structure that still preserves:

- source of truth;
- explicit current state;
- explicit next action;
- evidence-backed research when relevant;
- review before stable acceptance;
- durable log history.

Compact mode must not be used as an excuse to hide important state in chat.

## PROJECT_ENTRYPOINT.md

Single entrypoint for this specific project.

Must include:

- project name;
- project goal;
- required read order;
- current state file;
- latest workflow run;
- current next action.

For the canonical structure and section logic, use:

`docs/PROJECT_ENTRYPOINT_STANDARD.md`

## PROJECT_STATE.md

Current state snapshot.

The file should start with a short machine-readable frontmatter block:

```yaml
---
status: in-progress
project_mode: compact
current_step: 07_RESULT
current_run: workflow-runs/0001-initial-definition/
last_updated: 2026-05-21
next_action: Open the landing page locally or publish it with GitHub Pages.
---
```

Must include:

- current phase;
- current workflow run;
- confirmed decisions;
- open questions;
- active or candidate agents;
- local knowledge status;
- latest result;
- next action.

Keep the frontmatter short and stable.

It exists so a human or agent can recover project state without rereading the whole repository.

## PROJECT_RULES.md

Project-specific rules.

Must include:

- scope boundaries;
- forbidden actions;
- quality rules;
- tool rules;
- domain constraints;
- evidence rules;
- state separation rules.

## agents/

Stores project-specific agents.

Each agent should have its own folder and AGENT.md file.

Agents are created only when the workflow proves they are needed.

## project-library/

Stores project-local knowledge.

Suggested categories:

- patterns;
- anti-patterns;
- decisions;
- research notes;
- templates.

Project-local knowledge is not automatically central knowledge.

## workflow-runs/

Stores workflow runs.

Each run gets its own folder.

Each run follows the universal workflow contract.

## logs/

Stores project execution logs.

Required file:

logs/PROJECT_LOG.md

The log records workflow milestones, repository changes, decisions, reviews, knowledge extraction, and next actions.

## State Truth Rule

If project state conflicts:

1. committed repository artifacts beat chat memory;
2. PROJECT_STATE.md is the latest project state;
3. the latest workflow run is the current execution state;
4. logs preserve historical sequence;
5. central knowledge library governs reusable cross-project rules.

## No Hidden Project State

Important project state must not live only in chat.

If it matters, write it into a project artifact.

## CONTEXT_PACK.md

Optional compact briefing artifact.

Use it when a project will be handed between agents or sessions often and a short recovery file will materially reduce re-entry cost.

`CONTEXT_PACK.md` is not the primary source of truth.

It is a cache-like briefing layer that should summarize:

- current goal;
- current mode;
- latest durable decisions;
- current run;
- next action;
- which artifacts are canonical right now.
