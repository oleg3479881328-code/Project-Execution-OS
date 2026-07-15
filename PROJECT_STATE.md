---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-07-15
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

- Adopted composable executable capability blocks as a system-wide architecture for functionality that should be reused across applications.
- Added `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`.
- Added `capability-library/README.md` and `capability-library/REGISTRY.md`.
- Separated four layers explicitly:

```text
domain block
-> executable capability block
-> workflow composition
-> application adapter / UI
```

- Added a router path for reusable executable blocks and portable shared modules.
- Updated `blocks/README.md` so domain blocks are not confused with implemented code.
- Updated `blocks/video-production/BLOCK.md` to route download, probing, extraction, transcription, and clipping toward reusable capability contracts.
- Registered the first planned media chain:

```text
media.download
-> media.probe
-> media.extract_audio
-> media.transcribe
-> media.clip
```

- Updated `PROJECT_INDEX.md` and `PROJECT.md` with the new architecture.

## Architecture Decision

Reusable technical functionality should not be rebuilt separately inside each application.

Default model:

```text
build once behind a stable contract
-> package and version
-> validate independently
-> compose into project workflows
-> connect through thin application adapters
```

Package-first is the default. A capability becomes a service only when isolation, scaling, hardware, dependency, or multi-language consumer evidence justifies it.

## Current Focus

Keep the central project internally consistent and transfer-ready after every meaningful change.

Validate the capability architecture through real executable code rather than adding more specifications.

## Current Next Safe Action

Implement `media.probe` as the first candidate capability block using ffprobe.

Minimum validation target:

```text
manifest
request/result contract
artifact model
Python invocation
CLI adapter
contract test
local smoke test
registry promotion from idea to candidate
```

After that, proceed to `media.clip`, then `media.extract_audio`, `media.transcribe`, and `media.download`, unless real project evidence changes the sequence.

## Active Files For Re-entry

Read in this order when resuming central-project work:

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT.md`
4. `PROJECT_STATE.md`
5. `logs/latest.md`
6. `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md` for reusable code architecture
7. `capability-library/REGISTRY.md` for actual block readiness
8. `PROJECT_INDEX.md` only when broader navigation is needed
9. routed standards only when the active task requires them

For capability implementation work, also open:

```text
docs/EXISTING_SOLUTION_FIRST_STANDARD.md
docs/HARNESS_ENGINEERING_STANDARD.md
blocks/<relevant-domain>/BLOCK.md
```

For Impeccable or AI-coded frontend design QA work, open:

```text
blocks/design/TASTE_FRONTEND_EXECUTION_STANDARD.md
blocks/design/IMPECCABLE_DESIGN_QA_GATE.md
blocks/design/BLOCK.md
```

## Known Blockers

- All entries in `capability-library/REGISTRY.md` currently have status `idea`; no executable capability block has yet been implemented or validated under the new contract.
- The common artifact and request/result contracts remain architectural guidance until `media.probe` validates them in code.
- `gemini-tts-speech-generation` is registered as `candidate` / `not_reviewed`; it must not be treated as active until reviewed.
- `blocks/design/IMPECCABLE_DESIGN_QA_GATE.md` and `blocks/design/TASTE_FRONTEND_EXECUTION_STANDARD.md` are candidate guidance and should be validated on a real frontend task before promotion.
- `docs/HARNESS_ENGINEERING_STANDARD.md` is newly added and should be validated on a real reusable-agent workflow before being treated as mature operational guidance.

## Do-Not-Break Rules

- Do not bypass `START_HERE.md` as the stable top-level entrypoint.
- Do not replace `docs/ROUTER.md` with duplicated navigation logic elsewhere.
- Do not treat chat memory as durable project truth.
- Do not add files, folders, services, or architectural layers ritualistically.
- Do not claim execution without a confirmed repository event.
- Do not call a capability implemented, validated, or production-ready without matching registry evidence.
- Do not copy reusable block code into multiple applications as the normal integration method.
- Preserve the smallest sufficient context-loading path.
- Update this file and `logs/latest.md` after every meaningful central-project change.