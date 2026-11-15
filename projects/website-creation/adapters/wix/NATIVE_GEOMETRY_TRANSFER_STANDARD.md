# LOCALDESIGN → WIX STUDIO TWO — NATIVE GEOMETRY TRANSFER

## HARD TECHNICAL STANDARD — NEW CHAT KNOWLEDGE START HERE

Date: 2026-11-15. This is **reusable technical knowledge**, not a migration of one ZIP, donor page or Wix instance. The owner supplies a new fingerprint and target page separately. Source of proof: [native Wix geometry readback evidence](../../decisions/WIX_STUDIO2_SOURCE_VIEWPORT_COORDINATES.md).

**Acceptance level:** LOCAL-PROVEN for exact native image/text frame geometry at Desktop 1280/1920. Pilot/candidate for universal full-page automated import and full responsive visual QA. Distinguish these levels strictly.

### 1. Canonical startup

Global [START_HERE](../../../../START_HERE.md) → [PEOS ROUTER](../../../../docs/ROUTER.md) → [Website Creator PROJECT](../../PROJECT.md) → [Website Creator ROUTER](../../ROUTER.md) → this document → relevant current evidence and only the needed [Wix adapter documentation](README.md).

This is continuation of the existing Universal Website Translator / Wix native-adapter technology, not a new project. Do not create a new capture engine, CSS language, Chrome extension, browser controller, page-specific converter or HTML renderer. Standard route:

    Existing LocalDesign Site Fingerprint
    → normalize measured section/element geometry into Universal Page Recipe
    → existing Wix Studio Two native component adapter
    → official Wix Origami export/import
    → fresh Wix readback
    → real browser comparison at captured viewport sizes.

The technical process is established. The full automation is NOT yet accepted. The goal is to apply existing methods mechanically, without rediscovering geometry.

### 2. Input data contract — read, do not guess

For EACH observed responsive capture retain:
- Source URL, exact viewport CSS width and height, DPR, scrollX/scrollY, current rendered layout, transform effects.
- Page and section identities (source DOM selector), section actual bounding rectangle (left, top, width, height).
- Every element’s exact selector, component type, measured bounding rect (left, top, width, height), text content or exact source asset URL, DOM order, parent/stacking context, crop/fit properties, visibility.
- Distinct source evidence per viewport, e.g. desktop-1280, mobile-390 and other supplied width. Do NOT infer mobile coordinates by shrinking desktop.
- Compare elements and sections measured in one coordinate space. Group coordinates are NOT section coordinates. Page/document coordinates are NOT viewport coordinates at nonzero scroll.
- A lazy-loaded desktop image URL may be linked from another observed responsive capture only when the exact same stable source selector proves asset identity. No fallback image or inferred URL.
- Preserve original asset URL; do not use approximate, stock or replacement images. If inaccessible: explicit BLOCKED. No unnecessary extra media ZIP.

LOCALDESIGN gives computed post-transform rectangles. A screenshot alone is insufficient. Use DOM measured geometry from the source ZIP and real DOM measured Wix output.

### 3. Core geometry transformation: SOURCE SECTION → WIX NATIVE SECTION

Let S be source section rect and E be source element rect, both measured with getBoundingClientRect at the same scroll and width:

    localX = E.left - S.left
    localY = E.top  - S.top
    offsetFromSectionCenter = localX - S.width / 2
    fixedW = E.width
    fixedH = E.height
    sectionHeight = S.height

The proven Desktop layout for a fixed-size source element in a centered Wix section is:

    .native-element {
        --spx-resolver-type: fixed;
        width: Wpx;
        height: Hpx;
        grid-row: 1 / 2;
        grid-column: 1 / 2;
        align-self: start;
        justify-self: start;
        margin-left: calc(50% + OFFSETpx);
        margin-top: LOCAL_Ypx;
        margin-right: 0;
        margin-bottom: 0;
        position: relative;
    }

If OFFSET is negative: calc(50% - ABS_OFFSETpx).

Meaning: **width and height are fixed CSS pixels**; only the horizontal center reference is proportional to the actual Wix section/container width. The margin-top is measured source SECTION LOCAL Y. Never substitute source page Y or group Y. Desktop X is **not** a frozen pixel position from one screenshot: it is a centered offset when that behavior is supported by source evidence.

