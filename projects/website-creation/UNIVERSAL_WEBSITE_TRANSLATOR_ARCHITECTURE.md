# Universal Website Translator — Dramaturg + Stagecraft Architecture

Status: `candidate / active research direction`
Date: 2026-09-21

## Purpose

Capture the generalized architecture discovered while testing Dramaturg/Playwright automation in visual website editors.

The target is not a Showit-specific script system and not another browser automation engine.

The target pattern is:

```text
SOURCE WEBSITE
→ CAPTURE
→ NORMALIZE
→ UNIVERSAL RECIPE
→ EDITOR ADAPTER
→ BUILD
→ VERIFY
```

Working label: **Universal Website Translator**.

Detailed durable research/decision record:
https://docs.google.com/document/d/1RmTaj0rH7J-VV3mTgOJRl_J09rs5J8UI6L0HuKH3H6k/edit

## Core Decision

Use existing browser automation infrastructure first.

Current primary candidate:

```text
Website Creator control/translation layer
        ↓
Stagecraft skills / recipes
        ↓
Dramaturg / playwright-repl
        ↓
Playwright / playwright-crx
        ↓
real authenticated Chrome session
```

Do not rebuild the Playwright engine, Chrome debugger/CDP bridge, PW parser, recorder, locator generation, snapshot engine, replay engine, variable substitution, browser MCP bridge, tab-attach plumbing, or JS debugger unless a concrete upstream gap is proven.

## PW-First Rule

- Linear browser/editor operations → native `.pw`.
- JavaScript is an escape hatch for loops, conditions, calculations, DOM diff, complex extraction, editor internals, or capabilities `.pw` cannot express reliably.
- Do not invent a second DSL before native `.pw` is proven insufficient.

## Stagecraft / Brick Layer

Stagecraft already provides much of the intended reusable-brick model:

- `SKILL.md`;
- `.pw` skills;
- `.js` fallback;
- user skill directory;
- discovery/list/run;
- `{{variable}}` substitution;
- recording/replay;
- ref-to-stable-locator conversion.

Our higher-level semantic operations may look like:

```text
showit.canvas.rename(name)
showit.text.set_content(value)
wix.page.rename(name)
wix.image.replace(asset)
```

These are conceptual control-layer names, not claims about native Dramaturg commands. Their implementation should use proven `.pw` sequences wherever practical.

## Capture Layer

A donor/source site fingerprint may include:

- page/section structure;
- content;
- typography;
- colors;
- spacing;
- geometry;
- images/media references;
- responsive states;
- interaction/motion evidence;
- design tokens;
- DOM/accessibility evidence;
- screenshots.

The normalized result must not be tied to a single editor.

## Editor Adapter Boundary

One normalized recipe should be able to feed different target adapters:

```text
Universal Recipe
  ├─ Showit Adapter
  ├─ Wix Adapter
  ├─ Webflow Adapter
  └─ future editor adapters
```

Each adapter translates normalized intent into tested browser/editor bricks.

## Showit / Wix Proof Strategy

Showit is the first proving ground. Existing work has already shown routine editor actions collapsing from large custom JS attempts into very short `.pw` flows.

Wix is the next strong proof candidate. Test a representative set such as page operations, sections, text, images, layout, mobile/responsive behavior, SEO controls and save/preview/publish.

If the same capture → recipe → adapter model works for both, that is strong evidence the subsystem is generic rather than Showit-specific.

## Scope: "Almost Any Website"

The architecture can potentially automate websites whose workflows are available through normal Chrome/browser surfaces such as DOM, accessibility tree, keyboard/pointer events, forms, frames/iframes and Playwright-accessible controls.

This is not a 100% universal-automation claim.

Common boundary classes include CAPTCHA, hardware WebAuthn, some 2FA steps, OS-native dialogs, hostile anti-bot systems, browser-internal restricted pages, opaque canvas/video-only interfaces, and workflows requiring native desktop software.

## AI Role

Preferred route:

```text
Task
→ find existing brick
→ compose bricks
→ fill parameters
→ execute native PW
→ verify
→ repair/create only missing brick
→ QA
→ promote accepted brick
```

AI should progressively work against a semantic registry of proven operations instead of generating raw Playwright from scratch for each task.

## Controlled Healing

