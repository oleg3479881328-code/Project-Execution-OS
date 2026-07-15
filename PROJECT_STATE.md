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

The composable capability-block architecture now has its first executable implementation:

```text
media.probe 0.1.0 — candidate
```

Implementation location:

```text
capabilities/media-probe/
```

Pull request:

```text
https://github.com/oleg3479881328-code/Project-Execution-OS/pull/89
```

Implemented and recorded:

- package manifest and Python metadata;
- package-discovery entry point;
- CLI adapter;
- request, context, artifact, result, and structured error contracts;
- ffprobe provider and normalized metadata;
- read-only workspace boundary;
- unit, contract, missing-tool, and real ffprobe smoke tests;
- GitHub Actions workflow for Python 3.12 and 3.13;
- candidate validation record;
- registry promotion from `idea` to `candidate`.

Local evidence:

```text
Python 3.13.5
pytest 9.0.2
ffprobe 7.1.3
6 passed in 0.30s
manual CLI smoke test passed
```

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

The first implementation intentionally keeps its contracts inside the package. A shared capability SDK must not be extracted until a second implementation demonstrates real duplication.

## Current Focus

- Confirm PR #89 GitHub Actions results.
- Merge the candidate only when CI is green.
- Validate the contract against `media.clip` as the second executable block.
- Keep the distinction between `candidate` and `validated` explicit.

## Current Next Safe Action

After PR #89 merges:

1. run a native Windows smoke test for `media.probe`;
2. test representative MP4/H.264/AAC and variable-frame-rate inputs;
3. integrate `media.probe` into one real application workflow;
4. implement `media.clip` using ffmpeg;
5. compare the two implementations before extracting shared contract code.

## Active Files For Re-entry

Read in this order when resuming central-project work:

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT.md`
4. `PROJECT_STATE.md`
5. `logs/latest.md`
6. `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`
7. `capability-library/REGISTRY.md`
8. `capabilities/media-probe/BLOCK.md`
9. `capabilities/media-probe/VALIDATION.md`
10. `logs/2026-07-15-media-probe-candidate.md`
11. `PROJECT_INDEX.md` only when broader navigation is needed

For capability implementation work, also open:

```text
docs/EXISTING_SOLUTION_FIRST_STANDARD.md
docs/HARNESS_ENGINEERING_STANDARD.md
blocks/<relevant-domain>/BLOCK.md
```

## Known Blockers

- PR #89 CI must pass before merge.
- Native Windows path behavior is implemented but not yet verified on Windows.
- `media.probe` is not yet integrated into a real application, so it is not `validated`.
- The container could not re-clone the remote branch because DNS resolution for `github.com` was unavailable; the error is logged and CI is the independent repository check.
- Other media capability entries remain `idea`.
- `gemini-tts-speech-generation` remains `candidate` / `not_reviewed`.
- Design Taste and Impeccable standards remain candidate guidance pending real-project validation.

## Do-Not-Break Rules

- Do not bypass `START_HERE.md` as the stable top-level entrypoint.
- Do not replace `docs/ROUTER.md` with duplicated navigation logic elsewhere.
- Do not treat chat memory as durable project truth.
- Do not add files, folders, services, or architectural layers ritualistically.
- Do not claim execution without a confirmed repository event.
- Do not call a capability implemented, validated, or production-ready without matching registry evidence.
- Do not copy reusable block code into multiple applications as the normal integration method.
- Do not extract a common SDK from one block alone.
- Preserve the smallest sufficient context-loading path.
- Update this file and `logs/latest.md` after every meaningful central-project change.
