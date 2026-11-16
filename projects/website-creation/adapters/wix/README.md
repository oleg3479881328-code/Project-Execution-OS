# LocalDesign → Wix Studio Two — Geometry Adapter

**Главная техническая инструкция для нового чата:** [NATIVE_GEOMETRY_TRANSFER_STANDARD.md](NATIVE_GEOMETRY_TRANSFER_STANDARD.md) — все доказанные формулы LocalDesign → Wix, native CSS/Image/WRichText, breakpoints, импорт, readback, DOM QA и запреты на повторное изобретение.

**Status: CANDIDATE / LOCAL PILOT TESTED / LIVE BRIDGE NOT YET ACCEPTED.**
Date: 2026-11-15. Part of existing Website Creator / Universal Website Translator, not a new product or alternate browser automation engine.

## Existing canonical route

Global `START_HERE.md` → `docs/ROUTER.md` → `projects/website-creation/ROUTER.md` → `UNIVERSAL_WEBSITE_TRANSLATOR_ARCHITECTURE.md` → this adapter.

Source: **LocalDesign v2.4 Site Fingerprint ZIP**, including `site-fingerprint.json`, two observed widths (desktop-1280 / mobile-390), exact computed DOM rectangles, text and source media URL evidence. Do not recreate these browser-capture primitives.

Target: **Wix Studio Two native editor**, using only the already-proven **official Wix Origami export → edit → lint → import → re-export → Playwright DOM geometry QA** route. No custom HTML widget or browser-login script.

## Code and fixture

- [localdesign_wix.py](localdesign_wix.py) — stdlib pilot converter; source Fingerprint ZIP → normalized geometry recipe → native editable Wix Image/WRichText layout in an explicitly named test page.
- [Vesper test recipe](fixtures/vesper-experience.recipe.json) — real six-element donor measurements: 2 photos, 4 text fields.
- [run_wix_pipeline.sh](run_wix_pipeline.sh) — authorized official Wix export/import/readback sequence; not a new browser runtime.
- [verify_geometry.mjs](verify_geometry.mjs) — existing Playwright geometry acceptance and explicit PASS/FAIL with measured deltas.
- [Verified geometric acceptance record](../../decisions/WIX_STUDIO2_SOURCE_VIEWPORT_COORDINATES.md) — Wix rev. 25 images, rev. 28 native text; 1280/1920 DOM readbacks.

### Current tested invocation shape

```bash
python3 localdesign_wix.py extract \
  --fingerprint donor-fingerprint.zip \
  --section 'div#experience' \
  --out /tmp/vesper-experience.recipe.json

# Use the current official Wix authenticated environment.
wix origami export-site --site SITE_ID -d /tmp/wix-current --json

python3 localdesign_wix.py apply \
  --recipe /tmp/vesper-experience.recipe.json \
  --wix-export /tmp/wix-current \
  --page blank

# Preflight: ensure ONLY pages/blank changed, NOT pages/(home).
yarn lint && yarn tsc
wix origami import-site --site SITE_ID -d /tmp/wix-current --json

# Fresh re-export, build, inspect native DOM x/y/w/h at 1280 and 1920.
```

**Important:** `apply` only modifies the local Wix export. It does not import, publish or mark success. Missing native images / unsupported sections fail closed. Always obtain the user's authorization for target site/page changes.

## Confirmed source sample

Real Vesper capture was analyzed from LocalDesign v2.4. The exact donor section `div#experience` yields:
- Background photo center offset +123, Y=66, size 360×575.
- Foreground photo center offset +29, Y=144, size 280×414.
- `the` text center offset −469, Y=145, 138×47.
- Headline center offset −471, Y=148, 405×129.
- Body center offset −473, Y=287, 386×185.
- `learn more` center offset −473, Y=516, 183×18.

Source photo URL is visible in the mobile snapshot but not in desktop (lazy background), so the exact same DOM selector is used to match URL between observed widths. Geometry remains measured at desktop, not inferred. Images must already exist as original media in the target Wix Media Manager; if not, stop, use official import, and validate.

Local pilot test harness (the downloadable adapter bundle) passed **5 Python unit tests**, including source six-element extraction, centered CSS transformation, fail-closed invalid input, and synthetic native page patch. Existing LocalDesign v2.4 regression suite passed. **These do not constitute a successful live Wix adapter import.**

