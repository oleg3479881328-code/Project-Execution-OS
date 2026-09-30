# Showit Page Compiler v1 — Assembly Record

Date: 2026-09-30
Status: `ASSEMBLED / INTEGRATED ACCEPTANCE NOT YET RUN`

## Decision

The individually live-proven Showit primitives are now assembled into a reusable adapter module:

`../adapters/showit/showit-page-compiler-v1.js`

Canonical adapter entry:

`../adapters/showit/README.md`

## Included public capabilities

- discover current Showit page without hard-coded design/page IDs;
- load page JSON + ETag;
- runtime bearer auth from the already-authenticated Showit page;
- gzip whole-page save;
- local JPG/PNG selection;
- direct Showit media upload (`/useruploads → S3 PUT → /complete`);
- normalize uploaded asset metadata;
- compile text elements;
- compile graphic/image elements from placeholders or assets;
- compile Canvas blocks from a small adapter spec;
- insert multiple new Canvas blocks in memory;
- one page save for the compiled change set;
- durable readback;
- unchanged-old-block verification.

## Safety boundaries

- no auth token persisted in repository state;
- no hard-coded Showit design key or page ID;
- no hard-coded user ID in the compiler;
- fail closed on Canvas name collisions;
- fail closed on missing semantic anchor;
- old Canvas order and old Canvas payloads are verified unchanged after a build;
- page-level non-block metadata is verified unchanged;
- new media upload is separate from page save;
- `buildPage()` performs one page write for the compiled Canvas set.

## Execution boundary

The compiler core executes in the browser page context because it needs Showit-local browser state and browser APIs:

- `location`;
- `localStorage.authToken`;
- `File`;
- `Image`;
- `CompressionStream`;
- page `fetch` / CORS behavior.

In Dramaturg JS mode it therefore must be invoked through `page.evaluate(...)` or an equivalent page-context wrapper.

## Why this is not yet marked PROVEN LIVE

Every primitive used by the compiler has live proof, but the assembled public API is new code.

Per acceptance rules, assembly is not equivalent to acceptance.

Required integrated gate:

```text
install compiler in authenticated Showit page context
→ select at least one fresh local image
→ upload image through compiler API
→ compile multiple Canvas blocks containing text + uploaded image
→ exactly one page save
→ durable readback PASS
→ reload Showit editor
→ visual QA PASS
```

Only after that gate passes may `showit-page-compiler-v1.js` be promoted to `PROVEN LIVE`.

## Next action

Run one bounded integration acceptance against the existing test page. Use unique test Canvas names so the compiler can fail closed on reruns and so unrelated page state remains auditable.
