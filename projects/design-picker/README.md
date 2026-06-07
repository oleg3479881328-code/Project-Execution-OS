# Design Picker MVP

## Run

This first version is intentionally build-free.

1. Download `index.html`.
2. Open it in a modern browser.
3. Add donor URLs and preview URLs.
4. Select reusable patterns and decision status.
5. Export Markdown or JSON when ready.

## What Works

- browser-runnable visual donor grid;
- local persistence in `localStorage`;
- add, edit, and remove donor cards;
- source URL and optional preview URL;
- project type;
- style and section tags;
- status filtering;
- primary / partial / rejected / undecided decisions;
- pattern selection;
- owner notes;
- Markdown export;
- JSON export.

## What Is Deferred

- automatic metadata extraction;
- automatic screenshot generation;
- Linkwarden API integration;
- database;
- authentication;
- hosted deployment.

## Linkwarden Integration Seam

Linkwarden source inspection confirmed that generated previews are served through:

```text
/api/v1/archives/{linkId}?format=jpeg&preview=true&updatedAt=...
```

The next backend version should add a provider adapter and allow a Linkwarden-backed preview source.

## Security Note

The static MVP stores records only in the current browser profile. Do not treat it as a shared or durable production system yet.