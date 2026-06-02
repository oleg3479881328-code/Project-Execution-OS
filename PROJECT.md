# PROJECT.md

## Project

- Name: `Project Execution OS`
- Type: `layer-aware project operating system`
- Short description: `central standards, templates, routing, and reusable artifacts for starting and running projects across the right durable layers`

## Purpose

- Create a universal operating system for starting, running, reviewing, and preserving projects without forcing every idea into the same storage model.
- Support humans and AI agents through one stable entrypoint, one live router, and minimal task-specific context loading.

## Source Of Truth

- This repository is the committed source of truth for `Project Execution OS` standards, templates, skills, and reusable repository artifacts.
- `START_HERE.md` is the stable system door.
- `docs/ROUTER.md` is the live internal map.
- `PROJECT_STATE.md` and `logs/latest.md` preserve the current active continuity state for executor handoff.

## Current Status

- Mode: `document-first`
- Phase: `foundation`
- Status: `transfer-ready central project`

## Done So Far

- Established `START_HERE.md` as the stable top-level entrypoint.
- Split live routing into `docs/ROUTER.md`.
- Built central standards for lifecycle, context assembly, repository memory, review, research, handoff, and bootstrap.
- Migrated the canonical local project entrypoint to `PROJECT.md`.
- Adopted lightweight standalone bootstrap: local Git, `AGENTS.md`, and `PROJECT.md`.
- Confirmed separate handling for internal subprojects without nested Git by default.
- Smoke-tested the bootstrap model with temporary project `Test123`; the owner reports that the test project was deleted after validation.
- Added root `PROJECT_STATE.md` and `logs/latest.md` so this central project complies with its own active continuity standard.

## Current Focus

- Keep the central system internally consistent and transfer-ready after every meaningful change.

## Next Practical Step

- Await the owner's next bounded central-system task.

## Key Decisions And Constraints

- Do not duplicate evolving system logic into ad hoc files when the repository standards already define it.
- `Existing Solution First` applies before inventing new central mechanisms.
- `PROJECT.md` is the canonical local project entrypoint for GitHub-backed and file-executed projects.
- `PROJECT_INDEX.md` remains an index and must not replace the role of `PROJECT.md`.
- Local Git is the default bootstrap for real project folders; GitHub, Notion, and Google Drive are attached only when they are actually needed.
- Active projects must maintain `PROJECT_STATE.md` and `logs/latest.md` after meaningful changes.

## Read Next

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT_STATE.md`
4. `logs/latest.md`
5. `PROJECT_INDEX.md` only when broader navigation is needed
6. routed standards only when the active task requires them
