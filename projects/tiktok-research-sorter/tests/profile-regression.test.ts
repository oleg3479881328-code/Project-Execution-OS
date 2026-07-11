import { describe, expect, it } from 'vitest';
import { extractProfileFromPayload, mergeVideoRecords } from '../lib/tiktok-parser';
import type { VideoRecord } from '../lib/types';
import profileUserInfo from './fixtures/profile-user-info.json';

describe('extractProfileFromPayload — regression', () => {
  it('extracts profile from standard userInfo payload', () => {
    const result = extractProfileFromPayload(profileUserInfo, 'jasminebrookephotography');
    expect(result).toMatchObject({
      username: 'jasminebrookephotography',
      displayName: 'Jasmine Brooke Photography',
      bio: 'San Diego wedding photographer',
      followers: 1011,
      following: 249,
      totalLikes: 333600,
      videoCount: 87,
      verified: true,
    });
    expect(result?.profileUrl).toBe('https://www.tiktok.com/@jasminebrookephotography');
  });

  it('returns undefined for null payload', () => {
    expect(extractProfileFromPayload(null, 'testuser')).toBeUndefined();
  });

  it('returns undefined for empty object', () => {
    expect(extractProfileFromPayload({}, 'testuser')).toBeUndefined();
  });

  it('returns undefined when username does not match fallback', () => {
    const result = extractProfileFromPayload(profileUserInfo, 'wronguser');
    expect(result).toBeUndefined();
  });

  it('handles alternate field names (user_info, statistics)', () => {
    const payload = {
      user_info: {
        author: {
          unique_id: 'altprofile',
          nickname: 'Alt Profile',
          signature: 'Alternate fields',
          avatarLarger: 'https://example.com/alt-avatar.jpg',
          verified: false,
        },
        statistics: {
          follower_count: 500,
          following_count: 100,
          heart_count: 10000,
          video_count: 20,
        },
      },
    };
    const result = extractProfileFromPayload(payload, 'altprofile');
    expect(result).toMatchObject({
      username: 'altprofile',
      displayName: 'Alt Profile',
      bio: 'Alternate fields',
      followers: 500,
      following: 100,
      totalLikes: 10000,
      videoCount: 20,
      verified: false,
    });
  });

  it('handles minimal profile with only username', () => {
    const result = extractProfileFromPayload(
      { userInfo: { user: { uniqueId: 'minimal' } } },
      'minimal',
    );
    expect(result).toBeUndefined(); // no identity details and no stats
  });

  it('handles profile with stats but no identity details', () => {
    const result = extractProfileFromPayload(
      {
        userInfo: {
          user: { uniqueId: 'statsonly' },
          stats: { followerCount: 1000 },
        },
      },
      'statsonly',
    );
    expect(result).toBeDefined();
    expect(result!.username).toBe('statsonly');
    expect(result!.followers).toBe(1000);
  });
});

describe('mergeVideoRecords', () => {
  const baseVideo: VideoRecord = {
    id: '123',
    author: 'testuser',
    profileUrl: 'https://www.tiktok.com/@testuser',
    videoUrl: 'https://www.tiktok.com/@testuser/video/123',
    description: 'Original description',
    publishedAt: 1_700_000_000,
    durationSeconds: 15,
    views: 1000,
    likes: 100,
    comments: 10,
    shares: 5,
    saves: 50,
    coverUrl: 'https://example.com/cover.jpg',
    hashtags: ['original'],
    audioTitle: 'Original Sound',
    isPinned: false,
    collectedAt: 1_700_000_000,
    source: 'api',
  };

  it('merges two records, preferring non-dom source', () => {
    const domVideo: VideoRecord = {
      ...baseVideo,
      views: 500,
      likes: 0,
      source: 'dom',
    };
    const result = mergeVideoRecords(domVideo, baseVideo);
    expect(result.views).toBe(1000); // Math.max
    expect(result.likes).toBe(100); // Math.max
    expect(result.source).toBe('api'); // prefers non-dom
  });

  it('takes max of numeric metrics', () => {
    const highViews: VideoRecord = { ...baseVideo, views: 9999, source: 'api' };
    const result = mergeVideoRecords(baseVideo, highViews);
    expect(result.views).toBe(9999);
  });

  it('merges hashtags as union', () => {
    const withExtraTags: VideoRecord = {
      ...baseVideo,
      hashtags: ['original', 'newtag'],
      source: 'api',
    };
    const result = mergeVideoRecords(baseVideo, withExtraTags);
    expect(result.hashtags).toEqual(['original', 'newtag']);
  });

  it('preserves isPinned if either is true', () => {
    const pinned: VideoRecord = { ...baseVideo, isPinned: true, source: 'api' };
    const result = mergeVideoRecords(baseVideo, pinned);
    expect(result.isPinned).toBe(true);
  });

  it('fills missing fields from incoming', () => {
    const partial: VideoRecord = {
      ...baseVideo,
      publishedAt: undefined,
      durationSeconds: undefined,
      coverUrl: undefined,
      audioTitle: undefined,
      source: 'api',
    };
    const result = mergeVideoRecords(partial, baseVideo);
    expect(result.publishedAt).toBe(1_700_000_000);
    expect(result.durationSeconds).toBe(15);
    expect(result.coverUrl).toBe('https://example.com/cover.jpg');
    expect(result.audioTitle).toBe('Original Sound');
  });
});
