import { useEffect, useMemo, useState } from 'react';
import { browser } from 'wxt/browser';
import { enrichVideos, publicationFrequencyPerWeek, strongestHashtags, summarize } from '../../lib/analytics';
import { videosToCsv } from '../../lib/csv';
import {
  favoriteKey,
  groupFavoriteEntriesByChannel,
  orderedFavoriteEntries,
  selectFavoriteEntries,
} from '../../lib/favorites';
import { generateFavoritesHtml } from '../../lib/html-export';
import { formatCompactNumber } from '../../lib/numbers';
import { groupTopVideosPerAccount } from '../../lib/tag-research';
import { APP_VERSION } from '../../lib/types';
import type {
  ChannelSnapshot,
  DashboardData,
  EnrichedVideo,
  FavoriteEntry,
  ProfileSnapshot,
  RuntimeMessage,
  ScanOptions,
  TikTokPageContext,
  VideoRecord,
} from '../../lib/types';

type SortKey = 'views' | 'likes' | 'comments' | 'shares' | 'publishedAt' | 'viewsPerDay' | 'outlierScore' | 'engagementRate';
type ViewMode = 'profile' | 'tag' | 'favorites';

const emptyDashboard: DashboardData = {
  profiles: {},
  tagResearch: {},
  favorites: {},
  activeScan: { status: 'idle', videosFound: 0, updatedAt: Date.now() },
};

const defaultOptions: ScanOptions = {
  maxVideos: 300,
  maxIdleRounds: 5,
  scrollDelayMs: 1200,
  topVideosPerAccount: 1,
  minViews: 0,
};

function normalizeDashboard(value: Partial<DashboardData> | undefined): DashboardData {
  return {
    profiles: value?.profiles ?? {},
    tagResearch: value?.tagResearch ?? {},
    favorites: value?.favorites ?? {},
    activeScan: value?.activeScan ?? emptyDashboard.activeScan,
  };
}

async function activeTabId(): Promise<number | undefined> {
  const tabs = await browser.tabs.query({ active: true, currentWindow: true });
  return tabs[0]?.id;
}

