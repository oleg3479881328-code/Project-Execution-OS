import { describe, expect, it } from 'vitest';
import { parseCompactNumber } from '../lib/numbers';

describe('parseCompactNumber', () => {
  it('parses compact suffixes', () => {
    expect(parseCompactNumber('1.2K')).toBe(1200);
    expect(parseCompactNumber('3M')).toBe(3_000_000);
    expect(parseCompactNumber('1,2M')).toBe(1_200_000);
  });

  it('parses localized suffixes', () => {
    expect(parseCompactNumber('1,5 тыс.')).toBe(1500);
    expect(parseCompactNumber('2,3 млн')).toBe(2_300_000);
    expect(parseCompactNumber('1 млрд')).toBe(1_000_000_000);
  });

  it('parses grouped values', () => {
    expect(parseCompactNumber('12,345')).toBe(12_345);
    expect(parseCompactNumber('12.345')).toBe(12_345);
    expect(parseCompactNumber('1 234 567')).toBe(1_234_567);
  });

  it('rejects invalid and negative values', () => {
    expect(parseCompactNumber('not-a-number')).toBe(0);
    expect(parseCompactNumber('-2K')).toBe(0);
  });
});
