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


## 16. Full-page transfer — verified Vesper About evidence (2026-11-15)

This section **extends**, not replaces, §§1–15. It closes the earlier knowledge gap about native full-page *manual execution* and gives every new chat an exact, single route. This is the same canonical textbook; do not create another competing cookbook.

### Observed end-to-end evidence, with distinct acceptance scopes

Source: LocalDesign v2.4 for `https://vesper.tonicsiteshop.com/about`; desktop-1280 and mobile-390 observations. Target: already existing Wix Studio Two `blank-2` / page ID `dswnf` on My Site 33.

- Complete page: 11 Wix native sections counting the menu/header-like local section, 17 Image, 62 WRichText. The initial `intro` reused its previously imported native elements. Exact source images and GIFs, without substitutions.
- Official Wix server `import-site`: 41 → 42, exactly `pages/blank-2` updated; three other pages and global components unchanged; no publish.
- Fresh official Wix editor re-export confirmed 11 / 17 / 62 native sections/images/texts and real Wix media IDs.
- A source-to-reexport **CSS rule** comparison for the 71 elements newly added after `intro` checked fixed W/H, source section-local Y, centered desktop offsetX, independent mobile X/Y/W/H and section heights; 71/71 passed. The 8 previously proven `intro` elements were preserved.
- Source-measured Background colors for five sections were saved by official Wix import 44 → 45 and re-export confirmed exact colors, including mobile overrides:
  - `bio` #F7F5F2, `our-values` #F7F5F2, `at-at-glance` #958773;
  - `freebie` desktop #F7F5F2/mobile #F1ECE7;
  - `footer` desktop #FBFAF9/mobile #F7F5F2.
- Browser comparison before the Background correction found painted section differences; **no complete refreshed visual screenshot PASS** was recorded afterward.
- Geometry-only evidence and source-content readback **must not** be promoted to full page pixel-perfect acceptance or an automatically proven reusable full-page program.

**Full-page manual native transfer with import/readback = LOCAL-PROVEN. One-command portable scanner→Wix full-page automation = IMPLEMENTATION GAP / NOT ACCEPTED YET. Full visual typography, image crop, interactions and mobile parity = separate open gates.**

### Universal operator input and exact target scope

Required from owner: (1) source URL or an already captured LocalDesign ZIP; (2) target Wix Studio Two **site ID/editor URL**; (3) exact authorized **target existing page** (route or page ID); (4) explicit authorization for target-page draft mutation. Do not guess the target from the site homepage or create a page unless separately requested. Reuse the existing fingerprint; no repeat capture unless missing measured evidence is demonstrably required.

Verify fingerprint `schema=localdesign.site-fingerprint.v2.4`, `source`, `pages[].views` capture status, non-truncated node arrays, exact viewports/DPR, screenshots, asset URLs, source page lengths and section order. Fail closed on different URLs, missing viewports, unobservable assets or unverified interactive layers. Screenshot only does not prove editable element geometry.

### One algorithm, executed without per-page scripts

