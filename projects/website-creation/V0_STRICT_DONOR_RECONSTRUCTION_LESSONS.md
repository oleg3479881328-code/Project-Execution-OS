# Website Creator — v0 Strict Donor Reconstruction Lessons

## Status

- Scope: Website Creator donor-to-client strict reconstruction
- Tool: v0
- State: REQUIRED COMPANION TO `V0_STRICT_DONOR_RECONSTRUCTION_STANDARD.md`
- Last updated: 2026-10-01

## Purpose

This file is the durable incident/lesson log for strict donor reconstruction. It exists so proven mistakes are converted into permanent execution rules instead of being rediscovered in later chats.

Operating rule:

`OBSERVED FAILURE -> ROOT CAUSE -> PERMANENT RULE -> PRE-FLIGHT/ACCEPTANCE GATE`

No recurring mistake should remain only in chat history.

---

## Permanent Rule — One Complete MASTER Execution Block

When the operator must give v0 implementation instructions, provide one complete copy-paste MASTER block containing all currently required engineering constraints.

The MASTER block must include, when applicable:

- authority/source order;
- exact geometry sources;
- typography sources and real font-verification requirements;
- responsive contracts;
- client/donor responsibility split;
- image discovery scope;
- image uniqueness rules;
- photo-to-slot assignment rules;
- visual crop/focal-point rules;
- link provenance rules;
- QA/acceptance criteria;
- no-publish/no-deploy boundary.

Do not split mandatory instructions into a sequence of later patches such as geometry -> fonts -> uniqueness -> cropping. Mandatory instructions must not be added after the copy block as “also tell it this”.

---

# Incident — Strict full-page QA requested before RAW evidence was complete

## Observed failure

Gallery geometry was fully measured, but whole-page geometry/typography evidence was incomplete. A full-page numeric QA prompt was issued too early.

## Root cause

Acceptance scope was broader than the available evidence package.

## Permanent rule

Before execution, produce a measurement coverage matrix for every required viewport and domain:

- page/body;
- header;
- logo/brand;
- navigation;
- title/key text;
- gallery/content slots;
- section boundaries;
- footer;
- responsive visibility/states;
- typography/styles/colors required by acceptance.

Allowed coverage states:

- `MEASURED`
- `NOT_APPLICABLE`
- `MISSING_REFERENCE`

If any required acceptance property is `MISSING_REFERENCE`, do not issue the strict implementation prompt yet.

Permanent order:

`ACCEPTANCE SCOPE -> COVERAGE MATRIX -> FILL MISSING RAW -> PRE-FLIGHT PASS -> EXECUTION -> QA`

---

# Incident — Typography looked wrong after “correct” CSS

## Observed failure

v0 reported the expected `font-family`, but the rendered page still did not visually match the donor typography.

## Root causes

1. Declared `font-family` is not proof of the face actually rendered.
2. `getComputedStyle(...).fontFamily` reports the declared family list and does not prove which fallback glyph face painted the text.
3. Generic parent/container computed styles were being confused with visible-text typography.
4. A previous process rule incorrectly treated `document.fonts.check(...) === true` as sufficient proof that a specific face exists and is loaded.

## Important correction — `document.fonts.check()` is NOT proof of existence

MDN documents that `FontFaceSet.check()` may return `true` even when the requested font is nonexistent, because the method answers whether rendering would require an unloaded font from the document `FontFaceSet`; it is not a reliable “does this exact font exist?” test.

Therefore:

**Never use `document.fonts.check()` alone as proof of exact font availability or exact font rendering.**

## Permanent font verification contract

For each required web font family/weight/style:

1. Visible text properties come from the explicit visible-text RAW mapping, not generic container inheritance.
2. Wait for `await document.fonts.ready`.
3. Enumerate `document.fonts` and require a matching `FontFace` entry for the expected family.
4. Require the matching face entry/entries to have `status === "loaded"`.
5. Call `await document.fonts.load(spec, representativeText)` and require a **non-empty returned FontFace array** matching the expected family/weight/style for web fonts.
6. Compare the actual element `getComputedStyle()` values to the RAW typography contract.
7. Run geometry regression after font load because real glyph metrics can change widths, heights and wrapping.
8. Perform visual comparison against donor evidence for typography-sensitive regions.

