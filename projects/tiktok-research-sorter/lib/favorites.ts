import type { FavoriteEntry, VideoRecord } from './types';

export function favoriteKey(video: Pick<VideoRecord, 'author' | 'id'>): string {
  const author = video.author.trim().replace(/^@/, '').toLowerCase();
  return `${author}:${video.id.trim()}`;
}

export function orderedFavoriteEntries(favorites: Record<string, FavoriteEntry>): FavoriteEntry[] {
  return Object.values(favorites).sort((a, b) =>
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
