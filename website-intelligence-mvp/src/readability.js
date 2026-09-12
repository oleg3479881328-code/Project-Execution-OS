import { Readability } from '@mozilla/readability';
import { JSDOM } from 'jsdom';

export function readable(html, url) {
  try {
    const article = new Readability(new JSDOM(html, { url }).window.document).parse();
    const text = String(article?.textContent || '').replace(/\s+/g, ' ').trim();
    return { title: article?.title || '', text, chars: text.length, words: text ? text.split(/\s+/).length : 0 };
  } catch (error) { return { title: '', text: '', chars: 0, words: 0, error: error.message }; }
}
