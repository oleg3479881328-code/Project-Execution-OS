import { beforeEach, describe, expect, it, vi } from 'vitest';

const localState = new Map<string, unknown>();

vi.mock('wxt/browser', () => ({
  browser: {
    storage: {
      local: {
        async get(key: string) {
          return { [key]: localState.get(key) };
        },
        async set(value: Record<string, unknown>) {
          for (const [key, entry] of Object.entries(value)) {
            localState.set(key, entry);
          }
        }
      },
      onChanged: {
        addListener() {},
        removeListener() {}
      }
    }
  }
}));

import {
  DEFAULT_AI_SETTINGS,
  getAiSettings,
  listStoredPosts,
  updatePostAiAnalysis,
  upsertDetectedPost
} from '../lib/storage';
import type { DetectedPost } from '../lib/types';

function makePost(id: string, detectedAt: string): DetectedPost {
  return {
    id,
    title: `Post ${id}`,
    body: 'Looking for wedding photo coverage',
    permalink: `https://www.reddit.com/r/WedditNYC/comments/${id}/sample/`,
    subreddit: 'WedditNYC',
    detectedAt,
    ownerDecision: 'unreviewed',
    classification: {
      label: 'possible_match',
      score: 6,
      matchedSignals: ['photography'],
      reason: 'Photo-related discussion detected.'
    }
  };
}

describe('storage persistence', () => {
  beforeEach(() => {
    localState.clear();
  });

  it('returns default AI settings when none were saved', async () => {
    await expect(getAiSettings()).resolves.toEqual(DEFAULT_AI_SETTINGS);
  });

  it('persists AI analysis across post upserts', async () => {
    const original = await upsertDetectedPost(makePost('abc123', '2026-07-12T20:00:00.000Z'));
    expect(original.aiAnalysis).toBeUndefined();

    await updatePostAiAnalysis('abc123', {
      label: 'strong_match',
      confidence: 94,
      customerIntent: 'Hiring a wedding photographer now',
      responseRisk: 'low',
      reason: 'The post clearly asks for photographer recommendations.',
      recommendedAction: 'respond',
      analyzedAt: '2026-07-12T20:05:00.000Z',
      model: 'deepseek-v4-flash'
    });

    await upsertDetectedPost({
      ...makePost('abc123', '2026-07-12T20:10:00.000Z'),
      title: 'Updated title from a later DOM capture'
    });

    await upsertDetectedPost(makePost('def456', '2026-07-12T19:00:00.000Z'));

    const posts = await listStoredPosts();
    expect(posts.map((post) => post.id)).toEqual(['abc123', 'def456']);
    expect(posts[0]).toMatchObject({
      title: 'Updated title from a later DOM capture',
      aiAnalysis: {
        label: 'strong_match',
        confidence: 94,
        recommendedAction: 'respond',
        model: 'deepseek-v4-flash'
      }
    });
  });
});
