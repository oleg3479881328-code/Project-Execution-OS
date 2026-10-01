# Family Lab -> Olga Newborn — v0 Proof Status

Date: 2026-10-01
Status: EXECUTOR PASS / INDEPENDENT ACCEPTANCE STILL PENDING

## Scope

Design donor: https://thefamilylab.com/portfolio
Client content source: https://www.olgapolophotography.com/newborn
TECH SPEC: https://drive.google.com/drive/folders/1Eh4O80ZBIgwWB7mb7fZ_qzx9OFaFS_vD

## Current executor-reported result

- Gallery geometry: PASS
- Non-gallery geometry: PASS against accepted 06 RAW mapping
- Colors: PASS
- Responsive states: PASS
- Photo corpus: 239 verified unique candidates
- Gallery slots: 63
- Unique assigned photos: 63
- Duplicate assignments: 0
- Crop review: 252/252 viewport-slot states reviewed by executor
- Photo crop quality: PASS by executor review
- Horizontal overflow: none reported
- Publication/deploy: NOT performed

## Approved font-substitution policy

Exact proprietary donor fonts are no longer a blocking requirement for this workflow.

Priority order:

1. preserve donor geometry and layout;
2. preserve typography character, hierarchy, scale, density, rhythm, and visual role;
3. use legitimate/easily available web fonts;
4. use exact donor face when convenient and legal;
5. otherwise use an approved visually similar substitute;
6. never extract/copy/rehost proprietary donor font binaries.

Current approved mapping for this proof:

- Cormorant Garamond -> Cormorant Garamond
- freight-display-pro -> Cormorant Garamond
- futura-pt -> Jost
- baskerville-poster-pt -> Libre Baskerville

The executor reports all three final families (Cormorant Garamond, Jost, Libre Baskerville) are actually loaded through Google Fonts.

Acceptance classification for substituted typography:

`PASS WITH APPROVED SUBSTITUTE`

Do not label substituted families as exact-font PASS.

Small controlled adjustments to font-size, font-weight, line-height, and letter-spacing are allowed to compensate for substitute metrics, provided accepted layout geometry remains stable.

## Permanent distinction: executor PASS vs independent acceptance

A v0 self-report is evidence, not final acceptance.

Before promotion to accepted Website Creator capability or release, independently verify at minimum:

- viewport renders at 1440x1000, 1200x900, 1024x900, 390x844;
- geometry parity;
- typography visual match under approved-substitute policy;
- 63 unique photos and no duplicate normalized source assets;
- subject-safe crops across all 252 rendered states;
- real Olga link provenance;
- no donor identity leakage;
- no broken images/links/overflow;
- build/runtime health.

## Lessons retained

1. One MASTER copy-paste execution block only; no mandatory follow-up fragments outside it.
2. Acceptance scope and RAW measurement coverage must match before execution.
3. Gallery geometry must be literal measured playback, not generic masonry/grid inference.
4. Client image aspect ratio never controls donor slot geometry.
5. Full authorized client image corpus must be searched before declaring shortage.
6. Wix transformed URLs must be normalized to underlying original asset identity.
7. Distinct donor slots require distinct client images when enough verified images exist.
8. Aspect-ratio matching is only a candidate-ranking signal; all rendered crops require visual subject-safety QA.
9. `object-position` is client-content/focal data and may be slot/viewport-specific while slot geometry stays frozen.
10. Declared font-family or `document.fonts.check()` alone is not sufficient proof of exact font availability.
11. Exact proprietary fonts are optional when an approved visually similar legitimate substitute preserves the intended design character.
12. Geometry PASS does not imply typography/content/crop PASS.

## Current boundary

The page is not yet independently accepted and must not be described as final production PASS solely from executor self-report.

Next acceptance step: independent visual/technical QA of the generated preview before any publish/deploy decision.
