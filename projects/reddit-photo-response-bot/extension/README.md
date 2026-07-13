# WedditNYC Photo Lead Review — Chrome Side Panel

Internal Manifest V3 extension that detects visible posts on `r/WedditNYC`, classifies them locally, and provides the complete review workflow inside Chrome's side panel.

## Two-stage classification

### Stage 1 — local rules

Every detected post is immediately classified locally using deterministic phrases and weighted signals. This stage is fast, free, explainable, and requires no external request.

### Stage 2 — DeepSeek semantic analysis

When enabled, local `Strong` and `Possible` candidates can be sent through a secure Cloudflare Worker to DeepSeek for meaning-level review.

The AI result includes:

- final suggested label;
- confidence from 0 to 100;
- customer intent;
- response risk;
- short grounded reason;
- recommended action: respond, review, or skip.

A manual classification always has final priority over both automatic stages.

## Current scope

- Runs only on `www.reddit.com/r/WedditNYC/*` and `old.reddit.com/r/WedditNYC/*`.
- Detects loaded post cards, including newly inserted infinite-scroll items.
- Applies a deterministic local classifier.
- Supports optional per-post or batch DeepSeek analysis.
- Automatic candidate analysis is available but disabled by default.
- Stores detected posts, AI results, settings, and owner decisions in `chrome.storage.local`.
- Uses a persistent Chrome side panel as the only operator interface.
- Supports filters, manual classification changes, `Relevant`, `Irrelevant`, `Hide`, and source-post opening.
- Does not inject review controls into Reddit post cards.
- Cannot generate or publish Reddit comments.

## Secure AI architecture

```text
Chrome side panel
    -> HTTPS Cloudflare Worker
        -> DeepSeek API
```

- The DeepSeek API key exists only as a Cloudflare Worker secret.
- The extension stores only the Worker URL and a separate Worker access key.
- The DeepSeek API key must never be pasted into the extension, chat, GitHub, or source code.
- Chrome requests access only to the exact configured Worker origin.
- Post title/body are sent only when an AI analysis is run.

See `../deepseek-worker/README.md` for deployment.

## Side panel behavior

- Click the extension toolbar icon to open or close the panel.
- The panel stays beside the active webpage instead of appearing as a small popup.
- Open `r/WedditNYC/new` from the panel or navigate there normally.
- Visible Reddit posts are captured by the content script and appear in the panel automatically.
- Changes made in the panel persist after reload.

## Permissions

- `storage` — saves detected posts, classifications, AI settings/results, and owner decisions locally.
- `sidePanel` — hosts the operator interface beside Reddit.
- Required host access is limited to the two `r/WedditNYC` URL patterns.
- Optional HTTPS host access is requested at runtime only for the configured AI Worker origin.

No browsing-history permission, Reddit credentials, DeepSeek key, or server secret is included.

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

## AI setup after Worker deployment

1. Open the side panel.
2. Expand `DeepSeek semantic analysis`.
3. Enable the AI stage.
4. Enter the Worker URL.
5. Enter the separate Worker access key — not the DeepSeek API key.
6. Save and approve Chrome access to that exact Worker origin.
7. Analyze one post or run batch analysis for new local candidates.

## Manual validation

1. Build and load the unpacked extension.
2. Click the extension icon and confirm the side panel opens.
3. Open `https://www.reddit.com/r/WedditNYC/new/`.
4. Confirm visible and infinite-scroll posts appear without duplicates.
5. Confirm local classifications and manual decisions persist.
6. Configure a deployed Worker and analyze one controlled post.
7. Confirm the AI result includes label, confidence, intent, risk, reason, and action.
8. Confirm the Network panel sends the request to the Worker, not directly to DeepSeek.
9. Confirm no DeepSeek API key appears in extension storage, source, or built files.
10. Confirm no comment or reply action exists.

## Known boundary

The extension detects posts only while a matching Reddit page is open. AI calls create external API usage and send the selected post title/body to DeepSeek through the Worker. Reddit DOM changes may require parser maintenance.