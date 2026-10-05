# web.capture_structure

Status: `candidate 0.1.0`

## Purpose

Capture **only the runtime structure of the currently open web page** as compact normalized JSON.

This block is intentionally separate from Universal Site Fingerprint. It does not download assets, take screenshots, sample motion, crawl a site, create a ZIP, or infer a target-editor recipe.

Operator goal:

```text
CURRENT OPEN PAGE
→ one structure capture
→ one compact JSON
```

## Existing Solution First

Core providers are existing browser primitives, not a custom browser engine:

1. Preferred: Playwright `BrowserContext.newCDPSession(page)` + Chrome DevTools Protocol `DOMSnapshot.captureSnapshot`.
2. Fallback: Playwright `page.evaluate()` DOM walk when CDP sessions are unavailable in the current browser bridge.

The block adds only the missing PEOS contract + normalization + compact style deduplication.

## Block Contract

Input:
- a live Playwright-compatible `page` object already attached to the intended tab;
- optional capture settings.

Output schema: `peos.web_structure.v1`.

Output includes:
- source URL/title;
- viewport/document dimensions and scroll state;
- document/iframe structure when CDP exposes it;
- element and meaningful text nodes;
- parent relationships;
- selected semantic attributes;
- current image source reference when available (reference only; no download);
- absolute layout bounds;
- selected computed styles through a deduplicated style table;
- paint order / stacking-context evidence when CDP exposes it;
- provider and run statistics.

## Explicit Non-Scope

Not included:
- image/font/media downloads;
- screenshots;
- motion/animation samples;
- network archive/HAR;
- link graph normalization;
- multi-viewport sweep;
- crawl across multiple pages;
- ZIP packaging;
- Universal Page Recipe generation;
- Showit/Wix/editor actions.

Those remain separate capabilities/workflows.

## Providers

### `cdp-dom-snapshot` — preferred

Uses one Chrome DevTools Protocol snapshot request with a bounded computed-style whitelist.

Benefits:
- DOM + layout + styles from the browser runtime;
- shadow DOM flattened by the protocol;
- document snapshot support for frames;
- paint-order evidence;
- less JavaScript walking in page context.

### `dom-evaluate-fallback`

Used automatically only when CDP session creation/capture is unavailable.

Known limitation: it cannot fully flatten closed shadow roots or cross-origin frame contents.

## Dramaturg Operator Adapter

Canonical generated one-block script:

`adapters/dramaturg-one-block.js`

Usage:
1. Attach Dramaturg to the exact page/tab to capture.
2. Open JS mode / Script Editor.
3. Run the complete file as one block.
4. Expected result: one downloaded `page-structure-<host>-<timestamp>.json` plus a compact success object in Dramaturg.

The adapter does not navigate and does not mutate page content except for a temporary hidden download anchor that is removed immediately.

## Node / CLI Adapter

When a normal Playwright package is available:

```bash
peos-web-capture-structure --endpoint http://localhost:9222 -o page-structure.json
```

The CLI attaches to an existing Chromium browser through CDP; it does not create a crawler.

## Acceptance

Candidate acceptance:
- core unit tests pass;
- contract shape test passes;
- fallback smoke test passes;
- generated Dramaturg adapter matches current core source;
- live owner Dramaturg run remains the validation gate before promotion to `validated`.

## Safety / Permissions

- Read-only against the target page state.
- No credentials are copied from storage/cookies.
- No page navigation.
- No asset download.
- No external publication.
- Output may contain text/URLs/attributes visible to the authenticated page; treat the JSON according to the source page's sensitivity.

## Versioning

`0.1.0` establishes schema `peos.web_structure.v1`.
