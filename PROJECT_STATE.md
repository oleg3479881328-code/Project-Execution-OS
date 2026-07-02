---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-07-02
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

- Added `blocks/design/IMPECCABLE_DESIGN_QA_GATE.md` as a candidate reusable design-quality gate for AI-coded frontend work.
- Updated `blocks/design/BLOCK.md` from `candidate_v2` to `candidate_v3` to include AI-coded frontend QA as part of the Design Block.
- Updated `docs/ROUTER.md` so Impeccable, AI-slop review, frontend design detector, UI polish/audit after AI coding, and design quality gate requests route directly to the new gate.
- Updated `blocks/PROJECT_INDEX.md` so the curated Blocks Index reflects Design Block `candidate_v3` and its frontend QA scope.
- Source trail recorded in the new gate: Pimenov article plus official Impeccable repository.
- Creation/update commits: `f1c30782c68fce13586cfd8cb7c2485ae13a91e0`, `c82a79e5f287d90d87b875e404a52d98199d1432`, `41a820967f6b2aaaedc461ded76af7a3761c616e`, `480758ddc598d9fae8903c1fcf8cf97ef535cc29`.

## Current Focus

Keep the central project internally consistent and transfer-ready after every meaningful change.

## Current Next Safe Action

No implementation task is currently active.

Next safe action for the new Impeccable gate is validation on a real AI-coded frontend task before promoting it beyond `candidate` guidance.

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

For Impeccable or AI-coded frontend design QA work, open:

```text
blocks/design/IMPECCABLE_DESIGN_QA_GATE.md
blocks/design/BLOCK.md
```

## Known Blockers

- `PROJECT_INDEX.md` still needs a curated canonical-documents entry for `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` during the next safe large-index maintenance pass. Generated indexes already detect the new document automatically.
- `gemini-tts-speech-generation` is registered as `candidate` / `not_reviewed`; it must not be treated as active until reviewed.
- `blocks/design/IMPECCABLE_DESIGN_QA_GATE.md` is candidate guidance and should be validated on a real frontend task before promotion.

## Do-Not-Break Rules

- Do not bypass `START_HERE.md` as the stable top-level entrypoint.
- Do not replace `docs/ROUTER.md` with duplicated navigation logic elsewhere.
- Do not treat chat memory as durable project truth.
- Do not add files, folders, or architectural layers ritualistically.
- Do not claim execution without a confirmed repository event.
- Preserve the smallest sufficient context-loading path.
- Update this file and `logs/latest.md` after every meaningful central-project change.