1. **PEOS route** → this standard → existing `localdesign_wix.py`/adapter → existing reusable `run_wix_pipeline.sh`/QA candidates; first check capability status. No second scanner, browser controller, adapter or one-off page builder.
2. **Capture once** with existing LocalDesign v2.4 at source donor viewport(s); ZIP contains `site-fingerprint.json`, screenshots, technical report, QA manifest. If source does not expose full visual evidence for a required layer, report specific scanner delta (below), not an invented value.
3. **Normalize the whole page** into **one** source-agnostic Universal Page Recipe: canonical ordered sections, original section rect/height per viewport, element selector/type/text/URL/visibility/style/stack, source-to-target manifest stable identities; mobile-only elements and cross-breakpoint asset links by source selector. Include nested/subsequent footer content without assigning the wrong section. Store section paint from measured descendant/layer (source section outer `backgroundColor` can be transparent even if a child fills the section). Explicitly preserve unsupported video/vector/masks/interactions; no silent skips.
4. **Geometry rule** per viewport: source section local X/Y and W/H; centered offsetX for source-proven desktop fixed frames; **independent** mobile measured local X/Y/W/H. All native elements belong to their exact source section. Correct total page grid rows and original cumulative section heights **per breakpoint**, not just local child positions.
5. **Fresh Origami export** from exact owner-authorized Wix site; identify real target page ID/route, native page/header/footer/theme, breakpoint name, component contracts and media state. Assert git/file scope only target page before every import. Preserve all other pages, globals and shared headers.
6. **Native assembly**: one Section + InternalContainer + Background per source section, Image and WRichText for compatible items, ordered stacking. Use measured source page paints/opacity and exact text, not default white or arbitrary 10px placeholders. External original image/GIF URLs are only *source identities*; use official Wix Media Manager importer to create internal `uri`.
7. **Media known-good** from the 2026-11-15 live run: official `wix origami upload-media` scanned **zero** when new `Image` data was authored as a single line. Reformating those Image objects to the exact multiline form used by Wix's current exporter allowed official upload; 14/14 external source media succeeded, 0 failures. This is a *known version-specific parser behavior*, not license to implement a second uploader. After upload Wix rewrote `image.uri`; then TypeScript required removing unsupported newly generated `image.id` fields **and** adding native `image.url = media.getCroppedImageUrl('wix:image://v1/<uri>/<filename>#originWidth=<assetW>&originHeight=<assetH>', 0,0,0,0, assetW,assetH, {name,autoEncode:true,devicePixelRatio:1})` with matching real metadata. Consult the fresh export/current Wix version; server import is final authority. Do not set a mismatched URL/source-dimension pair.
8. **Official preflight** `yarn lint`, `yarn tsc`, `yarn build` and semantic scope/media/element counts. Import only after all pass. `wix origami import-site` must report only expected page updated, no pages deleted, non-target pages/globals unchanged and saved new revision. No publication.
9. **Fresh re-export** and read back all native components, exact measured CSS, source media IDs, section backgrounds, page grid rows, mobile breakpoint. Wix regenerates IDs: join using stable source selector + section/order/type/text/URL manifest; do not rely on submitted component IDs or unique text matching.
10. **Playwright QA** at every captured viewport on supported draft/editor renderer, screenshots compared to source. `LOCAL_GEOMETRY`: each element's offset from section center or mobile left, section-local Y and frame W/H; `PAGE_GEOMETRY`: actual source/Wix section starts and entire scroll height/flow; `ASSETS`: URL origin identity, cover/fit/crop, original media and animated GIF; `PAINT`: background/image/font/color/opacity/borders; `STACK`: hit-test + visual overlaps; `MOBILE`: independent display/hide/clip/overflow; `INTERACTIONS`: captured evidence and native functionality; `VISUAL`: screenshots excluding only explicitly deferred typography. Gate by gate, measured <=1 CSS px for supported static frames.
11. **Host chrome normalization**: observed Wix free-site `#WIX_ADS` top banner = 30px, donor `intro` began at Y=1, Wix section at Y=30. Compare source/Wix **content roots** in a common coordinate space. Do not offset all children by -29px or edit global Header to hide external Wix chrome. The distinct 15px scrollbar may change section width: normalize centered X with measured actual section width/left, never fixed +/-7.5.
12. **Accept or stop**: save machine-readable signed-off acceptance matrix and source/re-export/screenshot evidence, with exact failures classified by root cause. If an unsupported feature remains, report `PARTIAL / BLOCKED`, never `DONE`. User requested draft page mutation, **not automatic publish**.

### Scanner delta policy (extend existing LocalDesign, never rewrite)

Current v2.4 already supplies measured section/node rects, computed styles (including background colors/images, opacity, position, transform and text styles), original asset URLs, links, fontFaces and both screenshots. The **remaining missing evidence** for universal 1:1 must be confirmed per donor and added **additively** to the existing scanner only when absent:

- stable element/component identity across responsive snapshots and nested parent/section provenance; distinguish decorative descendants from actual independent visible layers and detect duplicated text;
- effective painted/background layer per section (including covering descendants and pseudo-elements), alpha, background crop/position and image/video sources;
- explicit hit-test/stacking context and clipping/masks/pseudo-element provenance where overlaps exist;
- interaction-state sampling (hover/click/menu/scroll/sticky/animation timeline) and non-static media, instead of assuming static DOM screenshot represents every state;
- intrinsic image dimensions alongside **on-canvas** CSS frame/crop and source URL;
- section order, page root/document geometry, viewport + scrollbar/clientWidth + platform banner/chrome, source font metadata;
- capture completeness flags and unsupported-feature inventory (do not silently drop).
  
