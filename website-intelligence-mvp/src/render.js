import { chromium } from 'playwright';
import { AxeBuilder } from '@axe-core/playwright';

export async function captureRendered(url, outDir) {
  const browser = await chromium.launch(); const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } }); const page = await context.newPage();
  const consoleErrors = []; const requestFailures = [];
  page.on('console', msg => { if (msg.type() === 'error' || msg.type() === 'warning') consoleErrors.push(msg.text()); });
  page.on('requestfailed', request => requestFailures.push({ url: request.url(), failure: request.failure()?.errorText || 'unknown' }));
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1500);
  await page.evaluate(async () => { await new Promise(resolve => { let y = 0; const step = () => { y += 700; window.scrollTo(0, y); if (y >= document.body.scrollHeight) return resolve(); setTimeout(step, 100); }; step(); }); });
  await page.waitForTimeout(2000);
  const html = await page.content(); const aria = await page.ariaSnapshot();
  await page.screenshot({ path: `${outDir}/fullpage.png`, fullPage: true });
  const axe = await new AxeBuilder({ page }).analyze();
  const result = { html, finalUrl: page.url(), aria, axe, consoleErrors, requestFailures };
  await browser.close(); return result;
}
