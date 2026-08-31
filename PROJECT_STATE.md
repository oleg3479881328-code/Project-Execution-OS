---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-08-30
source_of_truth: repository
active_branch: codex/issue-132-archify-pilot
---

# PROJECT_STATE.md

## Current Task

Issue #132 — bounded upstream Archify pilot. Artifacts generated and validated in the isolated review branch; owner visual review remains pending.

## Current State

`Project Execution OS` is active and transfer-ready.

The repository now contains all four intended layers:

```text
domain knowledge
-> executable capability
-> workflow / application adapter
-> owner-facing UI
```

## Latest Confirmed Milestone

`Block Studio 0.1.0` was implemented and merged as the first local visual application for capability blocks.

```text
Application: apps/block-studio/
Windows launcher: START_BLOCK_STUDIO.bat
PR: https://github.com/oleg3479881328-code/Project-Execution-OS/pull/90
Merge SHA: d70fbb1be0d419b3dcc5b47a9d3dc107a9551069
Status: candidate
```

The first interactive capability is:

```text
media.probe 0.1.0 — candidate
```

Owner-visible behavior:

- registry-driven block library;
- drag-and-drop video/audio selection;
- local browser preview;
- normalized duration, dimensions, formats, codecs, FPS, audio, and stream data;
- owner and developer modes;
- raw JSON, logs, contract, tests, and usage views;
- local runtime storage and explicit cleanup.

## Verification Evidence

```text
Local pytest: 5 passed
JavaScript syntax: passed
Real local H.264/AAC MP4 API test: passed
Ubuntu / Python 3.13 / ffprobe: passed
Windows / Python 3.13 / ffprobe: passed
Project OS integrity workflow: passed
```

The automated Windows run confirms package installation, ffprobe availability, file upload, capability execution, preview retrieval, and cleanup.

## Architecture Decision

Applications may present and compose capabilities, but must not copy provider implementation logic.

```text
apps/block-studio
-> Python entry-point discovery
-> media.probe contract
-> media.probe core
-> ffprobe
```

New capability manifests and registry entries are visible in the Studio library. A block becomes interactive when an application adapter is added.

## Current Focus

- Owner test on the target Windows computer with a real user-owned file.
- Keep Block Studio and `media.probe` at `candidate` until that confirmation is received.
- Build `media.clip` as the second capability and add its interactive Studio page.
- Extract shared SDK code only after real duplication appears between two blocks.

## Current Next Safe Action

```text
1. Open Block Studio on the owner's Windows computer.
2. Load a real MP4.
3. Run media.probe and inspect the visible result.
4. Record success or exact failure.
5. Begin media.clip.
```

## Active Files For Re-entry

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT.md`
4. `PROJECT_STATE.md`
5. `logs/latest.md`
6. `apps/README.md`
7. `apps/block-studio/README.md`
8. `apps/block-studio/VALIDATION.md`
9. `capability-library/REGISTRY.md`
10. `capabilities/media-probe/BLOCK.md`
11. `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`

## Known Blockers

- The owner has not yet run Block Studio on the target Windows computer.
- A real owner-owned media file has not yet been confirmed through the UI.
- Variable-frame-rate media remains an additional edge-case fixture.
- Other media capability entries remain `idea`.

## Do-Not-Break Rules

- Do not claim owner validation without the owner's explicit result.
- Do not copy capability provider code into Block Studio.
- Do not expose Block Studio beyond `127.0.0.1` by default.
- Do not retain temporary owner files after explicit cleanup.
- Do not promote `media.probe` or Block Studio beyond registry evidence.
- Do not extract a common SDK from one block alone.
- Update this file and `logs/latest.md` after every meaningful central-project change.
