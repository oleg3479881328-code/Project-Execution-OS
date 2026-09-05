# YouTube Ready Solutions

## Purpose

Preserve official platform surfaces and proven tool paths so agents reuse existing YouTube capabilities before inventing custom infrastructure.

## Official YouTube Surfaces

Use official YouTube and Google documentation first for:

- channel creation and management;
- YouTube Studio;
- YouTube Partner Program;
- Shorts monetization;
- channel monetization policies;
- copyright and Content ID;
- YouTube Data API;
- video uploads;
- playlists;
- analytics.

## Reusable Tool Paths

### Manual Channel Operations

Use YouTube Studio for:

- initial publishing;
- monetization setup;
- channel settings;
- thumbnail review;
- analytics review;
- rights/problem handling.

### Research / Transcript Intake

For analysis of a YouTube video:

1. use platform/native transcript or captions when readily accessible;
2. if normal transcript access is unavailable, blocked, or throttled, use the connected `Whisper Transcribe AI` integration on the YouTube URL;
3. compare transcript timestamps/coverage against the reported video duration;
4. if coverage is incomplete and full-video analysis matters, escalate to another approved transcription path such as local/media-file Whisper or Faster-Whisper where source access and rights permit;
5. only treat the transcript as evidence for the entire video after coverage is verified.

Canonical integration note:

`docs/integrations/whisper-transcribe-ai/README.md`

Do not build a custom YouTube transcript scraper merely because direct web transcript access fails before checking the connected transcription path.

### Platform-Neutral Production

Use `blocks/video-production/` for:

- yt-dlp where permitted;
- ffmpeg;
- CapCut;
- transcription;
- AI voice;
- multilingual rendering;
- video-factory automation.

### API Automation

Use YouTube Data API when:

- metadata management repeats;
- playlist operations repeat;
- approved upload workflows repeat;
- internal channel dashboards are needed;
- multi-channel operations need controlled tooling.

### Analytics

Use YouTube Studio analytics first for human review.

Add internal analytics storage when comparing:

- channels;
- languages;
- niches;
- templates;
- affiliate performance;
- production cost;
- revenue.

## Donor Review

Before inventing a channel format, review:

- direct niche competitors;
- successful analogue channels;
- Shorts formats;
- long-form formats;
- title patterns;
- thumbnail patterns;
- playlist structure;
- monetization path;
- originality/value-add.

## Final Rule

Use YouTube Studio and official APIs as the platform foundation. Reuse connected transcript intake for video research before inventing custom extraction, keep production tooling in Video Production Block, and avoid duplicating it here.
