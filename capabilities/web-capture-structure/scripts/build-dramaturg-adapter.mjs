import { readFile, writeFile } from 'node:fs/promises';

const source = await readFile(new URL('../src/inline-core.mjs', import.meta.url), 'utf8');
const body = source
  .replace(/export async function captureStructureFromPage/, 'async function captureStructureFromPage')
  .replace(/\nexport \{ BLOCK_ID, BLOCK_VERSION, SCHEMA, STANDARD_STYLE_PROPERTIES \};\s*$/, '\n');

const adapter = `// GENERATED FILE — do not hand-edit.
// Build: node scripts/build-dramaturg-adapter.mjs
// Dramaturg / playwright-repl JS mode. Uses the currently attached page only.

${body}

const __peosStructure = await captureStructureFromPage(page, { provider: 'auto' });
const __peosFilename = 'page-structure-' + new URL(__peosStructure.page.url).hostname.replace(/[^a-z0-9.-]+/gi, '-') + '-' + Date.now() + '.json';
await page.evaluate(({ filename, text }) => {
  const blob = new Blob([text], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = filename; a.style.display = 'none';
  document.documentElement.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}, { filename: __peosFilename, text: JSON.stringify(__peosStructure) });
({ status: 'success', block: __peosStructure.block, provider: __peosStructure.provider, url: __peosStructure.page.url, nodes: __peosStructure.stats.nodes, file: __peosFilename });
`;

await writeFile(new URL('../adapters/dramaturg-one-block.js', import.meta.url), adapter, 'utf8');
console.log('generated adapters/dramaturg-one-block.js');
