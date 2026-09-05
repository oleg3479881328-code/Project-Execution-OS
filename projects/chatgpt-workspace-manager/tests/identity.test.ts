import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import { STABLE_EXTENSION_ID, STABLE_EXTENSION_KEY } from '../src/core/extension-identity';

function chromeExtensionIdFromKey(base64Key: string): string {
  const digest = createHash('sha256').update(Buffer.from(base64Key, 'base64')).digest().subarray(0, 16);
  const alphabet = 'abcdefghijklmnop';
  let id = '';
  for (const byte of digest) {
    id += alphabet[byte >> 4];
    id += alphabet[byte & 0x0f];
  }
  return id;
}

describe('stable unpacked extension identity', () => {
  it('derives the frozen Chrome extension ID from the pinned public key', () => {
    expect(chromeExtensionIdFromKey(STABLE_EXTENSION_KEY)).toBe(STABLE_EXTENSION_ID);
    expect(STABLE_EXTENSION_ID).toBe('ejpgnlcdfbbjkhlnbfonplngcfcjmbaa');
  });
});
