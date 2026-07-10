import { describe, expect, it } from 'vitest';
import { enrichVideos, publicationFrequencyPerWeek, strongestHashtags } from '../lib/analytics';
import type { VideoRecord } from '../lib/types';

const record = (id: string, views: number, publishedAt: number, hashtags: string[]): VideoRecord => ({
  id,
  author: 'creator',
  profileUrl: 'https://www.tiktok.com/@creator',
  videoUrl: `https://www.tiktok.com/@creator/video/${id}`,
  description: '',
  publishedAt,
  views,
  likes: 0,
  comments: 0,
  shares: 0,
  hashtags,
  isPinned: false,
  collectedAt: 0,
  source: 'api',
});

describe('profile analytics', () => {
  it('estimates posts per week from known publication dates', () => {
    const videos = [
      record('1', 100, 1_700_000_000, []),
      record('2', 100, 1_700_604_800, []),
      record('3', 100, 1_701_209_600, []),
    ];
    expect(publicationFrequencyPerWeek(videos)).toBeCloseTo(1.5);
  });

  it('ranks hashtags by profile-relative performance', () => {
    const enriched = enrichVideos([
      record('1', 100, 1_700_000_000, ['wedding']),
      record('2', 100, 1_700_604_800, ['portrait']),
      record('3', 1000, 1_701_209_600, ['wedding']),
    ], 1_702_000_000);
    expect(strongestHashtags(enriched, 1)).toEqual(['wedding']);
  });
});
