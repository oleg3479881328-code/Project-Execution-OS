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
