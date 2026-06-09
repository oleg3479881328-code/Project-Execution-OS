# Notion Agent Workspace Stack

Type: `architecture-decision`
Lifecycle status: `candidate`
Captured: 2026-06-09

## Reusable Lesson

Notion should be used as a universal readable agent workspace layer for projects that need it, not as a second operating system and not as a mandatory layer for every project.

Use:

`START_HERE.md -> ROUTER -> PROJECT_ID -> project entrypoint -> matching Notion project page -> smallest relevant database slice -> bounded update in the correct truth-owning layer`

## Key Rules

- Reuse the same stable `PROJECT_ID` across GitHub, Notion, Drive, Bublup, Telegram, local folders, and agent handoffs.
- Preserve the Project Execution OS layer-aware truth map.
- Use Notion for readable management, coordination, and catalogue visibility when attached.
- Use GitHub for code, technical artifacts, commits, pull requests, and Codex execution evidence when attached.
- Do not build uncontrolled two-way synchronization before field ownership, conflict behavior, and rollback are defined.
- Prefer official Notion MCP, API, and native GitHub integration before custom automation.

## Entry Point

Use:

`blocks/notion/BLOCK.md`

## Live Pilot

A live Notion scaffold was created on 2026-06-09 with:

- Projects
- Tasks
- Research
- Decisions
- Assets
- Links
- Logs
- Knowledge Extracted
- Agent Notes

The initial test record uses:

`PROJECT_ID = project-execution-os`

## Validation Still Required

- fresh-agent re-entry by `PROJECT_ID`;
- one real task and log update;
- conflict-handling test;
- native GitHub integration review;
- decision on whether automation is needed after practical use.

## Final Rule

Use Notion to make durable project context readable and agent-accessible without duplicating the operating system or creating duplicate truth.