---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-06-10
source_of_truth: repository
active_branch: main
---

# PROJECT_STATE.md

## Current State

`Project Execution OS` is an active central project and is prepared for transfer to another executor.

The repository uses the minimum active continuity set required by `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

## Latest Confirmed Milestone

- PR `#44` was merged into `main`.
- Merge commit: `41d4db314141b00146d84a15bc81ac0ebfe2174d`.
- Added `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` as the reusable standard for measuring agent quality by successful outcomes, cost, latency, context efficiency, tool-use quality, regression protection, safety and transferability.
- Routed agent-quality, eval, observability and orchestration-complexity work through `docs/ROUTER.md`.
- Updated `SYSTEM_CONTEXT_MANIFEST.md` to `system-context-manifest-v10` / `knowledge-aware-core-v10` after the router changed.
- GitHub Actions validation passed before merge.

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

- `PROJECT_INDEX.md` still needs a curated canonical-documents entry for `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` during the next safe large-index maintenance pass. Generated indexes already detect the new document automatically.

## Do-Not-Break Rules

- Do not bypass `START_HERE.md` as the stable top-level entrypoint.
- Do not replace `docs/ROUTER.md` with duplicated navigation logic elsewhere.
- Do not treat chat memory as durable project truth.
- Do not add files, folders, or architectural layers ritualistically.
- Do not claim execution without a confirmed repository event.
- Preserve the smallest sufficient context-loading path.
- Update this file and `logs/latest.md` after every meaningful central-project change.