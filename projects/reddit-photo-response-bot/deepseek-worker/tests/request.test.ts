import { afterEach, describe, expect, it, vi } from 'vitest';
import worker from '../src/index';

const env = {
  DEEPSEEK_API_KEY: 'deepseek-secret',
  EXTENSION_ACCESS_KEY: 'extension-secret',
  DEEPSEEK_MODEL: 'deepseek-v4-flash'
};

describe('worker request handling', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('rejects unauthorized callers before contacting DeepSeek', async () => {
    const fetchSpy = vi.spyOn(globalThis, 'fetch');
    const response = await worker.fetch(
      new Request('https://worker.example/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          post: { title: 'Looking for a photographer' }
        })
      }),
      env
    );

    expect(response.status).toBe(401);
    await expect(response.json()).resolves.toEqual({ error: 'Unauthorized.' });
    expect(fetchSpy).not.toHaveBeenCalled();
  });

  it('forwards a valid analyze request and returns normalized JSON', async () => {
    const fetchSpy = vi.spyOn(globalThis, 'fetch').mockResolvedValue(
      new Response(
        JSON.stringify({
          choices: [
            {
              message: {
                content: JSON.stringify({
                  label: 'possible_match',
                  confidence: 81.2,
                  customerIntent: 'Comparing photographer options',
                  responseRisk: 'medium',
                  reason: 'The author is discussing photo vendors but has not chosen one.',
                  recommendedAction: 'review'
                })
              }
            }
          ]
        }),
        {
          status: 200,
          headers: { 'Content-Type': 'application/json' }
        }
      )
    );

    const response = await worker.fetch(
      new Request('https://worker.example/analyze', {
        method: 'POST',
        headers: {
          Authorization: 'Bearer extension-secret',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          post: {
            id: 'abc123',
            title: 'Need wedding photographer recommendations',
            body: 'Brooklyn venue, fall wedding',
            permalink: 'https://www.reddit.com/r/WedditNYC/comments/abc123/sample/',
            subreddit: 'WedditNYC'
          },
          localClassification: {
            label: 'strong_match',
            score: 9,
            matchedSignals: ['looking-for-photographer'],
            reason: 'Explicit request.'
          }
        })
      }),
      env
    );

    expect(fetchSpy).toHaveBeenCalledTimes(1);
    expect(fetchSpy.mock.calls[0]?.[0]).toBe('https://api.deepseek.com/chat/completions');

    const forwarded = JSON.parse(String(fetchSpy.mock.calls[0]?.[1]?.body));
    expect(forwarded.model).toBe('deepseek-v4-flash');
    expect(forwarded.thinking).toEqual({ type: 'disabled' });
    expect(forwarded.response_format).toEqual({ type: 'json_object' });
    expect(forwarded.messages[1].content).toContain('"title":"Need wedding photographer recommendations"');

    expect(response.status).toBe(200);
    await expect(response.json()).resolves.toMatchObject({
      label: 'possible_match',
      confidence: 81,
      customerIntent: 'Comparing photographer options',
      responseRisk: 'medium',
      recommendedAction: 'review',
      model: 'deepseek-v4-flash'
    });
  });
});
