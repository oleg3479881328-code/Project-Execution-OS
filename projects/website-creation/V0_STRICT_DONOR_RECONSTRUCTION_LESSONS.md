# Website Creator — v0 Strict Donor Reconstruction Lessons

## Status

- Scope: Website Creator donor-to-client strict reconstruction
- Tool: v0
- State: REQUIRED COMPANION TO `V0_STRICT_DONOR_RECONSTRUCTION_STANDARD.md`
- Last updated: 2026-10-01

## Purpose

This file is the durable incident/lesson log for strict donor reconstruction. It exists so proven mistakes are converted into permanent execution rules instead of being rediscovered in later chats.

For any strict v0 donor reconstruction, read this file together with:

- `projects/website-creation/V0_STRICT_DONOR_RECONSTRUCTION_STANDARD.md`

The operating rule is:

`OBSERVED FAILURE -> ROOT CAUSE -> PERMANENT RULE -> ACCEPTANCE GATE`

No recurring mistake should remain only in chat history.

---

## Permanent Rule: One Complete MASTER Execution Block

When the operator must give v0 implementation instructions, provide one complete copy-paste MASTER block containing all currently required engineering constraints.

The MASTER block must include, when applicable:

- authority/source order;
- exact geometry sources;
- typography sources and font-loading requirements;
- responsive contracts;
- client/donor responsibility split;
- image discovery scope;
- image uniqueness rules;
- photo-to-slot assignment rules;
- crop/focal-point rules;
- link provenance rules;
- QA/acceptance criteria;
- no-publish/no-deploy boundary.

Do not split mandatory instructions into a sequence such as:

1. fix geometry;
2. later fix fonts;
3. later fix image uniqueness;
4. later fix cropping.

That pattern causes state drift and repeated rework.

Mandatory instructions must not be added after the copy block as “also tell it this”. If the instruction is required for execution, it belongs inside the one MASTER block.

---

# Incident 2026-10-01 — Typography Looked Wrong After “Correct” CSS

## Observed failure

v0 reported typography changes but the rendered page still did not visually match the donor fonts.

## Root cause

A declared CSS `font-family` is not proof that the required font face is actually loaded and being rendered.

`getComputedStyle(element).fontFamily` can still report the declared family while the browser falls back to another font.

Inherited font values from generic donor containers can also be incorrectly treated as visible-text typography.

## Permanent rules

1. Visible text typography must come from explicit visible-text RAW mapping, not generic parent/container computed styles.
2. For the Family Lab -> Olga Newborn proof, `07 — RAW Exact Typography Mapping — 4 Viewports` is the typography authority.
3. Typography PASS requires actual font availability after `await document.fonts.ready`.
4. Required face/weight/style combinations must be checked with `document.fonts.check(...)`.
5. Do not silently substitute a fallback font.
6. Do not copy or redistribute proprietary donor font binaries.
7. If a required exact font cannot legitimately be loaded, status is `FONT BLOCKED`, and strict typography remains FAIL.
8. After real fonts load, rerun geometry measurements because glyph metrics may shift width/height/line wrapping.

## Acceptance gate

Typography cannot be PASS unless:

- expected visible-text RAW properties match;
- required fonts actually load;
- no silent fallback is used;
- post-font geometry remains within the geometry tolerance.

---

# Incident 2026-10-01 — False `INSUFFICIENT UNIQUE CLIENT IMAGES: 26/63`

## Observed failure

v0 scanned only the Olga Newborn landing page and concluded that only 26 unique newborn photographs existed.

## Root cause

The inventory scope was too narrow. The landing page was treated as the entire client photo corpus even though additional Olga-owned newborn photography exists in the site’s Lifestyle Newborn category and individual posts.

## Permanent rules

Before declaring an image shortage, define and exhaust the full authorized client-image corpus.

For the current proof, discovery scope includes:

1. `https://www.olgapolophotography.com/newborn`
2. `https://www.olgapolophotography.com/blog-1/categories/lifestyle-newborn`
3. all accessible pagination pages in that category;
4. the individual Lifestyle Newborn posts;
5. actual article photographs inside those posts, not just category thumbnails.

Stop discovery only when either:

