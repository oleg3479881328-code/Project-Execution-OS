# Video Production Tool Selection Matrix

## Purpose

Choose the smallest reliable video-production stack for the active workflow.

## Matrix

| Situation | Recommended Path | Why |
|---|---|---|
| Manual prototype | CapCut Desktop | Fastest owner-facing validation path. |
| Download and cut clips | yt-dlp + ffmpeg | Reliable command-line baseline. |
| Long video to short clips | yt-dlp/local import + transcript + ffmpeg + review UI | Supports repeatable clipping. |
| Multilingual reels | master script + translation + TTS + ffmpeg/CapCut batch exports | Separates content from localization. |
| Programmatic template videos | Remotion | Good when code-driven rendering matters. |
| Python experiment | MoviePy + ffmpeg | Good for lightweight scripting. |
| High-volume SaaS | upload/import + queue + workers + ffmpeg + AI services + storage | Supports scale and retries. |
| QuizLight video cards | transcript + timestamp selector + clip extraction + card generator | Matches educational workflow. |

## Source Handling Choices

Use:

- local import when files are owned;
- yt-dlp when source download is allowed;
- platform export APIs when available and appropriate;
- direct upload for public SaaS products.

## Editing Choices

Use:

- CapCut for manual validation and polish;
- ffmpeg for deterministic processing;
- Remotion for template-driven rendering;
- MoviePy for quick Python experiments.

## Caption Choices

Use:

- source subtitles when available and accurate;
- Whisper/Faster-Whisper for automatic transcription;
- manual correction for publish-quality output.

## Voice Choices

Use:

- ElevenLabs or similar premium TTS for polished content;
- lower-cost or local TTS for testing;
- human review before publishing.

## Automation Choices

Use:

- scripts for local MVP;
- queue/workers for SaaS scale;
- n8n or Make for orchestration around external tools;
- desktop presets when the owner needs direct control.

## Final Rule

Start with the smallest toolchain that proves the pipeline. Add cloud scale only after local workflow quality is validated.