Use a backwards-compatible v2.4 optional enrichment if compatible; otherwise version schema deliberately with regression fixtures. Never mutate the scanner from inferred requirements without inspecting its actual implementation and repository owner. ZIP content alone cannot identify a checked-out scanner source file.

### Minimum repeatable acceptance fixtures

- **Fixture A** Vesper `/about` desktop-1280 and mobile-390 ZIP → existing Wix Studio Two `blank-2`: 11 sections, original 17 images, 62 texts, 5 painted sections, no non-target updates; native readback geometry and independent breakpoint QA.
- **Fixture B** 1280→1920 desktop regression: centered offsetX remains invariant for proven fixed frames despite scrollbar/content-width difference, no unexpected section height scaling.
- **Fixture C** duplicate text, mobile-only image, external GIF, lazy-load URL, transparent parent with colored descendant, overlap and external Wix banner. Must fail closed on ambiguous mapping/unsupported dynamics.
- **Fixture D** second unrelated donor page + different Wix target/site: needed before promoting the **universal automated full-page implementation** from candidate to locally accepted.

**New-chat ready command:** “Read PEOS START_HERE → Website Creator ROUTER → this canonical native transfer standard; locate the current LocalDesign Fingerprint ZIP and exact target Wix page; execute the already-proven full-page Origami native route, validate source/target/media/readback/browser QA, report separate gates. Do not create a parallel scanner/adapter, edit other pages, invent media or publish.” 


### Viewport-contract rule (observed Desktop 1920 / Mobile 390)

**Implementation level: PRE-IMPORT SOURCE/NATIVE-STAGE VERIFIED; full imported/published visual parity NOT ACCEPTED.** The existing `full_page_recipe.py`, `compile_full_page.py`, `audit_source_layers.mjs`, `verify_full_page.py`, and `verify_full_browser.mjs` accept a LocalDesign v2.4 source observed at exactly one supported desktop viewport (`desktop-1280` **or** `desktop-1920`) plus independent `mobile-390`. The normalized recipe stores `desktopWidth` and viewports provenance; desktop geometry remains observed source geometry, **never** a renaming of 1280 to 1920. Captured source Mobile 390 is not synonymous with a Wix CSS breakpoint whose **maximum** is 389px.

For each native Wix import use only the current official export and read `theme.css` `@custom-media` definitions. The target page's authored mobile override must use an **already existing named breakpoint whose actual CSS range includes 390px** (for example a theme max-width 1023px selector if the page's previous max-width 389px selector misses the exact source 390 viewport). Only the authorized page's CSS media selector may change; **never edit global theme solely to force this mapping**, and do not claim responsive parity at widths that have not been captured and verified. If current page layout includes multiple authored named breakpoints requiring more source evidence, fail closed instead of flattening their rules.

Source media: different URL optimization sizes such as `/1600/SAME_SOURCE_ID/shared/image.jpg` versus `/800/SAME_SOURCE_ID/shared/image.jpg` can be recognized as a single image **only when the stable URL source identity matches exactly after removal of the numeric size segment** and there is exactly one observed asset per captured viewport. Preserve both observed source URLs in the normalized recipe; use the exact desktop source URL for native Wix Media Manager import. Do not treat optimized variants as two unrelated image instances or as interchangeable visuals without crop/asset QA. Any different source ID, filename, host or ambiguous variants remain BLOCKED; no substitutions.

**Mandatory preflight remains unchanged:** `yarn lint`, `yarn tsc`, `yarn build`, and changed-files scope must pass before official import. An existing TypeScript error in an **unrelated unchanged page** does not grant permission to alter that page, suppress TypeScript, or bypass the import gate. Diagnose the actual failing file, report the exact blocker, and obtain separate authorization or an approved standards-level exception before changing execution. A successful native workspace compilation, exact source-media upload and production build are **not** an imported or visually accepted page.


### Responsive typography and visual-media QA contract (Information 1920/390)

**Observed native build and readback (revision 64), not full pixel-level acceptance.** Fingerprint text items contain viewport-specific `desktopStyle` and `mobileStyle` (font family, size, line height, letter spacing, weight/style, transform, color and alignment). Existing `compile_full_page.py` now emits those values directly on the **WRichText component root**, separately for Desktop and the verified named Wix mobile breakpoint covering 390px. The official Origami CSS validator rejects selectors of form `.textId h2` and directs authors to style `.textId` instead. Keep original observed font names; font existence/licensing is a separate gate. The original Vesper Information uses fonts not in the Wix site's searched font catalog: Made Canvas Light, Commuter Sans Regular, Newsreader Display variants and Tenderness; only Raleway was found. Declaring an unavailable family in native CSS does **not** mean exact font parity and may render fallback glyphs. Do not upload unlicensed font binaries or silently substitute another family.

