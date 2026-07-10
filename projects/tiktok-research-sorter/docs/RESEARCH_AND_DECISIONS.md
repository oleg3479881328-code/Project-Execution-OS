# Research and Decisions

## Product decision

Build a local-first TikTok research extension rather than a visual-only grid sorter.

Primary workflow:

`open public profile -> scan -> normalize metrics -> calculate profile-relative analytics -> filter/sort -> export`

The product value is reliable collection and interpretation, not merely rearranging cards already visible in TikTok's DOM.

## Existing solutions reviewed

- Original reference: https://chromewebstore.google.com/detail/sort-for-tiktok-videos-by/dpfmkbcoaddghkkhebjcjaoaiaefigln
- Feed Sorter for TikTok and Instagram: https://chromewebstore.google.com/detail/bmljpagafjlkebnopbdncpnifkknlobk
- Sort Feed: https://chromewebstore.google.com/detail/sort-feed-works-on-instag/lhiilgfanjkbombmnlfelondlfohfpfg
- DuoSort: https://chromewebstore.google.com/detail/duosort-sort-instagram-po/bmlcnjplnpacanmknkdkjckodafioobp
- Open-source interception pattern: https://github.com/silverbirder/chrome-extensions-tiktok-scraping-downloader

Reusable patterns selected:

- side panel for long-running work;
- automatic scrolling with visible progress;
- CSV export;
- response-payload collection with DOM fallback;
- local-only MVP without account creation.

Custom work justified:

- profile-relative Outlier Score;
- per-profile deduplication and analytics;
- resilient heuristic parsing across several TikTok field variants;
- explicit challenge stop condition;
- Russian research interface.

## Framework decision

Selected stack:

`WXT 0.20.27 + TypeScript 5.8.3 + React 19.2.7 + Manifest V3`

Official WXT documentation:

- https://wxt.dev/guide/installation.html
- https://wxt.dev/guide/essentials/content-scripts.html
- https://wxt.dev/guide/essentials/entrypoints.html

Reasons:

- generated Manifest V3 configuration;
- side panel and content-script entrypoints;
- unlisted MAIN-world page hook;
- TypeScript-first build;
- clear future cross-browser path.

## Architecture decision

Data path:

```text
TikTok page
-> MAIN-world page hook observes selected fetch/XHR JSON responses
-> window.postMessage
-> isolated content script validates and normalizes records
-> background service worker merges per-profile records
-> chrome.storage.local
-> React side panel
```

Fallback collection order:

1. relevant TikTok JSON responses;
2. embedded initial-state JSON;
3. loaded profile DOM cards.

The collector never bypasses login, private accounts, CAPTCHA, rate limits, or other access controls.

## Analytics

Implemented:

```text
Views Per Day = views / age in days
Engagement Rate = (likes + comments + shares) / views * 100
Outlier Score = video views / median profile views
```

Median is used instead of average as the profile baseline because a small number of viral posts can heavily distort the average.

## Permissions

Required:

- `storage` — local profile records and scan state;
- `sidePanel` — persistent research interface;
- `activeTab` — send a user-initiated scan command to the current tab;
- host permission `https://www.tiktok.com/*` — run only on TikTok.

Not requested:

- all-sites access;
- downloads permission;
- cookies;
- identity;
- webRequest;
- external backend access.

## Dependency validation

Validated locally on 2026-07-10:

- Node.js 22.16.0;
- npm 10.9.2;
- TypeScript check passed;
- 5 unit tests passed;
- WXT Chrome MV3 production build passed;
- built extension size: approximately 219 KB;
- ZIP size: approximately 72 KB;
- production dependency audit: zero known vulnerabilities.

The development toolchain currently reports transitive advisories through WXT's browser-runner dependencies. They do not ship in the production extension bundle, but must be reviewed again before public release.

## Deferred scope

Not part of MVP:

- downloading videos or audio;
- watermark removal;
- transcription;
- AI analysis;
- backend accounts;
- cloud sync;
- payments;
- Instagram or Facebook adapters;
- scheduled background crawling.