For proprietary families such as `freight-display-pro`, `futura-pt`, and `baskerville-poster-pt`:

- use only a legitimate configured/authorized font source already available to the project;
- do not copy or redistribute donor font binaries;
- if the exact face cannot legitimately be loaded, report `FONT BLOCKED: <family>` and keep strict typography FAIL.

## Acceptance gate

Typography cannot be PASS unless:

- visible-text RAW properties match;
- matching loaded FontFace evidence exists for required web fonts;
- `document.fonts.load()` returns the expected matching face(s), not an empty fallback result;
- no silent fallback is used;
- post-font geometry stays within tolerance;
- visual typography comparison is acceptable.

---

# Incident — False `INSUFFICIENT UNIQUE CLIENT IMAGES: 26/63`

## Observed failure

v0 scanned only the Olga Newborn landing page and concluded that only 26 unique newborn photographs existed.

## Root cause

The inventory scope was too narrow. The landing page was treated as the entire client photo corpus even though additional Olga-owned newborn photography exists in the site’s Lifestyle Newborn category and individual posts.

## Permanent discovery rule

Before declaring shortage, define and exhaust the authorized client-image corpus.

For the current proof, discovery scope includes:

1. `https://www.olgapolophotography.com/newborn`
2. `https://www.olgapolophotography.com/blog-1/categories/lifestyle-newborn`
3. all accessible pagination pages in that category;
4. individual Lifestyle Newborn posts;
5. actual article photographs inside those posts, not just category thumbnails.

Stop discovery only when either:

- at least the required number of verified unique client photographs has been found; or
- the entire authorized corpus has been exhausted.

## Wix normalization rule

Different Wix transformation URLs of the same underlying original asset are one photograph, not multiple photographs. Normalize by original Wix media identity where available and ignore resize/crop/fit/quality/format/focal/derivative URL differences.

Different original Wix media IDs remain separate candidates unless visual duplicate review proves they are the same photograph.

## Acceptance gate

Any image-shortage claim must include:

- source pages scanned;
- category pages scanned;
- posts discovered/opened;
- raw image URLs discovered;
- normalized unique assets;
- duplicates removed;
- non-photo assets removed;
- final verified unique count.

---

# Permanent Rule — One Distinct Photo Per Distinct Gallery Slot

For a gallery with N distinct donor slots, use N distinct underlying client photographs whenever at least N verified unique client photographs are available.

Current proof:

`63 donor slots -> 63 distinct Olga photographs`

Allowed:

- same assigned photograph for the same slot across desktop/tablet/mobile.

Not allowed:

- same underlying photograph in two different slots;
- same Wix original reused through different transformation URLs;
- different crops of the same source photograph counted as unique.

Acceptance for the current proof:

- unique images used = 63;
- duplicate slot assignments = 0;
- duplicate normalized asset IDs = 0.

---

# Incident — Geometry correct, photographs cropped badly

## Observed failure

Donor slot geometry was numerically correct, but several Olga photographs were visibly damaged by crop: faces/heads/subjects fell outside fixed rectangles.

## Root cause

`object-fit: cover` and aspect-ratio matching were treated as sufficient photo-placement logic.

They are not.

Exact donor geometry and client-photo composition are separate concerns.

## Permanent authority separation

### Donor controls

- slot x/y/width/height;
- spacing;
- responsive geometry.

### Client-image assignment controls

- which unique client photograph goes into each fixed donor slot;
- focal position inside that slot.

The donor rectangle is authoritative.

The donor photograph’s original focal point is not transferable to unrelated client imagery.

## Aspect-ratio matching is only a ranking signal

Use:

