import { useEffect, useMemo, useState } from 'react';
import { browser } from 'wxt/browser';
import { enrichVideos, summarize } from '../../lib/analytics';
import { videosToCsv } from '../../lib/csv';
import { formatCompactNumber } from '../../lib/numbers';
import type { DashboardData, EnrichedVideo, RuntimeMessage, ScanOptions } from '../../lib/types';

type SortKey = 'views' | 'likes' | 'comments' | 'shares' | 'publishedAt' | 'viewsPerDay' | 'outlierScore' | 'engagementRate';

const emptyDashboard: DashboardData = {
  profiles: {},
  activeScan: { status: 'idle', videosFound: 0, updatedAt: Date.now() },
};

const defaultOptions: ScanOptions = {
  maxVideos: 300,
  maxIdleRounds: 5,
  scrollDelayMs: 1200,
};

async function activeTabId(): Promise<number | undefined> {
  const tabs = await browser.tabs.query({ active: true, currentWindow: true });
  return tabs[0]?.id;
}

function downloadText(filename: string, content: string, type: string): void {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  URL.revokeObjectURL(url);
}

function percent(value: number | undefined): string {
  return value === undefined ? '—' : `${value.toFixed(2)}%`;
}

export default function App() {
  const [dashboard, setDashboard] = useState<DashboardData>(emptyDashboard);
  const [selectedProfile, setSelectedProfile] = useState('');
  const [sortKey, setSortKey] = useState<SortKey>('outlierScore');
  const [query, setQuery] = useState('');
  const [minOutlier, setMinOutlier] = useState(0);
  const [maxVideos, setMaxVideos] = useState(defaultOptions.maxVideos);
  const [error, setError] = useState('');

  const refresh = async () => {
    const data = await browser.runtime.sendMessage({ type: 'GET_DASHBOARD' } satisfies RuntimeMessage) as DashboardData;
    setDashboard(data ?? emptyDashboard);
  };

  useEffect(() => {
    void refresh();
    const listener = (message: { type?: string; dashboard?: DashboardData }) => {
      if (message.type === 'DASHBOARD_UPDATED' && message.dashboard) setDashboard(message.dashboard);
    };
    browser.runtime.onMessage.addListener(listener);
    return () => browser.runtime.onMessage.removeListener(listener);
  }, []);

  const usernames = Object.keys(dashboard.profiles).sort();
  useEffect(() => {
    if (!selectedProfile && usernames[0]) setSelectedProfile(usernames[0]);
    if (dashboard.activeScan.username && dashboard.profiles[dashboard.activeScan.username]) {
      setSelectedProfile(dashboard.activeScan.username);
    }
  }, [dashboard.activeScan.username, usernames.join('|')]);

  const profile = selectedProfile ? dashboard.profiles[selectedProfile] : undefined;
  const enriched = useMemo(() => enrichVideos(profile?.videos ?? []), [profile?.videos]);
  const visible = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    return enriched
      .filter((video) => !normalizedQuery || `${video.description} ${video.hashtags.join(' ')}`.toLowerCase().includes(normalizedQuery))
      .filter((video) => (video.outlierScore ?? 0) >= minOutlier)
      .sort((a, b) => (Number(b[sortKey] ?? 0) - Number(a[sortKey] ?? 0)));
  }, [enriched, minOutlier, query, sortKey]);
  const summary = useMemo(() => summarize(enriched), [enriched]);

  const start = async () => {
    setError('');
    const tabId = await activeTabId();
    if (!tabId) return setError('Активная вкладка не найдена.');
    try {
      await browser.tabs.sendMessage(tabId, {
        type: 'START_SCAN',
        options: { ...defaultOptions, maxVideos },
      } satisfies RuntimeMessage);
    } catch {
      setError('Откройте публичный профиль TikTok и перезагрузите страницу.');
    }
  };

  const stop = async () => {
    const tabId = await activeTabId();
    if (tabId) await browser.tabs.sendMessage(tabId, { type: 'STOP_SCAN' } satisfies RuntimeMessage).catch(() => undefined);
  };

  const clear = async () => {
    if (!selectedProfile) return;
    const data = await browser.runtime.sendMessage({ type: 'CLEAR_PROFILE', username: selectedProfile } satisfies RuntimeMessage) as DashboardData;
    setDashboard(data);
    setSelectedProfile('');
  };

  const exportCsv = () => {
    if (!profile) return;
    downloadText(`${profile.username}-tiktok-analysis.csv`, `\uFEFF${videosToCsv(visible)}`, 'text/csv;charset=utf-8');
  };

  const exportJson = () => {
    if (!profile) return;
    downloadText(`${profile.username}-tiktok-analysis.json`, JSON.stringify(visible, null, 2), 'application/json');
  };

  return (
    <main className="app-shell">
      <header className="hero">
        <div>
          <p className="eyebrow">LOCAL-FIRST RESEARCH TOOL</p>
          <h1>TikTok Research Sorter</h1>
          <p className="subtitle">Находит сильнейшие ролики профиля и считает вирусные выбросы.</p>
        </div>
        <span className={`status status-${dashboard.activeScan.status}`}>{dashboard.activeScan.status}</span>
      </header>

      <section className="panel scan-panel">
        <div className="control-row">
          <label>
            Лимит роликов
            <select value={maxVideos} onChange={(event) => setMaxVideos(Number(event.target.value))}>
              {[50, 100, 300, 500, 1000].map((value) => <option key={value} value={value}>{value}</option>)}
            </select>
          </label>
          <button className="primary" onClick={start} disabled={dashboard.activeScan.status === 'scanning'}>Сканировать профиль</button>
          <button className="secondary" onClick={stop} disabled={dashboard.activeScan.status !== 'scanning'}>Стоп</button>
        </div>
        <div className="progress-track"><div className="progress-fill" style={{ width: `${Math.min(100, (dashboard.activeScan.videosFound / maxVideos) * 100)}%` }} /></div>
        <p className="scan-message">{dashboard.activeScan.message ?? 'Откройте профиль TikTok и нажмите «Сканировать профиль».'}</p>
        {error && <p className="error">{error}</p>}
      </section>

      <section className="panel toolbar">
        <label>
          Профиль
          <select value={selectedProfile} onChange={(event) => setSelectedProfile(event.target.value)}>
            <option value="">Нет данных</option>
            {usernames.map((username) => <option key={username} value={username}>@{username}</option>)}
          </select>
        </label>
        <label>
          Сортировка
          <select value={sortKey} onChange={(event) => setSortKey(event.target.value as SortKey)}>
            <option value="outlierScore">Outlier Score</option>
            <option value="views">Просмотры</option>
            <option value="viewsPerDay">Просмотры в день</option>
            <option value="engagementRate">Engagement Rate</option>
            <option value="likes">Лайки</option>
            <option value="comments">Комментарии</option>
            <option value="shares">Репосты</option>
            <option value="publishedAt">Дата</option>
          </select>
        </label>
        <label>
          Поиск
          <input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="слово или #хештег" />
        </label>
        <label>
          Outlier от
          <input type="number" min="0" step="0.5" value={minOutlier} onChange={(event) => setMinOutlier(Number(event.target.value))} />
        </label>
      </section>

      <section className="stats-grid">
        <article><span>Роликов</span><strong>{summary.count}</strong></article>
        <article><span>Медиана просмотров</span><strong>{formatCompactNumber(summary.medianViews)}</strong></article>
        <article><span>Средний ER</span><strong>{summary.averageEngagementRate.toFixed(2)}%</strong></article>
        <article><span>Макс. выброс</span><strong>{summary.maxOutlierScore.toFixed(1)}×</strong></article>
      </section>

      <section className="panel actions">
        <button onClick={exportCsv} disabled={!visible.length}>CSV</button>
        <button onClick={exportJson} disabled={!visible.length}>JSON</button>
        <button className="danger" onClick={clear} disabled={!profile}>Удалить профиль</button>
        <span>{visible.length} из {enriched.length}</span>
      </section>

      <section className="video-list">
        {visible.map((video, index) => <VideoCard key={video.id} video={video} rank={index + 1} />)}
        {!visible.length && <div className="empty">Пока нет собранных роликов.</div>}
      </section>
    </main>
  );
}

function VideoCard({ video, rank }: { video: EnrichedVideo; rank: number }) {
  return (
    <article className="video-card">
      <a className="cover" href={video.videoUrl} target="_blank" rel="noreferrer">
        {video.coverUrl ? <img src={video.coverUrl} alt="" /> : <div className="cover-placeholder">#{rank}</div>}
        <span className="rank">#{rank}</span>
      </a>
      <div className="video-copy">
        <div className="metrics">
          <strong>{formatCompactNumber(video.views)} views</strong>
          <span>{video.outlierScore?.toFixed(1) ?? '—'}× outlier</span>
          <span>{formatCompactNumber(video.viewsPerDay ?? 0)}/day</span>
        </div>
        <p>{video.description || 'Без описания'}</p>
        <div className="micro-metrics">
          <span>♥ {formatCompactNumber(video.likes)}</span>
          <span>💬 {formatCompactNumber(video.comments)}</span>
          <span>↗ {formatCompactNumber(video.shares)}</span>
          <span>ER {percent(video.engagementRate)}</span>
        </div>
        <div className="hashtags">{video.hashtags.slice(0, 6).map((tag) => <span key={tag}>#{tag}</span>)}</div>
      </div>
    </article>
  );
}
