# Project Structure Standard v1

## Purpose

This standard defines the folder structure for every project inside Project Execution OS.

Any human or AI agent must be able to open a project folder and understand the goal, current state, rules, agents, knowledge, workflow history, and next action.

## Project Root

Every project must live under the root projects folder.

Recommended project id format:

YYYYMMDD-short-kebab-name

Example:

projects/20260516-news-telegram-bot/

## Required Project Files And Folders

Every project must contain:

- PROJECT_ENTRYPOINT.md
- PROJECT_STATE.md
- PROJECT_RULES.md
- agents/
- project-library/
- workflow-runs/
- logs/

## PROJECT_ENTRYPOINT.md

Single entrypoint for this specific project.

Must include:

- project name;
- project goal;
- required read order;
- current state file;
- latest workflow run;
- current next action.

## PROJECT_STATE.md

Current state snapshot.

Must include:

- current phase;
- current workflow run;
- confirmed decisions;
- open questions;
- active or candidate agents;
- local knowledge status;
- latest result;
- next action.

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