Only use this mapping for frames observed to remain fixed across Desktop widths. If the source actually uses percent width, sticky positioning, transform animation, responsive reflow or another behavior, route through the existing appropriate native capability or mark unsupported; do not force it into this fixed-size model.

### 4. Scrollbars: 1280 viewport may contain 1265 content pixels

Verified donor cases showed a 15px difference between browser viewport width and section content width: 1280 vs 1265, 1920 vs 1905. Not a universal rule. Read section.width, section.left and document.documentElement.clientWidth for each actual browser run.

Worked example:

    At real 1920 viewport, source/Wix section width = 1905:
        section midpoint = 952.5
        image background center offset +123 => X 1075.5
        image foreground center offset  +29 => X 981.5

    At 1280 viewport, source section width = 1265 and centered on Wix canvas:
        content midpoint = 632.5
        centered-canvas offset = (1280-1265)/2 = 7.5
        image background X = 632.5+123+7.5 = 763
        image foreground X = 632.5+29+7.5 = 669

    At a local renderer with a true 1920-wide section:
        background X = 960+123 = 1083
        foreground X = 960+29 = 989

These are consistent center-relative positions, not a 7.5px error. **Never hardcode +7.5 or -7.5 to all sites.** Compare X relative to the section center and record the section width/left in each source and Wix run.

### 5. Section heights vs children positions — two separate QA gates

LOCAL_GEOMETRY verifies child offset from its own section and dimensions. PAGE_GEOMETRY verifies where the section begins in the total document.

    elementPageY = actualSectionPageY + elementLocalY

For sequential sections, section page Y depends on cumulative actual preceding section heights. In a previous test, children matched perfectly but earlier resized sections accumulated over 500px of page Y drift at 1920. This is NOT fixed by shifting children. Fix section sizes and flow separately, then compare absolute page Y.

Set section and internal container heights from source per breakpoint, not scaled accidentally by the Wix reference width / --spx() resolver. Measure actual rendered section heights after import.

### 6. Wix Studio Two native component contract

Use editable native Wix components:
- Section, InternalContainer, and Background as required by current export.
- Image with className, native image object, real Wix Media Manager URI, real media.getCroppedImageUrl URL and displayMode matching source fit/cover/crop.
- WRichText with className and richText object containing actual HTML text content.
- A separate native element for each separate source image/text element. No screenshot overlay, Custom HTML page, iframe imitation or Aria-based manual layout.

Work from a **fresh official Wix Origami export**. Representative page files:

    packages/site-app/src/pages/<TARGET_PAGE>/structure.jsx
    packages/site-app/src/pages/<TARGET_PAGE>/layout.css
    packages/site-app/src/pages/<TARGET_PAGE>/style.css
    packages/site-app/src/pages/<TARGET_PAGE>/unmapped.json

Inspect actual exported component structure; Wix schemas can change. Modify only the explicitly authorized page, preserving real page ID, route, shared headers, footers, global styles, other pages and media. Import can rename generated component IDs; do not rely on submitted IDs for readback—match content, real media URI and layout.

#### Image-specific mandatory distinction

There are three separate sizes:
1. Source asset/intrinsic pixel size.
2. Wix media origin/crop metadata in native Image object and required image.url.
3. On-canvas native Image frame W/H in layout.css.

Image media metadata and the actual URL/origin geometry must agree or Wix server-side validation can fail with origami(data-values). On-canvas CSS frame can be 360x575 even if Wix produces an optimized served image with intrinsic dimensions 351x560. This is not necessarily a frame geometry failure; flag image sharpness/crop as separate visual QA.

Use the official existing Wix media-upload mechanism if original source asset is not in the target Media Manager. Verify actual source/URI. Do not use substitutes.

#### Grid and mobile import validation

Actual Wix nested container rules may require the following within each relevant breakpoint:

    @origami-target internal-container-content-wrapper {
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: SECTION_HEIGHTpx;
    }

The exact surrounding selectors and @origami-target syntax must come from the latest export. An observed server importer error was "a grid container rule needs grid-template-rows and grid-template-columns" in 10 mobile containers. Wix CLI lint/TypeScript passed while server import rejected the page. **Server-side import acceptance overrides local lint.** Add precisely the missing declaration in the failing breakpoint instead of creating a new renderer/adapter.

