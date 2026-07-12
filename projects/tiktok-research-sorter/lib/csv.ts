import type { EnrichedVideo } from './types';

function protectSpreadsheetFormula(text: string): string {
  return /^[\t\r\n ]*[=+\-@]/u.test(text) ? `'${text}` : text;
}

function escapeCsv(value: unknown): string {
  const raw = value === null || value === undefined ? '' : String(value);
  const text = protectSpreadsheetFormula(raw);
  return /[",\n]/u.test(text) ? `"${text.replace(/"/gu, '""')}"` : text;
}

export function videosToCsv(videos: EnrichedVideo[]): string {
  const headers = [
    'profile_username', 'profile_url', 'video_id', 'video_url', 'description', 'published_at',
    'duration_seconds', 'views', 'likes', 'comments', 'shares', 'saves', 'engagement_rate',
    'views_per_day', 'outlier_score', 'hashtags', 'audio_title', 'is_pinned', 'collected_at', 'source',
  ];

  const rows = videos.map((video) => [
    video.author,
    video.profileUrl,
    video.id,
    video.videoUrl,
    video.description,
    video.publishedAt ? new Date(video.publishedAt * 1000).toISOString() : '',
    video.durationSeconds ?? '',
    video.views,
    video.likes,
    video.comments,
    video.shares,
    video.saves ?? '',
    video.engagementRate?.toFixed(4) ?? '',
    video.viewsPerDay?.toFixed(2) ?? '',
    video.outlierScore?.toFixed(4) ?? '',
    video.hashtags.join(' '),
    video.audioTitle ?? '',
    video.isPinned,
    new Date(video.collectedAt).toISOString(),
    video.source,
  ]);

  return [headers, ...rows].map((row) => row.map(escapeCsv).join(',')).join('\n');
}
