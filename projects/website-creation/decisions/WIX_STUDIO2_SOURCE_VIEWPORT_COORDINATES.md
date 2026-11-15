# Wix Studio 2 — mapping source viewport coordinates to editor canvas

Status: Verified for the Vesper donor capture and My Site 33 native editable page (2026-11-15). This is a reusable mapping method, **not** a claim that every source site uses 15 px scrollbars.

## Scope and evidence

- Source: LocalDesign Vesper capture from https://vesper.tonicsiteshop.com/, source `div#brand-bio`, viewport `1280 CSS px` (and 1920 px supplementary capture).
- Native target: Wix Studio 2, My Site 33, 1280 px desktop editor/canvas.
- Source measured content/section width: **1265 px** at a viewport width of 1280 px.
- The 15 px difference is consistent with vertical browser scrollbar occupancy, but the scrollbar mechanism should be independently confirmed by reading `window.innerWidth - document.documentElement.clientWidth`; do not treat 15 px as a universal constant.
- Wix target coordinate system is **1280 px**, with centered 1265 px reference content. Offset = `(1280 - 1265) / 2 = 7.5 px`.

## Accepted desktop transformation (for this capture only)

For horizontal coordinates measured relative to the left edge of a 1265px source section, and when that section should be centered in a 1280px Wix editor canvas:

```text
x_target = x_source_section + (W_target_canvas - W_source_section) / 2
x_target = x_source_section + 7.5px  // only when Wtarget=1280 and Wsource=1265
width_target = width_source // for measured fixed-size desktop boxes
```

Example native Wix Desktop 1280 browser geometry:
- left photo: source x=-155.5, target x=-148; both 308x476
- center photo: source x=253.5, target x=261; both 360x268
- right photo: source x=763.5, target x=771; both 469x638
- heading: source x=169.5, target x=177; both 926x196
- italic 'for': source x=251.5, target x=259; both 89x51

**These +7.5 px horizontal differences are not a layout defect. Do not subtract the offset again.** The previous interpretation as a 7.5px horizontal mistake is superseded.

## Important separate coordinate systems

- `page Y`, `section Y`, `viewport Y`, `group X/Y` are distinct; never use page Y as section-local Y.
- Browser viewport width (1280) is not guaranteed to equal source document's content width (1265).
- Compare centered relative coordinates, not raw screenshot X from canvases with different content widths.
- For source desktop positions with constant box widths at 1280/1440/1920, retain CSS-pixel box sizes and center their X positions rather than scaling widths with the viewport.
- **Vertical dimensions are an independent QA concern.** Earlier Wix preview on Desktop 1280 rendered the first hero section about 922px high against the 911px LocalDesign measurement because `--spx-ref-width:1265` scales `--spx(911)` at a 1280px viewport. A correct X-center calculation does not fix this Y/height discrepancy. Validate section heights and page totals separately before acceptance.
- Mobile is independent. The LocalDesign Mobile 390 capture defines its own element geometry, font treatments and visibility; do not derive Mobile by uniformly shrinking Desktop.

## QA / acceptance

1. On original source at exact viewport, record `innerWidth`, `documentElement.clientWidth`, source section `getBoundingClientRect()`, and element bounds; note actual scrollbar width.
2. On Wix 1280 canvas/preview, measure corresponding native element bounds; normalize X positions to their respective section/container centers.
3. Verify box width/height individually and screenshot positioning; check typography and cropping.
4. Independently compare section/page Y positions and heights, responsive layout at 390, and real rendered screenshots. A successful import or HTTP 200 is not visual acceptance.
5. Never silently apply the 7.5px delta to other projects unless measured widths support it.

## Implementation / source of truth

Project-specific instance: Wix Studio 2 site `83b1f529-47e8-4537-8d70-0168eef64789`, page `c1dmp` ('My Site 33'), Vesper donor. Current native geometry is centered already; do not move those five elements in X merely to match unnormalized source screenshot X.

## Verified Wedding Experience calibration (2026-11-15)

This is a tested instance of the general geometric acceptance procedure, not a pixel-perfect typography claim.

