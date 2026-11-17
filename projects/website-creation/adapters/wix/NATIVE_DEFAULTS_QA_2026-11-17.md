# Native Wix default fallbacks — implementation and QA (2026-11-17)

Canonical authority: [NATIVE_GEOMETRY_TRANSFER_STANDARD.md](NATIVE_GEOMETRY_TRANSFER_STANDARD.md) — owner-approved Wix-defaults policy. This is an evidence record for **the existing PEOS Wix adapter**, not a new rendering/ingestion workflow.

## Existing route (now implemented for fonts and mapped-element visual effects)

`LocalDesign v2.5.7 fingerprint ZIP` → existing `full_page_recipe.py` → existing `compile_full_page.py` → **`apply_wix_native_defaults.py`** (same native page export, optional policy pass; enabled by default with `WIX_NATIVE_DEFAULTS=YES`) → official `wix origami upload-media` / `finalize-media` / `lint` / `tsc` / `build` → existing import/readback/browser QA.

`apply_wix_native_defaults.py` is a small companion of the *existing adapter*, not a new scanner, converter or Wix builder:

- Verifies exact source fingerprint through existing `full_page_recipe.read_zip`; matches generated native `WRichText` IDs and source CSS family before making any change
- Resolves original source font families against the **current target Wix theme** `--wst-heading-N-font` and `--wst-paragraph-N-font`, not by choosing lookalikes
- For an original font not configured in that theme, replaces only `font-family` with the matching native Wix theme default; preserves exact X/Y/W/H, source text, typography metrics, original media and shared globals
- Records captured nondefault animation/filter/transform/clip effects on *mapped core elements* as `NATIVE_WIX_DEFAULT`; Wix keeps its native static behavior, no fabricated animations
- Writes `native-defaults-report.json` with sourceSelector, viewport, native component, original property, actual native theme choice and `sourceVisualParity: PARTIAL`
- Never downgrades `recipe.unsupported` or bypasses original media, target site/Page ID, changed-file-scope, official lint/tsc/build/import/readback and Playwright safety
- Reports `PASS_WITH_WIX_DEFAULTS` for native build/import but never `FULL_ACCEPTANCE` for visual source parity when any default is used

`run_wix_pipeline.sh` invokes this helper automatically between the official PEOS native compiler and Wix lint. `WIX_NATIVE_DEFAULTS=NO` explicitly preserves the legacy strict-font output, if required for comparative QA.

## Real original Vesper ZIP evidence

Source: owner supplied LocalDesign **2.5.7** actual Vesper `desktop-1920` / `mobile-390`, analyzed against the actual exported theme of approved experimental **Origami 261116 1511** site ID `7969ecbf-2525-43fd-9493-5670c637f351`.

- All source visual/font/effect capture fields are already available from LocalDesign 2.5.7; **no scanner modification is needed for this slice**
- Original normalized source: 12 sections; 75 main native elements; **413 mandatory unsupported source mapping records** (link/menu/footer/vector/overlap/asset), retained in unmodified original recipe
- **Isolated integration QA only**: created a temporary reduced recipe for testing exactly the font/default logic, with the 413 original unsupported records preserved in the untouched original JSON; removed dynamic/vector layers in the test-only copy. No import or publish from this reduced recipe.
- Real target Wix Theme defaults: `Georgia` for headings, `Arial` for paragraphs. **106 individual source font-family declarations** were switched to these actual Wix site defaults, plus **one captured original animation** documented as native static default: 107 source-aware fallback records, `sourceVisualParity=PARTIAL`
- Original 21 photos/GIF processed via the **official** Wix `upload-media` and `finalize-media` on the isolated export; 21 uploaded, 0 failed. Official `yarn lint`, `yarn tsc`, `yarn build` all **PASS**. Only existing experimental site's Media Manager was used; no editor page was imported or published.
- Standard PEOS tests: **25 PASS, 1 SKIP**, including six new tests for theme defaults and correct source provenance, source effect fallback, exact target/required object blocking, CSS geometry preservation and no replacement of installed theme fonts. `bash -n` and Python compile **PASS**.

## Remaining work / no false acceptance

This is **tested automation for native font/effect defaults**, NOT proof of universal fingerprint→Wix full-page completion. The original Vesper has 413 outstanding mapping records. The current canonical `run_wix_pipeline.sh` deliberately blocks such required source mappings instead of silently dropping them. These require existing Wix-native section/media/Chrome owner mapping work and a source-to-native coverage/visual QA gate; do **not** label the real Vesper ZIP `PASS_WITH_WIX_DEFAULTS` until those objects are accounted for.

The scanner should be modified only when an *actual missing measured property* is demonstrated. The captured style evidence already includes `fontFamily`, `animationName`, `transform`, `filter`, `clipPath` on Desktop and Mobile.
