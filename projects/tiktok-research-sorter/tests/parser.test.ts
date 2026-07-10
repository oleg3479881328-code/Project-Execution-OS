import { describe, expect, it } from 'vitest';
import { extractVideosFromPayload } from '../lib/tiktok-parser';

describe('TikTok payload parser', () => {
  it('finds nested item structures and normalizes metrics', () => {
    const payload = {
      itemList: [{
        id: '123456',
        desc: 'Wedding idea #bride',
        createTime: 1_700_000_000,
        author: { uniqueId: 'olga' },
        video: { duration: 15_000, cover: 'https://example.com/cover.jpg' },
        stats: { playCount: 10_000, diggCount: 700, commentCount: 20, shareCount: 10 },
      }],
    };

    const result = extractVideosFromPayload(payload);
    expect(result).toHaveLength(1);
    expect(result[0]).toMatchObject({
      id: '123456',
      author: 'olga',
      views: 10_000,
      likes: 700,
      durationSeconds: 15,
      hashtags: ['bride'],
    });
  });
});
