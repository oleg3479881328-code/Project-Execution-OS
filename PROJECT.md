# PROJECT.md

## Project

- Name: `Project Execution OS`
- Type: `layer-aware project operating system`
- Short description: `central standards, templates, routing, reusable knowledge blocks, composable executable capabilities, and application surfaces for starting and running projects across durable layers`

## Purpose

- Create a universal operating system for starting, running, reviewing, and preserving projects without forcing every idea into the same storage model.
- Support humans and AI agents through one stable entrypoint, one live router, and minimal task-specific context loading.
- Reduce repeated engineering by separating domain knowledge, reusable executable capabilities, workflow orchestration, and project-specific application logic.
- Make capability readiness visible and testable through owner-facing application surfaces.

## Source Of Truth

- This repository is the committed source of truth for `Project Execution OS` standards, templates, skills, reusable repository artifacts, capability registry state, and application adapters.
- `START_HERE.md` is the stable system door.
- `docs/ROUTER.md` is the live internal map.
- `PROJECT_STATE.md` and `logs/latest.md` preserve the current active continuity state for executor handoff.
- `capability-library/REGISTRY.md` is the source of truth for reusable capability readiness.
- `apps/` contains application adapters and user interfaces; reusable technical operations remain in `capabilities/`.

## Current Status

- Mode: `document-first with executable capabilities and visual application adapters`
- Phase: `foundation validation`
- Status: `transfer-ready central project`

## Done So Far

- Established `START_HERE.md` as the stable top-level entrypoint and `docs/ROUTER.md` as the live internal router.
- Built central standards for lifecycle, context assembly, repository memory, review, research, handoff, bootstrap, harness engineering, and composable capability blocks.
- Separated domain blocks, executable capability blocks, workflow composition, and application adapters.
- Registered the initial media capability chain: download, probe, audio extraction, transcription, and clipping.
- Implemented `media.probe` version `0.1.0` as the first executable candidate capability.
- Passed local, CLI, contract, smoke, and GitHub Actions validation for `media.probe`.
- Merged PR #89 as `74c6ae9585f55f84f6f5e342368636c3e1512a01`.
- Implemented `Block Studio 0.1.0` as the first visual application-layer surface in `apps/block-studio/`.
- Added capability discovery from the registry, manifests, and Python entry points.
- Added an interactive `media.probe` workflow with drag-and-drop upload, local preview, readable result cards, stream inspection, raw JSON, logs, contract, tests, and owner/developer modes.
- Added protected temporary storage, cleanup, local-only binding, and `START_BLOCK_STUDIO.bat` for Windows double-click startup.
- Passed Block Studio tests on Ubuntu and Windows with Python 3.13 and real `ffprobe` execution.
- Merged PR #90 as `d70fbb1be0d419b3dcc5b47a9d3dc107a9551069`.

## Current Focus

- Have the owner open Block Studio on the target Windows computer and process one real user-owned video.
- Keep `media.probe` and Block Studio at `candidate` until that owner confirmation exists.
- Implement `media.clip` as the second executable capability and connect it to the same Studio.
- Compare two real capability implementations before extracting shared SDK code.

## Next Practical Step

1. Download or pull the merged Block Studio files.
2. Double-click `START_BLOCK_STUDIO.bat`.
3. Load a real MP4, run `media.probe`, inspect the result, and confirm whether the owner experience works correctly.
4. Record any Windows-specific issue found on the target computer.
5. Implement `media.clip` and add its interactive Studio screen.
6. Then proceed to `media.extract_audio`, `media.transcribe`, and `media.download` unless real project evidence changes the sequence.

## Key Decisions And Constraints

- Do not duplicate evolving system logic into ad hoc files when repository standards already define it.
- `Existing Solution First` applies before inventing new providers or central mechanisms.
- `PROJECT.md` is the canonical local project entrypoint.
- Active projects must maintain `PROJECT_STATE.md` and `logs/latest.md` after meaningful changes.
- `blocks/<domain>/` stores reusable domain knowledge and decision guidance.
- `capabilities/<capability-id>/` stores one bounded reusable technical operation behind stable contracts.
- `apps/<application>/` owns application UI, interaction, and application-specific orchestration without copying provider logic.
- Package-first remains the default; do not create one microservice per block without evidence.
- `candidate` means code and minimum verification exist; it does not equal owner-confirmed or production-ready.
- Do not extract a common capability SDK from one implementation alone.

## Read Next

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT_STATE.md`
4. `logs/latest.md`
5. `apps/block-studio/README.md`
6. `apps/block-studio/VALIDATION.md`
7. `capability-library/REGISTRY.md`
8. `capabilities/media-probe/BLOCK.md`
9. `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`
10. `PROJECT_INDEX.md` only when broader navigation is needed
