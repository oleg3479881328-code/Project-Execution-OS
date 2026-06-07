# YouTube Block V2 Upgrade Notes — 2026-06-07

## Purpose

Record the V2 expansion of `blocks/youtube/`.

## Added

- `PUBLISHING_AND_METADATA.md`
- `MULTILINGUAL_SCALING.md`
- `CURRENT_PLATFORM_SNAPSHOT_2026-06-07.md`

## Updated

- `BLOCK.md`
- `REFERENCES.md`
- `VALIDATION_BACKLOG.md`
- `blocks/PROJECT_INDEX.md`

## Result

YouTube Block now separates:

- platform strategy and channel operations;
- production work delegated to `blocks/video-production/`;
- publishing packages and metadata;
- multilingual scaling;
- current freshness-sensitive platform notes;
- validation tasks before broad automation.

## Final Rule

Use YouTube Block for YouTube-specific work and Video Production Block for platform-neutral video creation workflows.