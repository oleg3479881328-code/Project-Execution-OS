# WedditNYC Photo Lead Review — Chrome Side Panel MVP

Internal Manifest V3 extension that detects visible posts on `r/WedditNYC`, classifies them locally, and provides the complete review workflow inside Chrome's side panel.

## Current scope

- Runs only on `www.reddit.com/r/WedditNYC/*` and `old.reddit.com/r/WedditNYC/*`.
- Detects loaded post cards, including newly inserted infinite-scroll items.
- Applies a deterministic local classifier.
- Stores detected posts and owner decisions in `chrome.storage.local`.
- Uses a persistent Chrome side panel as the only operator interface.
- Supports filters, manual classification changes, `Relevant`, `Irrelevant`, `Hide`, and source-post opening.
- Does not inject review controls into Reddit post cards.
- Does not call an external backend.
- Cannot generate or publish Reddit comments.

## Side panel behavior

- Click the extension toolbar icon to open or close the panel.
- The panel stays beside the active webpage instead of appearing as a small popup.
- Open `r/WedditNYC/new` from the panel or navigate there normally.
- Visible Reddit posts are captured by the content script and appear in the panel automatically.
- Changes made in the panel persist after reload.

## Stack decision

Selected: `WXT + TypeScript + React + Manifest V3`.

Why:

- WXT is the Project Execution OS default for serious extensions.
- WXT supports a native `sidepanel` entrypoint.
- Chrome's Side Panel API provides the persistent operator workspace requested for this project.
- The product is expected to grow into a richer review and response interface.
- Permissions remain narrow despite using a product-grade framework.

Alternatives considered:

- Plasmo: strong React option, but no advantage for this bounded MVP.
- CRXJS: good Vite-first option, but WXT has a more complete extension workflow.
- Extension.js: useful for zero-config work, but WXT better matches the planned growth path.
- Minimal MV3 starter: smallest initial code, but weaker long-term handoff and testing structure.

## Permissions

- `storage` — saves detected posts, classifications, and owner decisions locally.
- `sidePanel` — hosts the operator interface beside Reddit.
- Host access is limited to the two `r/WedditNYC` URL patterns.

No browsing-history permission, broad Reddit permission, external AI key, or server secret is included.

## Local development

Requirements: Chrome 114+, Node.js 20+, and npm.

```bash
npm install
npm run check
npm run dev
```

For a production unpacked build:

```bash
npm run build
```

Load `.output/chrome-mv3/` from `chrome://extensions` with Developer mode enabled.

## Manual validation

1. Build and load the unpacked extension.
2. Pin the extension icon if desired.
3. Click the extension icon and confirm the side panel opens.
4. Open `https://www.reddit.com/r/WedditNYC/new/`.
5. Confirm visible posts appear in the side panel.
6. Scroll and confirm newly loaded posts appear without duplicates.
7. Change a classification and owner decision in the side panel.
8. Reload Reddit and confirm decisions persist.
9. Confirm the extension does not add controls to Reddit cards.
10. Confirm no comment or reply action exists.

## Known boundary

This version detects posts only while a matching Reddit page is open. Reddit DOM changes may require parser maintenance. Real Chrome validation is still required before the draft PR is ready to merge.
