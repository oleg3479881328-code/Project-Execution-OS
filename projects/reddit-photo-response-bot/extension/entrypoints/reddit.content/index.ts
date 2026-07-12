import { classifyPost } from '../../lib/classifier';
import { findPostElements, parsePostElement } from '../../lib/reddit-dom';
import { upsertDetectedPost } from '../../lib/storage';

const processedPosts = new WeakSet<HTMLElement>();

function isTargetCommunity(): boolean {
  return /\/r\/wedditnyc(?:\/|$)/i.test(location.pathname);
}

async function capturePost(element: HTMLElement): Promise<void> {
  if (processedPosts.has(element)) return;
  processedPosts.add(element);

  const parsed = parsePostElement(element);
  if (!parsed) return;

  await upsertDetectedPost({
    ...parsed,
    detectedAt: new Date().toISOString(),
    classification: classifyPost(parsed.title, parsed.body),
    ownerDecision: 'unreviewed'
  });
}

async function scan(root: ParentNode = document): Promise<void> {
  if (!isTargetCommunity()) return;
  await Promise.all(findPostElements(root).map((post) => capturePost(post)));
}

export default defineContentScript({
  matches: [
    'https://www.reddit.com/r/WedditNYC/*',
    'https://old.reddit.com/r/WedditNYC/*'
  ],
  runAt: 'document_idle',
  main(ctx) {
    void scan();

    const observer = new MutationObserver((mutations) => {
      for (const mutation of mutations) {
        for (const node of mutation.addedNodes) {
          if (node instanceof HTMLElement) void scan(node);
        }
      }
    });

    observer.observe(document.documentElement, { childList: true, subtree: true });
    ctx.onInvalidated(() => observer.disconnect());
  }
});
