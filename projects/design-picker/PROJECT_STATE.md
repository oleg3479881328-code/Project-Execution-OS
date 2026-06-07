# Design Picker — Project State

Date: 2026-06-07

## Current Phase

`implementation bootstrap`

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

## Next Practical Step

Create a browser-runnable static MVP and verify the interaction model before adding backend integration.