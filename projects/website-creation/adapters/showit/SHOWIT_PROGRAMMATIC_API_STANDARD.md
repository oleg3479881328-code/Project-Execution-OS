# Showit Programmatic API — Canonical Execution Standard

Status: `CANONICAL / CURRENT`
Date: 2026-09-30
Scope: **programmatic Showit page construction and mutation through the proven Showit data/API path**

## 1. Purpose

This is the **single operational entrypoint for a fresh chat/agent** working on Showit programmatically.

Use this document when the task is to build or modify a Showit page through code/API/data-model operations rather than by reproducing editor clicks.

The required direction is:

```text
OWNER-SUPPLIED EXISTING SHOWIT PAGE
→ identify exact current page
→ load current page JSON + ETag
→ obtain runtime auth from authenticated Showit session
→ compile all supported changes in memory
→ upload required media through the proven media API flow
→ ONE authenticated whole-page save
→ durable readback
→ editor reload / visual QA
```

This document contains the **accepted operating rules and ready solutions only**. Do not reconstruct the discovery history.

---

## 2. Hard Boundary: Work On the Page the Owner Supplies

Default operating rule:

- the owner creates/selects the target Showit page manually;
- the program works on **that existing page file only**;
- do **not** create a new Showit page through API unless a future separately accepted capability explicitly authorizes it;
- do **not** modify the site manifest or page list as part of normal page compilation;
- do **not** switch to another page because it is easier;
- do **not** assume a blank page is actually blank — inspect it first;
- do **not** erase existing Canvas blocks unless the owner explicitly requested a replacement operation and that operation is covered by an accepted capability.

If the page already contains content, default to `RESUME / PRESERVE`, not destructive replacement.

If page identity is uncertain, **STOP BEFORE WRITE**.

---

## 3. Programmatic Architecture

Showit page editing is a **whole-document model**, not an element-by-element save model.

Canonical programmatic path:

```text
Universal Recipe / Site Model intent
        ↓
Showit Adapter
        ↓
current page JSON + current ETag
        ↓
compile Canvas / text / graphic changes in memory
        ↓
ONE gzip POST of the updated page model
        ↓
new ETag
        ↓
durable page readback
        ↓
visual QA
```

For supported page mutations, do **not** save after every Canvas, text element, or image element.

Media upload is a separate preparatory API flow. Once required media assets exist, the page itself is committed once.

---

## 4. Current Accepted Capability Status

### `PROVEN LIVE`

The following capabilities are accepted for programmatic use:

- discover the current Showit page without hard-coded design/page IDs;
- load the current page JSON;
- obtain the page-file `ETag` concurrency token;
- read `localStorage.authToken` at runtime inside the already-authenticated `app.showit.com` session;
- authenticate Showit API calls with `Authorization: Bearer <runtime-token>`;
- gzip and save the whole existing page through `POST /designs/<design-key>`;
- receive `saved:true` and a new `ETag`;
- create a normal Canvas from scratch as JSON;
- create text elements from scratch;
- create multiple brand-new Canvas blocks and multiple text elements in memory and commit them with exactly one page save;
- duplicate an existing normal Canvas programmatically;
- create a native empty `graphic` / image placeholder;
- bind an existing Showit asset through `graphic.content`;
- upload a local JPG/PNG without Showit's Media Library UI;
- convert the uploaded asset into `graphic.content` and bind it to a generated image element;
- compile text + uploaded imagery + multiple Canvas blocks and commit them in one page save;
- read the saved page back from durable storage;
- verify new blocks and verify pre-existing blocks remain unchanged for append operations;
- reload the Showit editor and complete visual QA.

Accepted integrated production direction:

```text
LOCAL FILES / EXISTING ASSETS
→ Showit media assets
→ Canvas + elements compiled in memory
→ ONE PAGE SAVE
→ durable readback
→ visual QA
```

### `NOT YET ACCEPTED AS GENERAL PRODUCTION CAPABILITY`

Do not claim or use the following as if they were already proven:

- creating a brand-new Showit page through API as the normal workflow;
- changing the site manifest/page list as part of page compilation;
- arbitrary destructive replacement of every existing Canvas on an owner page;
- automatic publish flow;
- galleries;
- forms;
- menus/navigation structures;
- video;
- advanced interactions/animations;
- WordPress/blog-specific Canvas structures;
- arbitrary donor-site → pixel-perfect Showit parity without separate QA;
- the public wrapper API of `showit-page-compiler-v1.js` as independently owner-accepted production authority.

If a requested operation falls outside the `PROVEN LIVE` set, **do not invent a new mechanism silently**. Stop, locate an existing solution/proof first, and only then extend the shared adapter if a real gap remains.

---

