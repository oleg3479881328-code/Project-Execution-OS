const TITLE_LIMIT = 100;
const ENHANCED_ATTR = 'youtubeTitleEnhanced';
const USER_EDITED_ATTR = 'youtubeTitleEdited';

function parseLocalizedCompactNumber(source: string): number | undefined {
  const normalized = source
    .toLowerCase()
    .replace(/\u00a0/g, ' ')
    .replace(/,/g, '.')
    .trim();

  const match = normalized.match(/([\d.]+)\s*(тыс\.?|млн|млрд|k|m|b)?/i);
  if (!match) return undefined;

  const value = Number(match[1]);
  if (!Number.isFinite(value)) return undefined;

  const suffix = match[2]?.replace('.', '').toLowerCase();
  const multiplier = suffix === 'тыс' || suffix === 'k'
    ? 1_000
    : suffix === 'млн' || suffix === 'm'
      ? 1_000_000
      : suffix === 'млрд' || suffix === 'b'
        ? 1_000_000_000
        : 1;

  return value * multiplier;
}

function formatEnglishCompact(source: string): string {
  const value = parseLocalizedCompactNumber(source);
  if (value === undefined) return '0';

  return new Intl.NumberFormat('en-US', {
    notation: 'compact',
    maximumFractionDigits: 1,
  }).format(value).replace(/\s+/g, '');
}