### 7. Responsive conversion is independent

At Desktop 1280 and 1920, fixed W/H and section-local Y remain constant only when source supports that behavior; X changes relative to section center.

At Mobile 390, use the observed mobile coordinates:

    mobileLocalX = mobileElement.left - mobileSection.left
    mobileLocalY = mobileElement.top  - mobileSection.top
    mobileW = observedMobileElement.width
    mobileH = observedMobileElement.height
    mobileSectionHeight = observedMobileSection.height

Apply native Wix mobile breakpoint CSS separately. In ONE tested Wix export the selector was "@media (--variants-mqxfr2bo1)"—not a globally guaranteed name. Re-read it from current Wix page export. Mobile source may hide, reorder, reflow or clip elements; do not manufacture missing mobile data.

Check mobile width, height, section positions, image crops, visibility, overflow and stacking independently. No Mobile PASS until measured on actual Wix rendered page.

### 8. Overlaps and z-order

Preserve source visual layering/DOM and hit-test evidence. Foreground image in verified overlap was above the background. Browser elementFromPoint at overlap samples confirms hit-test order, but not necessarily visible pixel order for transparent images, opacity, clipping, masks, pseudo-elements or pointer-events. Do both DOM hit-test and visual check when layers matter.

Do not invent arbitrary z-index to "fix" the page without comparing stacking contexts and visual evidence.

### 9. Text frame geometry is NOT font pixel parity

Verified native WRichText container geometry may be exact while inner text differs. In the accepted test:
- Heading native frame = 405x129, inner Wix h2 measured 405x140.38; donor h2 = 405x129.
- Paragraph native frame = 386x185, inner Wix p measured 386x105.28; donor p = 386x185.
- Different font families, heading line-height 70.2 vs donor 60, paragraph line-height 17.55 vs donor 30, paragraph letter spacing normal vs donor 0.75 explain much of the difference.

Owner decision: **Do typography later.** For current geometry gate compare native editor frame X/Y/W/H. Report inner text render mismatch as a separate deferred visual/typography item, not as a failure of correctly measured frame coordinates. Still flag actual clipping/collisions honestly.

### 10. Accepted execution sequence: no new technology

1. Enter PEOS canonical route; read this technical manual and current accepted Wix geometry evidence.
2. Owner gives source Fingerprint ZIP + target Wix page. Verify source URL inside ZIP; never confuse different pages of the same donor.
3. Read existing LocalDesign extraction and Universal Recipe/adapter contracts. Normalize section-local Y, center-relative desktop X, fixed/observed dimensions, separate mobile and real original asset identifiers.
4. Fresh Wix Studio Two site export via official Origami CLI; inspect current native components and breakpoint/grid structure.
5. Modify only the authorized Wix page in the fresh export. Do not alter Home, other test pages, globals or shared settings without explicit scope.
6. Verify original assets uploaded/matched via official Wix Media Manager. No placeholder.
7. Run official yarn lint, TypeScript check, production build when available. These are *preflight only*.
8. Import with official Wix Origami import-site. Confirm server accepted it, list of updated/unchanged/deleted pages and revision. If rejected, diagnose the specific official import errors.
9. **Re-export from editor after import**. Verify current native Section/Image/WRichText counts, actual IDs, exact CSS frame properties, assets and target-only change scope.
10. Open valid Wix draft preview / current site rendering through supported official route; measure actual DOM rectangles at the same widths as source; check center offsets, section-local Y, W/H, section heights, page Y and stacking. Do not invent preview URL or publish solely to bypass an unavailable draft preview.
11. Run visual screenshots against source at Desktop and separately Mobile. Typography excluded until owner activates it.
12. Mark independently: SOURCE_VERIFIED / NATIVE_COMPONENTS / IMPORTED / READBACK / LOCAL_GEOMETRY / PAGE_GEOMETRY / MOBILE / VISUAL. Only say DONE for gates actually passed. Do not publish unless owner explicitly requests.

### 11. Mechanical browser QA algorithm