## 5. Runtime Environment

The current proven adapter core runs **inside the already-authenticated `app.showit.com` page context** because it relies on browser-local runtime state/APIs:

- `location`;
- `performance` resource entries;
- `localStorage.authToken`;
- `File`;
- `Image`;
- `fetch`;
- `CompressionStream`;
- browser CORS/session behavior.

This does **not** make Playwright/Dramaturg the architecture.

They may be used as a carrier/test harness to execute code in the authenticated browser page context, but the actual construction path is the Showit JSON/API path.

Do not replace the accepted API/data-model route with a new browser-click workflow when the operation is already covered programmatically.

---

## 6. Exact Current-Page Discovery

Never hard-code a design key or page ID into reusable code.

The current accepted implementation discovers Showit page resources matching:

```text
designs.showit.co/<design-key>/pages/<page-id>.json
```

The reusable implementation obtains the current resource from the authenticated page's observed resource entries and extracts:

```text
designKey
pageId
```

### Safety rule

A browser session can contain resource history from pages opened earlier.

Therefore before any write:

1. identify the currently intended owner-supplied page;
2. load the candidate page JSON fresh;
3. inspect its page identity and Canvas inventory;
4. confirm that it is the expected target;
5. only then allow mutation.

Do not trust a stale resource match blindly.

---

## 7. Load Contract

Fresh page data is read from the current page JSON resource with cache busting / `cache: "no-store"`.

Canonical page-file shape includes:

```text
data.blocks      = ordered array of Canvas/block IDs
data.blockData   = map: block ID → Canvas/block object
```

The response `ETag` is the concurrency token for the next save.

Before mutation, retain the information required to verify:

- page identity is unchanged;
- old block order is unchanged where the operation is append-only;
- old block payloads are unchanged where required;
- page-level unrelated metadata is unchanged.

---

## 8. Authentication Contract

Authentication is runtime-only:

```js
const authToken = localStorage.getItem("authToken");
```

API header:

```text
Authorization: Bearer <authToken>
```

### Security rules

Never persist a real Showit token in:

- Git;
- docs;
- logs;
- fixtures;
- recipes;
- screenshots;
- generated source examples.

The token may be read only at execution time from the already-authenticated owner session and sent only to Showit's API.

---

## 9. Whole-Page Save Contract

After all supported changes have been compiled into the page model in memory, save once.

Payload:

```json
{
  "data": "<complete updated existing page JSON>",
  "file": {
    "isNew": false,
    "eTag": "<current ETag>"
  }
}
```

The payload is gzip-compressed with `CompressionStream("gzip")`.

Request:

```text
POST https://api.showit.com/designs/<design-key>
```

Required headers:

```text
Accept: */*
Content-Type: application/json
Content-Encoding: gzip
Authorization: Bearer <runtime authToken>
```

Acceptance for the write requires:

- HTTP request succeeds;
- response contains `saved:true`;
- response contains a new `eTag`;
- new ETag differs from the ETag used for the write.

`HTTP 200` or `saved:true` alone is **not sufficient acceptance**.

---

## 10. Concurrency / ETag Rule

Always use the freshest ETag from the current page file.

Canonical sequence:

```text
LOAD page + ETag A
→ compile all changes in memory
→ SAVE with ETag A
→ receive ETag B
→ READBACK expects ETag B
```

Do not reuse an old ETag for a later write.

Do not allow concurrent manual editor changes between the authoritative read and write when deterministic preservation matters.

On conflict or uncertainty, reload the current page model and recompute the mutation. Do not blind-retry an old whole-page payload.

---

## 11. Canvas / Block Model

Normal Canvas blocks live in:

```text
blocks[]
blockData[id]
```

New block IDs use the existing proven Showit-compatible pattern:

