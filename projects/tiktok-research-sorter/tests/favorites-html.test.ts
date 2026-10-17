import { describe, expect, it } from 'vitest';
import {
  channelSnapshotFromProfile,
  favoriteKey,
  groupFavoriteEntriesByChannel,
  mergeChannelSnapshots,
  minimalChannelSnapshot,
  orderedFavoriteEntries,
  selectFavoriteEntries,
} from '../lib/favorites';
import { generateFavoritesHtml } from '../lib/html-export';
import type { ChannelSnapshot, FavoriteEntry, ProfileSnapshot, VideoRecord } from '../lib/types';

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

function fullChannel(username: string, overrides: Partial<ChannelSnapshot> = {}): ChannelSnapshot {
  return {
    username,
    profileUrl: `https://www.tiktok.com/@${username}`,
    userId: '123456',
    secUid: 'MS4wLjABAAAA-test',
    displayName: 'Wedding Channel',
    bio: 'Wedding creator and photographer',
    avatarUrl: 'https://example.com/avatar.jpg',
    followers: 125000,
    following: 321,
    friends: 77,
    totalLikes: 9800000,
    videoCount: 456,
    verified: true,
    privateAccount: false,
    commerceAccount: true,
    website: 'https://example.com',
    region: 'US',
    language: 'en',
    accountCreatedAt: 1_600_000_000,
    medianViews: 75000,
    lastScannedAt: 1_700_000_000_000,
    profileDataUpdatedAt: 1_700_000_100_000,
    profileDataSource: 'api',
    collectedVideoCount: 88,
    averageEngagementRate: 4.25,
    strongestHashtags: ['wedding', 'photography'],
    capturedAt: 1_700_000_200_000,
    completeness: 'full',
    ...overrides,
  };
}

function favorite(entryVideo: VideoRecord, favoritedAt: number, channel = fullChannel(entryVideo.author)): FavoriteEntry {
  return {
    key: favoriteKey(entryVideo),
    video: entryVideo,
    channel,
    favoritedAt,
  };
}

