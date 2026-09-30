# Showit Adapter

Status: `CANDIDATE IMPLEMENTATION / LIVE-PROVEN PRIMITIVES`
Date: 2026-09-30

## Purpose

Reusable Showit adapter for the Universal Website Translator / Website Creator control layer.

This is not a replacement browser engine and not a client-specific script. It packages the Showit operations that were proven live in the owner's authenticated Showit session into one reusable adapter surface.

Canonical direction:

```text
Universal Recipe / Site Model intent
→ Showit Adapter
→ current page JSON + ETag
→ compile changes in memory
→ one authenticated gzip page save
→ durable readback
→ visual QA
```

## Current proven primitives

The following primitives have live proof in `../../proofs/`:

- current page discovery without hard-coded design/page IDs;
- page JSON load + ETag concurrency token;
- runtime auth through `localStorage.authToken` without persisting the token;
- whole-page gzip POST to `api.showit.com/designs/<design-key>`;
- direct Canvas duplication;
- Canvas creation from scratch;
- text element creation from scratch;
- multiple new Canvas blocks in one page save;
- empty image/graphic placeholder creation;
- existing asset → `graphic.content` binding;
- local image upload through `POST /useruploads → presigned S3 PUT → /complete`;
- local file → new Showit asset → Canvas binding;
- durable S3/page readback and unchanged-old-state verification.

## Module

`showit-page-compiler-v1.js`

Installs:

```js
globalThis.ShowitPageCompilerV1
```

Primary API:

```js
ShowitPageCompilerV1.info()
ShowitPageCompilerV1.loadPage()
ShowitPageCompilerV1.pickImages(options)
ShowitPageCompilerV1.uploadImage(file, options)
ShowitPageCompilerV1.uploadImages(files, options)
ShowitPageCompilerV1.createText(spec)
ShowitPageCompilerV1.createImage(spec)
ShowitPageCompilerV1.createCanvas(spec, existingBlockData)
ShowitPageCompilerV1.buildPage(spec)
ShowitPageCompilerV1.assetToGraphicContent(asset)
```

## `buildPage` contract

`buildPage()` does not save after every element. It:

1. loads the current page JSON + ETag;
2. compiles all requested new Canvas blocks and elements in memory;
3. inserts them as one deterministic change set;
4. performs exactly one authenticated gzip POST for the page;
5. reads the page back from durable storage;
6. verifies all new blocks and verifies all pre-existing blocks remained unchanged.

Example shape:

```js
await ShowitPageCompilerV1.buildPage({
  anchorName: "Existing Canvas Name",
  canvases: [
    {
      name: "NEW HERO",
      slug: "new-hero",
      background: "#111111:100",
      desktop: { w: 1200, h: 700 },
      mobile: { w: 320, h: 680 },
      elements: [
        {
          type: "text",
          text: "HELLO",
          desktop: { x: 60, y: 90, w: 700, h: 100, size: 58 },
          mobile: { x: 20, y: 70, w: 280, h: 90, size: 36 },
          color: "#f3f0e8:100"
        }
      ]
    }
  ]
})
```

## Media flow

New local file:

```text
File
→ POST api.showit.com/useruploads
→ asset + upload_id + presigned S3 URL
→ PUT raw bytes to S3
→ POST api.showit.com/useruploads/<upload_id>/complete
→ normalized asset
→ graphic.content
```

`uploadImage()` intentionally does not require or open Showit's Media Library UI.

## Security rule

Never store a real Showit auth token in Git, logs, fixtures, proof docs, examples, or generated recipes.

The adapter reads `localStorage.authToken` only at runtime inside the already-authenticated Showit tab and sends it only to Showit's API.

Presigned S3 URLs are ephemeral runtime values and must not be promoted into canonical project state.

## Current acceptance state

The individual primitives are live-proven.

`showit-page-compiler-v1.js` is a newly assembled reusable module and remains `CANDIDATE` until the integrated module itself passes a live acceptance run using its public API.

Do not mark the module `PROVEN LIVE` merely because its underlying primitives are proven. The integrated acceptance gate is:

```text
install module
→ upload at least one fresh local image through module API
→ build multiple Canvas blocks with text + image through buildPage()
→ exactly one page save
→ durable readback PASS
→ editor reload
→ visual QA PASS
```
