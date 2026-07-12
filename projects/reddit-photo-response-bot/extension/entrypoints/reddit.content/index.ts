import { classifyPost } from '../../lib/classifier';
import { findPostElements, parsePostElement } from '../../lib/reddit-dom';
import { updatePostDecision, upsertDetectedPost } from '../../lib/storage';
import type { DetectedPost, OwnerDecision, RelevanceLabel } from '../../lib/types';
import './style.css';

const CONTROL_ATTRIBUTE = 'data-rprb-controls';

function isTargetCommunity(): boolean {
  return /\/r\/wedditnyc(?:\/|$)/i.test(location.pathname);
}

function effectiveLabel(post: DetectedPost): RelevanceLabel {
  return post.manualLabel ?? post.classification.label;
}

function createSelect(
  post: DetectedPost,
  controls: HTMLDivElement,
  badge: HTMLSpanElement
): HTMLSelectElement {
  const select = document.createElement('select');
  select.className = 'rprb-select';
  select.setAttribute('aria-label', 'Post relevance');

  const labels: RelevanceLabel[] = [
    'strong_match',
    'possible_match',
    'not_match',
    'skip_vendor_risk'
  ];

  for (const label of labels) {
    const option = document.createElement('option');
    option.value = label;
    option.textContent = label.replaceAll('_', ' ');
    option.selected = effectiveLabel(post) === label;
    select.append(option);
  }

  select.addEventListener('change', async () => {
    const manualLabel = select.value as RelevanceLabel;
    await updatePostDecision(post.id, { manualLabel });
    controls.dataset.label = manualLabel;
    badge.textContent = manualLabel.replaceAll('_', ' ');
  });

  return select;
}

function createDecisionButton(
  post: DetectedPost,
  controls: HTMLDivElement,
  decision: OwnerDecision,
  label: string
): HTMLButtonElement {
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'rprb-button';
  button.textContent = label;
  if (post.ownerDecision === decision) button.classList.add('is-active');

  button.addEventListener('click', async () => {
    await updatePostDecision(post.id, { ownerDecision: decision });
    controls.dataset.decision = decision;
    controls
      .querySelectorAll('.rprb-button')
      .forEach((element) => element.classList.remove('is-active'));
    button.classList.add('is-active');
  });
  return button;
}

async function enhancePost(element: HTMLElement): Promise<void> {
  if (element.hasAttribute(CONTROL_ATTRIBUTE)) return;
  element.setAttribute(CONTROL_ATTRIBUTE, 'processing');

  const parsed = parsePostElement(element);
  if (!parsed) {
    element.removeAttribute(CONTROL_ATTRIBUTE);
    return;
  }

  const classification = classifyPost(parsed.title, parsed.body);
  const post = await upsertDetectedPost({
    ...parsed,
    detectedAt: new Date().toISOString(),
    classification,
    ownerDecision: 'unreviewed'
  });

  const controls = document.createElement('div');
  controls.className = 'rprb-controls';
  controls.dataset.label = effectiveLabel(post);
  controls.dataset.decision = post.ownerDecision;

  const badge = document.createElement('span');
  badge.className = 'rprb-badge';
  badge.textContent = effectiveLabel(post).replaceAll('_', ' ');
  badge.title = post.classification.reason;

  const reason = document.createElement('span');
  reason.className = 'rprb-reason';
  reason.textContent = post.classification.reason;

  const actions = document.createElement('div');
  actions.className = 'rprb-actions';
  actions.append(
    createSelect(post, controls, badge),
    createDecisionButton(post, controls, 'relevant', 'Relevant'),
    createDecisionButton(post, controls, 'irrelevant', 'Irrelevant'),
    createDecisionButton(post, controls, 'hidden', 'Hide')
  );

  controls.append(badge, reason, actions);
  element.prepend(controls);
  element.setAttribute(CONTROL_ATTRIBUTE, 'ready');
}

async function scan(root: ParentNode = document): Promise<void> {
  if (!isTargetCommunity()) return;
  const posts = findPostElements(root);
  await Promise.all(posts.map((post) => enhancePost(post)));
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
