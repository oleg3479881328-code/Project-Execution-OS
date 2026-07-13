import { describe, expect, it } from 'vitest';
import { parseAiAnalysis } from '../lib/ai-client';

describe('parseAiAnalysis', () => {
  it('accepts a valid semantic analysis response', () => {
    expect(
      parseAiAnalysis({
        label: 'strong_match',
        confidence: 92,
        customerIntent: 'Hiring a wedding photographer',
        responseRisk: 'low',
        reason: 'The author explicitly asks for photographer recommendations.',
        recommendedAction: 'respond',
        analyzedAt: '2026-07-12T20:00:00.000Z',
        model: 'deepseek-v4-flash'
      })
    ).toMatchObject({ label: 'strong_match', confidence: 92, responseRisk: 'low' });
  });

  it('rejects malformed or untrusted output', () => {
    expect(() =>
      parseAiAnalysis({
        label: 'buy_now',
        confidence: 150,
        customerIntent: '',
        responseRisk: 'none',
        reason: '',
        recommendedAction: 'spam',
        analyzedAt: 'never',
        model: ''
      })
    ).toThrow();
  });
});