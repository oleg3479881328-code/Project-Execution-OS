import { describe, expect, it } from 'vitest';
import { favoriteKey, orderedFavoriteEntries, selectFavoriteEntries } from '../lib/favorites';
import { generateFavoritesHtml } from '../lib/html-export';
import type { FavoriteEntry, VideoRecord } from '../lib/types';

function video(id: string, author: string, views: number, overrides: Partial<VideoRecord> = {}): VideoRecord {
  return {
    id,
    author,
    profileUrl: `https://www.tiktok.com/@${author}`,
    videoUrl: `https://www.tiktok.com/@${author}/video/${id}`,
    description: `Video ${id}`,
    publishedAt: 1_700_000_000,
    durationSeconds: 20,
    views,
    likes: 100,
    comments: 10,
    shares: 5,
    saves: 3,
    coverUrl: `https://example.com/${id}.jpg`,
    hashtags: ['wedding', 'photography'],
    audioTitle: 'Test audio',
    isPinned: false,
    collectedAt: 1_700_000_000_000,
    source: 'api',
    ...overrides,
  };
}

function favorite(entryVideo: VideoRecord, favoritedAt: number): FavoriteEntry {
  return {
    key: favoriteKey(entryVideo),
    video: entryVideo,
    favoritedAt,
  };
}

describe('favorites', () => {
  it('creates a stable case-insensitive key from author and video id', () => {
    expect(favoriteKey({ author: '@OlgaPhoto', id: '123' })).toBe('olgaphoto:123');
    expect(favoriteKey({ author: 'olgaphoto', id: '123' })).toBe('olgaphoto:123');
  });

  it('orders newest favorites first and exports only checked entries', () => {
    const first = favorite(video('1', 'alice', 100), 1000);
    const second = favorite(video('2', 'bob', 200), 2000);
    const favorites = { [first.key]: first, [second.key]: second };

    expect(orderedFavoriteEntries(favorites).map((entry) => entry.key)).toEqual([second.key, first.key]);
    expect(selectFavoriteEntries(favorites, [first.key]).map((entry) => entry.key)).toEqual([first.key]);
  });

  it('generates a standalone HTML page with links, preview, description, and metrics', () => {
    const entry = favorite(video('777', 'creator', 123_456), 2000);
    const html = generateFavoritesHtml([entry], { title: 'Client shortlist', generatedAt: 1_700_000_000_000 });

    expect(html).toContain('<!doctype html>');
    expect(html).toContain('<meta charset="utf-8">');
    expect(html).toContain('Client shortlist');
    expect(html).toContain('https://www.tiktok.com/@creator/video/777');
    expect(html).toContain('https://example.com/777.jpg');
    expect(html).toContain('Video 777');
    expect(html).toContain('data-video-key="creator:777"');
    expect(html).toContain('TikTok Research Sorter v0.4.0');
  });

  it('escapes user-controlled text and rejects non-http links and previews', () => {
    const unsafe = favorite(video('9', 'bad', 1, {
      description: '<script>alert("x")</script>',
      profileUrl: 'javascript:alert(1)',
      videoUrl: 'javascript:alert(2)',
      coverUrl: 'data:text/html,<script>alert(3)</script>',
      hashtags: ['<img src=x onerror=alert(4)>'],
    }), 3000);

    const html = generateFavoritesHtml([unsafe], { generatedAt: 1_700_000_000_000 });

    expect(html).not.toContain('<script>alert');
    expect(html).not.toContain('javascript:');
    expect(html).not.toContain('data:text/html');
    expect(html).toContain('&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;');
    expect(html).toContain('Превью недоступно');
  });

  it('keeps unselected favorites out of the generated selection', () => {
    const selected = favorite(video('11', 'one', 10), 2000);
    const omitted = favorite(video('22', 'two', 20), 1000);
    const favorites = { [selected.key]: selected, [omitted.key]: omitted };
    const chosen = selectFavoriteEntries(favorites, [selected.key]);
    const html = generateFavoritesHtml(chosen, { generatedAt: 1_700_000_000_000 });

    expect(html).toContain('/video/11');
    expect(html).not.toContain('/video/22');
  });
});
