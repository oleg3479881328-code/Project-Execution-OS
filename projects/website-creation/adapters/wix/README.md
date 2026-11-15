# LocalDesign → Wix Studio Two — Geometry Adapter

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
