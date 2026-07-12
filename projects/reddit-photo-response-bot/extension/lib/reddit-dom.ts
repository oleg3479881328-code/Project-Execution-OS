import type { ParsedRedditPost } from './types';

const POST_SELECTORS = [
  'shreddit-post',
  '[data-testid="post-container"]',
  'article[data-testid="post-container"]',
  '.thing.link'
];

export function findPostElements(root: ParentNode = document): HTMLElement[] {
  const found = new Set<HTMLElement>();
  if (root instanceof HTMLElement) {
    for (const selector of POST_SELECTORS) {
      if (root.matches(selector)) found.add(root);
    }
  }
  for (const selector of POST_SELECTORS) {
    root.querySelectorAll<HTMLElement>(selector).forEach((element) => found.add(element));
  }
  return [...found];
}

function textFromFirst(element: HTMLElement, selectors: string[]): string {
  for (const selector of selectors) {
    const match = element.querySelector<HTMLElement>(selector);
    const text = match?.innerText?.trim() || match?.textContent?.trim();
    if (text) return text;
  }
  return '';
}

function normalizePermalink(raw: string): string {
  try {
    return new URL(raw, location.origin).href;
  } catch {
    return raw;
  }
}

function extractId(element: HTMLElement, permalink: string): string {
  const candidates = [
    element.getAttribute('thingid'),
    element.getAttribute('data-post-id'),
    element.getAttribute('data-fullname'),
    element.id
  ].filter(Boolean) as string[];

  for (const candidate of candidates) {
    const match = candidate.match(/(?:t3_)?([a-z0-9]+)$/i);
    if (match?.[1]) return match[1];
  }

  const permalinkMatch = permalink.match(/\/comments\/([a-z0-9]+)\//i);
  if (permalinkMatch?.[1]) return permalinkMatch[1];

  const fallback = `${permalink}|${textFromFirst(element, ['h1', 'h2', 'h3'])}`;
  let hash = 0;
  for (let index = 0; index < fallback.length; index += 1) {
    hash = (hash * 31 + fallback.charCodeAt(index)) >>> 0;
  }
  return `local-${hash.toString(16)}`;
}

export function parsePostElement(element: HTMLElement): ParsedRedditPost | null {
  const title = textFromFirst(element, [
    '[slot="title"]',
    'a[data-testid="post-title"]',
    'h1',
    'h2',
    'h3',
    '.title'
  ]);

  const body = textFromFirst(element, [
    '[slot="text-body"]',
    '[data-post-click-location="text-body"]',
    '[data-testid="post-content"]',
    '.usertext-body'
  ]);

  const permalinkAttribute =
    element.getAttribute('permalink') || element.getAttribute('data-permalink');
  const permalinkAnchor = element.querySelector<HTMLAnchorElement>('a[href*="/comments/"]');
  const permalink = normalizePermalink(
    permalinkAttribute || permalinkAnchor?.href || location.href
  );

  if (!title || !permalink.includes('/comments/')) return null;

  return {
    id: extractId(element, permalink),
    title,
    body,
    permalink,
    subreddit: 'WedditNYC'
  };
}