## Explicit blocker / current end-to-end gap

An attempted remote launch of the newly committed adapter on the Wix dev machine was blocked by the execution security layer. No result from that attempted invocation was accepted. Do not bypass that security control. Resume only via authorized official Wix operations or user-controlled local environment with the supported Wix CLI.

The known accepted *manual* (not fully automated) geometrical import from Wix rev. 28 remains valid; adapter-to-live-import is a **separate pending acceptance gate**.

## Scope boundaries

- **Supported in pilot:** one selected section, a one-section test Wix page, two desktop/mobile captures, existing media, native Image and WRichText geometry, independent mobile coordinates.
- **Not yet accepted:** entire website and page graph, source video/vector/special layers, media not already uploaded, interactions, automatic batch asset loading, unmatched nested/group layers, cross-section Y accumulation, font pixel parity, mobile visual fidelity, whole-site screenshot comparisons, publish control.
- Keep status distinct: `CAPTURED`, `RECIPE_GENERATED`, `WORKSPACE_PATCHED`, `WIX_IMPORTED`, `READBACK_CONFIRMED`, `LOCAL_GEOMETRY_PASS`, `PAGE_GEOMETRY_PASS`, `VISUAL_ACCEPTED`. Never collapse these into a single green status.

## No-duplicate-system decision

Continue to use LocalDesign as capture, the canonical Universal Page Recipe boundary as normalization, official Wix Studio Two Origami native import as execution and existing Playwright QA. Do not invent a second browser automation engine, Wix clone, new Chrome extension or proprietary remote credential route.


## Full-page reusable capability — current code, 2026-11-15