- length: 9 characters;
- generated with `crypto.getRandomValues`;
- alphabet:

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-
```

New IDs must be collision-checked against existing `blockData`.

New Canvas names/slugs must not collide with existing content.

For append operations, insert new block IDs deterministically into `blocks[]`, add complete block objects to `blockData`, and preserve pre-existing blocks exactly.

---

## 12. Text Element Contract

Programmatic text creation is `PROVEN LIVE`.

The current reusable compiler supports normalized text specs containing at minimum:

```text
text
color
desktop: x, y, w, h, size
mobile:  x, y, w, h, size
```

It also supports the already-used Showit text properties such as line height and letter spacing where supplied.

Desktop and mobile geometry can be compiled before the page save.

Do not create/save text elements one-by-one.

---

## 13. Image / Graphic Contract

Showit represents a normal image element as a `graphic` element.

An empty native placeholder uses:

```json
{
  "type": "graphic",
  "visible": "a",
  "content": {},
  "mobile": { "w": 280, "h": 160, "x": 20, "y": 480, "a": 0 },
  "desktop": { "w": 300, "h": 450, "x": 820, "y": 100, "a": 0 },
  "sync": ["gs.t", "o", "blur", "border.rad", "shadow.style", "trIn.type"]
}
```

A bound Showit asset is represented in `graphic.content` as:

```json
{
  "key": "<asset key>",
  "aspect_ratio": 0.66688,
  "title": "<asset title>",
  "type": "asset"
}
```

For an already-existing Showit asset, image binding is a page-model mutation; no re-upload is required.

---

## 14. New Local Media Upload Contract

Direct local JPG/PNG upload is `PROVEN LIVE` and does not require opening Showit's Media Library UI.

Canonical flow:

```text
local File
→ read image dimensions
→ POST https://api.showit.com/useruploads
→ receive asset metadata + upload_id + presigned S3 URL + required headers
→ PUT raw file bytes to returned S3 URL
→ POST https://api.showit.com/useruploads/<upload_id>/complete
→ validate completed asset
→ normalize asset
→ convert to graphic.content
→ include image element in page compilation
→ ONE page save
```

Create-upload JSON includes:

```text
filename
size
width
height
folder_id
```

The presigned S3 URL and signing data are ephemeral runtime values.

Never promote them into canonical project state.

After completion, validate that the completed `asset_id` matches the asset created at the beginning of the upload flow.

---

## 15. One-Save Rule

For supported page construction:

```text
N Canvas
+ N text elements
+ N image elements
= compile in memory
→ ONE page save
```

Media uploads may require their own upload API requests before the page save. That does **not** change the one-page-save rule.

Do not confuse:

```text
media upload requests
```

with:

```text
page document save
```

The accepted integrated proof includes local image upload + multiple new Canvas blocks + text + image binding + exactly one page save.

---

## 16. Durable Readback Is Mandatory

After a page save, reload the page JSON from durable storage using a fresh cache-busted request.

Verify at minimum:

- returned ETag equals the new ETag from the save;
- expected new block IDs exist;
- expected Canvas names/slugs exist exactly once;
- expected text element data exists;
- expected image `graphic.content.key` and `aspect_ratio` are correct;
- new blocks are in the expected order;
- pre-existing blocks are unchanged for append operations;
- page identity and unrelated page metadata are unchanged.

Only after durable readback passes may the editor be reloaded for visual QA.

---

## 17. Visual QA Rule

After durable readback:

1. reload Showit editor;
2. verify expected Canvas entries are visible exactly once;
3. inspect desktop rendering;
4. inspect mobile rendering when the task affects mobile;
5. verify uploaded/bound imagery visibly renders;
6. verify no neighboring existing content was unexpectedly changed.

Important: exact DOM text locators are **not** a reliable acceptance gate for text rendered inside Showit's canvas editor. A locator count of `0` can coexist with correctly rendered text.

For inner Canvas content, use:

```text
exact JSON readback
+ editor reload
+ visual/render QA
```

---

## 18. Existing Reusable Implementation

Current adapter directory:

[`projects/website-creation/adapters/showit/`](./)

Current status authority:

[`README.md`](./README.md)

Current reusable compiler implementation:

[`showit-page-compiler-v1.js`](./showit-page-compiler-v1.js)

When installed in the authenticated `app.showit.com` page context, it exposes:

```js
globalThis.ShowitPageCompilerV1
```

Current public surface:

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

### Important status split

```text
underlying Showit API/data-model primitives      = PROVEN LIVE
integrated direct-bricks compiler path            = PROVEN LIVE / OWNER VISUAL QA PASS
showit-page-compiler-v1.js public wrapper API     = CANDIDATE until separately owner-run
```

Therefore:

- reuse the code and accepted mechanics;
- do not describe the wrapper public API itself as independently production-accepted yet;
- do not create a second wrapper merely because the existing wrapper is still candidate;
- if production use requires wrapper promotion, run the smallest bounded owner acceptance of its public API and then update the status.

---

## 19. `buildPage()` Current Contract

The existing wrapper's `buildPage()` is designed for deterministic append-style compilation.

Conceptual input:

```js
await ShowitPageCompilerV1.buildPage({
  anchorName: "Existing Canvas Name",
  position: "after",
  verifyUnchanged: true,
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
          color: "#f3f0e8:100",
          desktop: { x: 60, y: 90, w: 700, h: 100, size: 58 },
          mobile: { x: 20, y: 70, w: 280, h: 90, size: 36 }
        }
      ]
    }
  ]
});
```

It is intended to:

1. load the current page + ETag;
2. find the semantic anchor;
3. compile all requested Canvas/elements in memory;
4. perform exactly one page save;
5. durable-read the page back;
6. verify expected new blocks;
7. verify pre-existing blocks remain unchanged.

Do not reinterpret this current append contract as arbitrary destructive full-page replacement.

---

## 20. Fresh Chat Execution Algorithm

A fresh chat receiving a Showit programmatic task must follow this exact order:

```text
1. READ THIS DOCUMENT
2. READ adapters/showit/README.md for current status
3. READ showit-page-compiler-v1.js only if implementation detail is needed
4. RECEIVE owner-selected existing Showit page + desired Recipe/assets
5. RUN READ-ONLY inventory of the exact current page
6. CLASSIFY target state: FRESH or RESUME
7. MAP requested work only to PROVEN LIVE primitives
8. UPLOAD required local media through the proven upload flow
9. COMPILE all supported page changes in memory
10. RE-READ fresh current ETag if concurrency is uncertain
11. PERFORM ONE authorized page save
12. DURABLE READBACK
13. EDITOR RELOAD + VISUAL QA
14. REPORT VERIFIED result or STOP with exact unsupported gap
```

### FRESH

Use only when read-only inspection proves the owner-supplied target page is in the intended fresh state.

### RESUME

Use when the page already contains accepted work. Preserve it and continue deterministically.

Do not create duplicate Canvas blocks merely because a previous run already created part of the target.

---

## 21. No-Invention Rule

For Showit programmatic work:

```text
CURRENT CANONICAL STANDARD
→ EXISTING PROVEN API/DATA-MODEL CAPABILITY
→ EXISTING REUSABLE IMPLEMENTATION
→ EXECUTION
→ DURABLE READBACK
→ VISUAL QA
```

Do not:

- invent a PW workflow for an operation already covered by the API path;
- build a new Showit client from scratch while the existing adapter covers it;
- introduce Mimic as the runtime path for an already-understood Showit operation;
- introduce a new GitHub-fetch/eval transport layer as production authority;
- create per-client Showit scripts when the reusable adapter can express the operation;
- guess undocumented object shapes for unsupported element types;
- call a task done because a request returned 200.

If an accepted reusable primitive is missing:

```text
STOP
→ identify exact missing primitive
→ search existing project/proof/source first
→ if still missing, propose the smallest reusable extension
→ acceptance-test it independently
→ promote it into this canonical standard only after PASS
```

---

## 22. Acceptance Definition

A programmatic Showit operation is `DONE` only when all required gates pass:

```text
correct owner-supplied target page
+ correct fresh source JSON
+ correct current ETag
+ supported deterministic mutation
+ authenticated whole-page save
+ new ETag
+ durable readback
+ old-state preservation where required
+ editor reload
+ visual QA
```

Anything less is `NOT VERIFIED`.

---

## 23. Authoritative References

Operational adapter status:

- [`README.md`](./README.md)

Reusable compiler source:

- [`showit-page-compiler-v1.js`](./showit-page-compiler-v1.js)

Accepted integrated programmatic pipeline proof:

- [`SHOWIT_COMPILER_PROVEN_BRICKS_INTEGRATED_ACCEPTANCE_2026-09-30.md`](../../proofs/SHOWIT_COMPILER_PROVEN_BRICKS_INTEGRATED_ACCEPTANCE_2026-09-30.md)

Accepted multi-Canvas / one-save proof:

- [`SHOWIT_MULTI_CANVAS_ONE_SAVE_PROOF_2026-09-30.md`](../../proofs/SHOWIT_MULTI_CANVAS_ONE_SAVE_PROOF_2026-09-30.md)

Accepted from-scratch Canvas proof:

- [`SHOWIT_FROM_SCRATCH_CANVAS_PROOF_2026-09-30.md`](../../proofs/SHOWIT_FROM_SCRATCH_CANVAS_PROOF_2026-09-30.md)

Accepted image-placeholder proof:

- [`SHOWIT_IMAGE_PLACEHOLDER_PROOF_2026-09-30.md`](../../proofs/SHOWIT_IMAGE_PLACEHOLDER_PROOF_2026-09-30.md)

Universal architecture / upstream Recipe boundary:

- [`UNIVERSAL_WEBSITE_TRANSLATOR_ARCHITECTURE.md`](../../UNIVERSAL_WEBSITE_TRANSLATOR_ARCHITECTURE.md)

Website Creator canonical Site Model:

- [`SITE_MODEL_STANDARD.md`](../../SITE_MODEL_STANDARD.md)

---

## Final Rule

**The owner supplies the Showit page. The program compiles supported content into that exact page through the proven Showit JSON/API path. Build in memory, save the page once, read it back, and visually verify it. Reuse proven programmatic solutions; do not invent a parallel workflow.**
