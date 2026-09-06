import * as cheerio from 'cheerio';

const URL_ATTRS = ['src', 'data-src', 'poster'];
const SRCSET_ATTRS = ['srcset', 'data-srcset'];

function absolute(value, base) {
  if (!value || value.startsWith('data:') || value.startsWith('blob:')) return null;
  try { return new URL(value, base).href; } catch { return null; }
}

function candidates(value, base) {
  return String(value || '').split(',').map(part => part.trim().split(/\s+/)[0]).map(v => absolute(v, base)).filter(Boolean);
}

export function extractMedia(html, pageUrl) {
  const $ = cheerio.load(html);
  const records = new Map();
  const add = (url, item) => {
    if (!url) return;
    const old = records.get(url) || { url, srcset_candidates: [], alt: '', title: '', context: '' };
    records.set(url, { ...old, ...item, srcset_candidates: [...new Set([...(old.srcset_candidates || []), ...(item.srcset_candidates || [])])] });
  };
  $('img, picture source, video').each((_, el) => {
    const node = $(el); const tag = el.tagName.toLowerCase();
    const srcsets = SRCSET_ATTRS.flatMap(a => candidates(node.attr(a), pageUrl));
    const urls = URL_ATTRS.flatMap(a => [absolute(node.attr(a), pageUrl)]).filter(Boolean);
    for (const url of [...urls, ...srcsets]) add(url, { alt: node.attr('alt') || '', title: node.attr('title') || '', srcset_candidates: srcsets, context: node.closest('section, article, main, figure').find('h1,h2,h3,h4').first().text().trim() });
  });
  $('[style*="background-image"]').each((_, el) => {
    const matches = ($(el).attr('style') || '').matchAll(/url\(["']?([^"')]+)["']?\)/gi);
    for (const match of matches) add(absolute(match[1], pageUrl), { context: $(el).closest('section, article, main').find('h1,h2,h3,h4').first().text().trim() });
  });
  return [...records.values()].sort((a, b) => a.url.localeCompare(b.url));
}
