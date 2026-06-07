# Design Picker MVP

## Run

This version is intentionally build-free.

1. Download `index.html`.
2. Open it in a modern browser.
3. Add a donor URL.
4. Leave the preview field empty to generate an automatic screenshot preview.
5. Select reusable patterns and decision status.
6. Export Markdown or JSON when ready.

## What Works

- browser-runnable visual donor grid;
- local persistence in `localStorage`;
- add, edit, and remove donor cards;
- source URL normalization;
- automatic title fallback from the donor domain;
- automatic screenshot preview generation from donor URL through a screenshot endpoint;
- optional manual preview URL override;
- refresh preview action;
- project type;
- style and section tags;
- status filtering;
- primary / partial / rejected / undecided decisions;
- pattern selection;
- owner notes;
- Markdown export;
- JSON export.

## Current Preview Adapter

The static MVP uses a public screenshot endpoint:

```text
https://image.thum.io/get/width/1280/crop/720/noanimate/{encodedUrl}
```

This is only the first runnable adapter for validating the interaction model.

Do not treat it as the final production dependency.

## What Is Deferred

- server-side metadata extraction;
- Linkwarden API integration;
- durable database;
- authentication;
- hosted deployment;
- AI tagging;
- screenshot caching and provider credentials;
- private-network URL blocking on a backend.

## Linkwarden Integration Seam

Linkwarden source inspection confirmed that generated previews are served through:

```text
/api/v1/archives/{linkId}?format=jpeg&preview=true&updatedAt=...
```

The next backend version should replace or augment the public screenshot endpoint with a provider adapter and allow a Linkwarden-backed preview source.

## Security Note

The static MVP stores records only in the current browser profile.

Do not treat it as a shared or durable production system yet.

Because the current screenshot endpoint is external, only submit public website URLs during MVP validation.