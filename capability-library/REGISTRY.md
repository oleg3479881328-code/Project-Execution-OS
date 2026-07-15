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
| `media.probe` | idea | — | not created | ffprobe | media artifact | normalized media metadata | short-video workflow, QuizLight | depends on ffprobe availability |
| `media.extract_audio` | idea | — | not created | ffmpeg | video/audio artifact | normalized audio artifact | transcription workflows | codec and channel normalization policy not yet validated |
| `media.transcribe` | idea | — | not created | whisper.cpp, faster-whisper, optional cloud adapter | audio/video artifact | transcript artifact with segments and timestamps | short-video workflow, QuizLight | provider selection and hardware benchmarks not yet validated |
| `media.clip` | idea | — | not created | ffmpeg | media artifact plus time ranges | one or more clip artifacts | Reels factory, QuizLight phrase clips | exact-cut versus stream-copy behavior needs fixtures |
| `media.generate_captions` | idea | — | not created | transcript formatter, ffmpeg/libass optional | transcript artifact | SRT/VTT/ASS caption artifacts | short-video workflow | styling contract not yet defined |
| `media.render_vertical` | idea | — | not created | ffmpeg | media, captions, layout parameters | vertical video artifact | Reels/Shorts/TikTok factory | layout presets not yet defined |

## First Implementation Order

```text
1. media.probe
2. media.clip
3. media.extract_audio
4. media.transcribe
5. media.download
```

Reasoning:

- begin with deterministic local ffmpeg/ffprobe operations;
- establish artifact and result contracts before network and model-provider complexity;
- validate composition locally;
- add download permissions and transcription provider routing after the core media contract is stable.

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