import { describe, expect, it } from 'vitest';
import { extractProfileFromPayload } from '../lib/tiktok-parser';

describe('complete public channel profile parsing', () => {
  it('extracts identifiers, public counters, flags, locale, website, and account date', () => {
    const payload = {
      userInfo: {
        user: {
          id: '7000000000000000001',
          secUid: 'MS4wLjABAAAA-complete-profile',
          uniqueId: 'completecreator',
          nickname: 'Complete Creator',
          signature: 'Wedding filmmaker and educator',
          avatarLarger: 'https://example.com/avatar.jpg',
          verified: true,
          privateAccount: false,
          isCommerceUser: true,
          region: 'US',
          language: 'en',
          createTime: 1_550_000_000,
          bioLink: { link: 'https://ignored.example', url: 'https://creator.example' },
        },
        stats: {
          followerCount: 250000,
          followingCount: 425,
          friendCount: 88,
          heartCount: 12500000,
          videoCount: 678,
        },
      },
    };

    const profile = extractProfileFromPayload(payload, 'completecreator');
    expect(profile).toMatchObject({
      username: 'completecreator',
      userId: '7000000000000000001',
      secUid: 'MS4wLjABAAAA-complete-profile',
      displayName: 'Complete Creator',
      bio: 'Wedding filmmaker and educator',
      avatarUrl: 'https://example.com/avatar.jpg',
      followers: 250000,
      following: 425,
      friends: 88,
      totalLikes: 12500000,
      videoCount: 678,
      verified: true,
      privateAccount: false,
      commerceAccount: true,
      region: 'US',
      language: 'en',
      accountCreatedAt: 1_550_000_000,
      website: 'https://creator.example/',
    });
  });

  it('preserves explicit false flags instead of treating them as missing', () => {
    const profile = extractProfileFromPayload({
      userInfo: {
        user: {
          uniqueId: 'publiccreator',
          nickname: 'Public Creator',
          verified: false,
          privateAccount: false,
          isCommerceUser: false,
        },
      },
    }, 'publiccreator');

    expect(profile?.verified).toBe(false);
    expect(profile?.privateAccount).toBe(false);
    expect(profile?.commerceAccount).toBe(false);
  });

  it('converts millisecond account timestamps to seconds and rejects unsafe websites', () => {
    const profile = extractProfileFromPayload({
      userInfo: {
        user: {
          uniqueId: 'safecreator',
          nickname: 'Safe Creator',
          createTime: 1_550_000_000_000,
          website: 'javascript:alert(1)',
        },
      },
    }, 'safecreator');

    expect(profile?.accountCreatedAt).toBe(1_550_000_000);
    expect(profile?.website).toBeUndefined();
  });
});
