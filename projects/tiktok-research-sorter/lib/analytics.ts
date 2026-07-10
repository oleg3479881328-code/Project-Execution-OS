import type { EnrichedVideo, VideoRecord } from './types';

export function median(values: number[]): number {
  if (!values.length) return 0;
  const sorted = [...values].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  if (sorted.length % 2) return sorted[middle] ?? 0;
  return ((sorted[middle - 1] ?? 0) + (sorted[middle] ?? 0)) / 2;
}

export function enrichVideos(videos: VideoRecord[], nowSeconds = Math.floor(Date.now() / 1000)): EnrichedVideo[] {
  const baseline = median(videos.map((video) => video.views).filter((views) => views > 0));

  return videos.map((video) => {
    const ageDays = video.publishedAt
      ? Math.max(1, (nowSeconds - video.publishedAt) / 86_400)
      : undefined;
    const interactions = video.likes + video.comments + video.shares;

    return {
      ...video,
      ageDays,
      viewsPerDay: ageDays ? video.views / ageDays : undefined,
      engagementRate: video.views ? (interactions / video.views) * 100 : undefined,
      likeRate: video.views ? (video.likes / video.views) * 100 : undefined,
      commentRate: video.views ? (video.comments / video.views) * 100 : undefined,
      shareRate: video.views ? (video.shares / video.views) * 100 : undefined,
      outlierScore: baseline ? video.views / baseline : undefined,
    };
  });
}

export function summarize(videos: EnrichedVideo[]) {
  const engagementRates = videos.map((video) => video.engagementRate ?? 0).filter((value) => value > 0);
  const outliers = videos.map((video) => video.outlierScore ?? 0);
  return {
    count: videos.length,
    medianViews: median(videos.map((video) => video.views).filter((value) => value > 0)),
    averageEngagementRate: engagementRates.length
      ? engagementRates.reduce((sum, value) => sum + value, 0) / engagementRates.length
      : 0,
    maxOutlierScore: Math.max(0, ...outliers),
  };
}

export function publicationFrequencyPerWeek(videos: VideoRecord[]): number | undefined {
  const dates = videos
    .map((video) => video.publishedAt)
    .filter((value): value is number => typeof value === 'number' && value > 0)
    .sort((a, b) => a - b);
  if (dates.length < 2) return undefined;
  const spanWeeks = Math.max(1, ((dates.at(-1) ?? 0) - (dates[0] ?? 0)) / 604_800);
  return dates.length / spanWeeks;
}

export function strongestHashtags(videos: EnrichedVideo[], limit = 6): string[] {
  const stats = new Map<string, { uses: number; score: number }>();
  for (const video of videos) {
    const weight = Math.max(0.1, video.outlierScore ?? 0.1);
    for (const rawTag of video.hashtags) {
      const tag = rawTag.trim().toLowerCase();
      if (!tag) continue;
      const current = stats.get(tag) ?? { uses: 0, score: 0 };
      current.uses += 1;
      current.score += weight;
      stats.set(tag, current);
    }
  }

  return [...stats.entries()]
    .sort((a, b) => {
      const aAverage = a[1].score / a[1].uses;
      const bAverage = b[1].score / b[1].uses;
      return bAverage - aAverage || b[1].uses - a[1].uses || a[0].localeCompare(b[0]);
    })
    .slice(0, limit)
    .map(([tag]) => tag);
}
