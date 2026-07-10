import { describe, expect, it } from 'vitest';
import { enrichVideos, median } from '../lib/analytics';
import type { VideoRecord } from '../lib/types';

const video = (id: string, views: number): VideoRecord => ({
  id,
  author: 'creator',
  profileUrl: 'https://www.tiktok.com/@creator',
  videoUrl: `https://www.tiktok.com/@creator/video/${id}`,
  description: '',
  views,
  likes: 10,
  comments: 2,
  shares: 1,
  hashtags: [],
  isPinned: false,
  collectedAt: 0,
  source: 'api',
});

describe('analytics', () => {
  it('calculates median', () => {
    expect(median([1, 3, 2])).toBe(2);
    expect(median([1, 4, 2, 3])).toBe(2.5);
  });

  it('calculates outlier score per supplied profile', () => {
    const result = enrichVideos([video('1', 100), video('2', 200), video('3', 1000)]);
    expect(result[2]?.outlierScore).toBe(5);
  });
});