Future locator healing should be explicit and acceptance-based:

```text
brick fails
→ recon/heal
→ identify equivalent target
→ test
→ QA
→ accept
→ update canonical brick
```

Do not silently mutate canonical automation on every run.

## Relationship To Website Creator

This architecture is an additional capture/execution path, not a replacement for the existing Website Creator shared engine or Site Model.

Possible routes:

1. donor site → fingerprint → normalized recipe → external editor adapter;
2. donor site → fingerprint → normalized recipe → Website Creator Site Model/components;
3. Website Creator Site Model → external editor adapter when a client must use Showit/Wix/etc.

Keep site intent/data, design fingerprint, normalized recipe and target-platform implementation as separate layers.

## Next Proof

Do not fork Dramaturg first.

Prove:

```text
known working Showit PW operation
→ Stagecraft skill
→ parameter
→ run/replay against real authenticated Chrome
→ deterministic verification
```

Then repeat against a small representative Wix operation set.

## Final Rule

The strategic goal is not to build another browser automation engine.

The strategic goal is to build the **minimum missing translation/control layer above a proven browser engine**.

## 2026-09-21 — First Generated Universal Page Recipe

The architecture now has a first real artifact, not only a conceptual target.

Proof source:
`https://aperolspritz.tonicsiteshop.com/portfolio`

Generated chain:

`Universal Site Fingerprint → Universal Page Recipe v1 → Showit Adapter Plan / Wix Adapter Plan`

Artifact facts:
- 17 sections;
- 173 normalized elements;
- authored widths 1200 desktop / 320 mobile;
- source breakpoint 768 px;
- 165/173 source elements mapped to DOM evidence;
- normalized element kinds: text, image, button, divider, vector, icon, gallery, shape, unknown.

Adapter translation:
- Showit: 165 exact / 7 approximate / 1 unsupported;
- Wix: 155 exact / 17 approximate / 1 unsupported.

Status:
- Recipe schema/generator: GENERATED / ARTIFACT VALIDATED on this source;
- Showit adapter: translation artifact generated; execution must still route through the current Dramaturg capability registry;
- Wix adapter: translation candidate only / NOT LIVE PROVEN.

Canonical Drive folder:
https://drive.google.com/drive/folders/10oR140lzuXUK7eDq2nx77-oc6yBlb3Kc

Current generator:
https://docs.google.com/document/d/1Qr421BsCleTjv6zCY_-S0tiAfUuPmJ50QLHK6e6O8bU/edit

Compact machine recipe:
https://docs.google.com/document/d/1yLWHj78strzY2eoetWczw1_AkynKSvLYImvTaqEET40/edit

Architecture rule:
the older direct fingerprint→Showit-plan translator remains a useful target-specific donor/compatibility route, but the preferred boundary is now `Fingerprint → Universal Page Recipe → Editor Adapter`.

## 2026-09-30 — Showit Internal Save Path / HAR Proof

Status: `CAPTURE PROVEN / DIRECT API REPLAY NOT YET LIVE-PROVEN`.

A controlled HAR capture around Showit Canvas duplication plus inspection of the shipped Showit browser bundle established the current internal page-load/save model without relying on guessed selectors.

Observed generalized path:

```text
Showit editor load
→ authenticated site metadata GET through api.showit.com
→ current page JSON GET from designs.showit.co/<design-key>/pages/<page-id>.json
→ S3 response ETag becomes the page-file concurrency token
→ Canvas duplication mutates page JSON locally in the browser
→ page JSON is gzip-compressed with CompressionStream("gzip")
→ POST api.showit.com/designs/<design-key>
→ payload shape { data: <whole page JSON>, file: { isNew:false, eTag:<current ETag> } }
→ server returns saved:true + next eTag
```

Important findings:

- No separate `duplicateCanvas` HTTP endpoint was observed for the tested normal page Canvas path.
- The browser-side handler duplicates the selected block locally, inserts the new block immediately after the source block, updates the page file, then saves the page file.
- Showit's block-container logic uses a 9-character random ID generator backed by `crypto.getRandomValues` and the same URL-safe alphabet used by the shipped bundle.
- Native name/slug collision handling appends `-1`, `-2`, etc. and slugifies the resulting name; the captured proof showed the next suffix chosen when an earlier suffix already existed.
- For ordinary non-WordPress page blocks, native duplication strips `wp` properties from the cloned block/elements/states before insertion.
- The current API client adds `Authorization: Bearer <token>` when a token is present; the app persists the token in localStorage. Do not copy real tokens into durable notes, generated code, logs or fixtures.
- Modern Chrome HAR exports may redact sensitive Authorization values, so HAR is sufficient for structural discovery but should not be treated as a credential source.