- Donor at browser viewport 1280×911: `#experience` section Y=2163, height 729 px. Foreground couple/Nosara: X=669 Y=2307 W=280 H=414. Background Martin/texture: X=763 Y=2229 W=360 H=575.
- Wix native preview at the same viewport after applying fixed-pixel Desktop rules: section Y=2162 height=729 px; foreground X=669 Y=2306 W=280 H=414; background X=763 Y=2228 W=360 H=575. All photo dimensions and X positions match exactly; all observed page Y values differ by -1 px from the donor due to the upstream cumulative section position.
- Four source text-field boxes (relative to screen at 1280) were `(x,y,w,h)`: `the=(171,2308,138,47)`, headline `(169,2311,405,129)`, paragraph `(167,2450,386,185)`, link/button `(167,2679,183,18)`. Wix native text boxes now have exactly matching X/W/H, with page Y -1 px. Font shapes/text internal line-breaks are explicitly outside this geometry gate.
- Foreground couple overlaps background texture and is above it in Wix's actual browser hit-test; photos are separately editable Wix Image components and use the donor asset images.
- Desktop CSS implementation: keep fixed measured width/height in px, express X as `margin-left: calc(50% + centerOffsetPx)`, section-local top as a fixed px offset, and set section height to measured 729px. For this section, texture/photo-back offset = `+123px` from center, Y=66; couple/photo-front offset = `+29px`, Y=144. The mobile breakpoint retains its own existing geometry and is not inferred from Desktop.
- Additional probe at 1920px after correction: section height=729; both photos have accurate local geometry (foreground x=989 y=section+144, back x=1083 y=section+66), but section page Y is **2716.81** in Wix vs **2163** at the donor. Therefore **full-page absolute vertical parity at 1920 is NOT accepted**: earlier sections still accumulate responsive scaling differences.
- Wix native editor import succeeded as **site revision 19**, site `83b1f529-47e8-4537-8d70-0168eef64789`, unpublished. Wix lint passed. Legacy TypeScript type errors for Image `id` fields remain a separate, known import warning. Editor GUI field readback was not automated; the implementation was validated via native source + real preview DOM.

### Reusable acceptance distinction

A section can pass **LOCAL_GEOMETRY** (relative X/Y/W/H, z-order, independent breakpoint) while failing **PAGE_GEOMETRY** (absolute Y because earlier section heights differ). Record them as separate statuses. Never move individual children to compensate for a parent section's wrong page Y. Compare same viewport, browser client width, zoom and scroll state, and use real computed DOM geometry after Wix import as well as before it.


## Wix Studio 2 native test page `/blank` — resolved Aria responsive scaling (2026-11-15)

**Test context:** My Site 33, Wix page `/blank` (page ID `v9wbz`), independently editable Image elements `comp-mwia7xuh` and `comp-mwia7xvg`. This was a narrower geometry-only test, with two original Vesper image assets reused from Wix Media Manager. Wix Studio AI Aria had made image widths `28.13%` and `21.88%` with `align-self:end`, `justify-self:end`, responsive margins and aspect ratios; at 1920 browser width these produced 416.81×616.28 and 535.88×855.91 instead of 280×414 and 360×575.

**Accepted native layout fix:** exported site fresh (not the stale Home-only working copy), modified only the existing `pages/blank/layout.css` and `structure.jsx`, kept page and component IDs and existing mobile breakpoint, and imported via official `wix origami import-site`.

- Section remains 729px high on Desktop.
- Back Martin/texture (`comp-mwia7xuh`): `width:360px;height:575px;grid-row:1/2;grid-column:1/2;align-self:start;justify-self:start;margin-left:calc(50% + 123px);margin-top:66px;margin-right:0;margin-bottom:0;position:relative`.
- Foreground Nosara/couple (`comp-mwia7xvg`): `width:280px;height:414px;grid-row:1/2;grid-column:1/2;align-self:start;justify-self:start;margin-left:calc(50% + 29px);margin-top:144px;margin-right:0;margin-bottom:0;position:relative`.
- Both use the same already-uploaded Wix media images as the donor capture, not placeholders; `displayMode='fill'`.
- DOM image order places foreground last; actual Chromium overlap hit-test confirms foreground wins at both widths.
- Exact browser readback after import using existing Origami renderer: at 1280px, section height=729, back `X=763,localY=66,W=360,H=575`; foreground `X=669,localY=144,W=280,H=414`. At 1920px, section height=729, back `X=1083,localY=66,W=360,H=575`; foreground `X=989,localY=144,W=280,H=414`. This corresponds to source centered geometry for document width 1920. Real-browser document content width must be measured; if it is 1905, the desired X values are 1075.5 and 981.5 (−7.5 from these measurements), automatically following `50%` center alignment.
- At 390px, the **existing** separate mobile layout remains, not yet donor-matched. No mobile acceptance claim is made.
- Both local lint and TypeScript passed; actual Wix import succeeded to editor/site revision **25**. Official re-export confirmed exact fixed pixel rules survived and original media IDs remained. `pages/(home)` was explicitly `unchanged`. Site was not published.
- Important: Wix exported `Image` contract requires `image.url`; obtain it from the same site’s current `media.getCroppedImageUrl` pattern and keep its `width/height` media metadata consistent with url's origin size. These are source-asset metadata and are **not** the on-canvas CSS frame dimensions. Incorrect mismatch triggers `origami(data-values)`.
- For full acceptance, distinguish editor readback, local Origami renderer DOM checks, and the published site; this test confirms editor source persistence plus renderer DOM, not that unpublished draft is live on the public domain.

**Root-cause fix:** percentage-based image widths and bottom-anchored CSS layout are not acceptable substitutes for fixed-size donor geometry on Desktop. Use verified px frame rules and center-relative coordinates, then actual readback at both widths.
