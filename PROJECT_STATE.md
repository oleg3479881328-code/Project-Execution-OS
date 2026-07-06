---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-07-06
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

- Added `docs/HARNESS_ENGINEERING_STANDARD.md` as the central architecture wrapper for reusable or operational AI-agent workflows.
- Updated `docs/ROUTER.md` so harness engineering, agent runtime scaffold, tool/context/permission design, sandbox, memory and verification scaffold requests route directly to the new standard.
- Updated `PROJECT_INDEX.md` to include both `docs/HARNESS_ENGINEERING_STANDARD.md` and existing `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` in canonical documents.
- Updated `PROJECT.md` so the central entrypoint records the new harness-engineering layer.
- Source trail recorded in the new standard: `https://github.com/ai-boost/awesome-harness-engineering`.
- Creation/update commits on branch `harness-engineering-standard-v1`: `dcfd166a67876ac94302bbf450ba739cd00ed76f`, `fd898db662c8f3687862a2e95b59eaa0e9498f02`, `c5562ebc3d23a4f40878bd15c34b5ec44ce8e39e`, `8de112b5494a2980dc5146d977223b9293d966ad`, `8dfddd946090bd940993f09a3d1b9fc4d4227647`, `7a42b335d5db55f025824e967763dac497b8bd12`.

## Current Focus

Keep the central project internally consistent and transfer-ready after every meaningful change.

Harness engineering is now the first architecture layer for repeated or operational agents. Agent quality measurement remains handled by `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` after the scaffold is explicit.

## Current Next Safe Action

Use `docs/HARNESS_ENGINEERING_STANDARD.md` on the next real reusable agent or workflow before promoting it beyond one-off use.

Recommended next validation target: apply it to `projects/personal-secretary-os/PROJECT.md` or another active repeated workflow, then update the owning project state.

When a new task arrives:

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

For harness engineering work, open:

```text
docs/HARNESS_ENGINEERING_STANDARD.md
docs/AGENT_QUALITY_SCORECARD_STANDARD.md
```

For Impeccable or AI-coded frontend design QA work, open:

```text
blocks/design/IMPECCABLE_DESIGN_QA_GATE.md
blocks/design/BLOCK.md
```

## Known Blockers

- `gemini-tts-speech-generation` is registered as `candidate` / `not_reviewed`; it must not be treated as active until reviewed.
- `blocks/design/IMPECCABLE_DESIGN_QA_GATE.md` is candidate guidance and should be validated on a real frontend task before promotion.
- `docs/HARNESS_ENGINEERING_STANDARD.md` is newly added and should be validated on a real reusable-agent workflow before being treated as mature operational guidance.

## Do-Not-Break Rules

- Do not bypass `START_HERE.md` as the stable top-level entrypoint.
- Do not replace `docs/ROUTER.md` with duplicated navigation logic elsewhere.
- Do not treat chat memory as durable project truth.
- Do not add files, folders, or architectural layers ritualistically.
- Do not claim execution without a confirmed repository event.
- Preserve the smallest sufficient context-loading path.
- Update this file and `logs/latest.md` after every meaningful central-project change.
