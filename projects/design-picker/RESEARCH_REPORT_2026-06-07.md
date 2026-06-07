# Design Picker — Reuse-First Research Report

Date: 2026-06-07

## Goal

Find an adequate existing solution that can reduce or replace custom development of the internal Design Picker web application.

## Confirmed Product Need

The owner needs a visual interface where a donor website URL can be saved as a preview card, browsed in a grid, tagged, added to a project board, marked as primary / partial / rejected / undecided, annotated by reusable pattern, and exported as a design brief.

## Existing Solutions Checked

### 1. Linkwarden

Repository:

`https://github.com/linkwarden/linkwarden`

Relevant confirmed capabilities from the project README:

- self-hosted and open source;
- save a copy of each webpage as Screenshot and PDF;
- preserve a single HTML file;
- organize links by collection, sub-collection, name, description, and multiple tags;
- collaboration;
- search, filter, and sort;
- browser extension;
- API keys;
- bulk actions;
- image and PDF uploads;
- custom icons.

#### Fit

Strong fit for URL capture, visual preservation, collections, tags, and durable donor storage.

#### Gaps For Design Picker

- no confirmed project-specific `primary / partial / rejected / undecided` design-selection model;
- no confirmed pattern-level selection fields such as hero, pricing, cards, navigation, motion, dashboard, onboarding;
- no confirmed design-brief export shaped for agents and frontend handoff;
- visual browsing may require UI adaptation for design-selection use rather than general bookmark preservation.

#### Adaptation View

Strongest foundation candidate if the goal is to avoid rebuilding screenshot capture and archival.

### 2. Karakeep

Repository:

`https://github.com/karakeep-app/karakeep`

Relevant confirmed capabilities from the project README:

- self-hostable bookmark-everything app;
- save links, notes, images, and PDFs;
- automatic fetching for link titles, descriptions, and images;
- lists and collaboration;
- full-text search;
- AI tagging and summarization;
- Chrome, Firefox, and Safari extensions;
- REST API and multiple clients;
- full-page archival;
- bulk actions;
- self-hosting first;
- Next.js, Drizzle, NextAuth, tRPC, Puppeteer, and Meilisearch stack.

#### Fit

Strong fit for a visual card grid, URL metadata enrichment, tags, lists, browser import, and API-driven integration.

#### Gaps For Design Picker

- README confirms fetched images but not automatic webpage screenshots as the default visual artifact;
- no confirmed design-selection status model;
- no confirmed pattern-level selection workflow;
- no confirmed Markdown / JSON design-brief export.

#### Adaptation View

Strongest UI and stack donor. Potentially useful as a fork donor or as architectural inspiration. Less directly aligned than Linkwarden if screenshot fidelity is the critical first requirement.

### 3. Raindrop.io

Relevant note:

Karakeep documents Raindrop as a polished open-source bookmark manager that supports links, images, and files, but not self-hosting.

#### Fit

Useful UX donor.

#### Limitation

Not the preferred internal foundation because self-hosting and direct control matter for this project.

### 4. Readeck

Relevant note:

Readeck is a self-hosted read-it-later solution with tags, favourites, archives, and browser access.

#### Fit

Useful as a lightweight bookmark/read-later donor.

#### Limitation

Less aligned with the required visual design-board workflow than Linkwarden or Karakeep.

## Decision

Do not build the entire product from scratch.

Use a hybrid reuse strategy:

1. treat Linkwarden as the strongest functional foundation donor for URL preservation and screenshot capture;
2. treat Karakeep as the strongest UI and implementation-pattern donor for visual browsing, metadata import, API-driven enrichment, and modern Next.js structure;
3. build only the missing bounded Design Picker layer:
   - design projects;
   - primary / partial / rejected / undecided decisions;
   - selected reusable patterns;
   - owner notes;
   - Markdown / JSON design-brief export;
   - design-specific visual board UX.

## Recommended MVP Direction

Before forking a large upstream application, build a thin internal Design Picker MVP that can use a screenshot-provider adapter and preserve a future integration path to Linkwarden.

Reason:

- the missing design-selection workflow is small and specific;
- a deep fork would inherit unrelated bookmark-manager complexity;
- a thin custom layer can validate the UX quickly;
- Linkwarden can later become the capture/archive backend if its API fit is confirmed;
- Karakeep remains a useful architecture and UI donor without requiring adoption of its full product scope.

## Confirmed Facts vs Assumptions

### Confirmed

- Linkwarden auto-captures screenshot, PDF, and single HTML for webpages.
- Linkwarden supports collections, sub-collections, tags, filtering, browser extension, API keys, and uploads.
- Karakeep fetches titles, descriptions, and images automatically.
- Karakeep supports lists, tags, extensions, REST API, archival, and a modern Next.js-based stack.

### Assumptions To Validate

- Linkwarden API exposes enough information to reuse captured screenshots cleanly.
- A thin custom Design Picker can integrate with Linkwarden without maintaining a fragile deep fork.
- Hosted screenshot API or self-hosted Playwright remains the fastest MVP fallback if Linkwarden API integration is inconvenient.

## Next Validation Step

Inspect Linkwarden API and screenshot-storage access patterns. Then decide between:

A. thin custom app with Linkwarden integration;

B. thin custom app with independent screenshot-provider adapter;

C. bounded Linkwarden fork only if integration proves insufficient.