# TikTok Research Sorter v0.5.0 — channel profile export

## Objective

Extend Favorites and generated HTML so every selected video carries the fullest public channel information TikTok actually exposes.

## Required channel fields

- username and profile URL;
- display name, avatar, biography, verification, website;
- public user ID and secUid when available;
- followers, following, friends, total profile likes, public video count;
- region, language, private-account flag, commerce-account flag when available;
- locally collected video count, median views, average engagement, strongest hashtags;
- profile data source and collection/update timestamps.

## Behavior

- favorites preserve a durable channel snapshot independent from later profile/tag deletion;
- favorites are automatically refreshed when richer profile data is collected later;
- adding a favorite requests public profile enrichment from the current TikTok tab without changing the visible page;
- Favorites UI groups cards by channel and shows channel statistics;
- selected HTML export groups videos by channel and renders a complete channel card before that channel's selected videos;
- missing public fields are shown as unavailable rather than invented;
- exported text remains escaped and external URLs remain HTTP(S)-only.

## Version

All extension metadata, exports, CI artifacts, docs, and logs use `0.5.0`.
