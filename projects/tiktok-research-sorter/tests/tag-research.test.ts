import { describe, expect, it } from 'vitest';
import { groupTopVideosPerAccount, mergeDiscoveredVideos, selectTopVideosPerAccount } from '../lib/tag-research';
import { extractVideosFromPayload, parseTikTokVideoUrl } from '../lib/tiktok-parser';
import type { VideoRecord } from '../lib/types';
import tagFixture from './fixtures/tag-weddingphotography.json';

const fixtureVideos = () => extractVideosFromPayload(tagFixture, '', 'api');

describe('TikTok hashtag research', () => {
  it('extracts multiple authors from a hashtag payload', () => {
    const videos = fixtureVideos();
    expect(videos).toHaveLength(5);
    expect(new Set(videos.map((video) => video.author))).toEqual(new Set(['alicephoto', 'bobweddings', 'carolstudio']));
  });

  it('keeps the single highest-viewed video from every account', () => {
    const selected = selectTopVideosPerAccount(fixtureVideos(), 1, 0);
    expect(selected.map((video) => video.id)).toEqual(['tag003', 'tag001', 'tag005']);
  });

  it('supports two or three top videos per account', () => {
    const groups = groupTopVideosPerAccount(fixtureVideos(), 2, 0);
    expect(groups.find((group) => group.author === 'alicephoto')?.videos.map((video) => video.id)).toEqual(['tag001', 'tag002']);
    expect(groups.find((group) => group.author === 'bobweddings')?.videos.map((video) => video.id)).toEqual(['tag003', 'tag004']);
  });

  it('applies the minimum view threshold before grouping', () => {
    const groups = groupTopVideosPerAccount(fixtureVideos(), 3, 50_000);
    expect(groups.map((group) => group.author)).toEqual(['bobweddings', 'alicephoto']);
    expect(groups.flatMap((group) => group.videos).map((video) => video.id)).toEqual(['tag003', 'tag004', 'tag001']);
  });

  it('deduplicates the same account and video while preserving higher metrics', () => {
    const videos = fixtureVideos();
    const original = videos[0];
    expect(original).toBeDefined();
    const duplicate: VideoRecord = { ...original!, views: 999_999, source: 'api' };
    const merged = mergeDiscoveredVideos([...videos, duplicate]);
    expect(merged).toHaveLength(5);
    expect(merged.find((video) => video.id === original!.id)?.views).toBe(999_999);
  });

  it('parses author and video id from TikTok discovery links', () => {
    expect(parseTikTokVideoUrl('https://www.tiktok.com/@alicephoto/video/123456789')).toEqual({
      author: 'alicephoto',
      id: '123456789',
      videoUrl: 'https://www.tiktok.com/@alicephoto/video/123456789',
    });
    expect(parseTikTokVideoUrl('https://www.tiktok.com/tag/weddingphotography')).toBeUndefined();
  });
});