**Video/photo style breakpoint:** Original mobile-390 is covered by the site's existing `@custom-media` max-width 1023px, not the auto-generated max-width **389px**. This applies to `style.css` background paint and `--backgroundMediaOpacity` as well as `layout.css` geometry. Current native compiler uses the same validated mobile at-rule in both, ensuring the desktop-only `reviews` video layer becomes visually transparent on mobile so the original native image may show. Verify true video state and visual layering in the browser; hidden opacity alone does not mean video playback stops.

**Page header provenance:** Vesper `/information` on mobile390 has actual `div#mobile-menu-closed` from Y=0 to 51.19px containing VESPER and a hamburger SVG, **outside the twelve page sections**; its first section begins Y=51.19px. On Desktop1920, the corresponding `desktop-menu` is an overlay with approximately 1px flow height. A 12-section-only recipe can match all section-local frames but **cannot claim page geometry or visual parity** until the page-scoped responsive header and its controls are also reproduced, without changing shared global Wix Header. Do not disguise the missing header by shifting all children, adding arbitrary blank top padding or changing unrelated site pages.

**Public acceptance remains distinct from import:** Recent Wix Studio Two import `revision 63→64` updated only `pages/blank-3`; fresh exported CSS readback verified 104 font-size declarations for 52 text elements, native 12/12 sections, 72/72 original components, images 20/20 and no geometry CSS issues. Public site still rendered old Arial10px at exact Desktop1920 and mobile390, because new draft was not published. Acceptance requires explicitly authorized publication, fresh public Fingerprint at both viewport widths and actual pixel/font/video/mobile-menu comparison. If owner gives no explicit publication authorization, stop at verified editor draft with status PARTIAL rather than DONE.


## 2026-11-16 — CANDIDATE amendment: native Chrome (Header/Menu/Footer) and source replay

**Acceptance status: SOURCE TESTED, TARGET NOT ACCEPTED.** This amendment is confined to PR #172 and companion LocalDesign draft PR #3; it does not overwrite the established tested image/text geometry standard.

- The LocalDesign 2.5.7 source contract preserves donor Header/Menu/Footer as distinct source surfaces per viewport, including `display:none` menu states, exact label+href order, fixed overlays, native Footer slot, measured local rectangles and linked original SVG assets. A shared Footer is not a normal flow Section; current donor Vesper has 12 page sections plus Footer.
- Existing adapter `full_page_recipe.py` reads `chromeCandidates` and emits `sourceChrome` with verified source roots and anchor evidence. It distinguishes actual nav anchors using observed nested `<nav>` from logo/CTA anchors. Native Wix target components and missing routes still require independent proof.
- The existing LocalDesign ZIP package, raw DOM capture and original 23 SVG files may be replayed through **the same scanner source contract implementation** via `node scripts/replay-source-contract.mjs input.zip output.zip`. It verifies ZIP CRC and source version parity, writes `qa/source-replay-provenance.json` with hashes, preserves original capture version and source assets unchanged, and explicitly records the replay version. It must never assert a fresh screenshot, Chrome recapture, native Wix import or pixel parity. This avoids unnecessary rescans for schema-only improvements when the original data is complete.
- Source Wix readiness MUST remain blocked for unverified native Header/Menu/Footer, unavailable routes, invalid anchor links, inaccessible media, missing Theme tokens or absent desktop/mobile readback. Official Wix native Menu/VectorArt and shared slots are already documented; do not build custom widgets, fake routes, substitute vectors or edit unrelated target pages.
- Actual Vesper snapshot: 8 original nav items; inspected Wix target has Home only, leaving 7 target routes unresolved and 4 Footer anchors without href. No import authorized/completed. PEOS regression 10 PASS, 1 owner-only ZIP SKIP, LocalDesign v2.5.7 full npm and GitHub CI PASS. **Full target acceptance is still BLOCKED.**

This is an additive implementation note, not permission to bypass the normal `run_wix_pipeline.sh` gates.
