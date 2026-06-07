# Design Picker

## Purpose

Give the owner a visual, low-friction way to choose a website or product-interface design direction by pointing at concrete examples instead of describing taste from memory.

This module sits between donor research and design specification.

## Core Principle

The owner should be able to say:

- `I want this overall style`;
- `take the hero from this example`;
- `use a pricing structure similar to this one`;
- `I like these cards but not the colors`;
- `keep this interaction, simplify the animation`.

The design agent must translate those selections into reusable patterns and an implementation-ready design package.

Do not copy a donor website as a whole.

Extract patterns, constraints, and composition logic.

## Required Flow

`project intent -> donor research -> visual catalog -> owner selection -> pattern extraction -> design direction -> implementation handoff`

## Catalog Levels

### Level 1 — Curated Reference Library

A lightweight library of selected examples with screenshots, links, tags, and notes.

Keep this as the durable data layer and import/export format.

Recommended storage:

- repository-backed Markdown index;
- screenshot folder in the active project or reusable design-library area;
- optional Notion or Google Sheet mirror for browsing convenience.

### Level 2 — Design Board

A visual board for one active project.

It contains the shortlist shown to the owner before design work begins.

The owner can select:

- one primary donor;
- several partial donors;
- rejected directions;
- specific sections or components worth borrowing;
- style notes in plain language.

### Level 3 — Design Picker Web App

A dedicated internal web interface with thumbnail cards, URL import, preview generation, filters, saved selections, and export into a design brief.

Build this as the first usable MVP while preserving the lightweight repository-backed catalog as the durable fallback and export format.

See:

`blocks/design/DESIGN_PICKER_WEB_APP.md`

## Donor Card Schema

Each catalog item should contain:

| Field | Purpose |
| --- | --- |
| `id` | stable reference id |
| `title` | short human-readable name |
| `source_url` | original website or reference link |
| `screenshot_path` | local, object-storage, or repository-backed preview |
| `project_type` | landing page, SaaS, dashboard, marketplace, portfolio, AI product, onboarding, pricing, etc. |
| `style_tags` | minimal, editorial, bold, playful, premium, technical, dark, light, etc. |
| `section_tags` | hero, pricing, cards, navigation, FAQ, onboarding, dashboard, checkout, etc. |
| `strong_points` | what works well |
| `reuse_notes` | what can be adapted |
| `avoid_notes` | what must not be copied or what does not fit |
| `complexity` | low, medium, high |
| `implementation_notes` | stack, animation, responsive, or component implications |
| `license_or_copy_risk` | any copying or asset-use caveat |
| `added_date` | catalog maintenance |
| `source_type` | live site, gallery, template, component library, screenshot, internal project |

## Owner Selection Format

The design agent should summarize the owner's choices as a compact selection record:

```md
# Design Selection Record

## Primary Direction
- donor id:
- why selected:

## Borrow These Patterns
- donor id + section/component:
- donor id + section/component:

## Avoid
- rejected direction or pattern:

## Style Notes In Owner's Words
- ...

## Open Design Decisions
- ...
```

## Pattern Extraction Rules

For every selected donor, distinguish:

1. **visual style** — spacing, density, typography mood, color direction, image treatment;
2. **page composition** — section order, hierarchy, content grouping;
3. **interaction pattern** — navigation, filters, onboarding, CTA behavior, motion;
4. **conversion pattern** — proof, pricing, trust, urgency, upgrade flow;
5. **implementation burden** — complexity, responsive risks, animation cost, required libraries.

Never reduce the analysis to `make it like this site`.

## Deliverable After Selection

The agent must produce:

- selected donor summary;
- extracted reusable patterns;
- rejected patterns;
- page or interface structure;
- UI-system direction;
- responsive behavior notes;
- implementation complexity notes;
- frontend handoff input.

## Recommended Initial Implementation

Build a small internal web app with URL import, generated screenshots, manual tags, project boards, owner decisions, and Markdown / JSON export.

Keep the repository-backed catalog format as a stable fallback and data portability layer.

Do not begin with large-scale crawling, automated cloning, or an AI-heavy analysis layer.

Validate the MVP on one real project with 15–30 donor references before expanding it.

## Boundary

This module is for choosing and translating design references.

It does not replace:

- donor research;
- page strategy;
- wireframing;
- UI-system definition;
- implementation handoff;
- design review.

## Final Rule

Let the owner choose visually. Let the agent convert taste into buildable decisions.