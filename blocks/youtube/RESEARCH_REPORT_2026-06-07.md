# YouTube Research Report — 2026-06-07

## Purpose

Capture the initial research and owner-context pass behind `blocks/youtube/`.

## Artifact Decision

Classification: `full block`

Reason:

YouTube is a recurring cross-project platform domain with distinct channel strategy, Shorts and long-form roles, monetization, copyright/reused-content rules, analytics, API automation, playlists, uploads, and channel operations.

It should not be reduced to a section inside Video Production Block. Production tooling is platform-neutral; YouTube Block is the platform-specific operating layer.

## Domain Boundary

This block covers:

- channel strategy;
- YouTube Shorts;
- long-form videos;
- hybrid content systems;
- originality and copyright review;
- monetization;
- analytics;
- YouTube Data API automation;
- upload and playlist workflows;
- channel operations;
- multilingual channel networks;
- QuizLight YouTube workflows.

It does not cover platform-neutral editing pipelines, which belong in `blocks/video-production/`.

## Official Research Findings

1. YouTube Partner Program eligibility requires policy compliance and channel review; meeting numeric thresholds does not guarantee acceptance.
2. Higher-threshold YPP ad-revenue eligibility can be reached through either long-form watch hours or Shorts views.
3. YouTube monetization policies evaluate original/authentic value and warn against reused, repetitive, or mass-produced content without meaningful added value.
4. YouTube Data API provides official surfaces for channel/video/playlist workflows, and Google documents video upload flows.
5. Shorts and long-form should be treated as different formats with different jobs inside one channel strategy.

## Owner-Specific Reuse

This block directly supports:

- YouTube Shorts testing;
- anonymous original voiceover content;
- gadget/affiliate channels;
- cinema/facts channels;
- multilingual networks;
- YouTube video factory automation;
- QuizLight language-learning extraction;
- SaaS/product acquisition channels.

## Relationship To Video Production Block

`blocks/youtube/` owns:

- platform strategy;
- channel operations;
- monetization;
- copyright/reuse review;
- analytics;
- API/upload workflows.

`blocks/video-production/` owns:

- clipping;
- rendering;
- yt-dlp where permitted;
- ffmpeg;
- CapCut;
- captions;
- AI voice/avatar;
- multilingual production pipelines.

## Files Created

- `BLOCK.md`
- `PRODUCT_SURFACES.md`
- `READY_SOLUTIONS.md`
- `CHANNEL_STRATEGY.md`
- `SHORTS_AND_LONG_FORM.md`
- `CONTENT_AND_COPYRIGHT.md`
- `MONETIZATION.md`
- `ANALYTICS_AND_EXPERIMENTS.md`
- `AUTOMATION_AND_API.md`
- `PLATFORM_OPERATIONS.md`
- `IMPLEMENTATION_HANDOFF.md`
- `REFERENCES.md`
- `VALIDATION_BACKLOG.md`
- `RESEARCH_REPORT_2026-06-07.md`

## Final Recommendation

Register `blocks/youtube/` as a candidate full domain block and validate it first on a Shorts-first channel with original voiceover, a measurable monetization path, and a controlled publish-package workflow.