async function connectToActiveTikTokTab(): Promise<{ tabId: number; context?: TikTokPageContext }> {
  const tabId = await activeTabId();
  if (!tabId) throw new Error('Активная вкладка не найдена.');

  try {
    const response = await browser.tabs.sendMessage(tabId, { type: 'PING' } satisfies RuntimeMessage) as { context?: TikTokPageContext };
    return { tabId, context: response?.context };
  } catch {
    await browser.scripting.executeScript({ target: { tabId }, files: ['/content-scripts/content.js'] });
    await new Promise((resolve) => setTimeout(resolve, 180));
    const response = await browser.tabs.sendMessage(tabId, { type: 'PING' } satisfies RuntimeMessage) as { context?: TikTokPageContext };
    return { tabId, context: response?.context };
  }
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

function formatDate(timestamp: number | undefined): string {
  if (!timestamp) return '—';
  return new Intl.DateTimeFormat('ru-RU', {
    day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit',
  }).format(new Date(timestamp));
}

function formatUnixDate(timestampSeconds: number | undefined): string {
  if (!timestampSeconds) return '—';
  return new Intl.DateTimeFormat('ru-RU', {
    day: '2-digit', month: 'short', year: 'numeric',
  }).format(new Date(timestampSeconds * 1000));
}

function formatOptionalNumber(value: number | undefined): string {
  return value === undefined ? '—' : formatCompactNumber(value);
}

function yesNo(value: boolean | undefined): string {
  return value === undefined ? '—' : value ? 'Да' : 'Нет';
}

function initials(profile: { displayName?: string; username: string }): string {
  const source = profile.displayName || profile.username;
  return source.split(/\s+/).filter(Boolean).slice(0, 2).map((part) => part[0]?.toUpperCase()).join('') || 'TT';
}

export default function App() {
  const [dashboard, setDashboard] = useState<DashboardData>(emptyDashboard);
  const [viewMode, setViewMode] = useState<ViewMode>('profile');
  const [pageContext, setPageContext] = useState<TikTokPageContext>();
  const [selectedProfile, setSelectedProfile] = useState('');
  const [selectedTag, setSelectedTag] = useState('');
  const [sortKey, setSortKey] = useState<SortKey>('outlierScore');
  const [query, setQuery] = useState('');
  const [minOutlier, setMinOutlier] = useState(0);
  const [maxVideos, setMaxVideos] = useState(defaultOptions.maxVideos);
  const [topVideosPerAccount, setTopVideosPerAccount] = useState(defaultOptions.topVideosPerAccount);
  const [minViews, setMinViews] = useState(defaultOptions.minViews);
  const [selectedFavoriteKeys, setSelectedFavoriteKeys] = useState<Set<string>>(new Set());
  const [error, setError] = useState('');

  const applyDashboard = (value: Partial<DashboardData> | undefined) => setDashboard(normalizeDashboard(value));

  const refresh = async () => {
    const data = await browser.runtime.sendMessage({ type: 'GET_DASHBOARD' } satisfies RuntimeMessage) as DashboardData;
    applyDashboard(data);
  };

  const detectPageContext = async () => {
    try {
      const connection = await connectToActiveTikTokTab();
      setPageContext(connection.context);
      if (connection.context?.kind === 'tag') setViewMode('tag');
      if (connection.context?.kind === 'profile') setViewMode('profile');
    } catch {
      setPageContext(undefined);
    }
  };

  const requestChannelEnrichment = async (username: string, surfaceError = false) => {
    try {
      const { tabId } = await connectToActiveTikTokTab();
      const result = await browser.tabs.sendMessage(tabId, {
        type: 'ENRICH_CHANNEL',
        username,
      } satisfies RuntimeMessage) as { ok?: boolean; message?: string };
      if (surfaceError && !result?.ok) setError(result?.message || `Не удалось получить данные канала @${username}.`);
      if (result?.ok) setError('');
    } catch (cause) {
      if (surfaceError) {
        const details = cause instanceof Error ? cause.message : String(cause);
        setError(`Откройте любую страницу TikTok и повторите обновление канала. ${details}`);
      }
    }
  };

  useEffect(() => {
    void refresh();
    void detectPageContext();
    const listener = (message: { type?: string; dashboard?: DashboardData }) => {
      if (message.type === 'DASHBOARD_UPDATED' && message.dashboard) applyDashboard(message.dashboard);
    };
    browser.runtime.onMessage.addListener(listener);
    return () => browser.runtime.onMessage.removeListener(listener);
  }, []);

  const usernames = Object.keys(dashboard.profiles).sort();
  const tags = Object.keys(dashboard.tagResearch).sort();
  const favoriteEntries = useMemo(() => orderedFavoriteEntries(dashboard.favorites), [dashboard.favorites]);
  const favoriteKeysSignature = favoriteEntries.map((entry) => entry.key).join('|');

  useEffect(() => {
    if (!selectedProfile && usernames[0]) setSelectedProfile(usernames[0]);
    if (dashboard.activeScan.username && dashboard.profiles[dashboard.activeScan.username]) {
      setSelectedProfile(dashboard.activeScan.username);
    }
  }, [dashboard.activeScan.username, usernames.join('|')]);

  useEffect(() => {
    if (!selectedTag && tags[0]) setSelectedTag(tags[0]);
    if (dashboard.activeScan.tag && dashboard.tagResearch[dashboard.activeScan.tag.toLowerCase()]) {
      setSelectedTag(dashboard.activeScan.tag.toLowerCase());
      setViewMode('tag');
    }
  }, [dashboard.activeScan.tag, tags.join('|')]);

  useEffect(() => {
    const available = new Set(favoriteEntries.map((entry) => entry.key));
    setSelectedFavoriteKeys((current) => new Set([...current].filter((key) => available.has(key))));
  }, [favoriteKeysSignature]);

  const profile = selectedProfile ? dashboard.profiles[selectedProfile] : undefined;
  const enriched = useMemo(() => enrichVideos(profile?.videos ?? []), [profile?.videos]);
  const visible = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    return enriched
      .filter((video) => !normalizedQuery || `${video.description} ${video.hashtags.join(' ')}`.toLowerCase().includes(normalizedQuery))
      .filter((video) => (video.outlierScore ?? 0) >= minOutlier)
      .sort((a, b) => Number(b[sortKey] ?? 0) - Number(a[sortKey] ?? 0));
  }, [enriched, minOutlier, query, sortKey]);
  const summary = useMemo(() => summarize(enriched), [enriched]);
  const frequency = useMemo(() => publicationFrequencyPerWeek(profile?.videos ?? []), [profile?.videos]);
  const topHashtags = useMemo(() => strongestHashtags(enriched), [enriched]);

  const tagSnapshot = selectedTag ? dashboard.tagResearch[selectedTag] : undefined;
  useEffect(() => {
    if (!tagSnapshot) return;
    setTopVideosPerAccount(tagSnapshot.topVideosPerAccount);
    setMinViews(tagSnapshot.minViews);
  }, [selectedTag]);

  const tagGroups = useMemo(
    () => groupTopVideosPerAccount(tagSnapshot?.videos ?? [], topVideosPerAccount, minViews),
    [tagSnapshot?.videos, topVideosPerAccount, minViews],
  );
  const selectedTagVideos = useMemo(() => tagGroups.flatMap((group) => group.videos), [tagGroups]);
  const enrichedTagVideos = useMemo(() => new Map(
    enrichVideos(selectedTagVideos).map((video) => [favoriteKey(video), video]),
  ), [selectedTagVideos]);
  const enrichedFavoriteVideos = useMemo(() => new Map(
    enrichVideos(favoriteEntries.map((entry) => entry.video)).map((video) => [favoriteKey(video), video]),
  ), [favoriteEntries]);

  const start = async () => {
    setError('');
    try {
      const { tabId, context } = await connectToActiveTikTokTab();
      setPageContext(context);
      if (!context) throw new Error('Откройте публичный профиль TikTok или страницу хэштега TikTok.');
      setViewMode(context.kind);
      await browser.tabs.sendMessage(tabId, {
        type: 'START_SCAN',
        options: { ...defaultOptions, maxVideos, topVideosPerAccount, minViews },
      } satisfies RuntimeMessage);
    } catch (cause) {
      const details = cause instanceof Error ? cause.message : String(cause);
      setError(`Не удалось подключиться к вкладке TikTok. ${details}`);
    }
  };

  const stop = async () => {
    const tabId = await activeTabId();
    if (tabId) await browser.tabs.sendMessage(tabId, { type: 'STOP_SCAN' } satisfies RuntimeMessage).catch(() => undefined);
  };

  const toggleFavorite = async (video: VideoRecord) => {
    const adding = !dashboard.favorites[favoriteKey(video)];
    const data = await browser.runtime.sendMessage({ type: 'TOGGLE_FAVORITE', video } satisfies RuntimeMessage) as DashboardData;
    applyDashboard(data);
    if (adding) void requestChannelEnrichment(video.author, false);
  };

  const clearProfileData = async () => {
    if (!selectedProfile) return;
    const data = await browser.runtime.sendMessage({ type: 'CLEAR_PROFILE', username: selectedProfile } satisfies RuntimeMessage) as DashboardData;
    applyDashboard(data);
    setSelectedProfile('');
  };

  const clearTagData = async () => {
    if (!selectedTag) return;
    const data = await browser.runtime.sendMessage({ type: 'CLEAR_TAG_RESEARCH', tag: selectedTag } satisfies RuntimeMessage) as DashboardData;
    applyDashboard(data);
    setSelectedTag('');
  };

  const removeSelectedFavorites = async () => {
    const keys = [...selectedFavoriteKeys];
    if (!keys.length) return;
    const data = await browser.runtime.sendMessage({ type: 'REMOVE_FAVORITES', keys } satisfies RuntimeMessage) as DashboardData;
    applyDashboard(data);
    setSelectedFavoriteKeys(new Set());
  };

  const exportProfileCsv = () => {
    if (!profile) return;
    downloadText(`${profile.username}-tiktok-analysis-v${APP_VERSION}.csv`, `\uFEFF${videosToCsv(visible)}`, 'text/csv;charset=utf-8');
  };

  const exportProfileJson = () => {
    if (!profile) return;
    downloadText(
      `${profile.username}-tiktok-analysis-v${APP_VERSION}.json`,
      JSON.stringify({ version: APP_VERSION, profile, videos: visible }, null, 2),
      'application/json',
    );
  };

  const exportTagCsv = () => {
    if (!tagSnapshot) return;
    const enrichedVideos = selectedTagVideos.map((video) =>
      enrichedTagVideos.get(favoriteKey(video)) ?? video as EnrichedVideo
    );
    downloadText(`${tagSnapshot.tag}-top-videos-v${APP_VERSION}.csv`, `\uFEFF${videosToCsv(enrichedVideos)}`, 'text/csv;charset=utf-8');
  };

  const exportTagJson = () => {
    if (!tagSnapshot) return;
    downloadText(
      `${tagSnapshot.tag}-top-videos-v${APP_VERSION}.json`,
      JSON.stringify({
        version: APP_VERSION,
        tag: tagSnapshot.tag,
        tagUrl: tagSnapshot.tagUrl,
        topVideosPerAccount,
        minViews,
        scannedVideos: tagSnapshot.scannedVideos,
        accountsFound: tagSnapshot.accountsFound,
        accounts: tagGroups,
      }, null, 2),
      'application/json',
    );
  };

  const exportSelectedFavoritesHtml = () => {
    const selected = selectFavoriteEntries(dashboard.favorites, selectedFavoriteKeys);
    if (!selected.length) return;
    downloadText(
      `tiktok-favorites-with-channels-v${APP_VERSION}.html`,
      generateFavoritesHtml(selected, { title: 'Отобранные TikTok-ролики и каналы' }),
      'text/html;charset=utf-8',
    );
  };

  const scanning = dashboard.activeScan.status === 'scanning';
  const detectedLabel = pageContext?.kind === 'tag'
    ? `Страница хэштега #${pageContext.tag}`
    : pageContext?.kind === 'profile'
      ? `Профиль @${pageContext.username}`
      : 'Откройте профиль или страницу хэштега TikTok';

  const isFavorite = (video: Pick<VideoRecord, 'author' | 'id'>) => Boolean(dashboard.favorites[favoriteKey(video)]);

  return (
    <main className="app-shell">
      <header className="hero">
        <div>
          <p className="eyebrow">LOCAL-FIRST RESEARCH TOOL · v{APP_VERSION}</p>
          <h1>TikTok Research Sorter</h1>
          <p className="subtitle">Сохраняет ролики вместе с полной публичной информацией о каналах и создаёт готовые HTML-подборки.</p>
        </div>
        <span className={`status status-${dashboard.activeScan.status}`}>{dashboard.activeScan.status}</span>
      </header>

      <section className="panel context-panel">
        <span>Текущая вкладка</span>
        <strong>{detectedLabel}</strong>
        <button onClick={() => void detectPageContext()}>Обновить</button>
      </section>

      <section className="mode-tabs mode-tabs-three">
        <button className={viewMode === 'profile' ? 'active' : ''} onClick={() => setViewMode('profile')}>Профили</button>
        <button className={viewMode === 'tag' ? 'active' : ''} onClick={() => setViewMode('tag')}>Хэштеги</button>
        <button className={viewMode === 'favorites' ? 'active' : ''} onClick={() => setViewMode('favorites')}>
          ★ Избранное <span className="tab-count">{favoriteEntries.length}</span>
        </button>
      </section>

      {viewMode !== 'favorites' && (
        <section className="panel scan-panel">
          <div className="control-row">
            <label>
              Сканировать роликов
              <select value={maxVideos} onChange={(event) => setMaxVideos(Number(event.target.value))}>
                {[50, 100, 300, 500, 1000].map((value) => <option key={value} value={value}>{value}</option>)}
              </select>
            </label>
            {viewMode === 'tag' && (
              <>
                <label>
                  Лучших с аккаунта
                  <select value={topVideosPerAccount} onChange={(event) => setTopVideosPerAccount(Number(event.target.value))}>
                    {[1, 2, 3, 5, 10].map((value) => <option key={value} value={value}>{value}</option>)}
                  </select>
                </label>
                <label>
                  Минимум просмотров
                  <input type="number" min="0" step="1000" value={minViews} onChange={(event) => setMinViews(Math.max(0, Number(event.target.value)))} />
                </label>
              </>
            )}
            <button className="primary" onClick={start} disabled={scanning}>
              {viewMode === 'tag' ? 'Сканировать хэштег' : 'Сканировать профиль'}
            </button>
            <button className="secondary" onClick={stop} disabled={!scanning}>Стоп</button>
          </div>
          <div className="progress-track"><div className="progress-fill" style={{ width: `${Math.min(100, (dashboard.activeScan.videosFound / maxVideos) * 100)}%` }} /></div>
          <p className="scan-message">{dashboard.activeScan.message ?? 'Откройте нужную страницу TikTok и запустите сканирование.'}</p>
          {viewMode === 'tag' && <p className="hint">Выбираются лучшие ролики каждого аккаунта среди роликов, найденных на открытой странице хэштега.</p>}
          {error && <p className="error">{error}</p>}
        </section>
      )}

      {viewMode === 'favorites' && error && <section className="panel error-panel">{error}</section>}

      {viewMode === 'profile' && (
        <ProfileResults
          profile={profile}
          summary={summary}
          frequency={frequency}
          topHashtags={topHashtags}
          usernames={usernames}
          selectedProfile={selectedProfile}
          setSelectedProfile={setSelectedProfile}
          sortKey={sortKey}
          setSortKey={setSortKey}
          query={query}
          setQuery={setQuery}
          minOutlier={minOutlier}
          setMinOutlier={setMinOutlier}
          visible={visible}
          enrichedCount={enriched.length}
          exportCsv={exportProfileCsv}
          exportJson={exportProfileJson}
          clear={clearProfileData}
          isFavorite={isFavorite}
          toggleFavorite={toggleFavorite}
        />
      )}

      {viewMode === 'tag' && (
        <TagResults
          tags={tags}
          selectedTag={selectedTag}
          setSelectedTag={setSelectedTag}
          snapshot={tagSnapshot}
          groups={tagGroups}
          enrichedVideos={enrichedTagVideos}
          selectedCount={selectedTagVideos.length}
          minViews={minViews}
          exportCsv={exportTagCsv}
          exportJson={exportTagJson}
          clear={clearTagData}
          isFavorite={isFavorite}
          toggleFavorite={toggleFavorite}
        />
      )}

      {viewMode === 'favorites' && (
        <FavoritesResults
          entries={favoriteEntries}
          enrichedVideos={enrichedFavoriteVideos}
          selectedKeys={selectedFavoriteKeys}
          setSelectedKeys={setSelectedFavoriteKeys}
          toggleFavorite={toggleFavorite}
          refreshChannel={(username) => requestChannelEnrichment(username, true)}
          removeSelected={removeSelectedFavorites}
          exportHtml={exportSelectedFavoritesHtml}
        />
      )}
    </main>
  );
}

