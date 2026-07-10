import { describe, expect, it } from 'vitest';
import { parseCompactNumber } from '../lib/numbers';

describe('parseCompactNumber', () => {
  it('parses compact suffixes', () => {
    expect(parseCompactNumber('1.2K')).toBe(1200);
    expect(parseCompactNumber('3M')).toBe(3_000_000);
  });

  it('parses comma separated values', () => {
    expect(parseCompactNumber('12,345')).toBe(12_345);
  });
});
