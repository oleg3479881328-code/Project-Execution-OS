# yt-dlp and ffmpeg

## Purpose

Provide reusable guidance for rights-aware media import and deterministic video processing.

## Core Rule

Use yt-dlp only where downloading is permitted by rights and platform rules. Use ffmpeg for reproducible processing.

## Owner Context

The owner has previously used:

- `C:\yt-dlp` as a working folder;
- `yt-dlp` for section downloads;
- static ffmpeg builds;
- MP4 output for desktop editing;
- PowerShell copy-ready commands.

Keep project-specific command variants in project docs. Keep reusable patterns here.

## yt-dlp Uses

Use for:

- downloading permitted source media;
- selecting format combinations;
- downloading time sections;
- extracting metadata;
- retrieving subtitles when available;
- preparing local source files for processing.

## ffmpeg Uses

Use for:

- cutting clips;
- transcoding to MP4;
- resizing to vertical formats;
- extracting audio;
- normalizing loudness;
- burning captions;
- concatenating segments;
- generating thumbnails;
- batch processing.

## Common Processing Decisions

Define before running:

- input source;
- clip start/end;
- output aspect ratio;
- output resolution;
- video codec;
- audio codec;
- caption mode;
- target platform;
- output filename;
- rights note.

## Vertical Export Baseline

Typical short-form target:

- aspect ratio: 9:16;
- resolution: 1080x1920 when source quality allows;
- codec: H.264;
- audio: AAC;
- captions placed within mobile-safe zones.

## Batch Safety

For automation:

- write outputs to a separate folder;
- preserve original source;
- log command, input, output, and status;
- skip or flag failed jobs;
- do not overwrite reviewed exports silently.

## Final Rule

Use command-line tools for deterministic processing, then review output visually before publishing.