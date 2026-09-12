# Website Intelligence MVP

One-page, local RAW-vs-rendered proof for the Peterloon competitor page. It deliberately has no crawler platform, server, database, dashboard, Firecrawl, or asset downloading.

## Setup and run

```bash
npm install
npx playwright install chromium
npx dembrandt install-browser
npm test
npm run analyze -- "https://brittanybays.com/blog/romantic-pastel-tented-wedding-at-peterloon-estate"
```

The bounded render strategy waits for DOM content, waits 1.5 seconds, scrolls through the document, then waits 2 seconds for late media. It does not rely on `networkidle` because long-lived connections can prevent deterministic completion. Artifacts are written to `artifacts/`; `report.json` contains separate, transparent metrics and the hypothesis classification.

## Investigation note

The earlier simpler parser exposed almost none of the media because it treated the page as article text and did not expand the Squarespace image markup. The persisted RAW HTML contains only 6 `<img>` elements, 5 `img[src]` values, 3 `img[srcset]` values, and 4 lazy `img[data-src]` values; there are no `picture source[srcset]` or inline background-image records. The MVP's media extractor expands the `srcset` candidates and includes lazy attributes, producing 26 normalized URL records. This is parser/extraction coverage, not evidence that browser rendering added media: the same 26 records are present after rendering.
