# Website Creator — v0 Strict Donor Reconstruction Standard

## Status

- Scope: Website Creator donor-to-client redesign / reconstruction workflow
- Tool: v0
- State: ACTIVE / PROVEN FOR DESIGN TRANSLATION; STRICT 1:1 ACCEPTANCE STILL REQUIRES INDEPENDENT QA
- Last updated: 2026-10-01

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

## Owner Decision — Practical Fidelity Mode for Fonts

As of 2026-10-01, the owner explicitly does **not** require exact proprietary font identity when a close legal substitute is readily available.

The default production objective is therefore:

`EXACT / MEASURED LAYOUT FIDELITY + CLOSE VISUAL TYPOGRAPHIC FIDELITY`

rather than blocking the entire reconstruction on an exact commercial font face.

### Font-resolution priority

Use this order:

1. exact font when it is already available, legal, easy to load, and does not add unnecessary operational friction;
2. otherwise choose a close legal substitute with similar visual character and metrics;
3. visually tune the substitute to preserve the donor feel;
4. never extract or redistribute proprietary donor font binaries.

### Approved-substitute classification

When a substitute is intentionally used, do **not** report `EXACT FONT PASS`.

Report:

`TYPOGRAPHY: PASS WITH APPROVED SUBSTITUTE`

and record:

- donor font family;
- substitute family;
- reason for substitution;
- affected roles/elements;
- any metric adjustments made;
- post-substitution visual/geometry QA result.

### Substitute-selection criteria

Prefer a substitute that is close in:

- serif vs sans category;
- overall construction and historical/geometric character;
- stroke contrast;
- width/condensation;
- x-height/cap-height feel;
- weight;
- italic character when relevant;
- uppercase spacing behavior;
- perceived density.

### Metric-tuning rule

With an approved substitute, the donor typography values remain the starting reference, but small typography-only adjustments are allowed when necessary to recover the donor visual result:

- font-size;
- line-height;
- letter-spacing;
- font-weight within the substitute family.

Do not change page/section/gallery geometry merely to compensate for a poor substitute choice. First choose a better substitute; only then make minimal typography tuning.

### Acceptance rule

In Practical Fidelity Mode, typography passes when:

- the substitute is explicitly approved by project policy;
- no unauthorized donor font extraction is used;
- text visually matches the donor closely at accepted viewports;
- typography does not create unacceptable wrapping/overflow/geometry drift;
- owner/operator visual QA accepts the result.

An exact proprietary font is **not** a blocker in this mode.

## ZERO-GUESS PRE-FLIGHT GATE — REQUIRED BEFORE ANY STRICT 1:1 EXECUTION

This gate was added after the 2026-09-30 Family Lab → Olga Newborn proof exposed a process error: the execution prompt demanded full-page numeric parity before the TECH SPEC actually contained full-page numeric evidence. The gallery had complete RAW geometry, but header/logo/navigation/title/footer/section-boundary records were incomplete. That forced the executor to stop later and caused avoidable rework.

### Rule

**Never send a strict 1:1 implementation prompt until measurement coverage has been audited against the requested acceptance scope.**

Before execution, produce a `MEASUREMENT COVERAGE MATRIX` for every requested viewport and every page domain that will later be audited.

Minimum domains for full-page strict reconstruction:

1. PAGE / BODY
   - clientWidth
   - scrollWidth
   - document/page height
   - background
   - overflow state

2. HEADER
   - x/y/width/height
   - background/style
   - visibility state

3. BRAND / LOGO
   - x/y/width/height
   - typography or asset-box geometry
   - visibility state

4. NAVIGATION
   - containers
   - every visible nav item
   - x/y/width/height
   - typography
   - responsive visibility/state

5. PAGE TITLE / KEY TEXT
   - x/y/width/height
   - font family
   - font size
   - font weight
   - line-height
   - letter-spacing
   - alignment / transform / color

6. CONTENT / GALLERY
   - every required slot x/y/width/height
   - object-fit/object-position if applicable
   - ordering
   - visibility state

7. SECTION BOUNDARIES
   - section x/y/width/height or explicit start/end Y
   - backgrounds

8. FOOTER
   - x/y/width/height
   - child text/link geometry
   - typography
   - responsive state

9. RESPONSIVE STATE
   - each accepted viewport is its own contract
   - elements added/removed/hidden/repositioned must be captured, not inferred

10. STYLE EVIDENCE REQUIRED BY ACCEPTANCE
   - typography
   - colors/backgrounds
   - borders/radius/opacity where visible and acceptance-relevant

### Coverage matrix status values

For every domain/property use exactly one of:

- `MEASURED` — authoritative RAW value exists;
- `NOT_APPLICABLE` — element/property does not exist at that viewport;
- `MISSING_REFERENCE` — acceptance requires it but authoritative evidence is absent.

### Hard gate

If ANY property required by the requested acceptance criteria is `MISSING_REFERENCE`:

**DO NOT ISSUE THE IMPLEMENTATION PROMPT YET.**

First:

