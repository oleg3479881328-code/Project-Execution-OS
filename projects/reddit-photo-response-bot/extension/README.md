# WedditNYC Photo Lead Review — Chrome Extension MVP

Internal Manifest V3 extension that classifies visible posts on `r/WedditNYC` and stores owner review decisions locally.

## Current scope

- Runs only on `www.reddit.com/r/WedditNYC/*` and `old.reddit.com/r/WedditNYC/*`.
- Detects loaded post cards, including newly inserted infinite-scroll items.
- Applies a deterministic local classifier.
- Supports manual relevance override and owner decisions.
- Stores state in `chrome.storage.local`.
- Provides a popup with saved posts and source links.
- Does not call an external backend.
- Cannot generate or publish Reddit comments.

## Stack decision

Selected: `WXT + TypeScript + React + Manifest V3`.

Why:

- WXT is the Project Execution OS default for serious extensions.
- The official WXT React template supplies the current project structure and build conventions.
- The product is expected to grow into a richer operator interface.
- Permissions stay narrow despite using a product-grade framework.

Alternatives considered:

- Plasmo: strong React option, but no advantage for this bounded MVP.
- CRXJS: good Vite-first option, but WXT has a more complete extension workflow.
- Extension.js: useful for zero-config work, but WXT better matches the planned growth path.
- Minimal MV3 starter: smallest initial code, but weaker long-term handoff and testing structure.

## Local development

Requirements: Node.js 20+ and npm.

```bash
npm install
npm run check
npm run dev
```

WXT opens a development browser automatically. For a production unpacked build:

```bash
npm run build
```

Load `.output/chrome-mv3/` from `chrome://extensions` with Developer mode enabled.

## Manual validation

1. Load the unpacked build.
2. Open `https://www.reddit.com/r/WedditNYC/new/`.
3. Confirm visible posts receive one control panel each.
4. Scroll and confirm newly loaded posts are processed without duplicate controls.
5. Change a relevance label and an owner decision.
6. Reload the page and open the extension popup; confirm decisions persist.
7. Confirm no comment/reply action exists.

## Known boundary

This version works only while a matching Reddit page is open. DOM selectors may need maintenance when Reddit changes its markup.
