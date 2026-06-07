# Design Picker Web App

## Purpose

Define the first buildable web application for browsing design donors, importing references by URL, viewing previews, selecting visual patterns, and exporting an implementation-facing design brief.

## Product Decision

Build the visual picker as a lightweight internal web application.

Do not require the full reusable donor library to be populated before launch.

The application must support both:

1. curated internal donor cards;
2. on-demand import of external donor URLs with generated previews.

## Owner Experience

The owner should be able to:

1. paste a donor website URL;
2. see a preview card generated automatically;
3. browse cards in a visual grid;
4. filter by project type, style, section, and complexity;
5. open a donor detail view;
6. mark a donor as primary, partial, rejected, or undecided;
7. select what is useful: hero, cards, pricing, navigation, motion, onboarding, dashboard, checkout, or custom notes;
8. export a project design board and design-selection record for an agent.

## MVP Scope

### Include

- donor grid with thumbnail cards;
- URL import form;
- title, source URL, favicon or logo, generated preview image, tags, notes, and status;
- manual tag editing;
- project boards;
- primary / partial / rejected / undecided decisions;
- pattern-level selection notes;
- Markdown export;
- JSON export;
- refresh preview action;
- timestamp for preview freshness;
- fallback preview behavior.

### Exclude From First MVP

- full automated AI design analysis;
- semantic search;
- automatic large-scale crawling;
- public multi-user SaaS;
- billing;
- browser extension;
- copying full websites;
- automatic reuse of third-party visual assets.

## Preview Strategy

Use a layered fallback strategy.

### Layer 1 — Screenshot Preview

Preferred default for design browsing.

Generate a screenshot through a server-side screenshot provider or a self-hosted browser automation service.

Store:

- preview URL or object-storage path;
- capture date;
- viewport preset;
- capture status;
- provider;
- error message when capture fails.

### Layer 2 — Open Graph Preview

If a screenshot is unavailable, attempt to read page metadata and use `og:image`, title, description, and canonical URL.

This is a fallback only. Social preview images are useful but often do not represent the page layout accurately enough for design selection.

### Layer 3 — Manual Preview

Allow manual upload or paste of a screenshot.

This handles login walls, anti-bot systems, unstable pages, region restrictions, and pages where the useful design state is not the default landing state.

## Preview Provider Decision

For the first MVP, keep screenshot generation behind a provider adapter.

Recommended initial options:

1. hosted screenshot API for fastest launch;
2. self-hosted Playwright or Browserless-compatible capture service when cost, control, or privacy justify it.

Do not hard-wire the application to one provider.

Interface concept:

```ts
interface ScreenshotProvider {
  capture(input: {
    url: string;
    viewport: "desktop" | "mobile";
    fullPage?: boolean;
  }): Promise<{
    imageUrl: string;
    capturedAt: string;
    provider: string;
  }>;
}
```

## Suggested Data Model

### `donors`

| Field | Purpose |
| --- | --- |
| `id` | stable donor id |
| `title` | display title |
| `source_url` | original URL |
| `canonical_url` | normalized URL when available |
| `description` | short note |
| `logo_url` | favicon or logo |
| `og_image_url` | fallback metadata image |
| `preview_image_url` | generated or manually uploaded preview |
| `preview_source` | screenshot_api, self_hosted, og_image, manual |
| `preview_captured_at` | freshness timestamp |
| `preview_status` | ready, pending, failed |
| `project_type` | landing, SaaS, dashboard, marketplace, AI product, etc. |
| `style_tags` | array |
| `section_tags` | array |
| `complexity` | low, medium, high |
| `strong_points` | notes |
| `reuse_notes` | notes |
| `avoid_notes` | notes |
| `copy_risk_notes` | notes |
| `created_at` | audit field |
| `updated_at` | audit field |

### `projects`

| Field | Purpose |
| --- | --- |
| `id` | stable project id |
| `name` | project name |
| `goal` | short design goal |
| `created_at` | audit field |
| `updated_at` | audit field |

### `project_donor_selections`

| Field | Purpose |
| --- | --- |
| `id` | stable selection id |
| `project_id` | target project |
| `donor_id` | selected donor |
| `decision` | primary, partial, rejected, undecided |
| `selected_patterns` | hero, cards, pricing, navigation, motion, custom |
| `owner_notes` | plain-language notes |
| `created_at` | audit field |
| `updated_at` | audit field |

## Suggested Stack

Use a simple web stack optimized for fast internal deployment:

- Next.js or equivalent React-based full-stack framework;
- TypeScript;
- SQLite for local MVP or Postgres for hosted deployment;
- object storage for screenshots when hosted;
- a provider adapter for screenshots;
- a metadata extractor for title, favicon, canonical URL, description, and Open Graph fields;
- Markdown and JSON export endpoints.

## Import Flow

```text
paste URL
-> normalize URL
-> create pending donor record
-> fetch metadata
-> request screenshot
-> store preview
-> show generated donor card
-> allow manual edits and tags
-> optionally add to a project board
```

## Failure Handling

The import flow must not fail completely because one enrichment step fails.

Examples:

- metadata unavailable -> keep source URL and screenshot;
- screenshot unavailable -> use Open Graph preview;
- Open Graph image unavailable -> show placeholder and manual upload action;
- preview stale -> keep old screenshot until refresh succeeds;
- duplicate URL -> offer to open or refresh existing donor card.

## Security And Compliance Notes

- treat imported URLs as untrusted input;
- prevent server-side request forgery by blocking private-network and unsafe URL targets;
- do not execute arbitrary user scripts;
- rate-limit screenshot refreshes;
- avoid storing third-party assets as reusable production assets;
- use previews for research and selection, not for claiming ownership of donor materials;
- preserve source attribution and original URLs;
- allow removal of imported records and cached previews.

## First Validation Scenario

Use one real project and import 15–30 donors.

Validate whether the owner can:

1. browse visually without opening every site;
2. select one primary direction;
3. combine several partial patterns;
4. reject unsuitable options;
5. export a brief that a design agent can understand without additional interpretation.

## Future Expansion

Only after MVP validation consider:

- AI-assisted donor tagging;
- screenshot comparison over time;
- automatic section detection;
- visual similarity search;
- team collaboration;
- browser extension import button;
- design-agent integration;
- public SaaS packaging and monetization.

## Final Rule

The first web application is a visual decision tool, not an automated website copier.