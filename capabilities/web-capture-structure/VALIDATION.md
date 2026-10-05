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

## Promotion boundary

A live run proves the Dramaturg bridge, not universal correctness across every framework. Multi-site validation should follow before any production-critical dependency on exact DOM reconstruction.
