# Capability Block Registry

## Purpose

This registry is the source of truth for reusable executable capabilities recognized by `Project Execution OS`.

A row records architectural intent and implementation status. It must not imply that code exists when status is only `idea`.

## Status Definitions

- `idea` — need and contract direction recorded; implementation not yet created.
- `candidate` — implementation exists and minimum tests pass.
- `validated` — integrated successfully into at least one real application workflow.
- `production` — operational evidence, regression protection, and maintenance ownership exist.
- `deprecated` — replacement exists or new use is discouraged.
- `retired` — no longer supported.

## Registry

| Block ID | Status | Version | Implementation location | Initial providers | Inputs | Outputs | Validation targets | Known limitations |
|---|---|---:|---|---|---|---|---|---|
| `media.download` | idea | — | not created | yt-dlp, direct HTTP | authorized source descriptor | video/audio artifact | short-video workflow, QuizLight | rights and platform restrictions must remain explicit |
| `media.probe` | candidate | 0.1.0 | `capabilities/media-probe/` | ffprobe | one local media artifact | original artifact enriched with normalized probe metadata | short-video workflow, QuizLight | automated Windows and Block Studio integration passed; owner target-machine confirmation still required |
| `media.extract_audio` | idea | — | not created | ffmpeg | video/audio artifact | normalized audio artifact | transcription workflows | codec and channel normalization policy not yet validated |
| `media.transcribe` | idea | — | not created | whisper.cpp, faster-whisper, optional cloud adapter | audio/video artifact | transcript artifact with segments and timestamps | short-video workflow, QuizLight | provider selection and hardware benchmarks not yet validated |
| `media.clip` | idea | — | not created | ffmpeg | media artifact plus time ranges | one or more clip artifacts | Reels factory, QuizLight phrase clips | exact-cut versus stream-copy behavior needs fixtures |
| `media.generate_captions` | idea | — | not created | transcript formatter, ffmpeg/libass optional | transcript artifact | SRT/VTT/ASS caption artifacts | short-video workflow | styling contract not yet defined |
| `media.render_vertical` | idea | — | not created | ffmpeg | media, captions, layout parameters | vertical video artifact | Reels/Shorts/TikTok factory | layout presets not yet defined |

## Implementation Sequence

```text
1. media.probe          candidate 0.1.0
2. media.clip           next
3. media.extract_audio
4. media.transcribe
5. media.download
```

Reasoning:

- begin with deterministic local ffmpeg/ffprobe operations;
- establish artifact and result contracts before network and model-provider complexity;
- validate composition locally;
- add download permissions and transcription provider routing after the core media contract is stable.

## Candidate Evidence — media.probe 0.1.0

Implementation:

```text
capabilities/media-probe/
```

Manifest:

```text
capabilities/media-probe/manifest.yaml
```

Package entry points:

```text
project_execution_os.capabilities -> media_probe
peos-media-probe CLI
```

Local verification on 2026-07-15:

```text
Python 3.13.5
pytest 9.0.2
ffprobe 7.1.3
6 tests passed
manual CLI smoke test passed on generated WAV input
```

Application integration evidence:

```text
apps/block-studio/
real upload endpoint execution passed
real H.264/AAC MP4 smoke test passed
preview and temporary execution cleanup passed
GitHub Actions passed on Ubuntu and Windows with Python 3.13
```

Durable evidence:

```text
capabilities/media-probe/VALIDATION.md
apps/block-studio/VALIDATION.md
.github/workflows/media-probe-tests.yml
.github/workflows/block-studio-tests.yml
```

Promotion boundary:

`media.probe` remains `candidate`, not `validated`, until the owner runs Block Studio on the target Windows computer with a real user-owned media file and confirms the result.

## Promotion Evidence

Before promoting any entry from `idea` to `candidate`, record:

- implementation path;
- package version;
- manifest;
- contract tests;
- smoke-test command and result;
- known limitations.

Before promoting from `candidate` to `validated`, record:

- application and workflow used;
- representative input;
- produced artifact evidence;
- integration problems discovered;
- contract changes required;
- version used.

## Final Rule

The registry reports reality, not aspiration.

Do not mark a block ready until executable code and verification evidence exist.
