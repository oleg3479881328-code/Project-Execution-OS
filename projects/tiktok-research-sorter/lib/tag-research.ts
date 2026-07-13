import { mergeVideoRecords } from './tiktok-parser';
import type { VideoRecord } from './types';

export interface AccountVideoGroup {
  author: string;
  profileUrl: string;
  videos: VideoRecord[];
  topViews: number;
}

function normalizeLimit(value: number): number {
  if (!Number.isFinite(value)) return 1;
  return Math.min(20, Math.max(1, Math.floor(value)));
}

function normalizeMinViews(value: number): number {
  if (!Number.isFinite(value)) return 0;
  return Math.max(0, Math.floor(value));
}

export function mergeDiscoveredVideos(videos: VideoRecord[]): VideoRecord[] {
  const merged = new Map<string, VideoRecord>();

  for (const video of videos) {
    const author = video.author.trim().replace(/^@/, '').toLowerCase();
    if (!author || !video.id) continue;
    const key = `${author}:${video.id}`;
    const existing = merged.get(key);
    merged.set(key, existing ? mergeVideoRecords(existing, video) : { ...video, author });
  }

  return [...merged.values()];
}

export function groupTopVideosPerAccount(
  videos: VideoRecord[],
  topVideosPerAccount: number,
  minViews: number,
): AccountVideoGroup[] {
  const limit = normalizeLimit(topVideosPerAccount);
  const threshold = normalizeMinViews(minViews);
  const byAuthor = new Map<string, VideoRecord[]>();

  for (const video of mergeDiscoveredVideos(videos)) {
    if (video.views < threshold) continue;
    const list = byAuthor.get(video.author) ?? [];
    list.push(video);
    byAuthor.set(video.author, list);
  }

  return [...byAuthor.entries()]
    .map(([author, accountVideos]) => {
      const selected = [...accountVideos]
        .sort((a, b) => b.views - a.views || (b.publishedAt ?? 0) - (a.publishedAt ?? 0) || a.id.localeCompare(b.id))
        .slice(0, limit);
      return {
        author,
        profileUrl: selected[0]?.profileUrl ?? `https://www.tiktok.com/@${author}`,
        videos: selected,
        topViews: selected[0]?.views ?? 0,
      };
    })
    .filter((group) => group.videos.length > 0)
    .sort((a, b) => b.topViews - a.topViews || a.author.localeCompare(b.author));
}

export function selectTopVideosPerAccount(
  videos: VideoRecord[],
  topVideosPerAccount: number,
  minViews: number,
): VideoRecord[] {
  return groupTopVideosPerAccount(videos, topVideosPerAccount, minViews).flatMap((group) => group.videos);
}
