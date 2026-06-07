# Design Picker — Project State

Date: 2026-06-07

## Current Phase

`local MVP built and browser-validated`

## Confirmed Direction

Build a thin internal Design Picker web app.

Do not deep-fork Linkwarden at the first step.

Reuse Linkwarden as the strongest preservation backend donor and preserve an adapter path for future integration.

## Confirmed Linkwarden Findings

Code inspection confirms:

- preview images are served through `/api/v1/archives/{linkId}?format=jpeg&preview=true&updatedAt=...`;
- the Linkwarden UI already renders generated preview images;
- manual image upload for a link banner already exists;
- preserved formats include screenshot image, PDF, readable version, monolith HTML, and preview state;
- preservation repair logic can reset broken archive fields for reprocessing.

## MVP Decision

The first internal MVP must remain standalone enough to run without Linkwarden, but its screenshot capture layer must use an adapter interface so Linkwarden can become a backend later.

## First Build Scope

- donor cards grid;
- local in-memory starter dataset;
- add donor form;
- source URL;
- title;
- preview URL;
- project type;
- style tags;
- section tags;
- decision status: primary / partial / rejected / undecided;
- selected pattern notes;
- Markdown export;
- JSON export;
- clear integration seam for Linkwarden.

## Explicitly Deferred

- authentication;
- database;
- real screenshot generation;
- Linkwarden API credentials;
- server-side metadata scraping;
- multi-user access;
- deployment;
- AI tagging.

## Latest Result

A polished static local MVP now exists with:

- donor card grid;
- add, edit, delete, and refresh actions;
- decision statuses;
- pattern selection;
- search and filtering;
- local persistence;
- Markdown and JSON export;
- a preview-provider adapter seam;
- Windows launcher path.

## Validation Evidence

Browser validation confirmed:

- two real public donor URLs were added successfully;
- one donor was edited after creation;
- one donor persisted as `primary` and another as `partial`;
- automatic preview URLs were generated through the adapter;
- refresh preview worked;
- local persistence survived reload;
- Markdown and JSON exports downloaded with expected records;
- the layout remained usable at a narrow viewport without horizontal overflow.

## Active Files

- `projects/design-picker/index.html`
- `projects/design-picker/styles.css`
- `projects/design-picker/app.js`
- `projects/design-picker/Launch-Design-Picker.bat`
- `projects/design-picker/README.md`
- `projects/design-picker/PROJECT.md`
- `projects/design-picker/PROJECT_STATE.md`
- `projects/design-picker/logs/latest.md`

## Next Practical Step

Run the MVP against a larger real donor set and then choose between:

- keeping the static local tool and refining board workflow;
- adding Linkwarden-backed screenshot integration;
- introducing a lightweight local server only if richer metadata import becomes necessary.
