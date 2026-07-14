import { parseCompactNumber } from './numbers';
import type { ProfileRecord, VideoRecord } from './types';

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

function extractUrl(value: unknown): string | undefined {
  if (typeof value === 'string' && value.trim()) return value.trim();
  const record = asRecord(value);
  const list = record?.urlList ?? record?.url_list;
  if (Array.isArray(list)) return firstString(list[0]);
  return firstString(record?.url, record?.uri);
}

function sanitizeHttpUrl(value: string | undefined): string | undefined {
  if (!value) return undefined;
  try {
    const url = new URL(value);
    return url.protocol === 'http:' || url.protocol === 'https:' ? url.toString() : undefined;
  } catch {
    return undefined;
  }
}

function extractCover(video: Record<string, unknown>): string | undefined {
  return sanitizeHttpUrl(extractUrl(video.cover))
    ?? sanitizeHttpUrl(extractUrl(video.dynamicCover))
    ?? sanitizeHttpUrl(extractUrl(video.originCover));
}

function normalizeDurationSeconds(...values: unknown[]): number | undefined {
  const raw = firstNumber(...values);
  if (raw === undefined) return undefined;
  return raw > 3_600 ? Math.max(1, Math.round(raw / 1_000)) : raw;
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
  const profileUrl = `https://www.tiktok.com/@${author}`;

  return {
    id,
    author,
    profileUrl,
    videoUrl: `${profileUrl}/video/${id}`,
    description,
    publishedAt: publishedAt && publishedAt > 10_000_000_000 ? Math.floor(publishedAt / 1_000) : publishedAt,
    durationSeconds: normalizeDurationSeconds(videoRecord.duration, item.duration),
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
  let visitedCount = 0;
  const MAX_VISITS = 50_000;

  const visit = (value: unknown, depth: number): void => {
    if (depth > 14 || value === null || typeof value !== 'object') return;
    if (seen.has(value as object) || visitedCount >= MAX_VISITS) return;
    seen.add(value as object);
    visitedCount += 1;

    if (looksLikeVideoItem(value)) {
      const normalized = normalizeTikTokItem(value, fallbackAuthor, source);
      if (normalized) found.set(`${normalized.author.toLowerCase()}:${normalized.id}`, normalized);
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

function normalizeProfileCandidate(
  input: unknown,
  fallbackUsername = '',
  source: ProfileRecord['source'] = 'api',
): ProfileRecord | undefined {
  const container = asRecord(input);
  if (!container) return undefined;

  const userInfo = firstRecord(container.userInfo, container.user_info, container) ?? container;
  const user = firstRecord(userInfo.user, userInfo.author, container.user, container.author, userInfo) ?? userInfo;
  const stats = firstRecord(userInfo.stats, userInfo.statistics, container.stats, container.statistics, user.stats) ?? {};

  const username = firstString(
    user.uniqueId,
    user.unique_id,
    user.username,
    user.handle,
    container.uniqueId,
    fallbackUsername,
  )?.replace(/^@/, '');
  if (!username) return undefined;
  if (fallbackUsername && username.toLowerCase() !== fallbackUsername.toLowerCase()) return undefined;

  const displayName = firstString(user.nickname, user.displayName, user.display_name, container.nickname);
  const bio = firstString(user.signature, user.bio, user.description, container.signature);
  const avatarUrl = sanitizeHttpUrl(extractUrl(user.avatarLarger))
    ?? sanitizeHttpUrl(extractUrl(user.avatarMedium))
    ?? sanitizeHttpUrl(extractUrl(user.avatarThumb))
    ?? sanitizeHttpUrl(extractUrl(user.avatar))
    ?? sanitizeHttpUrl(extractUrl(container.avatarLarger));
  const followers = firstNumber(stats.followerCount, stats.follower_count, stats.followers);
  const following = firstNumber(stats.followingCount, stats.following_count, stats.following);
  const totalLikes = firstNumber(stats.heartCount, stats.heart_count, stats.heart, stats.diggCount, stats.likes);
  const videoCount = firstNumber(stats.videoCount, stats.video_count, stats.videos);
  const website = sanitizeHttpUrl(
    extractUrl(user.bioLink)
    ?? extractUrl(user.bio_link)
    ?? firstString(user.website, user.url),
  );
  const verified = Boolean(user.verified ?? user.isVerified ?? user.is_verified);

  const hasIdentityDetails = Boolean(displayName || bio || avatarUrl || website || verified);
  const hasProfileStats = [followers, following, totalLikes, videoCount].some((value) => value !== undefined);
  if (!hasIdentityDetails && !hasProfileStats) return undefined;

  return {
    username,
    profileUrl: `https://www.tiktok.com/@${username}`,
    displayName,
    bio,
    avatarUrl,
    followers,
    following,
    totalLikes,
    videoCount,
    verified,
    website,
    collectedAt: Date.now(),
    source,
  };
}

export function extractProfileFromPayload(
  payload: unknown,
  fallbackUsername = '',
  source: ProfileRecord['source'] = 'api',
): ProfileRecord | undefined {
  const seen = new WeakSet<object>();
  const candidates: ProfileRecord[] = [];
  let visitedCount = 0;
  const MAX_VISITS = 50_000;

  const visit = (value: unknown, depth: number): void => {
    if (depth > 12 || value === null || typeof value !== 'object') return;
    if (seen.has(value as object) || visitedCount >= MAX_VISITS) return;
    seen.add(value as object);
    visitedCount += 1;

    const candidate = normalizeProfileCandidate(value, fallbackUsername, source);
    if (candidate) candidates.push(candidate);

    if (Array.isArray(value)) {
      for (const child of value) visit(child, depth + 1);
      return;
    }
    for (const child of Object.values(value as Record<string, unknown>)) visit(child, depth + 1);
  };

  visit(payload, 0);
  return candidates.sort((a, b) => {
    const score = (profile: ProfileRecord) =>
      Number(profile.followers !== undefined) * 4
      + Number(profile.videoCount !== undefined) * 3
      + Number(Boolean(profile.avatarUrl)) * 2
      + Number(Boolean(profile.bio))
      + Number(Boolean(profile.displayName));
    return score(b) - score(a);
  })[0];
}

export function extractProfileFromDom(username: string): ProfileRecord {
  const text = (...selectors: string[]) => {
    for (const selector of selectors) {
      const el = document.querySelector<HTMLElement>(selector);
      if (el?.textContent?.trim()) return el.textContent.trim();
    }
    return undefined;
  };
  const avatar = document.querySelector<HTMLImageElement>(
    '[data-e2e="user-avatar"] img[src], header [class*="avatar"] img[src], header img[data-e2e="user-avatar"]'
  );
  const websiteAnchor = document.querySelector<HTMLAnchorElement>(
    '[data-e2e="user-bio"] a[href], [data-e2e="user-link"] a[href], a[data-e2e="user-link"]'
  );

  return {
    username,
    profileUrl: `https://www.tiktok.com/@${username}`,
    displayName: text('[data-e2e="user-title"]', 'header h1', '[class*="share-title"]'),
    bio: text('[data-e2e="user-bio"]', 'header [class*="user-bio"]', 'header [class*="signature"]'),
    avatarUrl: sanitizeHttpUrl(avatar?.currentSrc || avatar?.src || undefined),
    followers: firstNumber(text('[data-e2e="followers-count"]', 'header [class*="follower-count"]')),
    following: firstNumber(text('[data-e2e="following-count"]', 'header [class*="following-count"]')),
    totalLikes: firstNumber(text('[data-e2e="likes-count"]', 'header [class*="like-count"]', 'header [class*="heart-count"]')),
    verified: Boolean(document.querySelector('[data-e2e="user-title"] svg, [data-e2e="verified-badge"], header [class*="verified"]')),
    website: sanitizeHttpUrl(websiteAnchor?.href),
    collectedAt: Date.now(),
    source: 'dom',
  };
}

export function parseTikTokVideoUrl(value: string, baseUrl = 'https://www.tiktok.com'): { author: string; id: string; videoUrl: string } | undefined {
  try {
    const url = new URL(value, baseUrl);
    const match = url.pathname.match(/^\/@([^/]+)\/video\/(\d+)/i);
    if (!match?.[1] || !match[2]) return undefined;
    const author = decodeURIComponent(match[1]).replace(/^@/, '');
    if (!author) return undefined;
    return {
      author,
      id: match[2],
      videoUrl: `${url.origin}/@${author}/video/${match[2]}`,
    };
  } catch {
    return undefined;
  }
}

function extractVideoFromLink(link: HTMLAnchorElement): VideoRecord | undefined {
  const parsed = parseTikTokVideoUrl(link.href, location.origin);
  if (!parsed) return undefined;

  const card = link.closest<HTMLElement>(
    '[data-e2e="user-post-item"], [data-e2e="challenge-item"], [data-e2e="search-card-video-container"], article, li, div'
  );
  const viewsNode = card?.querySelector<HTMLElement>(
    '[data-e2e="video-views"], [data-e2e="search-card-video-views"], [class*="video-count"], strong'
  );
  const image = link.querySelector<HTMLImageElement>('img') ?? card?.querySelector<HTMLImageElement>('img');
  const description = image?.alt ?? link.getAttribute('aria-label') ?? '';
  const cardText = card?.textContent?.toLowerCase() ?? '';

  return {
    id: parsed.id,
    author: parsed.author,
    profileUrl: `https://www.tiktok.com/@${parsed.author}`,
    videoUrl: parsed.videoUrl,
    description,
    views: parseCompactNumber(viewsNode?.textContent),
    likes: 0,
    comments: 0,
    shares: 0,
    coverUrl: sanitizeHttpUrl(image?.currentSrc || image?.src || undefined),
    hashtags: Array.from(description.matchAll(/#([\p{L}\p{N}_]+)/gu), (entry) => entry[1] ?? '').filter(Boolean),
    isPinned: ['pinned', 'закреплено', 'fixé', 'angeheftet'].some((label) => cardText.includes(label)),
    collectedAt: Date.now(),
    source: 'dom',
  };
}

export function extractVideosFromDiscoveryDom(): VideoRecord[] {
  const found = new Map<string, VideoRecord>();
  const links = document.querySelectorAll<HTMLAnchorElement>('a[href*="/video/"]');

  for (const link of links) {
    const video = extractVideoFromLink(link);
    if (!video) continue;
    found.set(`${video.author.toLowerCase()}:${video.id}`, video);
  }

  return [...found.values()];
}

export function extractVideosFromDom(username: string): VideoRecord[] {
  const normalized = username.toLowerCase();
  return extractVideosFromDiscoveryDom().filter((video) => video.author.toLowerCase() === normalized);
}

export function mergeVideoRecords(current: VideoRecord, incoming: VideoRecord): VideoRecord {
  const priority: Record<VideoRecord['source'], number> = { dom: 1, 'embedded-json': 2, api: 3 };
  const preferIncoming = priority[incoming.source] >= priority[current.source];
  const choose = <T,>(next: T | undefined, previous: T | undefined): T | undefined =>
    preferIncoming ? next ?? previous : previous ?? next;

  return {
    ...current,
    id: current.id,
    author: choose(incoming.author, current.author) ?? current.author,
    profileUrl: choose(incoming.profileUrl, current.profileUrl) ?? current.profileUrl,
    videoUrl: choose(incoming.videoUrl, current.videoUrl) ?? current.videoUrl,
    description: choose(incoming.description || undefined, current.description || undefined) ?? '',
    publishedAt: choose(incoming.publishedAt, current.publishedAt),
    durationSeconds: choose(incoming.durationSeconds, current.durationSeconds),
    views: Math.max(current.views, incoming.views),
    likes: Math.max(current.likes, incoming.likes),
    comments: Math.max(current.comments, incoming.comments),
    shares: Math.max(current.shares, incoming.shares),
    saves: Math.max(current.saves ?? 0, incoming.saves ?? 0) || undefined,
    coverUrl: choose(incoming.coverUrl, current.coverUrl),
    hashtags: Array.from(new Set([...current.hashtags, ...incoming.hashtags])),
    audioTitle: choose(incoming.audioTitle, current.audioTitle),
    isPinned: current.isPinned || incoming.isPinned,
    collectedAt: Math.max(current.collectedAt, incoming.collectedAt),
    source: preferIncoming ? incoming.source : current.source,
  };
}
