import { describe, expect, it } from 'vitest';
import { classifyPost } from '../lib/classifier';

describe('classifyPost', () => {
  it('marks an explicit photographer request as strong', () => {
    const result = classifyPost('Looking for a wedding photographer in NYC');
    expect(result.label).toBe('strong_match');
    expect(result.matchedSignals).toContain('looking-for-photographer');
  });

  it('marks a pricing discussion as possible', () => {
    const result = classifyPost('Photography budget', 'What did you pay for your photographer?');
    expect(result.label).toBe('possible_match');
  });

  it('prioritizes vendor risk language', () => {
    const result = classifyPost('Photographer discussion', 'Please no vendors or DMs.');
    expect(result.label).toBe('skip_vendor_risk');
  });

  it('rejects unrelated vendor requests', () => {
    const result = classifyPost('Looking for a florist in Brooklyn');
    expect(result.label).toBe('not_match');
  });
});
