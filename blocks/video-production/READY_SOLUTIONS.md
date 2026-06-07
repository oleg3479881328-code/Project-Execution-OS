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

### Whisper / Faster-Whisper

Use for:

- transcription;
- subtitles;
- language detection;
- timestamped text.

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

Do not build a custom video tool until yt-dlp, ffmpeg, transcription tooling, template rendering, and automation platforms have been considered.