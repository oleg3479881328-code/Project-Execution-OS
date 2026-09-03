# Chrome Extension Architecture Patterns

## Purpose

Define reusable architecture choices for browser-extension products.

## Pattern 1 — Local Utility Extension

Use when the extension improves the browser experience and does not need accounts or backend state.

Typical parts:

- `manifest.json`;
- popup UI;
- options page;
- content script;
- `chrome.storage.local` or `chrome.storage.sync`.

Good for:

- page helpers;
- personal productivity;
- small learning tools;
- formatting and annotation helpers.

Avoid when payments, user accounts, provider keys, or team sync are required.

## Pattern 2 — Content Script plus Page UI

Use when the extension adds a visible interface to allowed webpages.

Typical parts:

- content script;
- isolated UI mount point;
- message passing between content script and background service worker;
- narrow host permissions.

Good for:

- learning overlays;
- productivity helpers;
- inline explanations;
- page-specific tools.

Risk:

- page DOM changes can break behavior;
- host permissions must stay narrow;
- user-visible behavior must match disclosure.

## Pattern 3 — Extension plus SaaS Backend

Use when the extension is part of a paid or account-based product.

Typical parts:

- extension UI;
- SaaS web app;
- backend API;
- auth provider;
- payment provider;
- license or subscription enforcement.

Good for:

- paid AI tools;
- team products;
- subscription products;
- cross-device state;
- server-side processing.

Rule:

Private keys and billing logic belong on the backend, not inside extension code.

## Pattern 4 — AI Extension

Use when the extension sends selected user-provided content to an AI backend or local model workflow.

Typical parts:

- extension UI for selecting or confirming input;
- backend AI proxy;
- rate limits;
- user account or license checks;
- privacy disclosures.

Good for:

- summarization;
- translation;
- study cards;
- writing helpers;
- research assistants.

Rule:

Make external model calls and data flow understandable to the user.

## Pattern 5 — Affiliate or Commerce Helper

Use when the extension supports product discovery, comparison, coupon, or affiliate workflows.

Typical parts:

- content script on allowed merchant domains;
- affiliate or link service;
- disclosure UX;
- backend configuration service;
- optional account layer.

Good for:

- deal helpers;
- product comparison;
- creator affiliate tools;
- shopping research tools.

Risk:

Disclosure, merchant rules, extension-store policies, and user trust are central.

## Pattern 6 — Internal Operator Extension

Use when the extension is for the owner's internal workflow, not public release.

Typical parts:

- persistent Chrome Side Panel by default when the tool has multiple controls, progress, results, or long-running state;
- toolbar popup only for tiny one-action utilities;
- strict domain allowlist;
- local configuration;
- no public monetization;
- no unnecessary data collection.

Good for:

- internal QA;
- browser workflow shortcuts;
- controlled operator tools;
- collectors/research tools that stay open while the user navigates the target site.

### Owner UI default — Project Execution OS

For persistent internal operator extensions, reuse the established Side Panel visual language instead of inventing a new black/white utility UI.

Canonical donor:

`projects/tiktok-research-sorter/entrypoints/sidepanel/`

Visual DNA:

- graphite / radial dark background;
- translucent dark panels;
- purple → magenta primary actions;
- teal progress and link accents;
- compact Inter/system typography;
- 12–14 px panel radii;
- colored status chips and visible progress.

Implementation baseline:

- Manifest V3 `side_panel.default_path`;
- `sidePanel` permission;
- `chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true })`;
- no `action.default_popup` for this pattern.

### Visible version rule

For owner-operated extensions, the installed build version must be visible immediately in the primary UI.

- show `vX.Y.Z` prominently in the Side Panel header, next to status;
- read it dynamically from `chrome.runtime.getManifest().version`;
- do not rely on a tiny footer-only version label;
- show the same manifest-derived version on secondary Results/History surfaces when present;
- toolbar action title may include the version as an additional check.

This prevents confusion during rapid unpacked-extension iteration and live acceptance testing.

## Final Rule

Choose the architecture pattern before choosing libraries. The product surface determines the stack, permissions, backend need, and compliance path.