```text
slotAspect = slotWidth / slotHeight
imageAspect = imageWidth / imageHeight
cropRetention = min(slotAspect / imageAspect, imageAspect / slotAspect)
cropLoss = 1 - cropRetention
```

This is useful for candidate ranking only.

It cannot detect:

- face position;
- baby/head position;
- multiple-person composition;
- subject near an edge;
- intentional negative space;
- whether a narrow crop destroys the story.

Therefore `cropLoss <= threshold` is never sufficient by itself for crop PASS.

Suggested prioritization only:

- `cropLoss <= 0.25` — preferred candidate pool;
- `0.25 < cropLoss <= 0.35` — high-priority visual review;
- `cropLoss > 0.35` — normally reassign unless visual inspection proves safe.

## New permanent rule — Visual crop QA is required for ALL slots

Do not visually review only slots above a crop-loss threshold.

**All 63 rendered slots must receive visual subject-safety review.**

Reason: a low crop-loss image can still cut a face if the subject is near the source-image edge.

Recommended workflow:

1. Build a labeled contact sheet or equivalent overview of all rendered slots.
2. Review every slot, not only high-cropLoss slots.
3. Mark each slot `SUBJECT_SAFE PASS/FAIL`.
4. For a FAIL slot, first search/reassign a better compatible unused image from the full client corpus.
5. Use content-adaptive `object-position` only when the subject can genuinely be saved inside the fixed rectangle.
6. Do not use focal shifting to rescue a fundamentally incompatible composition.
7. Re-run uniqueness and geometry after reassignment.

## Subject-safe rules

A crop must not accidentally cut:

- primary eyes/face;
- baby face/head;
- primary parent face;
- important family members;
- intended focal detail.

If the original client image intentionally contains an artistic crop, preserve that intent where possible.

## Object-position rule

`object-fit: cover` remains the rendering mechanism.

`object-position: 50% 50%` is only a default starting point for replacement client imagery.

Content-adaptive `object-position` is allowed to preserve the client photo’s focal subject while donor slot x/y/width/height remain frozen.

Examples:

- `50% 35%`
- `42% 50%`
- `65% 45%`

## Acceptance gate

For every slot record:

- slot ID;
- normalized asset ID;
- source page/post;
- intrinsic image dimensions;
- image aspect;
- slot aspect;
- crop-loss signal;
- object-position;
- `subjectSafe: PASS/FAIL`.

Photo crop quality remains FAIL if **any** slot is visually unsafe.

---

# Permanent Rule — Geometry PASS Does Not Mean Visual/Content PASS

Strict reconstruction has separate acceptance domains:

1. geometry;
2. typography + verified real font faces;
3. colors/styles;
4. responsive states;
5. client link provenance;
6. image uniqueness;
7. photo-to-slot composition/crop safety;
8. donor identity leakage;
9. independent visual QA.

`PARTIAL` is not PASS for strict acceptance.

A PASS in one domain does not authorize assumptions in another.

---

# Current Family Lab -> Olga Newborn Required Artifacts

TECH SPEC folder:

`https://drive.google.com/drive/folders/1Eh4O80ZBIgwWB7mb7fZ_qzx9OFaFS_vD`

Current authority domains:

- `03-RAW-Exact-Image-Slot-Geometry-63x4.csv` — gallery slot geometry;
- `04-RAW-Machine-Exact-Layout-Spec.json` — machine/page contract;
- `06 — RAW Full Page Critical Geometry + Typography — 4 Viewports` — non-gallery geometry/styles;
- `07 — RAW Exact Typography Mapping — 4 Viewports` — visible-text typography.

Do not mix authority domains or substitute inferred container values for explicit visible-element data.

---

# Updated MASTER Pre-Flight Coverage Matrix

Before issuing a MASTER implementation block, verify coverage for:

