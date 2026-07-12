# Implementation Handoff

## What is already complete

- Manifest V3 WXT project;
- React Chrome side panel;
- user-triggered profile scan;
- controlled automatic scrolling;
- selected fetch/XHR response observation;
- embedded JSON and DOM fallback collection;
- per-profile deduplication;
- local persistence;
- views/day, engagement, and outlier analytics;
- text and outlier filters;
- CSV and JSON export;
- unit tests and successful production build.

## Executor task

Perform real Chrome validation against public TikTok profiles and harden only the TikTok adapter where evidence shows a failure.

Do not redesign the product or expand permissions during this task.

## Setup

```bash
git checkout agent/tiktok-research-sorter-mvp
cd projects/tiktok-research-sorter
npm install
npm run check
npm test
npm run build
```

Load this folder through `chrome://extensions`:

```text
projects/tiktok-research-sorter/.output/chrome-mv3
```

Use Developer mode and `Load unpacked`.

Because the GitHub connector could not upload the locally generated lock file, commit the generated `package-lock.json` after confirming installation and checks.

## Browser test matrix

Test at minimum:

1. public profile with fewer than 50 videos;
2. public profile with several hundred videos;
3. profile while logged out of TikTok;
4. profile while logged in;
5. a second scan of an already stored profile;
6. stop button during active scanning;
7. CSV export with Cyrillic and emoji descriptions;
8. JSON export;
9. text and hashtag search;
10. Outlier Score filter;
11. TikTok challenge/CAPTCHA condition if it occurs naturally.

Do not try to trigger, bypass, automate, or solve CAPTCHA.

## Expected acceptance criteria

- toolbar action opens the side panel;
- scan starts only after user action;
- the page scrolls in controlled increments;
- already collected records survive side-panel closing;
- video IDs are not duplicated;
- profile A data never changes profile B's median or Outlier Score;
- richer API records replace DOM-only placeholders;
- stop halts further scrolling;
- a challenge stops the scan and displays a clear message;
- CSV opens correctly in Excel with UTF-8 text;
- no cookies, tokens, request headers, or private data are stored.

## Failure evidence

When parsing fails:

1. identify the exact response responsible for a new page of profile posts;
2. save only the JSON response body;
3. remove usernames, descriptions, URLs, tokens, signatures, device identifiers, and any personal data not needed for field-shape testing;
4. place the sanitized fixture under `tests/fixtures/`;
5. add a regression test before changing the parser;
6. update the adapter with the smallest compatible change.

Never commit cookies, authorization headers, query signatures, browser profiles, HAR files, or raw personal account data.

## Known boundaries

- TikTok markup and payload fields can change without notice.
- DOM collection can usually provide links, covers, and views, but richer metrics depend on structured payload availability.
- `chrome.storage.local` is adequate for the MVP; migrate to IndexedDB only after measured storage pressure or history-snapshot requirements justify it.
- Public Chrome Web Store submission requires a fresh policy and TikTok terms review.

## Completion report

The executor should return:

- Chrome version and operating system;
- profiles tested, described by size only rather than personal identity;
- pass/fail result for every test-matrix item;
- screenshots of the extension UI without personal data;
- sanitized fixtures added;
- files changed;
- commands and checks run;
- remaining blockers;
- recommendation: merge, revise, or stop.
