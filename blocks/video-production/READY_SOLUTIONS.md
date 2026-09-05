# Video Production Ready Solutions

## Purpose

Preserve maintained tools, frameworks, and donor paths so future agents check proven video-production solutions before inventing custom pipelines.

## Core Rule

Use existing tools for downloading, transcoding, transcription, captioning, editing, and AI generation before building custom replacements.

## Source Import / Download

### yt-dlp

Use for:

- downloading supported online media where rights and platform rules allow;
- selecting formats;
- downloading sections;
- obtaining metadata;
- subtitle retrieval when available.

### Direct Upload / Local Import

Use when:

- source files are owned locally;
- platform download is unnecessary;
- copyright control is clearer.

## Video Processing

### ffmpeg

Use for:

- cutting clips;
- transcoding;
- resizing;
- aspect-ratio conversion;
- audio extraction;
- subtitle burn-in;
- batch processing;
- concatenation;
- normalization.

### CapCut Desktop

Use for:

- manual review;
- fast desktop editing;
- captions;
- templates;
- polish;
- owner-friendly editing workflows.

### Remotion

Use when:

- videos should be generated programmatically from React code;
- template-driven rendering matters;
- automation and version control matter.

### MoviePy

Use when:

- Python-based composition or experiments are useful;
- lightweight scripted editing is enough.

## Transcription / Captions

### Whisper Transcribe AI — connected ChatGPT integration

Use as an Existing-Solution-First connected path when:

- a YouTube URL needs to be turned into transcript text for research or analysis;
- direct YouTube transcript access is unavailable, blocked, or throttled;
- an uploaded audio/video file needs convenient external transcription;
- timestamped transcript/subtitle data is useful inside the ChatGPT workflow.

Verified on 2026-09-05:

- connected provider accepted a YouTube URL directly;
- job processing and completed-result retrieval worked;
- returned transcript text, paragraph timestamps, subtitle entries, language field, and media duration.

Validation boundary:

- first test reported a 558-second video but returned transcript coverage only to about 60 seconds;
- always compare transcript coverage against media duration before treating the transcript as complete;
- do not summarize a partial transcript as if it represented the entire source.

Canonical integration note:

`docs/integrations/whisper-transcribe-ai/README.md`

### Whisper / Faster-Whisper

Use for:

- transcription;
- subtitles;
- language detection;
- timestamped text;
- local/private processing;
- full-control or batch workflows where a connected SaaS path is insufficient.

### Platform Captions

Use when platform-native captions are sufficient and review is manual.

## AI Voice

Evaluate:

- ElevenLabs;
- OpenAI TTS;
- cloud-provider TTS;
- local TTS when privacy or cost matters.

## AI Video / Visual Generation

Evaluate when appropriate:

- text-to-video tools;
- image-to-video tools;
- AI avatar tools;
- image generation tools;
- stock footage libraries.

## Workflow / Automation

Evaluate:

- Python scripts;
- Node.js scripts;
- n8n;
- Make;
- GitHub Actions for controlled batch jobs;
- local desktop queue tools;
- cloud render workers.

## Donor Evaluation Checklist

Before accepting a donor repo or automation:

- last meaningful update is recent;
- supported formats are clear;
- local setup is documented;
- licenses are compatible;
- source-rights assumptions are explicit;
- API secrets are not embedded;
- output quality can be reviewed;
- batch failure handling exists;
- platform-specific assumptions are documented.

## Final Rule

Do not build a custom video tool until yt-dlp, ffmpeg, connected transcription providers, local transcription tooling, template rendering, and automation platforms have been considered.