- at least the required number of verified unique client photographs has been found; or
- the entire defined authorized corpus has been exhausted.

Never report `INSUFFICIENT UNIQUE CLIENT IMAGES` after scanning only one landing page when the task explicitly permits additional client-owned sources.

## Wix normalization rule

Different Wix transformation URLs of the same underlying original asset are one photograph, not multiple photographs.

Normalize using the underlying original Wix media identity where available.

Strip/ignore transformation differences such as:

- resize dimensions;
- crop;
- fit;
- quality;
- format;
- focal point;
- derivative URL variants.

Different original Wix media IDs remain different candidates unless visual duplicate review proves they are the same photograph.

## Acceptance gate

Any image-shortage claim must include:

- source pages scanned;
- category pages scanned;
- posts discovered;
- posts opened;
- raw image URLs discovered;
- normalized unique assets;
- duplicates removed;
- non-photo assets removed;
- final verified unique count.

Without that evidence, shortage status is invalid.

---

# Permanent Rule — One Distinct Photo Per Distinct Gallery Slot

For a gallery with N distinct donor slots, use N distinct underlying client photographs whenever at least N verified unique client photographs are available.

For the current proof:

`63 distinct donor slots -> 63 distinct Olga photographs`

Allowed:

- the same assigned photo for the same slot across desktop/tablet/mobile.

Not allowed:

- the same underlying photo in two different slots;
- the same original Wix asset reused through different transformed URLs;
- different crops of the same source photo counted as unique.

## Acceptance gate

For the 63-slot proof:

- unique images used = 63;
- duplicate slot assignments = 0;
- duplicate normalized asset IDs = 0.

---

# Incident 2026-10-01 — Geometry Correct, Photographs Cropped Badly

## Observed failure

The donor slot geometry was numerically correct, but several Olga photographs were badly cut: faces/heads/people fell outside the visible slot because arbitrary photos were placed into fixed rectangles using `object-fit: cover` and generic center positioning.

## Root cause

`object-fit: cover` was treated as a complete photo-selection strategy.

It is not.

Exact donor geometry and client-photo composition are separate concerns.

## Permanent separation of authority

### Donor controls

- slot x;
- slot y;
- slot width;
- slot height;
- spacing;
- responsive slot geometry.

### Client image assignment controls

- which unique client photograph goes into which donor slot;
- which focal region of that photograph is visible inside the fixed donor rectangle.

The donor rectangle is authoritative.

The donor photograph’s focal point is NOT automatically transferable to a different client photograph.

## Permanent rules for photo-to-slot matching

1. Do not assign arbitrary images to arbitrary slots.
2. Build the unique client photo inventory first.
3. For each slot compute slot aspect ratio.
4. For each image compute intrinsic aspect ratio.
5. Use aspect compatibility as an assignment signal before rendering.
6. Prefer portrait source images for tall/narrow slots.
7. Prefer landscape source images for wide/short slots.
8. Treat assignment as a global matching problem, not a greedy one-slot-at-a-time patch.
9. A photo that crops poorly in one slot may be ideal in another.
10. Preserve visual variety when sufficient alternatives exist.
11. Never change accepted donor slot dimensions to save a poor photo assignment.
12. Never stretch/distort images.
13. Never use `contain` with empty bands merely to avoid crop.

## Crop-loss signal

A useful engineering signal is:

```text
slotAspect = slotWidth / slotHeight
imageAspect = imageWidth / imageHeight
cropRetention = min(slotAspect / imageAspect, imageAspect / slotAspect)
cropLoss = 1 - cropRetention
```

Use this for ranking assignments, not as the sole decision.

Suggested operating thresholds:

- `cropLoss <= 0.25` — preferred;
- `0.25 < cropLoss <= 0.35` — requires visual review;
- `cropLoss > 0.35` — prefer a different image unless visual review proves the crop is composition-safe.

## Subject-safe crop rules

A crop must not accidentally cut:

- primary eyes/face;
- baby face/head;
- primary parent face;
- important family members;
- the intended detail/focal subject.

If the original client image intentionally contains an artistic crop, preserve that intent where possible.

## Object-position rule

`object-fit: cover` remains the rendering mechanism.

