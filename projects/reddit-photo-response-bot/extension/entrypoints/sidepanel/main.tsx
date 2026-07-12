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

const LABEL_NAMES: Record<RelevanceLabel | 'all', string> = {
  all: 'All',
  strong_match: 'Strong',
  possible_match: 'Possible',
  not_match: 'Not a match',
  skip_vendor_risk: 'Vendor risk'
};

function effectiveLabel(post: DetectedPost): RelevanceLabel {
  return post.manualLabel ?? post.classification.label;
}

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
        return filter === 'all' || effectiveLabel(post) === filter;
      }),
    [filter, posts]
  );

  const strongCount = posts.filter((post) => effectiveLabel(post) === 'strong_match').length;
  const unreviewedCount = posts.filter((post) => post.ownerDecision === 'unreviewed').length;

  async function setDecision(id: string, ownerDecision: OwnerDecision) {
    await updatePostDecision(id, { ownerDecision });
    await refresh();
  }

  async function setManualLabel(id: string, manualLabel: RelevanceLabel) {
    await updatePostDecision(id, { manualLabel });
    await refresh();
  }

  return (
    <main>
      <header className="panel-header">
        <div>
          <p className="eyebrow">Reddit lead review</p>
          <h1>WedditNYC</h1>
          <p className="summary">
            {posts.length} detected · {strongCount} strong · {unreviewedCount} unreviewed
          </p>
        </div>
        <div className="header-actions">
          <button className="secondary" onClick={() => void refresh()}>
            Refresh
          </button>
          <button
            className="secondary"
            onClick={async () => {
              await clearHiddenPosts();
              await refresh();
            }}
          >
            Clear hidden
          </button>
        </div>
      </header>

      <section className="community-actions">
        <button
          className="primary"
          onClick={() => browser.tabs.create({ url: 'https://www.reddit.com/r/WedditNYC/new/' })}
        >
          Open r/WedditNYC/new
        </button>
      </section>

      <nav aria-label="Post filters" className="filters">
        {LABELS.map((label) => (
          <button
            key={label}
            className={filter === label ? 'active' : ''}
            onClick={() => setFilter(label)}
          >
            {LABEL_NAMES[label]}
          </button>
        ))}
      </nav>

      <section className="post-list">
        {visiblePosts.length === 0 ? (
          <div className="empty">
            <h2>No posts in this view</h2>
            <p>Open r/WedditNYC in Chrome. Visible posts will appear here automatically.</p>
          </div>
        ) : (
          visiblePosts.map((post) => {
            const label = effectiveLabel(post);
            return (
              <article key={post.id} data-label={label}>
                <div className="card-topline">
                  <span className="badge">{LABEL_NAMES[label]}</span>
                  <span className="decision">{post.ownerDecision}</span>
                </div>

                <h2>{post.title}</h2>
                <p className="reason">{post.classification.reason}</p>

                {post.classification.matchedSignals.length > 0 && (
                  <div className="signals" aria-label="Matched signals">
                    {post.classification.matchedSignals.map((signal) => (
                      <span key={signal}>{signal}</span>
                    ))}
                  </div>
                )}

                <label className="field">
                  <span>Classification</span>
                  <select
                    value={label}
                    onChange={(event) =>
                      void setManualLabel(post.id, event.target.value as RelevanceLabel)
                    }
                  >
                    {LABELS.filter((value): value is RelevanceLabel => value !== 'all').map(
                      (value) => (
                        <option key={value} value={value}>
                          {LABEL_NAMES[value]}
                        </option>
                      )
                    )}
                  </select>
                </label>

                <div className="actions">
                  <button onClick={() => browser.tabs.create({ url: post.permalink })}>Open</button>
                  <button
                    className={post.ownerDecision === 'relevant' ? 'selected' : ''}
                    onClick={() => void setDecision(post.id, 'relevant')}
                  >
                    Relevant
                  </button>
                  <button
                    className={post.ownerDecision === 'irrelevant' ? 'selected' : ''}
                    onClick={() => void setDecision(post.id, 'irrelevant')}
                  >
                    Irrelevant
                  </button>
                  <button onClick={() => void setDecision(post.id, 'hidden')}>Hide</button>
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