`MISSING_REFERENCE -> return to fingerprint/raw evidence -> extract measurement -> add to TECH SPEC -> re-run coverage matrix`

Only after all required rows are `MEASURED` or `NOT_APPLICABLE` may implementation begin.

### Acceptance-scope consistency rule

Do not ask the executor to prove a metric that the evidence package cannot independently specify.

Examples:

- If acceptance asks for `footer max X/Y/W/H deviation`, RAW must contain footer geometry.
- If acceptance asks for exact nav typography, RAW must contain per-element nav typography.
- If acceptance asks for responsive visibility parity, RAW must contain visibility/display state per viewport.
- If acceptance asks for full-page height parity, RAW must contain page/document height per viewport.

**Acceptance criteria and evidence coverage must be generated as a matched pair.**

### Package completeness checklist

A strict full-page TECH SPEC is not complete merely because it contains:

- screenshots;
- design notes;
- image geometry;
- overall page dimensions.

For a full-page numeric reconstruction it must also contain the non-gallery critical geometry needed by the acceptance contract.

The operator must explicitly state one of these before handing work to v0:

- `PRE-FLIGHT COVERAGE: PASS — execution may begin`
- `PRE-FLIGHT COVERAGE: BLOCKED — missing references listed below`

No silent transition from incomplete evidence to execution is allowed.

## Core Communication Pattern

Use this short authority reminder whenever v0 becomes confused:

- client images = CONTENT
- fingerprint + TECH SPEC = GEOMETRY / TYPOGRAPHY / LAYOUT / RESPONSIVE REFERENCE
- RAW CSV/JSON = machine-readable source of truth
- do not infer
- do not redesign
- do not publish

When v0 asks a question that the TECH SPEC already answers, do not paraphrase the design again. Point it to the exact canonical artifact and restate the authority split.

## One-Block Operator Rule

When the user needs a prompt to give an executor, return **one complete copy-paste block** containing every mandatory instruction.

Do not put required instructions after the block as “also add this” or “I would also tell it”.

Anything required for execution or acceptance belongs inside the single block.

Explanatory commentary may follow only if it is non-required context.

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

Strict geometry QA must compare every requested element against source measurements.

For every measured element and viewport compare:

- actual X vs expected X;
- actual Y vs expected Y;
- actual WIDTH vs expected WIDTH;
- actual HEIGHT vs expected HEIGHT.

Required final report for each audited domain:

1. maximum X deviation;
2. maximum Y deviation;
3. maximum WIDTH deviation;
4. maximum HEIGHT deviation;
5. worst offending element for each metric.

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

## Evidence Completeness Before QA

Before asking for a QA category, verify the RAW package contains the source values needed to calculate that category.

Examples:

- Gallery QA requires slot geometry RAW.
- Header QA requires header/logo geometry RAW.
- Navigation QA requires nav container/item geometry and typography RAW.
- Title QA requires title geometry and typography RAW.
- Footer QA requires footer/child geometry RAW.
- Full-page QA requires page metrics and section-boundary RAW.

If evidence is missing, the correct status is `BLOCKED BEFORE EXECUTION`, not “let the executor try and discover the gap later.”

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
- `06 — RAW Full Page Critical Geometry + Typography — 4 Viewports`

The RAW CSV and JSON were added specifically so the operator does not need to paste 252 geometry records into chat and so v0 has no reason to infer missing values.

The `06` artifact was added after the first full-page audit correctly identified that the earlier machine package covered gallery slots and page metrics but did not provide sufficient non-gallery records for header/logo/navigation/title/footer/section/typography strict acceptance.

### Incident lesson — 2026-09-30

What went wrong:

1. Gallery evidence became exact before the whole-page evidence package was complete.
2. The operator then issued a whole-page strict QA prompt.
3. v0 correctly reported `MISSING_REFERENCE` for non-gallery domains.
4. We had to return to the fingerprint and generate additional full-page RAW evidence.

Permanent prevention:

`ACCEPTANCE SCOPE -> COVERAGE MATRIX -> FILL MISSING RAW -> PRE-FLIGHT PASS -> EXECUTION PROMPT -> QA`

Never reverse that order.

## Reusable Operator Prompt Pattern

When v0 requests geometry that is already present, answer in this form:

> Open and use the authoritative RAW artifacts from the TECH SPEC folder directly. Do not calculate geometry yourself. Use literal measured values for every accepted viewport. Client assets are CONTENT ONLY. Run automated audit against every required RAW record and report X/Y/WIDTH/HEIGHT deviations. If a required acceptance property has no authoritative RAW value, report MISSING_REFERENCE and stop for that property. Do not publish.

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

`donor selection -> fingerprint -> define acceptance scope -> measurement coverage matrix -> fill missing RAW evidence -> PRE-FLIGHT PASS -> TECH SPEC -> client content/link mapping -> one-block v0 implementation prompt -> automated geometry/style audit -> independent QA -> reusable Website Creator integration -> preview -> release`

This is the preferred communication/implementation path for future strict donor reconstruction work with v0 until a stronger accepted automation replaces it.
