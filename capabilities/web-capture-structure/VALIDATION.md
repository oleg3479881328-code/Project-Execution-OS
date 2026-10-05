# Validation — web.capture_structure 0.1.0

## Current status

`candidate`

## Local verification

Executed on 2026-10-05 with Node.js 22.16.0:

```bash
npm run build:adapter
npm test
```

Result:

```text
4 tests passed
0 failed
```

Acceptance covers normalization, provider selection/fallback and output-contract shape with deterministic fixtures/fake Playwright page objects.

## Live validation gate

Not yet promoted to `validated` until the owner runs `adapters/dramaturg-one-block.js` against at least one real attached Chrome page and confirms:

- script finishes without navigation;
- one JSON file is downloaded;
- JSON parses;
- URL/title/viewport match the open page;
- node count is non-zero and representative;
- visible text/elements and geometry are present;
- provider is recorded (`cdp-dom-snapshot` preferred; fallback accepted when CDP is unavailable);
- target page remains operational and visually unchanged after capture.

## Live run evidence — 2026-10-05

Representative real-page run completed through Dramaturg against:

```text
https://thefamilylab.com/
```

Produced artifact:

```text
page-structure-thefamilylab.com-1791206140733.json
```

Observed artifact facts:

- schema: `peos.web_structure.v1`
- block: `web.capture_structure 0.1.0`
- provider: `dom-evaluate-fallback`
- page title: `Family Photogpraher`
- viewport: `1534 × 847`, DPR 1
- document: `1519 × 3944`
- JSON size: 159,192 bytes
- documents: 1
- nodes: 214
- unique style rows: 155
- element nodes: 189
- text nodes: 24
- image elements: 10
- link elements: 18
- missing parent references: 0
- invalid `styleRef` references: 0
- representative visible text, image URLs, navigation links and geometry are present.

The fallback warning is expected and accepted by contract:

```text
CDP DOMSnapshot was unavailable; fallback cannot fully flatten cross-origin iframes or closed shadow roots.
```

Machine-verifiable live acceptance therefore passes for artifact creation, parsing, representative structure and internal-reference integrity.

One manual gate remains: owner confirmation that the target page remained operational and visually unchanged after execution.

## Promotion boundary

A live run proves the Dramaturg bridge, not universal correctness across every framework. Multi-site validation should follow before any production-critical dependency on exact DOM reconstruction.
