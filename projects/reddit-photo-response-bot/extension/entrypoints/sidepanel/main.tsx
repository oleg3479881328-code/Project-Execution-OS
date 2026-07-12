import React, { useEffect, useMemo, useRef, useState } from 'react';
import ReactDOM from 'react-dom/client';
import { browser } from 'wxt/browser';
import {
  analyzePostWithAi,
  isAiConfigured,
  requestProxyPermission
} from '../../lib/ai-client';
import {
  AI_SETTINGS_STORAGE_KEY,
  clearHiddenPosts,
  getAiSettings,
  listStoredPosts,
  POSTS_STORAGE_KEY,
  saveAiSettings,
  updatePostAiAnalysis,
  updatePostDecision
} from '../../lib/storage';
import type {
  AiSettings,
  DetectedPost,
  OwnerDecision,
  RelevanceLabel
} from '../../lib/types';
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
  return post.manualLabel ?? post.aiAnalysis?.label ?? post.classification.label;
}

function isLocalCandidate(post: DetectedPost): boolean {
  const label = post.manualLabel ?? post.classification.label;
  return label === 'strong_match' || label === 'possible_match';
}

function App() {
  const [posts, setPosts] = useState<DetectedPost[]>([]);
  const [filter, setFilter] = useState<(typeof LABELS)[number]>('all');
  const [settings, setSettings] = useState<AiSettings>({
    enabled: false,
    autoAnalyzeCandidates: false,
    proxyUrl: '',
    accessKey: ''
  });
  const [settingsDraft, setSettingsDraft] = useState<AiSettings>(settings);
  const [settingsLoaded, setSettingsLoaded] = useState(false);
  const [settingsMessage, setSettingsMessage] = useState('');
  const [analyzingIds, setAnalyzingIds] = useState<Set<string>>(new Set());
  const [batchRunning, setBatchRunning] = useState(false);
  const autoAttempted = useRef<Set<string>>(new Set());

  async function refresh() {
    setPosts(await listStoredPosts());
  }

  useEffect(() => {
    void Promise.all([refresh(), getAiSettings().then((saved) => {
      setSettings(saved);
      setSettingsDraft(saved);
      setSettingsLoaded(true);
    })]);

    const listener = (changes: Record<string, { newValue?: unknown; oldValue?: unknown }>) => {
      if (changes[POSTS_STORAGE_KEY]) void refresh();
      if (changes[AI_SETTINGS_STORAGE_KEY]) {
        void getAiSettings().then((saved) => {
          setSettings(saved);
          setSettingsDraft(saved);
        });
      }
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
  const aiCount = posts.filter((post) => post.aiAnalysis).length;
  const aiConfigured = isAiConfigured(settings);

  async function setDecision(id: string, ownerDecision: OwnerDecision) {
    await updatePostDecision(id, { ownerDecision });
    await refresh();
  }

  async function setManualLabel(id: string, manualLabel: RelevanceLabel) {
    await updatePostDecision(id, { manualLabel });
    await refresh();
  }

  async function runAiAnalysis(post: DetectedPost) {
    if (!isAiConfigured(settings)) {
      setSettingsMessage('Enable AI and save a valid HTTPS Worker URL and access key first.');
      return;
    }

    setAnalyzingIds((current) => new Set(current).add(post.id));
    await updatePostAiAnalysis(post.id, post.aiAnalysis, undefined);
    try {
      const result = await analyzePostWithAi(post, settings);
      await updatePostAiAnalysis(post.id, result, undefined);
    } catch (error) {
      const message = error instanceof Error ? error.message : 'AI analysis failed.';
      await updatePostAiAnalysis(post.id, post.aiAnalysis, message);
    } finally {
      setAnalyzingIds((current) => {
        const next = new Set(current);
        next.delete(post.id);
        return next;
      });
      await refresh();
    }
  }

  async function analyzeCandidates() {
    if (!aiConfigured) {
      setSettingsMessage('Configure the AI Worker before running batch analysis.');
      return;
    }

    setBatchRunning(true);
    const candidates = posts.filter(
      (post) => isLocalCandidate(post) && !post.aiAnalysis && post.ownerDecision !== 'hidden'
    );
    for (const post of candidates) await runAiAnalysis(post);
    setBatchRunning(false);
  }

  async function saveSettingsFromUserGesture() {
    setSettingsMessage('');
    try {
      const next = {
        ...settingsDraft,
        proxyUrl: settingsDraft.proxyUrl.trim().replace(/\/+$/, ''),
        accessKey: settingsDraft.accessKey.trim()
      };

      if (next.enabled) {
        if (!next.proxyUrl || !next.accessKey) {
          throw new Error('Worker URL and Worker access key are required.');
        }
        const granted = await requestProxyPermission(next.proxyUrl);
        if (!granted) throw new Error('Chrome permission for the Worker origin was not granted.');
      }

      await saveAiSettings(next);
      setSettings(next);
      setSettingsDraft(next);
      setSettingsMessage('AI settings saved locally.');
    } catch (error) {
      setSettingsMessage(error instanceof Error ? error.message : 'Could not save AI settings.');
    }
  }

  useEffect(() => {
    if (!settingsLoaded || !settings.autoAnalyzeCandidates || !aiConfigured) return;
    const next = posts.find(
      (post) =>
        isLocalCandidate(post) &&
        !post.aiAnalysis &&
        !post.aiError &&
        !analyzingIds.has(post.id) &&
        !autoAttempted.current.has(post.id)
    );
    if (!next) return;
    autoAttempted.current.add(next.id);
    void runAiAnalysis(next);
  }, [aiConfigured, analyzingIds, posts, settings.autoAnalyzeCandidates, settingsLoaded]);

  return (
    <main>
      <header className="panel-header">
        <div>
          <p className="eyebrow">Reddit lead review</p>
          <h1>WedditNYC</h1>
          <p className="summary">
            {posts.length} detected · {strongCount} strong · {unreviewedCount} unreviewed · {aiCount} AI checked
          </p>
        </div>
        <div className="header-actions">
          <button className="secondary" onClick={() => void refresh()}>Refresh</button>
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
        <button
          className="ai-batch"
          disabled={!aiConfigured || batchRunning}
          onClick={() => void analyzeCandidates()}
        >
          {batchRunning ? 'Analyzing candidates…' : 'AI analyze new candidates'}
        </button>
      </section>

      <details className="ai-settings">
        <summary>DeepSeek semantic analysis</summary>
        <div className="settings-grid">
          <label className="toggle-field">
            <input
              type="checkbox"
              checked={settingsDraft.enabled}
              onChange={(event) =>
                setSettingsDraft((current) => ({ ...current, enabled: event.target.checked }))
              }
            />
            <span>Enable AI stage</span>
          </label>
          <label className="toggle-field">
            <input
              type="checkbox"
              checked={settingsDraft.autoAnalyzeCandidates}
              onChange={(event) =>
                setSettingsDraft((current) => ({
                  ...current,
                  autoAnalyzeCandidates: event.target.checked
                }))
              }
            />
            <span>Automatically analyze local Strong/Possible posts</span>
          </label>
          <label className="field">
            <span>Worker URL</span>
            <input
              type="url"
              placeholder="https://your-worker.workers.dev"
              value={settingsDraft.proxyUrl}
              onChange={(event) =>
                setSettingsDraft((current) => ({ ...current, proxyUrl: event.target.value }))
              }
            />
          </label>
          <label className="field">
            <span>Worker access key — not the DeepSeek API key</span>
            <input
              type="password"
              autoComplete="off"
              value={settingsDraft.accessKey}
              onChange={(event) =>
                setSettingsDraft((current) => ({ ...current, accessKey: event.target.value }))
              }
            />
          </label>
          <button className="primary" onClick={() => void saveSettingsFromUserGesture()}>
            Save AI settings
          </button>
          {settingsMessage && <p className="settings-message">{settingsMessage}</p>}
          <p className="privacy-note">
            The DeepSeek API key stays only in the Worker secret store. Post title and body are sent only when AI analysis runs.
          </p>
        </div>
      </details>

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
            const isAnalyzing = analyzingIds.has(post.id);
            return (
              <article key={post.id} data-label={label}>
                <div className="card-topline">
                  <span className="badge">{LABEL_NAMES[label]}</span>
                  <span className="decision">{post.ownerDecision}</span>
                </div>

                <h2>{post.title}</h2>
                <p className="reason"><strong>Local:</strong> {post.classification.reason}</p>

                {post.classification.matchedSignals.length > 0 && (
                  <div className="signals" aria-label="Matched signals">
                    {post.classification.matchedSignals.map((signal) => (
                      <span key={signal}>{signal}</span>
                    ))}
                  </div>
                )}

                {post.aiAnalysis && (
                  <section className="ai-result" data-risk={post.aiAnalysis.responseRisk}>
                    <div className="ai-result-title">
                      <strong>DeepSeek: {LABEL_NAMES[post.aiAnalysis.label]}</strong>
                      <span>{post.aiAnalysis.confidence}% confidence</span>
                    </div>
                    <p><strong>Intent:</strong> {post.aiAnalysis.customerIntent}</p>
                    <p><strong>Risk:</strong> {post.aiAnalysis.responseRisk}</p>
                    <p><strong>Reason:</strong> {post.aiAnalysis.reason}</p>
                    <p><strong>Action:</strong> {post.aiAnalysis.recommendedAction}</p>
                    <small>{post.aiAnalysis.model} · {new Date(post.aiAnalysis.analyzedAt).toLocaleString()}</small>
                  </section>
                )}

                {post.aiError && <p className="ai-error">AI error: {post.aiError}</p>}

                <label className="field">
                  <span>Final classification</span>
                  <select
                    value={label}
                    onChange={(event) =>
                      void setManualLabel(post.id, event.target.value as RelevanceLabel)
                    }
                  >
                    {LABELS.filter((value): value is RelevanceLabel => value !== 'all').map(
                      (value) => (
                        <option key={value} value={value}>{LABEL_NAMES[value]}</option>
                      )
                    )}
                  </select>
                </label>

                <div className="ai-actions">
                  <button
                    disabled={!aiConfigured || isAnalyzing}
                    onClick={() => void runAiAnalysis(post)}
                  >
                    {isAnalyzing ? 'Analyzing…' : post.aiAnalysis ? 'Reanalyze with AI' : 'Analyze with AI'}
                  </button>
                </div>

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