describe('favorites and channel snapshots', () => {
  it('creates a stable case-insensitive key from author and video id', () => {
    expect(favoriteKey({ author: '@OlgaPhoto', id: '123' })).toBe('olgaphoto:123');
    expect(favoriteKey({ author: 'olgaphoto', id: '123' })).toBe('olgaphoto:123');
  });

  it('migrates an old favorite without channel data to a partial channel snapshot', () => {
    const oldEntry = {
      key: 'legacy:1',
      video: video('1', 'legacy', 100),
      favoritedAt: 1000,
    } as unknown as FavoriteEntry;
    const normalized = orderedFavoriteEntries({ [oldEntry.key]: oldEntry })[0];
    expect(normalized?.channel.username).toBe('legacy');
    expect(normalized?.channel.completeness).toBe('partial');
  });

  it('creates a rich channel snapshot from a scanned profile', () => {
    const profile: ProfileSnapshot = {
      username: 'creator',
      profileUrl: 'https://www.tiktok.com/@creator',
      userId: '42',
      secUid: 'sec-42',
      displayName: 'Creator Name',
      bio: 'Creator bio',
      avatarUrl: 'https://example.com/creator.jpg',
      followers: 5000,
      following: 100,
      friends: 50,
      totalLikes: 100000,
      videoCount: 20,
      verified: true,
      privateAccount: false,
      commerceAccount: false,
      website: 'https://creator.example',
      region: 'US',
      language: 'en',
      accountCreatedAt: 1_500_000_000,
      videos: [video('1', 'creator', 1000), video('2', 'creator', 3000, { hashtags: ['tips'] })],
      medianViews: 2000,
      lastScannedAt: 1_700_000_000_000,
      profileDataUpdatedAt: 1_700_000_100_000,
      profileDataSource: 'api',
    };
    const channel = channelSnapshotFromProfile(profile);
    expect(channel).toMatchObject({
      username: 'creator',
      followers: 5000,
      following: 100,
      friends: 50,
      totalLikes: 100000,
      videoCount: 20,
      collectedVideoCount: 2,
      medianViews: 2000,
      completeness: 'full',
    });
    expect(channel.averageEngagementRate).toBeGreaterThan(0);
    expect(channel.strongestHashtags).toContain('tips');
  });

  it('keeps richer channel fields when snapshots are merged', () => {
    const partial = minimalChannelSnapshot(video('1', 'creator', 100));
    const rich = fullChannel('creator');
    const merged = mergeChannelSnapshots(partial, rich);
    expect(merged.completeness).toBe('full');
    expect(merged.followers).toBe(125000);
    expect(merged.userId).toBe('123456');
  });

  it('groups multiple favorite videos under one channel', () => {
    const first = favorite(video('1', 'creator', 100), 1000);
    const second = favorite(video('2', 'Creator', 200), 2000, fullChannel('Creator'));
    const groups = groupFavoriteEntriesByChannel([first, second]);
    expect(groups).toHaveLength(1);
    expect(groups[0]?.entries).toHaveLength(2);
    expect(groups[0]?.channel.followers).toBe(125000);
  });

  it('orders newest favorites first and exports only checked entries', () => {
    const first = favorite(video('1', 'alice', 100), 1000);
    const second = favorite(video('2', 'bob', 200), 2000);
    const favorites = { [first.key]: first, [second.key]: second };

    expect(orderedFavoriteEntries(favorites).map((entry) => entry.key)).toEqual([second.key, first.key]);
    expect(selectFavoriteEntries(favorites, [first.key]).map((entry) => entry.key)).toEqual([first.key]);
  });

  it('generates standalone HTML with complete channel and video information', () => {
    const entry = favorite(video('777', 'creator', 123_456), 2000);
    const html = generateFavoritesHtml([entry], { title: 'Client shortlist', generatedAt: 1_700_000_000_000 });

    expect(html).toContain('<!doctype html>');
    expect(html).toContain('<meta charset="utf-8">');
    expect(html).toContain('Client shortlist');
    expect(html).toContain('https://www.tiktok.com/@creator/video/777');
    expect(html).toContain('https://example.com/777.jpg');
    expect(html).toContain('Video 777');
    expect(html).toContain('data-video-key="creator:777"');
    expect(html).toContain('data-channel="creator"');
    expect(html).toContain('Wedding Channel');
    expect(html).toContain('125 000');
    expect(html).toContain('MS4wLjABAAAA-test');
    expect(html).toContain('Коммерческий аккаунт');
    expect(html).toContain('TikTok Research Sorter v0.6.0');
  });

  it('escapes channel and video text and rejects non-http links and previews', () => {
    const unsafeChannel = fullChannel('bad', {
      displayName: '<script>alert("channel")</script>',
      bio: '<img src=x onerror=alert(1)>',
      profileUrl: 'javascript:alert(2)',
      website: 'data:text/html,<script>alert(3)</script>',
      avatarUrl: 'javascript:alert(4)',
      strongestHashtags: ['<svg onload=alert(5)>'],
    });
    const unsafe = favorite(video('9', 'bad', 1, {
      description: '<script>alert("x")</script>',
      profileUrl: 'javascript:alert(6)',
      videoUrl: 'javascript:alert(7)',
      coverUrl: 'data:text/html,<script>alert(8)</script>',
      hashtags: ['<img src=x onerror=alert(9)>'],
    }), 3000, unsafeChannel);

    const html = generateFavoritesHtml([unsafe], { generatedAt: 1_700_000_000_000 });

    expect(html).not.toContain('<script>alert');
    expect(html).not.toContain('javascript:');
    expect(html).not.toContain('data:text/html');
    expect(html).toContain('&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;');
    expect(html).toContain('&lt;script&gt;alert(&quot;channel&quot;)&lt;/script&gt;');
    expect(html).toContain('Превью недоступно');
  });

  it('keeps unselected favorites and their channels out of generated HTML', () => {
    const selected = favorite(video('11', 'one', 10), 2000, fullChannel('one', { displayName: 'Selected Channel' }));
    const omitted = favorite(video('22', 'two', 20), 1000, fullChannel('two', { displayName: 'Omitted Channel' }));
    const favorites = { [selected.key]: selected, [omitted.key]: omitted };
    const chosen = selectFavoriteEntries(favorites, [selected.key]);
    const html = generateFavoritesHtml(chosen, { generatedAt: 1_700_000_000_000 });

    expect(html).toContain('/video/11');
    expect(html).toContain('Selected Channel');
    expect(html).not.toContain('/video/22');
    expect(html).not.toContain('Omitted Channel');
  });
});
