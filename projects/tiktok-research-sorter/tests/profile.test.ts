import { describe, expect, it } from 'vitest';
import { extractProfileFromPayload } from '../lib/tiktok-parser';

describe('TikTok profile parser', () => {
  it('extracts user identity and profile counters from userInfo', () => {
    const payload = {
      userInfo: {
        user: {
          uniqueId: 'jasminebrookephotography',
          nickname: 'Jasmine Brooke Photography',
          signature: 'San Diego wedding photographer',
          avatarLarger: 'https://example.com/avatar.jpg',
          verified: true,
        },
        stats: {
          followerCount: 1011,
          followingCount: 249,
          heartCount: 333600,
          videoCount: 87,
        },
      },
    };

    expect(extractProfileFromPayload(payload, 'jasminebrookephotography')).toMatchObject({
      username: 'jasminebrookephotography',
      displayName: 'Jasmine Brooke Photography',
      bio: 'San Diego wedding photographer',
      followers: 1011,
      following: 249,
      totalLikes: 333600,
      videoCount: 87,
      verified: true,
    });
  });
});
