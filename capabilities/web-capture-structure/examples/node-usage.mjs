import { captureStructureFromPage } from '../src/index.mjs';

// `page` is an already attached Playwright Page from the calling application.
const structure = await captureStructureFromPage(page);
console.log(JSON.stringify(structure, null, 2));
