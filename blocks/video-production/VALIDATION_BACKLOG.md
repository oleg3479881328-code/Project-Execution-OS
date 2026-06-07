# Video Production Validation Backlog

## Purpose

Track what must be validated before Video Production Block recommendations are treated as proven operational workflows.

## Status

`candidate`

The block includes researched tooling and owner-tested elements, but end-to-end automation still requires validation.

## Local Pipeline Validation

- Validate yt-dlp permitted-source download flow.
- Validate ffmpeg clip extraction.
- Validate MP4 H.264/AAC export.
- Validate vertical 9:16 conversion.
- Validate batch folder processing.
- Validate PowerShell-friendly command packaging.

## CapCut Validation

- Validate reusable project template.
- Validate caption style preset.
- Validate export preset.
- Validate manual-review handoff after automated preprocessing.

## Transcript / Caption Validation

- Validate source-subtitle retrieval.
- Validate Whisper transcription.
- Validate faster-whisper transcription.
- Validate caption timing cleanup.
- Validate multilingual subtitle generation.

## AI Stack Validation

- Validate TTS generation.
- Validate multilingual voice output.
- Validate AI clip-suggestion ranking.
- Validate AI visual generation for original content.
- Validate avatar workflow only where useful.

## Factory Validation

- Validate one long video to multiple shorts.
- Validate one master to multiple languages.
- Validate gadget affiliate pipeline.
- Validate facts/cinema pipeline.
- Validate QuizLight video-card pipeline.
- Validate publish-package builder.
- Validate analytics feedback loop.

## SaaS / Automation Validation

- Validate local script MVP.
- Validate queue-based processing.
- Validate retry logging.
- Validate review-gate status.
- Validate output storage and naming.
- Validate rights-note storage.

## Known Unvalidated Assumptions

- yt-dlp + ffmpeg + CapCut is the best local baseline for the owner.
- Whisper/faster-whisper is sufficient for transcript-first automation.
- multilingual TTS quality is good enough for scalable reels after language QA.
- publish packages should precede full autopublishing.
- QuizLight video-card extraction can reuse the same transcript/timestamp pipeline.

## Final Rule

Do not mark this block active until at least one complete factory pipeline is validated from source intake through reviewed export and analytics capture.