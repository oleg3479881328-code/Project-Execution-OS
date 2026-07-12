import { describe, expect, it } from 'vitest';
import { videosToCsv } from '../lib/csv';
import type { EnrichedVideo } from '../lib/types';

const video = (description: string): EnrichedVideo => ({
  id: '123',
  author: 'creator',
  profileUrl: 'https://www.tiktok.com/@creator',
  videoUrl: 'https://www.tiktok.com/@creator/video/123',
  description,
  views: 100,
  likes: 1,
  comments: 0,
  shares: 0,
  hashtags: [],
  isPinned: false,
  collectedAt: 1_700_000_000_000,
  source: 'api',
});

describe('videosToCsv', () => {
  it('escapes commas and quotes', () => {
    const csv = videosToCsv([video('A "quoted", description')]);
    expect(csv).toContain('"A ""quoted"", description"');
  });

  it('neutralizes spreadsheet formulas', () => {
    const csv = videosToCsv([video('=HYPERLINK("https://example.com")')]);
    expect(csv).toContain("'=HYPERLINK");
  });
});
