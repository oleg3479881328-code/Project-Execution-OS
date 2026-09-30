# Website Creator — v0 Strict Donor Reconstruction Standard

## Status

- Scope: Website Creator donor-to-client redesign / reconstruction workflow
- Tool: v0
- State: ACTIVE / PROVEN FOR DESIGN TRANSLATION; STRICT 1:1 ACCEPTANCE STILL REQUIRES INDEPENDENT QA
- Last updated: 2026-09-30

## Purpose

This standard captures the exact working communication pattern for using v0 as a design translator / donor builder without allowing it to improvise away from measured evidence.

The objective is not “make something inspired by this site.”

The objective is:

`DONOR DESIGN EVIDENCE + CLIENT CONTENT/ASSETS/LINKS -> IMPLEMENTATION THAT REPLAYS THE DONOR GEOMETRY`

## Authority Split

### Donor site provides only

- geometry;
- typography;
- spacing;
- image-slot dimensions;
- layout rhythm;
- responsive behavior;
- motion/hover behavior when captured;
- structural visual composition.

### Client site provides only

- client photos;
- client content;
- client brand identity;
- client factual claims;
- client contact data;
- client real links / URL destinations.

### v0 role

v0 is the implementation layer.

It is not allowed to become design authority when exact donor evidence exists.

## Core Communication Pattern

Use this short authority reminder whenever v0 becomes confused:

- client images = CONTENT
- fingerprint + TECH SPEC = GEOMETRY / TYPOGRAPHY / LAYOUT / RESPONSIVE REFERENCE
- RAW CSV/JSON = machine-readable source of truth
- do not infer
- do not redesign
- do not publish

When v0 asks a question that the TECH SPEC already answers, do not paraphrase the design again. Point it to the exact canonical artifact and restate the authority split.

## What v0 Must Never Do In Strict 1:1 Mode

Do not allow v0 to:

- “improve” the donor;
- reinterpret or modernize the donor;
- simplify the layout;
- invent missing geometry;
- infer slot dimensions from screenshots when measured values exist;
- use client-image native aspect ratios to determine slot height;
- normalize image heights;
- align independently measured images into shared rows;
- substitute a conventional CSS Grid for measured donor geometry;
- substitute CSS columns / generic masonry logic for measured donor geometry;
- interpolate captured viewport geometry when the exact target viewport is part of the acceptance set;
- claim PASS from image count, no overflow, or no console errors alone;
- copy donor photos, donor logo, donor copy, donor business identity, or donor links into the client page;
- publish/deploy before geometry QA passes and the owner authorizes publishing.

## Important Failure Pattern: “Masonry” Is Too Ambiguous

The word `masonry` is insufficient for strict reconstruction.

Observed failure pattern:

1. v0 is told “three masonry columns.”
2. It correctly creates three visually independent columns.
3. It still calculates image flow/heights mechanically from its own algorithm or from client-image aspect ratios.
4. The result looks plausible but is not the donor geometry.

Therefore, in strict 1:1 mode do not rely on the word `masonry` as the implementation contract.

The correct model is literal geometry playback.

## Literal Geometry Playback Contract

For the current Family Lab Portfolio proof:

`63 donor image rectangles × 4 captured viewports = 252 explicit geometry states`

For every slot and every viewport, v0 must use the exact measured:

- `x`
- `y`
- `width`
- `height`

No slot height may be derived from the client image.

Client images are content only.

Image placement rule:

```css
slot {
  /* exact measured x/y/width/height */
}

slot img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 50%; /* unless measured evidence says otherwise */
}
```

For maximum fidelity, explicit positioning is allowed/preferred when needed:

- gallery container: `position: relative`;
- slot: explicit measured position and size;
- image fills the exact slot rectangle.

Coordinates may be normalized internally relative to a gallery origin, but final rendered geometry must match the measured donor coordinates.

## Responsive Contract

Treat each captured viewport as an explicit measured state.

Current proof viewports:

- desktop 1440 × 1000;
- desktop 1200 × 900;
- tablet 1024 × 900;
- mobile 390 × 844.

Do not assume one generic responsive formula is sufficient for acceptance.

At mobile 390, all image slots may form one vertical flow only if the measured mobile geometry says so. Even then, each slot keeps its own exact measured height.

## Geometry QA Contract

Strict geometry QA must compare every slot against source measurements.

For every slot and viewport compare:

- actual X vs expected X;
- actual Y vs expected Y;
- actual WIDTH vs expected WIDTH;
- actual HEIGHT vs expected HEIGHT.

Required final report:

1. maximum X deviation;
2. maximum Y deviation;
3. maximum WIDTH deviation;
4. maximum HEIGHT deviation;
5. worst offending slot for each metric.

Current proof acceptance target:

`max deviation <= 1 CSS px`

for all four metrics.

If HEIGHT is not measured and reported, geometry QA is incomplete.

Secondary checks such as:

- correct image count;
- no horizontal overflow;
- no console errors;
- correct column count;

are useful but do not replace geometry parity.

## Client-Link Preservation Rule

When redesigning an existing client site:

- preserve meaningful real client destinations;
- do not invent `#` placeholders;
- do not guess email, phone, social, gallery, service, or contact URLs;
- preserve unusual historical slugs when they are the live source destinations;
- remove donor links;
- remove platform-owned/system links that are not meaningful client destinations;
- map old link FUNCTION and DESTINATION into the new visual layout rather than preserving old visual placement.

## Olga Polo / The Family Lab Proof

### Design donor

`https://thefamilylab.com/portfolio`

### Client content source

`https://www.olgapolophotography.com/newborn`

### TECH SPEC folder

`https://drive.google.com/drive/folders/1Eh4O80ZBIgwWB7mb7fZ_qzx9OFaFS_vD`

Key artifacts:

- `00 — START HERE — v0 Strict 1:1 Reconstruction Contract`
- `01 — Technical Design Spec — Geometry Typography Responsive`
- `02 — QA Acceptance — Strict 1:1`
- `03 — Exact Image Slot Geometry — 63×4 Viewports`
- `04 — Machine Exact Layout Spec — Full Normalized Data`
- `05 — v0 EXECUTION PROMPT — Paste as One Block`
- `03-RAW-Exact-Image-Slot-Geometry-63x4.csv`
- `04-RAW-Machine-Exact-Layout-Spec.json`

The RAW CSV and JSON were added specifically so the operator does not need to paste 252 geometry records into chat and so v0 has no reason to infer missing values.

## Reusable Operator Prompt Pattern

When v0 requests the geometry again, answer in this form:

> Open and use the RAW CSV/JSON from the TECH SPEC folder directly. Do not calculate geometry yourself. For every slot and every captured viewport, use literal x/y/width/height values. Client images are CONTENT ONLY and must be cropped inside those exact donor rectangles. Run automated geometry audit across all records and report max X/Y/WIDTH/HEIGHT deviation plus the worst slot for each metric. Do not publish.

## Acceptance Boundary

A v0 self-report is evidence, not independent acceptance.

Before Website Creator promotes a strict reconstruction to accepted production capability, independently verify:

- code structure;
- links;
- image provenance;
- build;
- responsive render;
- geometry parity;
- visual parity;
- no unsupported factual claims;
- no donor identity leakage.

## Generalized Workflow

`donor selection -> fingerprint -> TECH SPEC -> RAW machine geometry -> client content/link mapping -> v0 implementation -> automated geometry audit -> independent QA -> reusable Website Creator integration -> preview -> release`

This is the preferred communication/implementation path for future strict donor reconstruction work with v0 until a stronger accepted automation replaces it.
