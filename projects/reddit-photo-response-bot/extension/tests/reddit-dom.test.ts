import { beforeEach, describe, expect, it } from 'vitest';
import { findPostElements, parsePostElement } from '../lib/reddit-dom';

describe('reddit DOM parsing', () => {
  beforeEach(() => {
    document.body.innerHTML = '';
    window.history.replaceState({}, '', '/r/WedditNYC/');
  });

  it('parses a shreddit post fixture', () => {
    document.body.innerHTML = `
      <shreddit-post thingid="t3_abc123" permalink="/r/WedditNYC/comments/abc123/sample/">
        <h2 slot="title">Looking for a city hall photographer</h2>
        <div slot="text-body">We need two hours in Manhattan.</div>
      </shreddit-post>
    `;

    const element = findPostElements()[0];
    expect(element).toBeDefined();
    const parsed = parsePostElement(element!);
    expect(parsed).toMatchObject({
      id: 'abc123',
      title: 'Looking for a city hall photographer',
      subreddit: 'WedditNYC'
    });
    expect(parsed?.permalink).toContain('/comments/abc123/');
  });

  it('returns null when no post title exists', () => {
    const element = document.createElement('shreddit-post');
    element.setAttribute('permalink', '/r/WedditNYC/comments/abc123/sample/');
    expect(parsePostElement(element)).toBeNull();
  });
});
