# Notion Workspace Contract

## Purpose

Define the minimum Notion structure that lets any authorized agent enter any Project Execution OS project without asking the owner to explain the workspace again.

## Identity Contract

Every Notion project page must expose these fields or visibly equivalent properties:

- `PROJECT_ID` — stable machine-readable project key.
- `PROJECT_NAME` — human-readable project name.
- `PROJECT_STATUS` — idea, candidate, active, paused, archived, deprecated.
- `PROJECT_TYPE` — app, workflow, content, research, system, legal, personal, other.
- `PROJECT_ENTRYPOINT` — preferred project front door URL or repository path.
- `GITHUB_REPO` — repository URL when GitHub exists.
- `NOTION_PROJECT_URL` — self URL of the Notion project page.
- `OWNER` — human owner.
- `CURRENT_MODE` — new project, continue, review, research, execution, handoff, archive.
- `LAST_AGENT_TOUCH` — last agent update date or timestamp.
- `ACTIVE_LAYERS` — Chat, Local Git, GitHub, Notion, Drive, Bublup, Telegram, other.
- `TRUTH_MAP` — brief explanation of what truth belongs to each active layer.

## Important Correction

There is no universal rule that GitHub is the source of truth for every project.

The truth map depends on the attached layers:

- readable status, high-level decisions, catalogue visibility, and coordination -> Notion when attached;
- code, commits, pull requests, technical files, and Codex implementation evidence -> GitHub when attached;
- local execution history before GitHub attachment -> local Git and project files;
- heavy source assets -> Google Drive or another approved asset layer;
- current discussion -> Chat until promoted into the correct durable layer.

## Workspace Shape

Minimum project page sections:

- Overview
- Current State
- Next Practical Step
- Tasks
- Research
- Decisions
- Assets
- Links
- Logs
- Knowledge Extracted
- Agent Notes

## Database Layer

A durable multi-project workspace should use linked databases for recurring project data:

- Projects
- Tasks
- Research
- Decisions
- Assets
- Links
- Logs
- Knowledge Extracted

A lightweight project may begin with one project page and inline sections, but it must preserve `PROJECT_ID`, the truth map, and links to attached layers.

## Project Entry Flow

When an agent enters a Notion-connected project:

1. Read Project Execution OS `START_HERE.md`.
2. Follow `docs/ROUTER.md`.
3. Resolve the target `PROJECT_ID`.
4. Open the project entrypoint.
5. Open the matching Notion project page by `PROJECT_ID`.
6. Read only the smallest relevant linked database slice.
7. Compare the current task with the truth map.
8. Write updates only into the correct layer.
9. Record conflicts instead of silently overwriting them.

## Naming Rule

Use the same stable `PROJECT_ID` everywhere the project is represented:

- GitHub repository or project folder
- Notion project page
- Google Drive folder
- Bublup folder
- Telegram channel or thread
- local folder
- agent handoff package

## Permission Rule

Agents must use only the access explicitly granted to them.

Prefer project-scoped access over workspace-wide access whenever the tool permits it.

## Final Rule

The Notion workspace is valid only when a fresh authorized agent can identify the project, locate its durable layers, understand the current state, and take the next safe action without reconstructing chat history.