At matching viewport, compare element and its parent section from getBoundingClientRect:

    localX = elementRect.left - sectionRect.left
    localY = elementRect.top - sectionRect.top
    offsetX = localX - sectionRect.width/2
    width = elementRect.width
    height = elementRect.height
    sectionHeight = sectionRect.height

Measure effective document Y by adding scrollY to viewport Y, consistently for source and target. Use computed post-transform rectangles, not untransformed offsetLeft. Report differences:
- delta centered offsetX,
- delta section-local Y,
- delta W/H,
- delta section height,
- delta absolute page Y,
- layer overlap order,
- original asset/crop parity,
- desktop/mobile independent QA.

For proven static frames, tolerance up to 1 CSS px was the working QA gate, with **0px error actually demonstrated** on four elements. A 200 HTTP response or a successful build is not accepted as geometric proof.

### 12. Demonstrated reference numbers (ONLY an example, not a new source to use)

Verified at actual 1920 viewport with 1905 content-width section:

| Native type | offset from section center | section-local Y | W x H | real X |
|---|---:|---:|---:|---:|
| Background image | +123 | 66 | 360x575 | 1075.5 |
| Foreground image | +29 | 144 | 280x414 | 981.5 |
| Heading WRichText | -471 | 148 | 405x129 | 481.5 |
| Paragraph WRichText | -473 | 287 | 386x185 | 479.5 |

On Wix 1280 centered canvas: background X763, foreground X669, heading X169, paragraph X167. Frame dimensions and section-local Y remain identical. Foreground above background in overlap hit-test. The proven section was 729px high.

Root cause of the first failed Wix Aria result: widths 28.13% and 21.88%, bottom anchors, preserve-aspect responsive scaling → rendered photos grew ~1.49x at 1920. Fixed CSS px and top/center rules resolved it. The user specifically does not want further experiments with Aria.

### 13. Known pitfalls to prevent repeating the entire project

- Do not blindly restore an old export: it may not include a page created later in Wix editor.
- Do not compute image geometry from filename/resolution.
- Do not change unrelated site pages. Inspect git diff / importer scope, and require unchanged non-target pages.
- Do not claim an automated new converter is ACCEPTED just because a synthetic test is green. Existing candidate adapter currently has limited one-section pilot proof; full-page automatic conversion is **not accepted**.
- Do not repeatedly create page-specific files named build_<page>.py or B64 inline transports when existing universal route should be used. These were expedient attempts during exploration, not canonical technology.
- Do not assume local lint covers Wix import server validations: mobile grid columns and image origin metadata have caused server rejections.
- Do not claim editor import success equals browser QA or public-site publication.
- Do not move children to conceal cumulative section heights.
- Do not claim mobile parity from desktop geometry.
- Do not spend current geometry phase tuning fonts without owner authorization.

### 14. Existing durable files: knowledge vs implementation status

- [Primary geometry evidence and accepted examples](../../decisions/WIX_STUDIO2_SOURCE_VIEWPORT_COORDINATES.md).
- [Wix adapter README and current limits](README.md).
- [Existing adapter candidate](localdesign_wix.py): useful reusable code, but not end-to-end LIVE-PROVEN.
- [Existing orchestration candidate](run_wix_pipeline.sh) and [Playwright QA candidate](verify_geometry.mjs): consult current statuses; do not rebuild another orchestrator for each donor.
- [Universal Website Translator architecture](../../UNIVERSAL_WEBSITE_TRANSLATOR_ARCHITECTURE.md).
- [Live Website Creator PROJECT_STATE](../../PROJECT_STATE.md), [latest log](../../logs/latest.md).
- [Official Wix Studio Two skills](https://www.wix.com/skills/studio-two/SKILL.md) and official Origami import/export documentation, confirm against current site/export version.

### 15. New chat direct execution instruction

Read global PEOS START_HERE and this technical guide before touching Wix. Geometry algorithm is **already proven**. Take the new Fingerprint and target page supplied by the owner, apply fixed frame/section center-offset mapping and independent responsive captures, import native Wix components using the existing Origami adapter, run fresh readback and real browser QA. No Aria, HTML substitute, new capture system, invented media or one-off build scripts. Separate confirmed local-geometry capability from still-unproven full-page automated acceptance. No publish without explicit authorization.