function ProfileResults({
  profile,
  summary,
  frequency,
  topHashtags,
  usernames,
  selectedProfile,
  setSelectedProfile,
  sortKey,
  setSortKey,
  query,
  setQuery,
  minOutlier,
  setMinOutlier,
  visible,
  enrichedCount,
  exportCsv,
  exportJson,
  clear,
  isFavorite,
  toggleFavorite,
}: {
  profile?: ProfileSnapshot;
  summary: ReturnType<typeof summarize>;
  frequency: number | undefined;
  topHashtags: string[];
  usernames: string[];
  selectedProfile: string;
  setSelectedProfile: (value: string) => void;
  sortKey: SortKey;
  setSortKey: (value: SortKey) => void;
  query: string;
  setQuery: (value: string) => void;
  minOutlier: number;
  setMinOutlier: (value: number) => void;
  visible: EnrichedVideo[];
  enrichedCount: number;
  exportCsv: () => void;
  exportJson: () => void;
  clear: () => void;
  isFavorite: (video: Pick<VideoRecord, 'author' | 'id'>) => boolean;
  toggleFavorite: (video: VideoRecord) => Promise<void>;
}) {
  return (
    <>
      {profile && <ProfileCard profile={profile} summary={summary} frequency={frequency} topHashtags={topHashtags} />}

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
        <article><span>Собрано роликов</span><strong>{summary.count}</strong></article>
        <article><span>Медиана просмотров</span><strong>{formatCompactNumber(summary.medianViews)}</strong></article>
        <article><span>Средний ER</span><strong>{summary.averageEngagementRate.toFixed(2)}%</strong></article>
        <article><span>Макс. выброс</span><strong>{summary.maxOutlierScore.toFixed(1)}×</strong></article>
      </section>

      <section className="panel actions">
        <button onClick={exportCsv} disabled={!visible.length}>CSV</button>
        <button onClick={exportJson} disabled={!visible.length}>JSON</button>
        <button className="danger" onClick={clear} disabled={!profile}>Удалить профиль</button>
        <span>{visible.length} из {enrichedCount}</span>
      </section>

      <section className="video-list">
        {visible.map((video, index) => (
          <VideoCard
            key={favoriteKey(video)}
            video={video}
            rank={index + 1}
            showOutlier
            favorite={isFavorite(video)}
            onToggleFavorite={() => void toggleFavorite(video)}
          />
        ))}
        {!visible.length && <div className="empty">Пока нет собранных роликов.</div>}
      </section>
    </>
  );
}

