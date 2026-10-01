# Website Creator — Numeric Donor Layout Mode

## Status

- Scope: donor-to-client reconstruction when the owner wants donor-like design by measured numbers, but client photographs must remain uncropped and natural-ratio.
- State: ACTIVE / REUSABLE
- Added: 2026-10-01

## Core rule

When authoritative RAW geometry exists, do **not** re-measure the donor from screenshots and do not replace measured values with visual estimates.

Source priority:

`RAW fingerprint geometry > normalized TECH SPEC > screenshots/overlays as QA only`

Screenshots are for validation. They are not allowed to override authoritative numeric geometry.

## Why this mode exists

Strict slot playback with `object-fit: cover` preserves donor rectangles but can destroy client photographs.

Fixed-height slots with `object-fit: contain` preserve photographs but create letterboxing and lose the donor's rhythm.

Numeric Donor Layout Mode keeps the donor's measurable composition while allowing each client photograph to keep its natural aspect ratio.

## What remains numeric / donor-controlled

For every accepted viewport preserve from RAW:

- gallery start position;
- column count;
- column X positions;
- column widths;
- horizontal gutters;
- first-item Y for each column;
- vertical gap rhythm;
- header geometry;
- nav geometry;
- title geometry;
- section boundaries where compatible with natural content;
- responsive margins/column state.

## What becomes content-controlled

For gallery photographs:

- intrinsic aspect ratio;
- natural rendered height;
- photo identity;
- one visual block = one actual single-frame photograph.

Do not force client photographs back into donor image heights.

## Natural-ratio rendering

Use one image per visual block:

```css
img {
  display: block;
  width: 100%;
  height: auto;
}
```

No destructive crop. No `object-fit: cover`. No fixed image height. No diptych/collage assets when the owner requests one photograph per block.

## Donor-rhythm matching without crop

Use each donor slot's measured aspect ratio as a **selection target**, not a crop box.

For donor slot `s`:

```text
targetAspect = donorWidth / donorHeight
imageAspect  = intrinsicWidth / intrinsicHeight
matchScore   = abs(log(imageAspect / targetAspect))
```

Globally assign unique client photographs to donor slots to minimize aspect mismatch while preserving single-frame provenance and visual variety.

Then render each assigned photograph at the measured donor column width with natural height.

For each independent column:

```text
nextY = previousRenderedBottom + donorVerticalGap
```

This preserves donor-like stagger/rhythm without cutting the client image.

## Family Lab -> Olga Newborn numeric proof

Authoritative source: `03-RAW-Exact-Image-Slot-Geometry-63x4.csv`.

At desktop 1440 the RAW donor geometry shows:

- column 1 X = `240.8`
- column 2 X = `566.525`
- column 3 X = `892.25`
- column width = `291.725`
- horizontal gutter = `34.0`
- column 1 first Y = `554.288`
- column 2 first Y = `565.938`
- column 3 first Y = `554.288`
- normal vertical gap between successive donor slots = `34.0`

Therefore any screenshot-derived claim such as “donor gallery is nearly full viewport”, “353px columns”, or “10px gutters” conflicts with the authoritative RAW and must be rejected.

At desktop 1200:

- X = `240.8`, `486.525`, `732.25`
- width = `211.725`
- gutter = `34.0`
- first Y approximately `585.413`, `590.788`, `585.413`

At tablet 1024:

- X approximately `64.8`, `369.188`, `673.576`
- width = `270.388`
- gutter approximately `34.0`

At mobile 390:

- one column
- X = `20.8`
- width = `333.6`
- natural-ratio images stacked vertically.

## Header / title authority

Use full-page RAW (`06`) and typography RAW (`07`) directly rather than screenshot estimates.

For the Family Lab desktop-1440 proof, examples include:

- top header: `x=0.8, y=0.8, w=1423.2, h=266.0`
- bottom header: `x=0.8, y=266.8, w=1423.2, h=54.0`
- primary nav container: `x=271.925, y=300.8, w=385.575, h=20.0`
- title wrapper: `x=240.8, y=419.288, w=943.2, h=33.0`

Do not replace these with screenshot guesses such as nav `y≈87` or gallery start `≈345` when authoritative RAW says otherwise.

## QA rule

Numeric build first, screenshots second.

Required order:

`RAW -> implementation -> measured regression -> same-viewport screenshot/overlay -> owner visual acceptance`

Never:

`screenshot estimate -> guessed numbers -> implementation`

when RAW exists.

## Permanent acceptance principle

A reconstruction can be numerically donor-faithful and still fail visual QA, but visual QA must diagnose differences **without corrupting known-good numeric geometry**.

When a visual mismatch appears:

1. verify the implementation against RAW;
2. if implementation differs from RAW, fix it numerically;
3. if implementation matches RAW, inspect content-selection, typography, asset composition, or a deliberate mode change;
4. do not invent replacement geometry from screenshots unless the RAW is proven stale or wrong.
