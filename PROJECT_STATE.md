---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-06-01
source_of_truth: repository
active_branch: main
---

# PROJECT_STATE.md

## Current State

`Project Execution OS` is an active central project and is prepared for transfer to another executor.

The repository now uses the minimum active continuity set required by `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

## Latest Confirmed Milestone

- PR `#6` was merged into `main`.
- Merge commit: `8c86466fa6394bcaf9d833a5ca29d7464893eeba`.
- Canonical local project entrypoint: `PROJECT.md`.
- New standalone real project folders bootstrap with local Git, `AGENTS.md`, and `PROJECT.md`.
- Internal subprojects inside an existing repository inherit the parent Git layer and do not receive nested `git init` unless separately authorized.
- Zero-state and active-state project structures are explicitly separated.
- Project index maintenance, stable-prefix behavior, communication-channel routing, and executor continuity are part of the active standards.
- GitHub Actions validates both project structure and system-context manifest integrity.
- The bootstrap model was smoke-tested with temporary project `Test123`; the owner reports that the temporary test project has been deleted.

## Current Focus

Keep the central project internally consistent and transfer-ready after every meaningful change.

## Current Next Safe Action

No implementation task is currently active.

Await the owner's next bounded central-system task. When a new task arrives:

1. enter through `START_HERE.md`;
2. follow `docs/ROUTER.md`;
3. read `PROJECT.md`, then this file and `logs/latest.md`;
4. perform only the smallest justified change;
5. update `PROJECT_STATE.md` and `logs/latest.md` after the meaningful step.

## Active Files For Re-entry

Read in this order when resuming central-project work:

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT.md`
4. `PROJECT_STATE.md`
5. `logs/latest.md`
6. `PROJECT_INDEX.md` only when broader navigation is needed
7. routed standards only when the active task requires them

## Known Blockers

None currently recorded.

## Do-Not-Break Rules

- Do not bypass `START_HERE.md` as the stable top-level entrypoint.
- Do not replace `docs/ROUTER.md` with duplicated navigation logic elsewhere.
- Do not treat chat memory as durable project truth.
- Do not add files, folders, or architectural layers ritualistically.
- Do not claim execution without a confirmed repository event.
- Preserve the smallest sufficient context-loading path.
- Update this file and `logs/latest.md` after every meaningful central-project change.
