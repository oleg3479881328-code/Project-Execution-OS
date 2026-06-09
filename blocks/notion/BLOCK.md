# Notion Agent Workspace Block

## Purpose

Provide a reusable Notion workspace layer for Project Execution OS so any authorized agent can enter any project through the same project identity, page contract, database schema, agent rules, and synchronization boundaries.

## Status

`candidate`

This block becomes active only after one real project validates the workspace contract and agent re-entry flow.

## Core Principle

Notion is a readable project-memory and management layer when a project needs it.

It is not a second operating system and it does not replace layer-specific sources of truth.

## When To Use

Use this block for:

- Notion workspace architecture for Project Execution OS projects;
- agent-compatible project pages;
- cross-project Project ID routing;
- shared Notion databases for projects, tasks, research, decisions, assets, links, logs, and extracted knowledge;
- Notion MCP or API access design;
- GitHub and Notion coordination boundaries;
- reusable Notion templates.

## When Not To Use

Do not use this block for:

- one-off private notes;
- projects that do not need durable Notion context;
- storing secrets, tokens, passwords, or confidential documents;
- replacing GitHub for code, commits, pull requests, or technical artifacts;
- broad automation before repeated manual use proves the need.

## Read Next

Read only the smallest relevant file:

1. Workspace architecture and identity: `WORKSPACE_CONTRACT.md`
2. Databases and properties: `DATABASE_SCHEMA.md`
3. Agent behavior: `AGENT_RULES.md`
4. Ready donors and integration options: `READY_SOLUTIONS.md`
5. Validation before activation: `VALIDATION_BACKLOG.md`
6. Research evidence: `RESEARCH_REPORT_2026-06-09.md`
7. Source URLs: `REFERENCES.md`

## Typical Flow

```text
START_HERE.md
-> docs/ROUTER.md
-> project entrypoint
-> resolve PROJECT_ID
-> open matching Notion project page
-> load only the smallest relevant linked database slice
-> perform bounded work
-> record status, decision, task, research, log, or knowledge candidate in the correct layer
```

## Boundary

This block defines the reusable Notion layer only.

It must not store project-specific state, credentials, private personal data, or active project decisions that belong inside an individual project workspace.

## Final Rule

Notion should make a project understandable to the next agent without owner explanation.

It must never create duplicate truth.