import { parseCompactNumber } from './numbers';
import type { VideoRecord } from './types';

function asRecord(value: unknown): Record<string, unknown> | undefined {
  return value !== null && typeof value === 'object' && !Array.isArray(value)
    ? (value as Record<string, unknown>)
    : undefined;
}

function firstRecord(...values: unknown[]): Record<string, unknown> | undefined {
  for (const value of values) {
    const record = asRecord(value);
    if (record) return record;
  }
  return undefined;
}

function firstString(...values: unknown[]): string | undefined {
  for (const value of values) {
    if (typeof value === 'string' && value.trim()) return value.trim();
    if (typeof value === 'number' && Number.isFinite(value)) return String(value);
  }
  return undefined;
}

function firstNumber(...values: unknown[]): number | undefined {
  for (const value of values) {
    const parsed = parseCompactNumber(value);
    if (parsed > 0 || value === 0 || value === '0') return parsed;
  }
  return undefined;
}

function extractCover(video: Record<string, unknown>): string | undefined {
  const cover = video.cover;
  if (typeof cover === 'string') return cover;
  const coverRecord = asRecord(cover);
  const urlList = coverRecord?.urlList;
  return Array.isArray(urlList) ? firstString(urlList[0]) : firstString(coverRecord?.url);
}

function extractHashtags(item: Record<string, unknown>, description: string): string[] {
  const fromDescription = Array.from(description.matchAll(/#([\p{L}\p{N}_]+)/gu), (match) => match[1] ?? '').filter(Boolean);
  const textExtra = item.textExtra;
  const fromExtra = Array.isArray(textExtra)
    ? textExtra.flatMap((entry) => {
        const record = asRecord(entry);
        const name = firstString(record?.hashtagName, record?.hashtag_name);
        return name ? [name] : [];
      })
    : [];
  return Array.from(new Set([...fromDescription, ...fromExtra]));
}

export function normalizeTikTokItem(
  input: unknown,
  fallbackAuthor = '',
  source: VideoRecord['source'] = 'api',
): VideoRecord | undefined {
  const item = asRecord(input);
  if (!item) return undefined;

  const stats = firstRecord(item.stats, item.statsV2, item.statistics) ?? {};
  const authorRecord = firstRecord(item.author, item.authorInfo, item.author_info) ?? {};
  const videoRecord = firstRecord(item.video, item.videoInfo, item.video_info) ?? {};
  const musicRecord = firstRecord(item.music, item.musicInfo, item.music_info) ?? {};

  const id = firstString(item.id, item.awemeId, item.aweme_id, item.itemId, item.item_id);
  const author = firstString(
    authorRecord.uniqueId,
    authorRecord.unique_id,
    authorRecord.secUid,
    item.author,
    item.authorUniqueId,
    fallbackAuthor,
  )?.replace(/^@/, '');

  if (!id || !author) return undefined;

  const description = firstString(item.desc, item.description, item.title) ?? '';
  const publishedAt = firstNumber(item.createTime, item.create_time, item.createdAt);
  const durationMs = firstNumber(videoRecord.duration, item.duration);
  const profileUrl = `https://www.tiktok.com/@${author}`;

  return {
    id,
    author,
    profileUrl,
    videoUrl: `${profileUrl}/video/${id}`,
    description,
    publishedAt: publishedAt && publishedAt > 10_000_000_000 ? Math.floor(publishedAt / 1000) : publishedAt,
    durationSeconds: durationMs ? (durationMs > 600 ? Math.round(durationMs / 1000) : durationMs) : undefined,
    views: firstNumber(stats.playCount, stats.play_count, stats.viewCount, stats.views) ?? 0,
    likes: firstNumber(stats.diggCount, stats.digg_count, stats.likeCount, stats.likes) ?? 0,
    comments: firstNumber(stats.commentCount, stats.comment_count, stats.comments) ?? 0,
    shares: firstNumber(stats.shareCount, stats.share_count, stats.shares) ?? 0,
    saves: firstNumber(stats.collectCount, stats.collect_count, stats.saveCount, stats.saves),
    coverUrl: extractCover(videoRecord),
    hashtags: extractHashtags(item, description),
    audioTitle: firstString(musicRecord.title, musicRecord.musicName, musicRecord.music_name),
    isPinned: Boolean(item.isPinnedItem ?? item.isPinned ?? item.is_pinned),
    collectedAt: Date.now(),
    source,
  };
}

function looksLikeVideoItem(value: unknown): boolean {
  const record = asRecord(value);
  if (!record) return false;
  const hasId = Boolean(firstString(record.id, record.awemeId, record.aweme_id, record.itemId, record.item_id));
  const hasStats = Boolean(firstRecord(record.stats, record.statsV2, record.statistics));
  const hasVideo = Boolean(firstRecord(record.video, record.videoInfo, record.video_info));
  return hasId && (hasStats || hasVideo);
}

export function extractVideosFromPayload(
  payload: unknown,
  fallbackAuthor = '',
  source: VideoRecord['source'] = 'api',
): VideoRecord[] {
  const found = new Map<string, VideoRecord>();
  const seen = new WeakSet<object>();

  const visit = (value: unknown, depth: number): void => {
    if (depth > 14 || value === null || typeof value !== 'object') return;
    if (seen.has(value as object)) return;
    seen.add(value as object);

    if (looksLikeVideoItem(value)) {
      const normalized = normalizeTikTokItem(value, fallbackAuthor, source);
      if (normalized) found.set(normalized.id, normalized);
    }

    if (Array.isArray(value)) {
      for (const child of value) visit(child, depth + 1);
      return;
    }

    for (const child of Object.values(value as Record<string, unknown>)) visit(child, depth + 1);
  };

  visit(payload, 0);
  return [...found.values()];
}

export function extractVideosFromDom(username: string): VideoRecord[] {
  const found = new Map<string, VideoRecord>();
  const links = document.querySelectorAll<HTMLAnchorElement>(`a[href*="/@${CSS.escape(username)}/video/"]`);

  for (const link of links) {
    const url = new URL(link.href, location.origin);
    const match = url.pathname.match(/\/video\/(\d+)/);
    const id = match?.[1];
    if (!id || found.has(id)) continue;

    const card = link.closest<HTMLElement>('[data-e2e="user-post-item"], [data-e2e="user-post-item-list"] > div, div');
    const viewsNode = card?.querySelector<HTMLElement>('[data-e2e="video-views"], strong');
    const image = link.querySelector<HTMLImageElement>('img') ?? card?.querySelector<HTMLImageElement>('img');
    const description = image?.alt ?? link.getAttribute('aria-label') ?? '';

    found.set(id, {
      id,
      author: username,
      profileUrl: `https://www.tiktok.com/@${username}`,
      videoUrl: url.toString().split('?')[0] ?? url.toString(),
      description,
      views: parseCompactNumber(viewsNode?.textContent),
      likes: 0,
      comments: 0,
      shares: 0,
      coverUrl: image?.currentSrc || image?.src || undefined,
      hashtags: Array.from(description.matchAll(/#([\p{L}\p{N}_]+)/gu), (entry) => entry[1] ?? '').filter(Boolean),
      isPinned: Boolean(card?.textContent?.toLowerCase().includes('pinned')),
      collectedAt: Date.now(),
      source: 'dom',
    });
  }

  return [...found.values()];
}

export function mergeVideoRecords(current: VideoRecord, incoming: VideoRecord): VideoRecord {
  const preferIncoming = incoming.source !== 'dom' || current.source === 'dom';
  return {
    ...current,
    ...incoming,
    description: incoming.description || current.description,
    publishedAt: incoming.publishedAt ?? current.publishedAt,
    durationSeconds: incoming.durationSeconds ?? current.durationSeconds,
    views: Math.max(current.views, incoming.views),
    likes: Math.max(current.likes, incoming.likes),
    comments: Math.max(current.comments, incoming.comments),
    shares: Math.max(current.shares, incoming.shares),
    saves: Math.max(current.saves ?? 0, incoming.saves ?? 0) || undefined,
    coverUrl: incoming.coverUrl ?? current.coverUrl,
    hashtags: Array.from(new Set([...current.hashtags, ...incoming.hashtags])),
    audioTitle: incoming.audioTitle ?? current.audioTitle,
    isPinned: current.isPinned || incoming.isPinned,
    collectedAt: Math.max(current.collectedAt, incoming.collectedAt),
    source: preferIncoming ? incoming.source : current.source,
  };
}
