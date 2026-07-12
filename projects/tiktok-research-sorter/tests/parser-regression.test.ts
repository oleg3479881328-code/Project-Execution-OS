import { describe, expect, it } from 'vitest';
import { extractVideosFromPayload, normalizeTikTokItem } from '../lib/tiktok-parser';
import basicVideoList from './fixtures/basic-video-list.json';
import emptyItemList from './fixtures/empty-item-list.json';
import nullPayload from './fixtures/null-payload.json';
import missingFields from './fixtures/missing-fields.json';
import cyclicPayload from './fixtures/cyclic-payload.json';
import pinnedVideo from './fixtures/pinned-video.json';
import alternateFieldNames from './fixtures/alternate-field-names.json';

describe('extractVideosFromPayload — regression', () => {
  it('extracts videos from a basic itemList payload', () => {
    const result = extractVideosFromPayload(basicVideoList, 'olga');
    expect(result).toHaveLength(2);
    expect(result[0]).toMatchObject({
      id: '123456',
      author: 'olga',
      views: 10000,
      likes: 700,
      comments: 20,
      shares: 10,
      durationSeconds: 15,
      hashtags: ['bride', 'wedding'],
    });
    expect(result[1]).toMatchObject({
      id: '123457',
      author: 'olga',
      views: 5000,
      likes: 300,
      durationSeconds: 30,
      hashtags: ['portrait'],
    });
  });

  it('returns empty array for empty itemList', () => {
    expect(extractVideosFromPayload(emptyItemList)).toEqual([]);
  });

  it('returns empty array for null payload', () => {
    expect(extractVideosFromPayload(nullPayload)).toEqual([]);
  });

  it('handles missing fields gracefully', () => {
    const result = extractVideosFromPayload(missingFields, 'testuser');
    expect(result).toHaveLength(3);

    const noStats = result.find((video) => video.id === '999001');
    expect(noStats).toBeDefined();
    expect(noStats?.views).toBe(0);
    expect(noStats?.durationSeconds).toBe(10);

    const noAuthor = result.find((video) => video.id === '999002');
    expect(noAuthor).toBeDefined();
    expect(noAuthor?.author).toBe('testuser');
    expect(noAuthor?.views).toBe(1000);

    const noVideo = result.find((video) => video.id === '999003');
    expect(noVideo).toBeDefined();
    expect(noVideo?.views).toBe(2000);
    expect(noVideo?.durationSeconds).toBeUndefined();
  });

  it('handles cyclic payload without infinite loop', () => {
    const cyclic = JSON.parse(JSON.stringify(cyclicPayload)) as Record<string, unknown>;
    cyclic.selfRef = cyclic;

    const result = extractVideosFromPayload(cyclic, 'testuser');
    expect(result).toHaveLength(1);
    expect(result[0]?.id).toBe('cyclic001');
  });

  it('detects pinned videos', () => {
    const result = extractVideosFromPayload(pinnedVideo, 'testuser');
    expect(result).toHaveLength(2);

    const pinned = result.find((video) => video.id === 'pinned001');
    expect(pinned).toBeDefined();
    expect(pinned?.isPinned).toBe(true);

    const normal = result.find((video) => video.id === 'normal001');
    expect(normal).toBeDefined();
    expect(normal?.isPinned).toBe(false);
  });

  it('handles alternate field names', () => {
    const result = extractVideosFromPayload(alternateFieldNames, 'altuser');
    expect(result).toHaveLength(1);
    expect(result[0]).toMatchObject({
      id: 'alt001',
      author: 'altuser',
      views: 7777,
      likes: 444,
      comments: 22,
      shares: 11,
      durationSeconds: 25,
      hashtags: ['alt'],
    });
  });
});

describe('normalizeTikTokItem — edge cases', () => {
  it('returns undefined for invalid input', () => {
    expect(normalizeTikTokItem(null)).toBeUndefined();
    expect(normalizeTikTokItem('string')).toBeUndefined();
    expect(normalizeTikTokItem(42)).toBeUndefined();
    expect(normalizeTikTokItem([])).toBeUndefined();
  });

  it('returns undefined when id is missing', () => {
    expect(normalizeTikTokItem({ desc: 'no id', author: { uniqueId: 'user' } })).toBeUndefined();
  });

  it('returns undefined when author is missing', () => {
    expect(normalizeTikTokItem({ id: '123', desc: 'no author' })).toBeUndefined();
  });

  it('strips @ prefix from author', () => {
    const result = normalizeTikTokItem({ id: '123', author: { uniqueId: '@testuser' } });
    expect(result?.author).toBe('testuser');
  });

  it('normalizes timestamp from milliseconds to seconds', () => {
    const result = normalizeTikTokItem({
      id: '123',
      createTime: 1_700_000_000_000,
      author: { uniqueId: 'user' },
    });
    expect(result?.publishedAt).toBe(1_700_000_000);
  });

  it('distinguishes seconds from milliseconds for duration', () => {
    const longVideo = normalizeTikTokItem({
      id: 'long',
      author: { uniqueId: 'user' },
      video: { duration: 1200 },
    });
    const millisecondVideo = normalizeTikTokItem({
      id: 'short',
      author: { uniqueId: 'user' },
      video: { duration: 15_000 },
    });
    expect(longVideo?.durationSeconds).toBe(1200);
    expect(millisecondVideo?.durationSeconds).toBe(15);
  });

  it('handles saves and audio title', () => {
    const result = normalizeTikTokItem({
      id: '123',
      author: { uniqueId: 'user' },
      stats: { collectCount: 500 },
      music: { title: 'Original Sound' },
    });
    expect(result?.saves).toBe(500);
    expect(result?.audioTitle).toBe('Original Sound');
  });
});