**Canonical procedure / status authority:** [NATIVE_GEOMETRY_TRANSFER_STANDARD.md §16](NATIVE_GEOMETRY_TRANSFER_STANDARD.md).
**Open final acceptance issue:** [#171](https://github.com/oleg3479881328-code/Project-Execution-OS/issues/171).

Do not use the one-section `localdesign_wix.py apply` as though it already builds whole pages.

Existing adapter now includes two **new bounded modules**, not a second scanner/editor stack:

- [`full_page_recipe.py`](full_page_recipe.py) — ZIP v2.4 → whole page normalized Recipe; records individual source element selectors, sections, per-breakpoint frames, paint candidates, exact source image URLs, mobile-only sections, and top-level detached layers such as `footer_0`.
- [`compile_full_page.py`](compile_full_page.py) — recipe → **workspace-only native page patch** in an already exported Wix site; requires explicit existing target page **folder and page ID** and `--allow-replace-page`; preserves the current Page wrapper, global header/footer/theme and other page files. Includes `finalize-media` step after official Wix CLI source-media upload.
- Existing [`verify_geometry.mjs`](verify_geometry.mjs) is still **single-section pilot QA**. It does not prove full-page browser acceptance. Full-page source-coverage + browser QA remains Issue #171.

### General workflow to run in any chat/agent

```bash
# From Website Creator Wix adapter; owner provides exact ZIP and target page.
python3 full_page_recipe.py --fingerprint SOURCE.zip --out recipe.json

# In an authorized official Wix dev environment, with fresh site export.
wix origami export-site --site SITE_ID -d wix-export --json
python3 compile_full_page.py compile --recipe recipe.json --export wix-export \
  --page TARGET_FOLDER --page-id TARGET_PAGE_ID --allow-replace-page

# Critical official Wix Media Manager step (original source URLs, no placeholders).
wix origami upload-media --site SITE_ID -d wix-export --json
python3 compile_full_page.py finalize-media --export wix-export --page TARGET_FOLDER

cd wix-export
yarn lint && yarn tsc && yarn build
wix origami import-site --site SITE_ID -d . --json

# Mandatory separate readback into a fresh directory; no publish.
wix origami export-site --site SITE_ID -d ../readback --json
# Then inspect all section/image/text/media/paint counts, run same-viewport Playwright
# LOCAL/PAGE geometry + visual/stack/mobile/interactions QA per standard §16.
```

**Stop rules:** never treat a generated recipe or imported site as full visual acceptance. `compile` is a **candidate** on a copied Wix export, not yet a proven no-touch deployment to an unrelated site. Exact original source assets only, no mutation of Home/shared globals. If style/background layering or media is ambiguous, stop rather than silently approximate. No publish without authorization.

### Current measurable evidence

- Vesper `/about` v2.4 latest donor ZIP: full-page normalizer **12 sections (separate mobile+desktop menus), 80 source elements, 18 exact images**, including `div#bio` original photo and 6 detached `div#footer_0` photos. Older v2.4 ZIP yielded 79 elements because its observed source DOM differed. **This reveals a real gap in previously reported Wix 17-image import**; source coverage not yet PASS.
- Compiler synthetic/local mock: **12 sections / 80 elements / 18 images** written to selected mock page.
- Compiler on a copied real Studio Two Origami export: wrote **11 sections / 79 elements / 17 images** using the earlier saved recipe; native lint preflight was interrupted by a **Wix dev machine loss during yarn install**, therefore full compiler acceptance remains BLOCKED.
- Earlier manual native full-page import + readback (rev42) and native Background colors (rev45) are proven separately; neither constitutes one-command fully automated universal browser QA.

Use this README to run, and the single existing canonical standard for knowledge. When the real full-page acceptance gates pass on two different donor pages/targets, promote only this same adapter; do not create one-off builders.


### Single-command full-page mode (candidate; native Wix workspace required)

The **existing** [run_wix_pipeline.sh](run_wix_pipeline.sh) now has an opt-in `WIX_MODE=full-page`, retaining its original one-section route by default. It orchestrates the modules listed here and uses official Wix Origami for all site mutations:

```bash
WIX_MODE=full-page \
WIX_SITE_ID="<existing site ID>" \
FINGERPRINT_ZIP="<source LocalDesign v2.4 ZIP>" \
WIX_TARGET_PAGE="<existing page folder>" \
WIX_TARGET_PAGE_ID="<verified page ID>" \
APPROVED_REPLACE_PAGE=YES \
PREVIEW_URL="<verified official draft/public preview URL>" \
bash run_wix_pipeline.sh
```

Optional `WIX_SOURCE_SECTIONS` points to a JSON array of source selectors only if section ordering is ambiguous; normal automatic discovery must be tried first. Optional `WIX_WORK_DIR` keeps the reproducible evidence directory. Omit `PREVIEW_URL` only to stop at `READBACK` with **Browser QA BLOCKED**, never call the page `DONE`. This mode **REPLACES authored content on the authorized page**; do not run it on another existing page without explicit user approval. No publish operation is included.

The source-coverage gates are implemented in [verify_full_page.py](verify_full_page.py), and actual Playwright DOM/asset gates in [verify_full_browser.mjs](verify_full_browser.mjs). Browser scripts write screenshots but do **not** claim automated screenshot pixel-diff parity or interaction validation. **These full-page modules have not yet passed complete real-Wix importer/readback/browser acceptance; status: CANDIDATE, not production one-click proven.** Track acceptance in [#171](https://github.com/oleg3479881328-code/Project-Execution-OS/issues/171).


## 2026-11-15 — Unified full-page runner + regression gate

The existing `run_wix_pipeline.sh` has a guarded `WIX_MODE=full-page` branch, reusing `full_page_recipe.py`, `compile_full_page.py`, `verify_full_page.py`, and `verify_full_browser.mjs`. It is the **single orchestration entrypoint**; do not create a second per-page runner.

Sample owner invocation (authenticated official Wix Origami environment; explicit site/page authority required):

```bash
WIX_MODE=full-page \
WIX_SITE_ID='<exact site ID>' \
FINGERPRINT_ZIP='/absolute/path/localdesign.zip' \
WIX_TARGET_PAGE='<existing exported page folder>' \
WIX_TARGET_PAGE_ID='<real page id in fresh export>' \
APPROVED_REPLACE_PAGE=YES \
PREVIEW_URL='<verified official Wix draft URL pointing at that target page>' \
bash run_wix_pipeline.sh
```

**Operational safeguards:**
- `PREVIEW_URL` is **mandatory before any mutation**. Never let an imported page count as accepted if browser QA has not run.
- Wix official `upload-media` may upload fewer files than source image instances, because images may already exist or repeat. Zero uploaded is not automatically an error; any uploader failure is an error. The per-image native URI and current `media.getCroppedImageUrl` are verified in `finalize-media`, and all images are rechecked after import.
- The pipeline requires the exact target page ID, explicit `APPROVED_REPLACE_PAGE=YES`, target-only Git diff, exact import scope, and fresh readback. It does not publish.
- Browser geometry and asset gate success is **not** `VISUAL=PASS`: screenshots/pixel differences, typography, overlaps, motion and interactions remain independently evaluated, never silently promoted.
- The full-page native Wix **manual proof** is real; this automatic one-command variant is still CANDIDATE until real accepted runs on two unrelated donors/targets demonstrate full import/readback/browser/visual QA.

**Repeatable regression suite:** `tests/test_full_page_recipe.py` runs synthetic source identity, detached footer-gallery, color paint, mobile-geometry and ambiguity tests. For owner's actual Vesper v2.4 ZIP:

```bash
LOCALDESIGN_VESPER_ZIP='/absolute/path/vesper-current.zip' \
  python3 -m unittest discover -s tests -v
```

Measured owner ZIP regression: current original Vesper /about capture yielded 12 selected source sections, 80 meaningful native candidates and **18 distinct image instances** (including the previously omitted Bio photo and six detached footer gallery images); an older capture yielded 12, 79 and 17 respectively. Do not hardcode these fixture-specific counts for other donors. Full-page counts must be generated and verified **per capture**.

Execution / acceptance backlog is tracked in [PEOS Issue #171](https://github.com/oleg3479881328-code/Project-Execution-OS/issues/171).


## Source dynamic media completeness gate (2026-11-15, verified)

The single existing full-page runner now executes `audit_source_layers.mjs` after LocalDesign recipe normalization and **before Wix export/media upload/page mutation**. This extends the existing acceptance workflow, **not** the original Chrome fingerprint scanner. It checks the live original donor using the existing Playwright capability and reports missing native video/iframe/canvas layers. A missing layer is `BLOCKED_MISSING_SOURCE_LAYERS`; a geometry-only pass cannot override it.

Verified on the actual Vesper `/about` source on Desktop 1280: `div#at-at-glance` contains a native Showit `<video>` inside a clipped background layer, source `https://static.showit.co/file/n86F2GdvRo6G8NIpT6hCXw/shared/pexels-anna-nekrashevich-7946210_n1xmcir9.mp4`, `autoplay=true`, `loop=true`, `muted=true`, `objectFit=cover`, parent-layer opacity `0.4`, poster fallback `pexels-maria-orlova-4946388.jpg`. The v2.4 ZIP recipe contains **no video element**, and older 12/80/18 geometry QA therefore produced a false overall impression of visual completeness.

The official installed Wix Studio Two component catalog has `wixSystemElements.Background.videoMedia` with native `autoplay`, `loop`, `muted`, `fittingType`, and `posterEffect` props. **Do not guess a Video media object schema or silently substitute a JPG**: actual MP4 import + native Background binding + opacity/crop/render QA must be accepted using a fresh export and the official Wix Media API before declaring this video's visual gate PASS.

Scanner source status: LocalDesign v2.4 Chrome scanner implementation has not been located in the PEOS repo; historically distributed as an extension ZIP. Therefore this change is a verified **safety/coverage gate in the existing adapter**; it is not a claim that the scanner extension itself was edited. Next accepted extension-schema improvement is additive `backgroundVideo[]` per observed viewport with `sourceUrl`, `posterUrl`, `autoplay`, `muted`, `loop`, `opacity`, `objectFit`, actual layer/frame rect, clip owner and source section identity; then compile via native Wix `Background.videoMedia` and re-export/Playwright acceptance. Preserve v2.4 fields and default to fail-closed on unobserved dynamic layers.

Run coverage only, no Wix mutation:

```bash
node audit_source_layers.mjs /path/to/normalized.recipe.json /path/to/source-layer-audit.json
```

**Current acceptance:** Full static geometry and media on saved `blank-2` revision 47 = PASS on 1280/390; missing video means complete visual 1:1 = BLOCKED. No additional editor changes or publishing were made by this audit.