function TagResults({
  tags,
  selectedTag,
  setSelectedTag,
  snapshot,
  groups,
  enrichedVideos,
  selectedCount,
  minViews,
  exportCsv,
  exportJson,
  clear,
  isFavorite,
  toggleFavorite,
}: {
  tags: string[];
  selectedTag: string;
  setSelectedTag: (value: string) => void;
  snapshot: DashboardData['tagResearch'][string] | undefined;
  groups: ReturnType<typeof groupTopVideosPerAccount>;
  enrichedVideos: Map<string, EnrichedVideo>;
  selectedCount: number;
  minViews: number;
  exportCsv: () => void;
  exportJson: () => void;
  clear: () => void;
  isFavorite: (video: Pick<VideoRecord, 'author' | 'id'>) => boolean;
  toggleFavorite: (video: VideoRecord) => Promise<void>;
}) {
  return (
    <>
      <section className="panel toolbar">
        <label>
          Хэштег
          <select value={selectedTag} onChange={(event) => setSelectedTag(event.target.value)}>
            <option value="">Нет данных</option>
            {tags.map((tag) => <option key={tag} value={tag}>#{tag}</option>)}
          </select>
        </label>
        {snapshot && <a className="source-link" href={snapshot.tagUrl} target="_blank" rel="noreferrer">Открыть #{snapshot.tag}</a>}
      </section>

      <section className="stats-grid">
        <article><span>Просканировано</span><strong>{snapshot?.scannedVideos ?? 0}</strong></article>
        <article><span>Аккаунтов</span><strong>{snapshot?.accountsFound ?? 0}</strong></article>
        <article><span>Выбрано роликов</span><strong>{selectedCount}</strong></article>
        <article><span>Минимум просмотров</span><strong>{formatCompactNumber(minViews)}</strong></article>
      </section>

      <section className="panel actions">
        <button onClick={exportCsv} disabled={!selectedCount}>CSV</button>
        <button onClick={exportJson} disabled={!selectedCount}>JSON</button>
        <button className="danger" onClick={clear} disabled={!snapshot}>Удалить хэштег</button>
        <span>{groups.length} аккаунтов</span>
      </section>

      <section className="account-groups">
        {groups.map((group) => (
          <section className="account-group" key={group.author}>
            <header>
              <a href={group.profileUrl} target="_blank" rel="noreferrer">@{group.author}</a>
              <span>{group.videos.length} лучших · максимум {formatCompactNumber(group.topViews)}</span>
            </header>
            <div className="video-list">
              {group.videos.map((video, index) => {
                const displayVideo = enrichedVideos.get(favoriteKey(video)) ?? video as EnrichedVideo;
                return (
                  <VideoCard
                    key={favoriteKey(video)}
                    video={displayVideo}
                    rank={index + 1}
                    showAuthor={false}
                    favorite={isFavorite(video)}
                    onToggleFavorite={() => void toggleFavorite(video)}
                  />
                );
              })}
            </div>
          </section>
        ))}
        {!groups.length && <div className="empty">Нет роликов, подходящих под выбранный минимум просмотров.</div>}
      </section>
    </>
  );
}

function FavoritesResults({
  entries,
  enrichedVideos,
  selectedKeys,
  setSelectedKeys,
  toggleFavorite,
  refreshChannel,
  removeSelected,
  exportHtml,
}: {
  entries: FavoriteEntry[];
  enrichedVideos: Map<string, EnrichedVideo>;
  selectedKeys: Set<string>;
  setSelectedKeys: (value: Set<string>) => void;
  toggleFavorite: (video: VideoRecord) => Promise<void>;
  refreshChannel: (username: string) => Promise<void>;
  removeSelected: () => Promise<void>;
  exportHtml: () => void;
}) {
  const groups = groupFavoriteEntriesByChannel(entries);
  const allSelected = entries.length > 0 && selectedKeys.size === entries.length;

  const toggleSelection = (key: string, checked: boolean) => {
    const next = new Set(selectedKeys);
    if (checked) next.add(key);
    else next.delete(key);
    setSelectedKeys(next);
  };

  return (
    <>
      <section className="panel favorites-intro">
        <div>
          <p className="eyebrow">ИЗБРАННОЕ</p>
          <h2>Отбор роликов и каналов для отправки</h2>
          <p>HTML-файл включает выбранные ролики и все публичные данные каналов, которые удалось получить от TikTok.</p>
        </div>
        <strong>{entries.length}</strong>
      </section>

      <section className="panel actions favorites-actions">
        <button onClick={() => setSelectedKeys(new Set(entries.map((entry) => entry.key)))} disabled={!entries.length || allSelected}>Выбрать все</button>
        <button onClick={() => setSelectedKeys(new Set())} disabled={!selectedKeys.size}>Снять выбор</button>
        <button className="primary" onClick={exportHtml} disabled={!selectedKeys.size}>Скачать HTML с каналами</button>
        <button className="danger" onClick={() => void removeSelected()} disabled={!selectedKeys.size}>Удалить выбранное</button>
        <span>Выбрано: {selectedKeys.size} · Каналов: {groups.length}</span>
      </section>

      <section className="favorite-channel-groups">
        {groups.map((group) => (
          <section className="favorite-channel-group" key={group.key}>
            <ChannelCard channel={group.channel} onRefresh={() => void refreshChannel(group.channel.username)} />
            <div className="video-list favorites-list">
              {group.entries.map((entry, index) => {
                const video = enrichedVideos.get(entry.key) ?? entry.video as EnrichedVideo;
                return (
                  <VideoCard
                    key={entry.key}
                    video={video}
                    rank={index + 1}
                    favorite
                    selected={selectedKeys.has(entry.key)}
                    onSelectedChange={(checked) => toggleSelection(entry.key, checked)}
                    onToggleFavorite={() => void toggleFavorite(entry.video)}
                    favoritedAt={entry.favoritedAt}
                  />
                );
              })}
            </div>
          </section>
        ))}
        {!entries.length && <div className="empty">Избранных роликов пока нет. Нажмите звёздочку на любой карточке.</div>}
      </section>
    </>
  );
}

function ChannelCard({ channel, onRefresh }: { channel: ChannelSnapshot; onRefresh: () => void }) {
  return (
    <section className="panel channel-card">
      <div className="channel-head">
        <a className="channel-avatar" href={channel.profileUrl} target="_blank" rel="noreferrer">
          {channel.avatarUrl ? <img src={channel.avatarUrl} alt="" /> : <span>{initials(channel)}</span>}
        </a>
        <div className="channel-identity">
          <div className="channel-title-row">
            <h2>{channel.displayName || `@${channel.username}`}</h2>
            {channel.verified && <span className="verified" title="Проверенный аккаунт">✓</span>}
            <span className={`channel-completeness ${channel.completeness}`}>{channel.completeness === 'full' ? 'полные данные' : 'частичные данные'}</span>
          </div>
          <a href={channel.profileUrl} target="_blank" rel="noreferrer">@{channel.username}</a>
          {channel.bio && <p>{channel.bio}</p>}
          <div className="channel-links">
            <a href={channel.profileUrl} target="_blank" rel="noreferrer">Профиль TikTok ↗</a>
            {channel.website && <a href={channel.website} target="_blank" rel="noreferrer">Сайт ↗</a>}
          </div>
        </div>
        <button className="secondary channel-refresh" onClick={onRefresh}>Обновить канал</button>
      </div>

      <div className="channel-stats">
        <article><span>Подписчики</span><strong>{formatOptionalNumber(channel.followers)}</strong></article>
        <article><span>Подписки</span><strong>{formatOptionalNumber(channel.following)}</strong></article>
        <article><span>Друзья</span><strong>{formatOptionalNumber(channel.friends)}</strong></article>
        <article><span>Лайки профиля</span><strong>{formatOptionalNumber(channel.totalLikes)}</strong></article>
        <article><span>Видео в профиле</span><strong>{formatOptionalNumber(channel.videoCount)}</strong></article>
        <article><span>Собрано видео</span><strong>{formatCompactNumber(channel.collectedVideoCount)}</strong></article>
        <article><span>Медиана просмотров</span><strong>{formatCompactNumber(channel.medianViews)}</strong></article>
        <article><span>Средний ER</span><strong>{percent(channel.averageEngagementRate)}</strong></article>
      </div>

      <div className="channel-details">
        <div><span>User ID</span><strong>{channel.userId || '—'}</strong></div>
        <div><span>secUid</span><strong>{channel.secUid || '—'}</strong></div>
        <div><span>Регион</span><strong>{channel.region || '—'}</strong></div>
        <div><span>Язык</span><strong>{channel.language || '—'}</strong></div>
        <div><span>Создан</span><strong>{formatUnixDate(channel.accountCreatedAt)}</strong></div>
        <div><span>Закрытый аккаунт</span><strong>{yesNo(channel.privateAccount)}</strong></div>
        <div><span>Коммерческий</span><strong>{yesNo(channel.commerceAccount)}</strong></div>
        <div><span>Источник</span><strong>{channel.profileDataSource || '—'}</strong></div>
        <div><span>Обновлено</span><strong>{formatDate(channel.profileDataUpdatedAt || channel.capturedAt)}</strong></div>
      </div>

      <div className="profile-topics">
        <span>Сильные темы канала</span>
        <div>
          {channel.strongestHashtags.map((tag) => <span key={tag}>#{tag}</span>)}
          {!channel.strongestHashtags.length && <em>Появятся после сбора роликов канала.</em>}
        </div>
      </div>
    </section>
  );
}

function ProfileCard({
  profile,
  summary,
  frequency,
  topHashtags,
}: {
  profile: ProfileSnapshot;
  summary: ReturnType<typeof summarize>;
  frequency: number | undefined;
  topHashtags: string[];
}) {
  const coverage = profile.videoCount
    ? `${profile.videos.length} из ${formatCompactNumber(profile.videoCount)}`
    : String(profile.videos.length);

  return (
    <section className="panel profile-card">
      <div className="profile-head">
        <a className="profile-avatar" href={profile.profileUrl} target="_blank" rel="noreferrer">
          {profile.avatarUrl ? <img src={profile.avatarUrl} alt="" /> : <span>{initials(profile)}</span>}
        </a>
        <div className="profile-identity">
          <div className="profile-name-row">
            <h2>{profile.displayName || `@${profile.username}`}</h2>
            {profile.verified && <span className="verified" title="Проверенный аккаунт">✓</span>}
          </div>
          <a href={profile.profileUrl} target="_blank" rel="noreferrer">@{profile.username}</a>
          {profile.bio && <p>{profile.bio}</p>}
          {profile.website && <a className="profile-site" href={profile.website} target="_blank" rel="noreferrer">Сайт профиля ↗</a>}
        </div>
      </div>

      <div className="profile-stats profile-stats-wide">
        <article><span>Подписчики</span><strong>{formatOptionalNumber(profile.followers)}</strong></article>
        <article><span>Подписки</span><strong>{formatOptionalNumber(profile.following)}</strong></article>
        <article><span>Друзья</span><strong>{formatOptionalNumber(profile.friends)}</strong></article>
        <article><span>Лайки профиля</span><strong>{formatOptionalNumber(profile.totalLikes)}</strong></article>
        <article><span>Видео в профиле</span><strong>{formatOptionalNumber(profile.videoCount)}</strong></article>
        <article><span>Собрано видео</span><strong>{formatCompactNumber(profile.videos.length)}</strong></article>
        <article><span>Медиана просмотров</span><strong>{formatCompactNumber(profile.medianViews)}</strong></article>
        <article><span>Средний ER</span><strong>{summary.averageEngagementRate.toFixed(2)}%</strong></article>
      </div>

      <div className="profile-details">
        <div><span>User ID</span><strong>{profile.userId || '—'}</strong></div>
        <div><span>secUid</span><strong>{profile.secUid || '—'}</strong></div>
        <div><span>Регион</span><strong>{profile.region || '—'}</strong></div>
        <div><span>Язык</span><strong>{profile.language || '—'}</strong></div>
        <div><span>Создан</span><strong>{formatUnixDate(profile.accountCreatedAt)}</strong></div>
        <div><span>Закрытый аккаунт</span><strong>{yesNo(profile.privateAccount)}</strong></div>
        <div><span>Коммерческий</span><strong>{yesNo(profile.commerceAccount)}</strong></div>
        <div><span>Источник</span><strong>{profile.profileDataSource || '—'}</strong></div>
      </div>

      <div className="profile-insights">
        <div><span>Последнее сканирование</span><strong>{formatDate(profile.lastScannedAt)}</strong></div>
        <div><span>Обновление профиля</span><strong>{formatDate(profile.profileDataUpdatedAt)}</strong></div>
        <div><span>Покрытие</span><strong>{coverage}</strong></div>
        <div><span>Частота публикаций</span><strong>{frequency === undefined ? '—' : `${frequency.toFixed(1)} в неделю`}</strong></div>
      </div>

      <div className="profile-topics">
        <span>Сильные темы</span>
        <div>
          {topHashtags.map((tag) => <span key={tag}>#{tag}</span>)}
          {!topHashtags.length && <em>Появятся после сбора описаний и хештегов.</em>}
        </div>
      </div>
    </section>
  );
}

function VideoCard({
  video,
  rank,
  showOutlier = false,
  showAuthor = true,
  favorite = false,
  selected,
  onSelectedChange,
  onToggleFavorite,
  favoritedAt,
}: {
  video: EnrichedVideo;
  rank: number;
  showOutlier?: boolean;
  showAuthor?: boolean;
  favorite?: boolean;
  selected?: boolean;
  onSelectedChange?: (checked: boolean) => void;
  onToggleFavorite?: () => void;
  favoritedAt?: number;
}) {
  return (
    <article className={`video-card${selected ? ' selected' : ''}`}>
      <div className="card-controls">
        {onSelectedChange && (
          <label className="select-control" title="Выбрать для HTML">
            <input type="checkbox" checked={Boolean(selected)} onChange={(event) => onSelectedChange(event.target.checked)} />
            <span>Выбрать</span>
          </label>
        )}
        {onToggleFavorite && (
          <button
            className={`favorite-star${favorite ? ' active' : ''}`}
            onClick={onToggleFavorite}
            title={favorite ? 'Удалить из избранного' : 'Добавить в избранное'}
            aria-label={favorite ? 'Удалить из избранного' : 'Добавить в избранное'}
          >
            {favorite ? '★' : '☆'}
          </button>
        )}
      </div>
      <a className="cover" href={video.videoUrl} target="_blank" rel="noreferrer">
        {video.coverUrl ? <img src={video.coverUrl} alt="" /> : <div className="cover-placeholder">#{rank}</div>}
        <span className="rank">#{rank}</span>
      </a>
      <div className="video-copy">
        {showAuthor && <a className="video-author" href={video.profileUrl} target="_blank" rel="noreferrer">@{video.author}</a>}
        <div className="metrics">
          <strong>{formatCompactNumber(video.views)} views</strong>
          {showOutlier && <span>{video.outlierScore?.toFixed(1) ?? '—'}× outlier</span>}
          {video.viewsPerDay !== undefined && <span>{formatCompactNumber(video.viewsPerDay)}/day</span>}
        </div>
        <p>{video.description || 'Без описания'}</p>
        <div className="micro-metrics">
          <span>♥ {formatCompactNumber(video.likes)}</span>
          <span>💬 {formatCompactNumber(video.comments)}</span>
          <span>↗ {formatCompactNumber(video.shares)}</span>
          <span>ER {percent(video.engagementRate)}</span>
        </div>
        <div className="hashtags">{video.hashtags.slice(0, 6).map((tag) => <span key={tag}>#{tag}</span>)}</div>
        {favoritedAt && <div className="favorite-date">Добавлено: {formatDate(favoritedAt)}</div>}
      </div>
    </article>
  );
}