But `object-position: 50% 50%` is only a default starting point, not a universal contract for replacement client imagery.

Content-adaptive `object-position` is allowed to preserve the client photo’s focal subject, while keeping the donor slot rectangle unchanged.

Examples may include:

- `50% 35%`;
- `42% 50%`;
- `65% 45%`.

Only focal position may change for composition safety; accepted slot x/y/width/height remain frozen.

## Acceptance gate

For every slot, crop QA should be able to report:

- slot ID;
- normalized client asset ID;
- source page/post;
- intrinsic image width/height;
- image aspect;
- slot aspect;
- crop-loss signal;
- object-position;
- subject-safe PASS/FAIL.

Photo crop quality is FAIL if:

- a primary face/head is accidentally cut;
- the important subject is pushed outside the frame;
- a clearly better compatible unused photo exists;
- a duplicate photo was reused.

---

# Permanent Rule — Geometry PASS Does Not Mean Visual/Content PASS

A page may be numerically correct and still be unacceptable.

Strict reconstruction has separate acceptance domains:

1. geometry;
2. typography + actual font loading;
3. colors/styles;
4. responsive states;
5. client link provenance;
6. image uniqueness;
7. photo-to-slot composition/crop safety;
8. donor identity leakage;
9. independent visual QA.

`PARTIAL` is not PASS for strict acceptance.

A PASS in one domain does not authorize assumptions in another domain.

---

# Updated MASTER Pre-Flight Coverage Matrix

Before issuing the MASTER implementation block, verify coverage for:

- PAGE / BODY geometry;
- HEADER geometry;
- LOGO / BRAND geometry;
- NAVIGATION geometry + visible-text typography;
- TITLE geometry + visible-text typography;
- GALLERY 63×viewport slot geometry;
- SECTION boundaries;
- FOOTER geometry + typography;
- RESPONSIVE visibility/states;
- COLORS/backgrounds;
- actual font-source/loadability status;
- client image discovery scope;
- client image uniqueness capacity;
- photo-to-slot assignment strategy;
- crop/focal safety criteria;
- real client links;
- final QA output requirements.

If a required area is absent, status is:

`PRE-FLIGHT COVERAGE: BLOCKED`

Do not hand execution to v0 and wait for it to discover the missing engineering input later.

---

# Updated Generalized Workflow

Use this order:

`donor selection`
`-> fingerprint`
`-> define acceptance scope`
`-> measurement coverage matrix`
`-> fill missing RAW evidence`
`-> typography availability check`
`-> authorized client-image corpus definition`
`-> exhaustive/threshold image inventory`
`-> unique-image normalization`
`-> photo-to-slot composition plan`
`-> PRE-FLIGHT PASS`
`-> ONE MASTER EXECUTION BLOCK`
`-> implementation`
`-> geometry audit`
`-> actual-font audit`
`-> duplicate-image audit`
`-> crop/focal safety audit`
`-> link/provenance audit`
`-> independent visual QA`
`-> preview`
`-> release only after owner authorization`

---

# Current Family Lab -> Olga Newborn Required Artifacts

TECH SPEC folder:

`https://drive.google.com/drive/folders/1Eh4O80ZBIgwWB7mb7fZ_qzx9OFaFS_vD`

Current authoritative artifacts include:

- `03-RAW-Exact-Image-Slot-Geometry-63x4.csv` — gallery slot geometry;
- `04-RAW-Machine-Exact-Layout-Spec.json` — machine/page contract;
- `06 — RAW Full Page Critical Geometry + Typography — 4 Viewports` — non-gallery critical geometry/styles;
- `07 — RAW Exact Typography Mapping — 4 Viewports` — visible-text typography.

The operator must treat these as separate authority domains rather than mixing inherited values across them.

---

# Operator Discipline

When a new failure is observed during this proof or future proofs:

1. do not only patch the current v0 prompt;
2. identify the failure class;
3. decide whether it generalizes;
4. update this lesson log and/or the canonical strict standard;
5. add a pre-flight or acceptance gate that prevents recurrence.

The goal is cumulative system improvement: every confirmed failure should make the next project easier, not merely make the current page pass.