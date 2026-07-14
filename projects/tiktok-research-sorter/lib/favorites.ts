import { enrichVideos, strongestHashtags, summarize } from './analytics';
import type { ChannelSnapshot, FavoriteEntry, ProfileSnapshot, VideoRecord } from './types';

export interface FavoriteChannelGroup {
  key: string;
  channel: ChannelSnapshot;
  entries: FavoriteEntry[];
  latestFavoritedAt: number;
}

export function profileKey(username: string): string {
  return username.trim().replace(/^@/, '').toLowerCase();
}

export function favoriteKey(video: Pick<VideoRecord, 'author' | 'id'>): string {
  return `${profileKey(video.author)}:${video.id.trim()}`;
}

export function minimalChannelSnapshot(video: Pick<VideoRecord, 'author' | 'profileUrl'>): ChannelSnapshot {
  const username = video.author.trim().replace(/^@/, '');
  const now = Date.now();
  return {
    username,
    profileUrl: video.profileUrl || `https://www.tiktok.com/@${username}`,
    medianViews: 0,
    lastScannedAt: now,
    collectedVideoCount: 0,
    strongestHashtags: [],
    capturedAt: now,
    completeness: 'partial',
  };
}

export function channelSnapshotFromProfile(profile: ProfileSnapshot): ChannelSnapshot {
  const enriched = enrichVideos(profile.videos);
  const summary = summarize(enriched);
  const meaningfulFields = [
    profile.displayName,
    profile.bio,
    profile.avatarUrl,
    profile.followers,
    profile.following,
    profile.totalLikes,
    profile.videoCount,
    profile.userId,
    profile.secUid,
  ].filter((value) => value !== undefined && value !== '').length;

  return {
    username: profile.username,
    profileUrl: profile.profileUrl,
    userId: profile.userId,
    secUid: profile.secUid,
    displayName: profile.displayName,
    bio: profile.bio,
    avatarUrl: profile.avatarUrl,
    followers: profile.followers,
    following: profile.following,
    friends: profile.friends,
    totalLikes: profile.totalLikes,
    videoCount: profile.videoCount,
    verified: profile.verified,
    privateAccount: profile.privateAccount,
    commerceAccount: profile.commerceAccount,
    website: profile.website,
    region: profile.region,
    language: profile.language,
    accountCreatedAt: profile.accountCreatedAt,
    medianViews: profile.medianViews,
    lastScannedAt: profile.lastScannedAt,
    profileDataUpdatedAt: profile.profileDataUpdatedAt,
    profileDataSource: profile.profileDataSource,
    collectedVideoCount: profile.videos.length,
    averageEngagementRate: enriched.length ? summary.averageEngagementRate : undefined,
    strongestHashtags: strongestHashtags(enriched, 12),
    capturedAt: Date.now(),
    completeness: meaningfulFields >= 3 ? 'full' : 'partial',
  };
}

function channelScore(channel: ChannelSnapshot): number {
  return [
    channel.displayName,
    channel.bio,
    channel.avatarUrl,
    channel.followers,
    channel.following,
    channel.friends,
    channel.totalLikes,
    channel.videoCount,
    channel.userId,
    channel.secUid,
    channel.website,
    channel.region,
    channel.language,
    channel.accountCreatedAt,
  ].filter((value) => value !== undefined && value !== '').length
    + channel.collectedVideoCount
    + (channel.completeness === 'full' ? 20 : 0);
}

export function mergeChannelSnapshots(current: ChannelSnapshot, incoming: ChannelSnapshot): ChannelSnapshot {
  const incomingIsRicher = channelScore(incoming) >= channelScore(current);
  const primary = incomingIsRicher ? incoming : current;
  const secondary = incomingIsRicher ? current : incoming;

  return {
    ...secondary,
    ...primary,
    username: primary.username || secondary.username,
    profileUrl: primary.profileUrl || secondary.profileUrl,
    medianViews: Math.max(current.medianViews, incoming.medianViews),
    lastScannedAt: Math.max(current.lastScannedAt, incoming.lastScannedAt),
    profileDataUpdatedAt: Math.max(current.profileDataUpdatedAt ?? 0, incoming.profileDataUpdatedAt ?? 0) || undefined,
    collectedVideoCount: Math.max(current.collectedVideoCount, incoming.collectedVideoCount),
    averageEngagementRate: primary.averageEngagementRate ?? secondary.averageEngagementRate,
    strongestHashtags: Array.from(new Set([...current.strongestHashtags, ...incoming.strongestHashtags])).slice(0, 12),
    capturedAt: Math.max(current.capturedAt, incoming.capturedAt),
    completeness: current.completeness === 'full' || incoming.completeness === 'full' ? 'full' : 'partial',
  };
}

export function normalizeFavoriteEntry(entry: Partial<FavoriteEntry> & { video: VideoRecord }): FavoriteEntry {
  const key = entry.key || favoriteKey(entry.video);
  return {
    key,
    video: entry.video,
    channel: entry.channel ?? minimalChannelSnapshot(entry.video),
    favoritedAt: entry.favoritedAt ?? Date.now(),
  };
}

export function orderedFavoriteEntries(favorites: Record<string, FavoriteEntry>): FavoriteEntry[] {
  return Object.values(favorites)
    .map((entry) => normalizeFavoriteEntry(entry))
    .sort((a, b) =>
      b.favoritedAt - a.favoritedAt
      || b.video.views - a.video.views
      || a.key.localeCompare(b.key)
    );
}

export function selectFavoriteEntries(
  favorites: Record<string, FavoriteEntry>,
  selectedKeys: Iterable<string>,
): FavoriteEntry[] {
  const selected = new Set(selectedKeys);
  return orderedFavoriteEntries(favorites).filter((entry) => selected.has(entry.key));
}

export function groupFavoriteEntriesByChannel(entries: FavoriteEntry[]): FavoriteChannelGroup[] {
  const groups = new Map<string, FavoriteChannelGroup>();

  for (const rawEntry of entries) {
    const entry = normalizeFavoriteEntry(rawEntry);
    const key = profileKey(entry.channel.username || entry.video.author);
    const existing = groups.get(key);
    if (!existing) {
      groups.set(key, {
        key,
        channel: entry.channel,
        entries: [entry],
        latestFavoritedAt: entry.favoritedAt,
      });
      continue;
    }

    existing.channel = mergeChannelSnapshots(existing.channel, entry.channel);
    existing.entries.push(entry);
    existing.latestFavoritedAt = Math.max(existing.latestFavoritedAt, entry.favoritedAt);
  }

  return [...groups.values()]
    .map((group) => ({
      ...group,
      entries: group.entries.sort((a, b) => b.favoritedAt - a.favoritedAt || b.video.views - a.video.views),
    }))
    .sort((a, b) => b.latestFavoritedAt - a.latestFavoritedAt || a.key.localeCompare(b.key));
}