- page/body geometry;
- header geometry;
- logo/brand geometry;
- navigation geometry + visible-text typography;
- title geometry + visible-text typography;
- gallery slot geometry;
- section boundaries;
- footer geometry + typography;
- responsive visibility/states;
- colors/backgrounds;
- legitimate exact font-source/loadability status;
- authorized client-image corpus;
- client image uniqueness capacity;
- photo-to-slot assignment strategy;
- visual crop/focal safety for all slots;
- real client links;
- QA output requirements.

If a required area is absent:

`PRE-FLIGHT COVERAGE: BLOCKED`

---

# Updated Generalized Workflow

`donor selection`
`-> fingerprint`
`-> define acceptance scope`
`-> coverage matrix`
`-> fill missing RAW`
`-> exact font source/loadability proof`
`-> authorized client-image corpus definition`
`-> image inventory`
`-> unique-image normalization`
`-> global aspect-compatible photo assignment`
`-> render all slots`
`-> visual subject-safety review of ALL slots`
`-> PRE-FLIGHT/implementation readiness`
`-> ONE MASTER EXECUTION BLOCK`
`-> implementation`
`-> geometry audit`
`-> real-font audit`
`-> duplicate-image audit`
`-> all-slot crop/focal audit`
`-> link/provenance audit`
`-> independent visual QA`
`-> preview`
`-> release only after owner authorization`

---

# Incident — Executor crop QA passed; exact font sources are the remaining strict blocker

## Observed result

The executor reported:

- `239` verified unique Olga photo candidates;
- `63` distinct slot assignments;
- `0` duplicate assignments;
- crop-review sheets for all four accepted viewports;
- `252/252` rendered crop states reviewed with `0` unsafe states reported;
- gallery geometry PASS;
- non-gallery geometry PASS;
- colors and responsive states PASS;
- zero actual matching loaded `FontFace` entries for all four required families;
- overall strict 1:1 FAIL because exact typography cannot yet be rendered from legitimate project font sources.

## Permanent lesson — executor visual PASS is not final acceptance

An executor-produced contact sheet and self-reported `PHOTO CROP QUALITY: PASS` are evidence, not owner/operator acceptance.

Before release, independently inspect the rendered review sheets or equivalent viewport captures.

## Permanent lesson — font-source availability is a pre-flight dependency

Before strict execution begins, create a `FONT SOURCE MATRIX` for every required family/weight/style containing:

- exact family/web name;
- required weight;
- required style;
- page role(s);
- provider/source;
- licensing mode;
- web-use mechanism;
- project access available YES/NO;
- expected browser proof method;
- status `READY`, `NOT_APPLICABLE`, or `BLOCKED`.

If any required row is `BLOCKED`, strict typography is blocked before implementation. Do not discover this only after geometry/content work is complete.

## Legitimate resolution paths for the current proof

- `Cormorant Garamond` has a legitimate Google Fonts / OFL path and can be integrated without copying donor-hosted files.
- `Futura PT` is available through Adobe Fonts; for website use, use an Adobe Fonts Web Project/embed code or another separately licensed authorized webfont source.
- Freight / `freight-display-pro` is available through Adobe Fonts; use an Adobe Fonts Web Project/embed code where the required face/weight is included, or another separately licensed authorized source.
- `Baskerville Poster PT` is a commercial ParaType family with Webfont licensing available from authorized sellers such as MyFonts. Do not assume it is covered by another provider until verified.

## Adobe-hosted font ownership rule

For production client sites using Adobe Fonts, the durable production setup should use the client’s own qualifying Adobe/Creative Cloud subscription and Web Project/embed code. Do not make a client production site depend indefinitely on an unrelated operator’s Adobe account.

## No donor-font extraction

Never resolve this blocker by extracting, copying, self-hosting, or redistributing proprietary donor font binaries.

---

# Operator Discipline

When a new failure is observed:

1. do not only patch the current prompt;
2. identify the failure class;
3. determine whether it generalizes;
4. update this lesson log and/or the canonical strict standard;
5. add a pre-flight or acceptance gate that prevents recurrence.

Goal: every confirmed failure makes the next reconstruction easier and safer, rather than merely fixing the current page.