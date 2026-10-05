import test from 'node:test';
import assert from 'node:assert/strict';
import { captureStructureFromPage } from '../src/index.mjs';

test('fails clearly without a page object', async () => {
  await assert.rejects(() => captureStructureFromPage(null), /Playwright-compatible page object/);
});

test('forced cdp provider fails closed when CDP is unavailable', async () => {
  const page = { evaluate: async () => ({ url:'https://x.test', title:'x', viewport:{}, scroll:{}, document:{} }), context: () => ({}) };
  await assert.rejects(() => captureStructureFromPage(page, { provider:'cdp' }), /newCDPSession/);
});
