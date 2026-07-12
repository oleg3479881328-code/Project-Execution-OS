import React, { useEffect, useMemo, useState } from 'react';
import ReactDOM from 'react-dom/client';
import { browser } from 'wxt/browser';
import {
  clearHiddenPosts,
  listStoredPosts,
  POSTS_STORAGE_KEY,
  updatePostDecision
} from '../../lib/storage';
import type { DetectedPost, OwnerDecision, RelevanceLabel } from '../../lib/types';
import './style.css';

const LABELS: Array<RelevanceLabel | 'all'> = [
  'all',
  'strong_match',
  'possible_match',
  'not_match',
  'skip_vendor_risk'
];

function App() {
  const [posts, setPosts] = useState<DetectedPost[]>([]);
  const [filter, setFilter] = useState<(typeof LABELS)[number]>('all');

  async function refresh() {
    setPosts(await listStoredPosts());
  }

  useEffect(() => {
    void refresh();
    const listener = (changes: Record<string, { newValue?: unknown; oldValue?: unknown }>) => {
      if (changes[POSTS_STORAGE_KEY]) void refresh();
    };
    browser.storage.onChanged.addListener(listener);
    return () => browser.storage.onChanged.removeListener(listener);
  }, []);

  const visiblePosts = useMemo(
    () =>
      posts.filter((post) => {
        if (post.ownerDecision === 'hidden') return false;
        const label = post.manualLabel ?? post.classification.label;
        return filter === 'all' || label === filter;
      }),
    [filter, posts]
  );

  async function setDecision(id: string, ownerDecision: OwnerDecision) {
    await updatePostDecision(id, { ownerDecision });
    await refresh();
  }

  return (
    <main>
      <header>
        <div>
          <h1>WedditNYC leads</h1>
          <p>{posts.length} detected posts</p>
        </div>
        <button
          className="secondary"
          onClick={async () => {
            await clearHiddenPosts();
            await refresh();
          }}
        >
          Clear hidden
        </button>
      </header>

      <nav aria-label="Post filters">
        {LABELS.map((label) => (
          <button
            key={label}
            className={filter === label ? 'active' : ''}
            onClick={() => setFilter(label)}
          >
            {label.replaceAll('_', ' ')}
          </button>
        ))}
      </nav>

      <section className="post-list">
        {visiblePosts.length === 0 ? (
          <p className="empty">Open r/WedditNYC to detect visible posts.</p>
        ) : (
          visiblePosts.map((post) => {
            const label = post.manualLabel ?? post.classification.label;
            return (
              <article key={post.id} data-label={label}>
                <div className="row">
                  <span className="badge">{label.replaceAll('_', ' ')}</span>
                  <span className="decision">{post.ownerDecision}</span>
                </div>
                <h2>{post.title}</h2>
                <p>{post.classification.reason}</p>
                <div className="actions">
                  <button onClick={() => browser.tabs.create({ url: post.permalink })}>
                    Open
                  </button>
                  <button onClick={() => setDecision(post.id, 'relevant')}>Relevant</button>
                  <button onClick={() => setDecision(post.id, 'irrelevant')}>Irrelevant</button>
                  <button onClick={() => setDecision(post.id, 'hidden')}>Hide</button>
                </div>
              </article>
            );
          })
        )}
      </section>
    </main>
  );
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
