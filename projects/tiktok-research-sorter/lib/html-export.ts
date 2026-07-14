import { enrichVideos } from './analytics';
import { groupFavoriteEntriesByChannel } from './favorites';
import { APP_VERSION } from './types';
import type { ChannelSnapshot, FavoriteEntry } from './types';

export interface FavoritesHtmlOptions {
  title?: string;
  generatedAt?: number;
}

function escapeHtml(value: unknown): string {
  return String(value ?? '')
    .replace(/&/gu, '&amp;')
    .replace(/</gu, '&lt;')
    .replace(/>/gu, '&gt;')
    .replace(/"/gu, '&quot;')
    .replace(/'/gu, '&#39;');
}

function safeHttpUrl(value: string | undefined): string | undefined {
  if (!value) return undefined;
  try {
    const url = new URL(value);
    return url.protocol === 'http:' || url.protocol === 'https:' ? url.toString() : undefined;
  } catch {
    return undefined;
  }
}

function formatNumber(value: number | undefined): string {
  return value === undefined ? '—' : new Intl.NumberFormat('ru-RU').format(value);
}

function formatPercent(value: number | undefined): string {
  return value === undefined ? '—' : `${value.toFixed(2)}%`;
}

function formatDateMs(timestamp: number | undefined): string {
  if (!timestamp) return '—';
  return new Intl.DateTimeFormat('ru-RU', {
    day: '2-digit',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(new Date(timestamp));
}

function formatDateSeconds(timestampSeconds: number | undefined): string {
  if (!timestampSeconds) return '—';
  return new Intl.DateTimeFormat('ru-RU', {
    day: '2-digit',
    month: 'long',
    year: 'numeric',
  }).format(new Date(timestampSeconds * 1000));
}

function yesNo(value: boolean | undefined): string {
  return value === undefined ? '—' : value ? 'Да' : 'Нет';
}

function renderPreview(coverUrl: string | undefined, author: string): string {
  const safeCover = safeHttpUrl(coverUrl);
  if (!safeCover) return '<div class="preview placeholder">Превью недоступно</div>';
  return `<img class="preview" src="${escapeHtml(safeCover)}" alt="Превью ролика @${escapeHtml(author)}" loading="lazy">`;
}

function renderAvatar(channel: ChannelSnapshot): string {
  const avatarUrl = safeHttpUrl(channel.avatarUrl);
  if (avatarUrl) {
    return `<img src="${escapeHtml(avatarUrl)}" alt="Аватар @${escapeHtml(channel.username)}" loading="lazy">`;
  }
  const initials = (channel.displayName || channel.username)
    .split(/\s+/u)
    .filter(Boolean)
    .slice(0, 2)
    .map((part) => part[0]?.toUpperCase() ?? '')
    .join('') || 'TT';
  return `<span>${escapeHtml(initials)}</span>`;
}

function renderDetail(label: string, value: unknown): string {
  return `<div><span>${escapeHtml(label)}</span><strong>${escapeHtml(value ?? '—')}</strong></div>`;
}

function renderChannel(channel: ChannelSnapshot): string {
  const profileUrl = safeHttpUrl(channel.profileUrl);
  const website = safeHttpUrl(channel.website);
  const hashtags = channel.strongestHashtags
    .map((tag) => `<span>#${escapeHtml(tag.replace(/^#/u, ''))}</span>`)
    .join('');

  return `
    <section class="channel-card" data-channel="${escapeHtml(channel.username.toLowerCase())}">
      <div class="channel-head">
        <a class="channel-avatar" href="${escapeHtml(profileUrl ?? '#')}" target="_blank" rel="noopener noreferrer">
          ${renderAvatar(channel)}
        </a>
        <div class="channel-identity">
          <div class="channel-title">
            <h2>${escapeHtml(channel.displayName || `@${channel.username}`)}</h2>
            ${channel.verified ? '<span class="verified" title="Проверенный аккаунт">✓</span>' : ''}
            <span class="completeness ${escapeHtml(channel.completeness)}">${channel.completeness === 'full' ? 'полные данные' : 'частичные данные'}</span>
          </div>
          <a class="username" href="${escapeHtml(profileUrl ?? '#')}" target="_blank" rel="noopener noreferrer">@${escapeHtml(channel.username)}</a>
          ${channel.bio ? `<p class="bio">${escapeHtml(channel.bio)}</p>` : '<p class="bio muted">Биография не указана.</p>'}
          <div class="channel-links">
            <a href="${escapeHtml(profileUrl ?? '#')}" target="_blank" rel="noopener noreferrer">Открыть профиль ↗</a>
            ${website ? `<a href="${escapeHtml(website)}" target="_blank" rel="noopener noreferrer">Сайт ↗</a>` : ''}
          </div>
        </div>
      </div>

      <div class="channel-metrics">
        <div><span>Подписчики</span><strong>${escapeHtml(formatNumber(channel.followers))}</strong></div>
        <div><span>Подписки</span><strong>${escapeHtml(formatNumber(channel.following))}</strong></div>
        <div><span>Друзья</span><strong>${escapeHtml(formatNumber(channel.friends))}</strong></div>
        <div><span>Лайки профиля</span><strong>${escapeHtml(formatNumber(channel.totalLikes))}</strong></div>
        <div><span>Видео в профиле</span><strong>${escapeHtml(formatNumber(channel.videoCount))}</strong></div>
        <div><span>Собрано видео</span><strong>${escapeHtml(formatNumber(channel.collectedVideoCount))}</strong></div>
        <div><span>Медиана просмотров</span><strong>${escapeHtml(formatNumber(channel.medianViews))}</strong></div>
        <div><span>Средний ER</span><strong>${escapeHtml(formatPercent(channel.averageEngagementRate))}</strong></div>
      </div>

      <div class="channel-details">
        ${renderDetail('User ID', channel.userId || '—')}
        ${renderDetail('secUid', channel.secUid || '—')}
        ${renderDetail('Регион', channel.region || '—')}
        ${renderDetail('Язык', channel.language || '—')}
        ${renderDetail('Дата создания', formatDateSeconds(channel.accountCreatedAt))}
        ${renderDetail('Закрытый аккаунт', yesNo(channel.privateAccount))}
        ${renderDetail('Коммерческий аккаунт', yesNo(channel.commerceAccount))}
        ${renderDetail('Источник данных', channel.profileDataSource || '—')}
        ${renderDetail('Последнее сканирование', formatDateMs(channel.lastScannedAt))}
        ${renderDetail('Профиль обновлён', formatDateMs(channel.profileDataUpdatedAt || channel.capturedAt))}
      </div>

      <div class="channel-topics">
        <span>Сильные темы канала</span>
        <div>${hashtags || '<em>Недостаточно собранных роликов.</em>'}</div>
      </div>
    </section>`;
}

function renderVideoCard(entry: FavoriteEntry, rank: number, enrichedVideo: ReturnType<typeof enrichVideos>[number] | undefined): string {
  const video = enrichedVideo ?? entry.video;
  const videoUrl = safeHttpUrl(video.videoUrl);
  const profileUrl = safeHttpUrl(video.profileUrl);
  const hashtags = video.hashtags
    .map((tag) => `<span>#${escapeHtml(tag.replace(/^#/u, ''))}</span>`)
    .join('');
  const description = video.description?.trim() || 'Без описания';
  const engagement = 'engagementRate' in video && typeof video.engagementRate === 'number'
    ? `${video.engagementRate.toFixed(2)}%`
    : '—';

  return `
    <article class="video-card" data-video-key="${escapeHtml(entry.key)}">
      <div class="rank">${rank}</div>
      <a class="preview-link" href="${escapeHtml(videoUrl ?? '#')}" target="_blank" rel="noopener noreferrer">
        ${renderPreview(video.coverUrl, video.author)}
      </a>
      <div class="content">
        <div class="video-head">
          <div>
            <a class="author" href="${escapeHtml(profileUrl ?? '#')}" target="_blank" rel="noopener noreferrer">@${escapeHtml(video.author)}</a>
            <div class="date">Опубликовано: ${escapeHtml(formatDateSeconds(video.publishedAt))}</div>
            <div class="date">Добавлено в избранное: ${escapeHtml(formatDateMs(entry.favoritedAt))}</div>
          </div>
          <a class="open" href="${escapeHtml(videoUrl ?? '#')}" target="_blank" rel="noopener noreferrer">Открыть ролик ↗</a>
        </div>
        <p class="description">${escapeHtml(description)}</p>
        <div class="video-metrics">
          <div><span>Просмотры</span><strong>${escapeHtml(formatNumber(video.views))}</strong></div>
          <div><span>Лайки</span><strong>${escapeHtml(formatNumber(video.likes))}</strong></div>
          <div><span>Комментарии</span><strong>${escapeHtml(formatNumber(video.comments))}</strong></div>
          <div><span>Репосты</span><strong>${escapeHtml(formatNumber(video.shares))}</strong></div>
          <div><span>Сохранения</span><strong>${escapeHtml(formatNumber(video.saves))}</strong></div>
          <div><span>ER</span><strong>${escapeHtml(engagement)}</strong></div>
          <div><span>Длительность</span><strong>${video.durationSeconds === undefined ? '—' : `${escapeHtml(video.durationSeconds)} сек.`}</strong></div>
          <div><span>Закреплён</span><strong>${video.isPinned ? 'Да' : 'Нет'}</strong></div>
        </div>
        ${video.audioTitle ? `<div class="audio">Аудио: ${escapeHtml(video.audioTitle)}</div>` : ''}
        <div class="hashtags">${hashtags}</div>
      </div>
    </article>`;
}

export function generateFavoritesHtml(
  entries: FavoriteEntry[],
  options: FavoritesHtmlOptions = {},
): string {
  const title = options.title?.trim() || 'Отобранные TikTok-ролики и каналы';
  const generatedAt = options.generatedAt ?? Date.now();
  const enriched = enrichVideos(entries.map((entry) => entry.video));
  const enrichedByKey = new Map(entries.map((entry, index) => [entry.key, enriched[index]]));
  const groups = groupFavoriteEntriesByChannel(entries);

  const channelSections = groups.map((group) => `
    <section class="channel-section">
      ${renderChannel(group.channel)}
      <div class="videos">
        ${group.entries.map((entry, index) => renderVideoCard(entry, index + 1, enrichedByKey.get(entry.key))).join('\n')}
      </div>
    </section>`).join('\n');

  const generatedLabel = formatDateMs(generatedAt);

  return `<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="generator" content="TikTok Research Sorter v${APP_VERSION}">
  <title>${escapeHtml(title)}</title>
  <style>
    :root { color-scheme: light; font-family: Inter, Arial, sans-serif; color: #1d2230; background: #f3f5f9; }
    * { box-sizing: border-box; }
    body { margin: 0; background: #f3f5f9; }
    .page { width: min(1180px, calc(100% - 32px)); margin: 0 auto; padding: 36px 0 60px; }
    .header { background: linear-gradient(135deg, #171b2c, #34235d); color: #fff; border-radius: 24px; padding: 28px; margin-bottom: 24px; }
    .header h1 { margin: 0; font-size: clamp(26px, 5vw, 44px); line-height: 1.05; }
    .header p { margin: 12px 0 0; color: #d4d3e8; line-height: 1.5; }
    .summary { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 18px; }
    .summary span { background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.16); border-radius: 999px; padding: 8px 12px; font-size: 13px; }
    .channel-section { display: grid; gap: 16px; margin-bottom: 28px; }
    .channel-card, .video-card { background: #fff; border: 1px solid #e2e6ef; border-radius: 20px; box-shadow: 0 14px 35px rgba(30,36,52,.08); }
    .channel-card { padding: 22px; border-top: 5px solid #6840d8; }
    .channel-head { display: grid; grid-template-columns: 92px minmax(0,1fr); gap: 18px; align-items: start; }
    .channel-avatar { width: 92px; height: 92px; border-radius: 50%; overflow: hidden; display: grid; place-items: center; text-decoration: none; background: linear-gradient(135deg, #2d3346, #6840d8); color: #fff; font-size: 26px; font-weight: 900; }
    .channel-avatar img { width: 100%; height: 100%; object-fit: cover; }
    .channel-title { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
    .channel-title h2 { margin: 0; font-size: 26px; }
    .verified { width: 20px; height: 20px; border-radius: 50%; display: grid; place-items: center; background: #36a9ff; color: #fff; font-size: 12px; }
    .completeness { border-radius: 999px; padding: 5px 8px; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; }
    .completeness.full { color: #087f58; background: #e8faf2; border: 1px solid #bfe9d6; }
    .completeness.partial { color: #8a6300; background: #fff6dc; border: 1px solid #efdfa8; }
    .username { display: inline-block; margin-top: 5px; color: #6840d8; font-weight: 800; text-decoration: none; }
    .bio { margin: 12px 0 0; color: #394052; line-height: 1.5; white-space: pre-wrap; }
    .muted { color: #8b92a2; }
    .channel-links { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px; }
    .channel-links a, .open { color: #fff; background: #6840d8; border-radius: 10px; padding: 9px 12px; font-weight: 700; text-decoration: none; }
    .channel-metrics, .video-metrics { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 10px; margin-top: 20px; }
    .channel-metrics div, .video-metrics div { background: #f5f6fa; border: 1px solid #e7e9f0; border-radius: 12px; padding: 10px; }
    .channel-metrics span, .video-metrics span, .channel-details span { display: block; color: #81889a; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; }
    .channel-metrics strong, .video-metrics strong { display: block; margin-top: 5px; font-size: 17px; }
    .channel-details { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 8px 18px; margin-top: 18px; padding-top: 18px; border-top: 1px solid #eceef4; }
    .channel-details div { min-width: 0; }
    .channel-details strong { display: block; margin-top: 4px; overflow-wrap: anywhere; font-size: 13px; }
    .channel-topics { margin-top: 18px; }
    .channel-topics > span { color: #81889a; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; }
    .channel-topics > div, .hashtags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 9px; }
    .channel-topics div span, .hashtags span { color: #087f73; background: #e9faf7; border: 1px solid #c9eee8; border-radius: 999px; padding: 5px 8px; font-size: 12px; }
    .channel-topics em { color: #8b92a2; font-size: 13px; }
    .videos { display: grid; gap: 16px; }
    .video-card { position: relative; display: grid; grid-template-columns: 220px minmax(0,1fr); gap: 20px; padding: 16px; }
    .rank { position: absolute; top: 24px; left: 24px; z-index: 2; background: rgba(0,0,0,.76); color: #fff; border-radius: 10px; padding: 6px 9px; font-weight: 800; }
    .preview-link { display: block; min-height: 300px; border-radius: 14px; overflow: hidden; background: #111522; text-decoration: none; }
    .preview { width: 100%; height: 100%; min-height: 300px; object-fit: cover; display: block; }
    .placeholder { display: grid; place-items: center; color: #aeb5c7; padding: 20px; text-align: center; }
    .content { min-width: 0; padding: 4px 4px 4px 0; }
    .video-head { display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; }
    .author { color: #6840d8; font-size: 18px; font-weight: 800; text-decoration: none; }
    .date { margin-top: 5px; color: #7d8496; font-size: 13px; }
    .description { margin: 20px 0; color: #303747; font-size: 16px; line-height: 1.55; white-space: pre-wrap; }
    .audio { margin-top: 15px; color: #5d6475; font-size: 13px; }
    .empty { background: #fff; border: 1px dashed #cbd1df; border-radius: 18px; padding: 50px 20px; text-align: center; color: #6e7586; }
    .footer { margin-top: 26px; color: #7d8494; font-size: 12px; text-align: center; }
    @media (max-width: 820px) {
      .channel-metrics, .video-metrics { grid-template-columns: repeat(2, minmax(0,1fr)); }
      .video-card { grid-template-columns: 1fr; }
      .preview-link, .preview { min-height: 420px; max-height: 620px; }
    }
    @media (max-width: 560px) {
      .channel-head { grid-template-columns: 1fr; }
      .channel-avatar { width: 78px; height: 78px; }
      .channel-details { grid-template-columns: 1fr; }
      .video-head { display: grid; }
      .open { justify-self: start; }
    }
    @media print {
      body { background: #fff; }
      .page { width: 100%; padding: 0; }
      .header, .channel-card, .video-card { box-shadow: none; }
      .channel-card, .video-card { break-inside: avoid; }
    }
  </style>
</head>
<body>
  <main class="page">
    <header class="header">
      <h1>${escapeHtml(title)}</h1>
      <p>Выбранные TikTok-ролики с полной публичной информацией о каналах, ссылками, описаниями, метриками и превью.</p>
      <div class="summary">
        <span>Каналов: ${groups.length}</span>
        <span>Роликов: ${entries.length}</span>
        <span>Создано: ${escapeHtml(generatedLabel)}</span>
        <span>TikTok Research Sorter v${APP_VERSION}</span>
      </div>
    </header>
    <section>
      ${channelSections || '<div class="empty">В подборке нет выбранных роликов.</div>'}
    </section>
    <footer class="footer">Страница создана локально. Показаны только публичные данные, которые TikTok реально предоставил во время сбора. Внешние превью могут позднее перестать загружаться.</footer>
  </main>
</body>
</html>`;
}
