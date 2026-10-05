#!/usr/bin/env node
import { writeFile } from 'node:fs/promises';
import { captureStructureFromPage } from '../src/index.mjs';

function parseArgs(argv) {
  const out = { endpoint: 'http://localhost:9222', output: 'page-structure.json', provider: 'auto' };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--endpoint') out.endpoint = argv[++i];
    else if (a === '--output' || a === '-o') out.output = argv[++i];
    else if (a === '--page') out.page = Number(argv[++i]);
    else if (a === '--provider') out.provider = argv[++i];
    else if (a === '--include-hidden') out.includeHidden = true;
    else if (a === '--help' || a === '-h') out.help = true;
    else throw new Error(`Unknown argument: ${a}`);
  }
  return out;
}

const args = parseArgs(process.argv.slice(2));
if (args.help) {
  console.log('Usage: peos-web-capture-structure [--endpoint http://localhost:9222] [--page N] [-o page-structure.json] [--provider auto|cdp|dom] [--include-hidden]');
  process.exit(0);
}

let playwright;
try {
  playwright = await import('playwright');
} catch {
  console.error('playwright is required for the CLI adapter. Install it in the calling environment: npm install playwright');
  process.exit(2);
}

const browser = await playwright.chromium.connectOverCDP(args.endpoint);
try {
  const context = browser.contexts()[0];
  if (!context) throw new Error('No browser context available at CDP endpoint');
  const pages = context.pages();
  const page = pages[Number.isInteger(args.page) ? args.page : Math.max(0, pages.length - 1)];
  if (!page) throw new Error('No page available at CDP endpoint');
  const result = await captureStructureFromPage(page, { provider: args.provider, includeHidden: args.includeHidden });
  await writeFile(args.output, JSON.stringify(result, null, 2), 'utf8');
  console.log(JSON.stringify({ status: 'success', output: args.output, provider: result.provider, nodes: result.stats.nodes, url: result.page.url }));
} finally {
  await browser.close();
}
