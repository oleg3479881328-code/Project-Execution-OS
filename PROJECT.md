# PROJECT.md

## Project

- Name: `Project Execution OS`
- Type: `layer-aware project operating system`
- Short description: `central standards, templates, routing, reusable knowledge blocks, and composable executable capability architecture for starting and running projects across the right durable layers`

## Purpose

- Create a universal operating system for starting, running, reviewing, and preserving projects without forcing every idea into the same storage model.
- Support humans and AI agents through one stable entrypoint, one live router, and minimal task-specific context loading.
- Reduce repeated engineering by separating domain knowledge, reusable executable capabilities, workflow orchestration, and project-specific application logic.

## Source Of Truth

- This repository is the committed source of truth for `Project Execution OS` standards, templates, skills, reusable repository artifacts, and capability registry state.
- `START_HERE.md` is the stable system door.
- `docs/ROUTER.md` is the live internal map.
- `PROJECT_STATE.md` and `logs/latest.md` preserve the current active continuity state for executor handoff.
- `capability-library/REGISTRY.md` is the source of truth for whether a reusable executable capability is only planned, implemented, validated, production-ready, deprecated, or retired.

## Current Status

- Mode: `document-first with executable capability candidates`
- Phase: `foundation validation`
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
- Added `docs/HARNESS_ENGINEERING_STANDARD.md` as the architecture wrapper for reusable or operational agent workflows.
- Added `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md` as the system-wide architecture for reusable executable capabilities.
- Added `capability-library/README.md` and `capability-library/REGISTRY.md`.
- Separated domain blocks from executable capability blocks, workflow composition, and application adapters.
- Registered the initial media capability chain: download, probe, audio extraction, transcription, and clipping.
- Implemented `media.probe` version `0.1.0` as the first executable candidate capability in `capabilities/media-probe/`.
- Added request, context, artifact, result, error, provider, and CLI contracts.
- Added unit, contract, negative-path, real ffprobe smoke tests, and pull-request CI.
- Promoted `media.probe` from `idea` to `candidate` after 6 local tests and a manual CLI smoke test passed.
- Passed GitHub Actions on Python 3.12 and 3.13 plus the central Project OS integrity check.
- Merged PR #89 into `main` with squash commit `74c6ae9585f55f84f6f5e342368636c3e1512a01`.
- Refreshed `SYSTEM_CONTEXT_MANIFEST.md` after the capability route changed the active router blob.

## Current Focus

- Keep the central system internally consistent and transfer-ready after every meaningful change.
- Apply harness engineering step by step by routing architecture/scaffold questions to `docs/HARNESS_ENGINEERING_STANDARD.md` before quality measurement.
- Build repeated application functionality as versioned capability blocks rather than duplicating code inside each project.
- Validate the shared contract against a second executable capability instead of prematurely extracting a common SDK.

## Next Practical Step

- Run a native Windows smoke test before treating Windows path behavior as verified.
- Test representative MP4/H.264/AAC and variable-frame-rate inputs.
- Integrate `media.probe` into one real application workflow before promotion to `validated`.
- Implement `media.clip` as the second capability using ffmpeg.
- Reuse the `media.probe` contract shape where evidence supports it, but extract shared code only after actual duplication appears.
- Then implement `media.extract_audio`, `media.transcribe`, and `media.download` unless real project evidence changes the sequence.

## Key Decisions And Constraints

- Do not duplicate evolving system logic into ad hoc files when the repository standards already define it.
- `Existing Solution First` applies before inventing new central mechanisms or capability providers.
- `PROJECT.md` is the canonical local project entrypoint for GitHub-backed and file-executed projects.
- `PROJECT_INDEX.md` remains an index and must not replace the role of `PROJECT.md`.
- Local Git is the default bootstrap for real project folders; GitHub, Notion, and Google Drive are attached only when they are actually needed.
- Active projects must maintain `PROJECT_STATE.md` and `logs/latest.md` after meaningful changes.
- Harness engineering is the architecture wrapper for reusable agents; `AGENT_QUALITY_SCORECARD_STANDARD.md` measures the resulting workflow after the scaffold is explicit.
- `blocks/<domain>/` stores reusable domain knowledge and decision guidance.
- Executable capability blocks perform one bounded technical operation behind stable contracts.
- Workflows compose capability blocks; applications own project-specific business logic and UI.
- Package-first is the default. Do not create a microservice for every block without evidence that an in-process package is insufficient.
- Do not call a capability reusable merely because a specification exists. Registry status must reflect actual code and validation evidence.
- `candidate` means implementation and minimum tests exist; it does not mean real application validation is complete.
- Do not extract a common capability SDK from one implementation alone.

## Read Next

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT_STATE.md`
4. `logs/latest.md`
5. `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md` for reusable executable functionality
6. `capability-library/REGISTRY.md` for current implementation readiness
7. `capabilities/media-probe/BLOCK.md` and `capabilities/media-probe/VALIDATION.md` for the first candidate
8. `PROJECT_INDEX.md` only when broader navigation is needed
9. routed standards only when the active task requires them