Mimic implication:

- Mimic remains a useful external donor for HAR/cURL/API-client discovery, but for this Showit path its current HAR endpoint reduction keeps only the latest capture per `(method, path)`, which can discard sequential whole-document state transitions that are essential to understanding editor mutations.
- Therefore the preferred next proof is a bounded in-session Showit adapter operation using the already authenticated browser context, not a Mimic-generated client.

Next acceptance gate:

```text
current authenticated Showit tab
→ discover current design/page resource without hard-coded IDs
→ read current page JSON + ETag
→ find exactly one Canvas by semantic name
→ apply the native duplicate algorithm
→ gzip + POST the whole page with current ETag
→ receive saved:true + new ETag
→ reload/read back page
→ verify exactly one expected duplicate exists and unrelated page state is unchanged
```

Until that write/readback gate passes, direct internal-API duplication is evidence-backed but not `LIVE-PROVEN`.

## 2026-09-30 — Showit Direct API Duplicate — PROVEN LIVE

Status: `LIVE-PROVEN / CURRENT ACCEPTED PROOF`.

The previously defined write/readback gate passed in the owner's real authenticated Showit Chrome session through Dramaturg JS mode.

Proof operation:

```text
semantic target: IRONLINE — PROCESS
→ discover current design key and current page resource from the live app
→ GET current page JSON from designs.showit.co
→ read current ETag
→ find exactly one Canvas by human-readable name
→ deep-copy the Canvas locally
→ generate a fresh 9-character block ID
→ generate unique name/slug
→ insert duplicate immediately after source block
→ gzip the whole page payload
→ read localStorage.authToken inside the authenticated Showit page
→ POST api.showit.com/designs/<design-key> with Authorization: Bearer <authToken>
→ server returns saved:true + new ETag
→ GET page JSON again from S3
→ durable readback verifies new block, exact name/slug, position and new ETag
→ reload editor
→ UI readback finds exactly one new Canvas
```

Accepted evidence from the live run:

- target: `IRONLINE — PROCESS`;
- created: `IRONLINE — PROCESS-1`;
- source ID: `X1yYuF3c3`;
- generated new block ID: `n_KQCJQ4K`;
- page ID: `JmaXuE-zc`;
- old ETag: `eee13e4fb46e6a060303b5f19fdb8457`;
- new ETag: `59d65ae6c1ef5d366a45bd9f71d49860`;
- durable readback passed on attempt 1;
- stored index: 7;
- total blocks after write: 11;
- editor reloaded successfully;
- UI exact-text count for the created Canvas: 1;
- final marker: `SHOWIT DIRECT API DUPLICATE — PROOF COMPLETED`.

Security rule:

- `authToken` value itself is never copied into durable notes, generated fixtures or logs.
- The adapter may read `localStorage.authToken` only inside the already-authenticated user session at execution time and send it as `Authorization: Bearer <token>` to Showit's own API.

Architecture consequence:

The Showit adapter is no longer limited to UI-click execution for this class of operation. For page-file mutations that can be expressed safely against the known page model, the preferred path is now:

```text
authenticated Showit tab
→ LOAD page JSON + ETag
→ transform whole page model locally
→ one authenticated gzip POST
→ durable S3 readback
→ editor reload / visual QA
```

This is a whole-document save model, not an element-by-element save model. A future compiler may therefore build or transform many Canvas/elements in memory and commit the page in one save, subject to preserving Showit's data-model invariants and passing readback/visual QA.

Next proof:

```text
create one new Canvas from scratch in memory
→ include multiple text/graphic elements
→ one whole-page authenticated save
→ durable readback
→ editor reload
→ visual QA
```

Do not jump directly to full-page generation until the from-scratch Canvas proof passes. Media upload remains a separate unproven capability and must be investigated independently before a full Recipe → Showit page compiler is promoted.