function cleanVideoTitle(description: string): string {
  let title = description
    .replace(/https?:\/\/\S+/gi, ' ')
    .replace(/#[\p{L}\p{N}_]+/gu, ' ')
    .replace(/@[\p{L}\p{N}_.]+/gu, ' ')
    .replace(/[\p{Extended_Pictographic}\uFE0F]/gu, ' ')
    .replace(/\s+/g, ' ')
    .trim();

  title = title.split(/\.{3}|…|[!?](?:\s|$)|\n/)[0]?.trim() ?? '';

  const disposablePrefixes = [
    /^you just gotta\s+/i,
    /^you gotta\s+/i,
    /^you just have to\s+/i,
    /^you have to\s+/i,
    /^just gotta\s+/i,
  ];

  for (const prefix of disposablePrefixes) {
    title = title.replace(prefix, '');
  }

  title = title
    .replace(/^[\s"'“”‘’.,:;\-–—]+/, '')
    .replace(/[\s"'“”‘’.,:;\-–—]+$/, '')
    .replace(/\s+/g, ' ')
    .trim();

  if (!title) return 'TikTok video';
  return `${title.charAt(0).toUpperCase()}${title.slice(1)}`;
}

function truncateAtWord(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  const shortened = text.slice(0, Math.max(0, maxLength)).trimEnd();
  const lastSpace = shortened.lastIndexOf(' ');
  return (lastSpace > 12 ? shortened.slice(0, lastSpace) : shortened).trim();
}

function resolveAuthor(card: HTMLElement): string {
  const directAuthor = card.querySelector<HTMLElement>('.video-author')?.textContent?.trim();
  if (directAuthor) return directAuthor.replace(/^@/, '');

  const groupedAuthor = card.closest('.account-group')
    ?.querySelector<HTMLElement>(':scope > header a')
    ?.textContent
    ?.trim();
  if (groupedAuthor) return groupedAuthor.replace(/^@/, '');

  const favoriteAuthor = card.closest('.favorite-channel-group')
    ?.querySelector<HTMLElement>('.channel-identity > a')
    ?.textContent
    ?.trim();
  return favoriteAuthor?.replace(/^@/, '') ?? '';
}

function buildYouTubeTitle(card: HTMLElement): string {
  const viewsSource = card.querySelector<HTMLElement>('.metrics strong')?.textContent ?? '';
  const likesSource = card.querySelector<HTMLElement>('.micro-metrics span:first-child')?.textContent ?? '';
  const description = card.querySelector<HTMLElement>('.video-copy > p')?.textContent ?? '';
  const author = resolveAuthor(card);

  const views = formatEnglishCompact(viewsSource);
  const likes = formatEnglishCompact(likesSource);
  const prefix = `${views} views ${likes} likes`;
  const suffix = author ? `@${author}` : '';
  const availableForTitle = Math.max(12, TITLE_LIMIT - prefix.length - suffix.length - 2);
  const shortTitle = truncateAtWord(cleanVideoTitle(description), availableForTitle);

  return [prefix, shortTitle, suffix].filter(Boolean).join(' ').slice(0, TITLE_LIMIT).trim();
}

function injectStyles(): void {
  if (document.getElementById('youtube-title-enhancer-styles')) return;

  const style = document.createElement('style');
  style.id = 'youtube-title-enhancer-styles';
  style.textContent = `
    .youtube-title-block {
      display: grid;
      gap: 6px;
      margin: 0 42px 9px 0;
      padding: 8px;
      border: 1px solid rgba(36, 231, 202, .24);
      border-radius: 10px;
      background: rgba(36, 231, 202, .07);
    }
    .youtube-title-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }
    .youtube-title-label {
      color: #74ead8;
      font-size: 9px;
      font-weight: 800;
      letter-spacing: .08em;
    }
    .youtube-title-copy {
      padding: 4px 7px;
      border-radius: 7px;
      color: #07120f;
      background: #74ead8;
      font-size: 9px;
      font-weight: 800;
    }
    .youtube-title-copy.copied {
      background: #a9f4c9;
    }
    .youtube-title-input {
      width: 100%;
      min-height: 48px;
      resize: vertical;
      color: #fff;
      background: #0d1517;
      border: 1px solid rgba(116, 234, 216, .24);
      border-radius: 8px;
      padding: 7px 8px;
      font: 600 11px/1.35 Inter, ui-sans-serif, system-ui, sans-serif;
    }
    .youtube-title-input:focus {
      border-color: #74ead8;
      box-shadow: 0 0 0 3px rgba(116, 234, 216, .12);
      outline: none;
    }
  `;
  document.head.append(style);
}

function refreshEnhancedCard(card: HTMLElement): void {
  const input = card.querySelector<HTMLTextAreaElement>('.youtube-title-input');
  if (!input || input.dataset[USER_EDITED_ATTR] === 'true') return;

  const nextTitle = buildYouTubeTitle(card);
  if (input.value !== nextTitle) input.value = nextTitle;
}

function enhanceCard(card: HTMLElement): void {
  const existingInput = card.querySelector<HTMLTextAreaElement>('.youtube-title-input');
  if (existingInput) {
    refreshEnhancedCard(card);
    return;
  }

  const videoCopy = card.querySelector<HTMLElement>('.video-copy');
  if (!videoCopy) return;

  const block = document.createElement('div');
  block.className = 'youtube-title-block';

  const head = document.createElement('div');
  head.className = 'youtube-title-head';

  const label = document.createElement('span');
  label.className = 'youtube-title-label';
  label.textContent = 'YOUTUBE TITLE';

  const copyButton = document.createElement('button');
  copyButton.type = 'button';
  copyButton.className = 'youtube-title-copy';
  copyButton.textContent = 'Copy';

  const input = document.createElement('textarea');
  input.className = 'youtube-title-input';
  input.rows = 2;
  input.maxLength = TITLE_LIMIT;
  input.spellcheck = false;
  input.value = buildYouTubeTitle(card);
  input.setAttribute('aria-label', 'YouTube title');
  input.addEventListener('input', () => {
    input.dataset[USER_EDITED_ATTR] = 'true';
  });

  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(input.value.trim());
      copyButton.textContent = 'Copied';
      copyButton.classList.add('copied');
      window.setTimeout(() => {
        copyButton.textContent = 'Copy';
        copyButton.classList.remove('copied');
      }, 1200);
    } catch {
      input.focus();
      input.select();
      document.execCommand('copy');
    }
  });

  head.append(label, copyButton);
  block.append(head, input);
  videoCopy.prepend(block);
  card.dataset[ENHANCED_ATTR] = 'true';
}

function enhanceAllCards(): void {
  injectStyles();
  document.querySelectorAll<HTMLElement>('.video-card').forEach(enhanceCard);
}

let scheduled = false;
function scheduleEnhancement(): void {
  if (scheduled) return;
  scheduled = true;
  window.requestAnimationFrame(() => {
    scheduled = false;
    enhanceAllCards();
  });
}

const root = document.getElementById('root');
if (root) {
  new MutationObserver(scheduleEnhancement).observe(root, {
    childList: true,
    subtree: true,
    characterData: true,
  });
}

scheduleEnhancement();
