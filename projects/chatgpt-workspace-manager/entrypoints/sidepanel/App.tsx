import { browser } from '#imports';
import { useEffect, useMemo, useState } from 'react';
import {
  DB_SCHEMA_VERSION,
  db,
  getConversationMessages,
  getSetting,
  getWorkspaceConversations,
  latestCapabilities,
  recordCapabilities,
  replaceConversationMessages,
  setSetting,
  updateOwnerMetadata,
  upsertConversationMetadata
} from '../../src/core/db';
import type {
  CanonicalMessage,
  CapabilityHealth,
  DiagnosticsReport,
  SyncSummary,
  WorkspaceConversation
} from '../../src/core/models';
import { chatGPTAdapter } from '../../src/providers/chatgpt/adapter';
import BackupControls from './BackupControls';

const VERSION = browser.runtime.getManifest().version;

type Tab = 'workspace' | 'health';

export default function App() {
  const [tab, setTab] = useState<Tab>('workspace');
  const [query, setQuery] = useState('');
  const [conversations, setConversations] = useState<WorkspaceConversation[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [messages, setMessages] = useState<CanonicalMessage[]>([]);
  const [noteDraft, setNoteDraft] = useState('');
  const [capabilities, setCapabilities] = useState<CapabilityHealth[]>([]);
  const [syncing, setSyncing] = useState(false);
  const [hydrating, setHydrating] = useState(false);
  const [offlineMode, setOfflineMode] = useState(false);
  const [status, setStatus] = useState('Cached workspace ready');
  const [error, setError] = useState<string | null>(null);

  const selected = useMemo(
    () => conversations.find((conversation) => conversation.id === selectedId) ?? null,
    [conversations, selectedId]
  );

  useEffect(() => {
    void initialize();
  }, []);

  useEffect(() => {
    void loadWorkspace(query);
  }, [query]);

  async function initialize() {
    try {
      await db.open();
      const savedOfflineMode = (await getSetting<boolean>('offlineMode')) ?? false;
      setOfflineMode(savedOfflineMode);
      await loadWorkspace('');
      await runHealth(false, savedOfflineMode);
    } catch (cause) {
      setError(readableError(cause));
    }
  }

  async function loadWorkspace(search: string) {
    try {
      const items = await getWorkspaceConversations(search);
      setConversations(items);
    } catch (cause) {
      setError(readableError(cause));
    }
  }

  async function syncMetadata() {
    if (offlineMode) {
      setError(null);
      setStatus('Offline test mode — cached workspace preserved; live sync intentionally blocked');
      await recordCapabilities([
        {
          capability: 'list-conversations',
          status: 'unavailable',
          strategy: 'local',
          checkedAt: Date.now(),
          message: 'Intentionally blocked by Offline test mode.',
          diagnosticCode: 'OFFLINE_TEST_MODE'
        }
      ]);
      setCapabilities(await latestCapabilities());
      return;
    }

    setSyncing(true);
    setError(null);
    setStatus('Syncing ChatGPT metadata…');
    try {
      const result = await chatGPTAdapter.listConversations();
      const upserted = await upsertConversationMetadata(result.conversations);
      const summary: SyncSummary = {
        syncedAt: Date.now(),
        received: result.total ?? result.conversations.length,
        upserted
      };
      await setSetting('lastSync', summary);
      await loadWorkspace(query);
      setStatus(`Synced ${upserted} conversations`);
      await runHealth(false);
      await recordCapabilities([
        {
          capability: 'list-conversations',
          status: 'healthy',
          strategy: 'live-api',
          checkedAt: Date.now(),
          message: `Validated by successful metadata sync (${upserted} conversations).`
        }
      ]);
      setCapabilities(await latestCapabilities());
    } catch (cause) {
      setError(readableError(cause));
      setStatus('Live sync unavailable — cached workspace preserved');
      await runHealth(false);
      await recordCapabilities([
        {
          capability: 'list-conversations',
          status: 'unavailable',
          strategy: 'live-api',
          checkedAt: Date.now(),
          message: readableError(cause),
          diagnosticCode: errorCode(cause)
        }
      ]);
      setCapabilities(await latestCapabilities());
    } finally {
      setSyncing(false);
    }
  }

  async function selectConversation(conversation: WorkspaceConversation) {
    setSelectedId(conversation.id);
    setNoteDraft(conversation.owner.note ?? '');
    setError(null);
    setMessages([]);

    const cached = await getConversationMessages(conversation.id);
    if (cached.length > 0) {
      setMessages(cached);
      setStatus(offlineMode ? 'Offline test: preview loaded from local cache' : 'Preview loaded from local cache');
      return;
    }

    if (offlineMode) {
      setStatus('Offline test: selected conversation has no local message cache');
      setError('Live hydration is intentionally disabled while Offline test mode is on.');
      return;
    }

    setHydrating(true);
    setStatus('Hydrating selected conversation…');
    try {
      const detail = await chatGPTAdapter.readConversation(conversation.id);
      const { owner: _owner, ...providerConversation } = conversation;
      await db.conversations.put({
        ...providerConversation,
        ...detail.conversation,
        contentHydrated: true,
        lastHydratedAt: Date.now()
      });
      await replaceConversationMessages(conversation.id, detail.messages);
      setMessages(detail.messages);
      await loadWorkspace(query);
      setStatus(`Hydrated ${detail.messages.length} messages`);
      await recordCapabilities([
        {
          capability: 'read-conversation',
          status: 'healthy',
          strategy: 'live-api',
          checkedAt: Date.now(),
          message: 'Validated by successful on-demand preview.'
        }
      ]);
      setCapabilities(await latestCapabilities());
    } catch (cause) {
      setError(readableError(cause));
      setStatus('Preview unavailable — local metadata remains available');
      await recordCapabilities([
        {
          capability: 'read-conversation',
          status: 'unavailable',
          strategy: 'live-api',
          checkedAt: Date.now(),
          message: readableError(cause),
          diagnosticCode: errorCode(cause)
        }
      ]);
      setCapabilities(await latestCapabilities());
    } finally {
      setHydrating(false);
    }
  }

  async function toggleFavorite(conversation: WorkspaceConversation) {
    await updateOwnerMetadata(conversation.id, { favorite: !conversation.owner.favorite });
    await loadWorkspace(query);
  }

  async function saveNote() {
    if (!selected) return;
    await updateOwnerMetadata(selected.id, { note: noteDraft.trim() });
    await loadWorkspace(query);
    setStatus('Note saved locally');
  }

  async function toggleOfflineMode() {
    const next = !offlineMode;
    setOfflineMode(next);
    await setSetting('offlineMode', next);
    setError(null);
    setStatus(
      next
        ? 'Offline test mode enabled — live ChatGPT access blocked by the extension'
        : 'Offline test mode disabled — live ChatGPT access restored'
    );
    await runHealth(false, next);
  }

  async function runHealth(switchTab = false, forceOffline = offlineMode) {
    const checkedAt = Date.now();
    const local: CapabilityHealth[] = [];
    try {
      await db.open();
      await db.conversations.limit(1).toArray();
      local.push({ capability: 'local-db', status: 'healthy', strategy: 'local', checkedAt });
      local.push({ capability: 'local-search', status: 'healthy', strategy: 'local', checkedAt });
    } catch (cause) {
      local.push({
        capability: 'local-db',
        status: 'unavailable',
        strategy: 'local',
        checkedAt,
        message: readableError(cause),
        diagnosticCode: 'LOCAL_DB_FAILURE'
      });
      local.push({ capability: 'local-search', status: 'unavailable', strategy: 'local', checkedAt });
    }

    const remote: CapabilityHealth[] = forceOffline
      ? [
          {
            capability: 'chatgpt-tab',
            status: 'unknown',
            strategy: 'local',
            checkedAt,
            message: 'Skipped by Offline test mode.',
            diagnosticCode: 'OFFLINE_TEST_MODE'
          },
          {
            capability: 'session',
            status: 'unavailable',
            strategy: 'local',
            checkedAt,
            message: 'Intentionally blocked by Offline test mode.',
            diagnosticCode: 'OFFLINE_TEST_MODE'
          },
          {
            capability: 'list-conversations',
            status: 'unavailable',
            strategy: 'local',
            checkedAt,
            message: 'Intentionally blocked by Offline test mode.',
            diagnosticCode: 'OFFLINE_TEST_MODE'
          },
          {
            capability: 'read-conversation',
            status: 'unavailable',
            strategy: 'local',
            checkedAt,
            message: 'Live reads blocked; cached previews remain available.',
            diagnosticCode: 'OFFLINE_TEST_MODE'
          }
        ]
      : await chatGPTAdapter.health();

    const merged = [...local, ...remote];
    await recordCapabilities(merged);
    const latest = await latestCapabilities();
    setCapabilities(latest);
    if (switchTab) setTab('health');
  }

  async function exportDiagnostics() {
    const latest = await latestCapabilities();
    const syncSummary = await getSetting<SyncSummary>('lastSync');
    const report: DiagnosticsReport = {
      exportedAt: new Date().toISOString(),
      extensionVersion: VERSION,
      dbSchemaVersion: DB_SCHEMA_VERSION,
      adapterVersion: chatGPTAdapter.version,
      capabilities: latest.map(({ id: _id, ...item }) => item),
      syncSummary,
      browser: {
        userAgent: navigator.userAgent,
        platform: navigator.platform
      }
    };

    const blob = new Blob([JSON.stringify(report, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = `chatgpt-workspace-manager-diagnostics-${Date.now()}.json`;
    anchor.click();
    window.setTimeout(() => URL.revokeObjectURL(url), 1_000);
  }

  return (
    <main className="app-shell">
      <header className="topbar">
        <div>
          <div className="eyebrow">PRIVATE OPERATOR TOOL</div>
          <h1>ChatGPT Workspace</h1>
        </div>
        <div className="header-status">
          <span className="version">v{VERSION}</span>
          <span className={`status-dot ${healthClass(overallHealth(capabilities))}`} />
        </div>
      </header>

      <nav className="tabs">
        <button className={tab === 'workspace' ? 'active' : ''} onClick={() => setTab('workspace')}>
          Workspace
        </button>
        <button className={tab === 'health' ? 'active' : ''} onClick={() => void runHealth(true)}>
          Health
        </button>
      </nav>

      <div className="status-line">
        <span>{status}</span>
        {error && <span className="error-text">{error}</span>}
      </div>

      {tab === 'workspace' ? (
        <section className="workspace-view">
          <div className="toolbar">
            <input
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Search local titles…"
              aria-label="Search conversations"
            />
            <button className="primary" disabled={syncing || offlineMode} onClick={() => void syncMetadata()}>
              {offlineMode ? 'Offline' : syncing ? 'Syncing…' : 'Sync'}
            </button>
          </div>

          <div className="summary-row">
            <span>{conversations.length} local conversations</span>
            <span>{offlineMode ? 'OFFLINE TEST' : `DB v${DB_SCHEMA_VERSION}`}</span>
          </div>

          <div className="workspace-grid">
            <div className="conversation-list" aria-label="Conversation list">
              {conversations.length === 0 ? (
                <div className="empty-state">No cached conversations yet. Open ChatGPT and press Sync.</div>
              ) : (
                conversations.map((conversation) => (
                  <button
                    key={conversation.id}
                    className={`conversation-card ${conversation.id === selectedId ? 'selected' : ''}`}
                    onClick={() => void selectConversation(conversation)}
                  >
                    <div className="conversation-title-row">
                      <span className="conversation-title">{conversation.title}</span>
                      <span
                        className={`favorite ${conversation.owner.favorite ? 'on' : ''}`}
                        role="button"
                        tabIndex={0}
                        title="Toggle favorite"
                        onClick={(event) => {
                          event.stopPropagation();
                          void toggleFavorite(conversation);
                        }}
                      >
                        ★
                      </span>
                    </div>
                    <div className="conversation-meta">
                      <span>{formatTime(conversation.updatedAt)}</span>
                      {conversation.archived && <span className="chip">Archived</span>}
                      {conversation.nativeProjectId && <span className="chip">Context</span>}
                      {conversation.owner.note && <span className="chip accent">Note</span>}
                    </div>
                  </button>
                ))
              )}
            </div>

            <div className="preview-panel">
              {!selected ? (
                <div className="empty-state">Select a conversation to preview it on demand.</div>
              ) : (
                <>
                  <div className="preview-header">
                    <div>
                      <div className="eyebrow">SELECTED</div>
                      <h2>{selected.title}</h2>
                    </div>
                    <button
                      className={`icon-button ${selected.owner.favorite ? 'favorite-on' : ''}`}
                      title="Toggle favorite"
                      onClick={() => void toggleFavorite(selected)}
                    >
                      ★
                    </button>
                  </div>

                  <div className="note-box">
                    <label htmlFor="conversation-note">Local note</label>
                    <textarea
                      id="conversation-note"
                      value={noteDraft}
                      onChange={(event) => setNoteDraft(event.target.value)}
                      placeholder="Private note stored only in the extension database…"
                    />
                    <button onClick={() => void saveNote()}>Save note</button>
                  </div>

                  <div className="messages">
                    {hydrating ? (
                      <div className="empty-state">Loading conversation from ChatGPT…</div>
                    ) : messages.length === 0 ? (
                      <div className="empty-state">No cached messages available.</div>
                    ) : (
                      messages.map((message) => (
                        <article key={message.key} className={`message ${message.role}`}>
                          <div className="message-role">{message.role}</div>
                          <div className="message-text">{message.textPlain || '[non-text content]'}</div>
                        </article>
                      ))
                    )}
                  </div>
                </>
              )}
            </div>
          </div>
        </section>
      ) : (
        <section className="health-view">
          <div className="health-actions">
            <button className="primary" onClick={() => void runHealth()}>
              Run checks
            </button>
            <button onClick={() => void toggleOfflineMode()}>
              {offlineMode ? 'Disable offline test' : 'Enable offline test'}
            </button>
            <button onClick={() => void exportDiagnostics()}>Export diagnostics</button>
          </div>

          <BackupControls extensionVersion={VERSION} />

          <div className="health-list">
            {capabilities.map((capability) => (
              <div key={capability.capability} className="health-row">
                <div>
                  <strong>{capability.capability}</strong>
                  <div className="health-message">
                    {capability.message || capability.diagnosticCode || capability.strategy || 'No details'}
                  </div>
                </div>
                <span className={`health-chip ${healthClass(capability.status)}`}>{capability.status}</span>
              </div>
            ))}
          </div>
          <div className="diagnostic-footnote">
            {offlineMode
              ? 'Offline test mode blocks live ChatGPT calls inside the extension; local cache remains active.'
              : 'Diagnostics exclude conversation titles and message content by default.'}
            {' '}Runtime ID: {browser.runtime.id}. Update by replacing files in the permanent install folder and pressing Reload in chrome://extensions; never Remove for routine updates.
          </div>
        </section>
      )}
    </main>
  );
}

function formatTime(value?: number): string {
  if (!value) return 'Unknown time';
  try {
    return new Intl.DateTimeFormat(undefined, {
      month: 'short',
      day: 'numeric',
      hour: 'numeric',
      minute: '2-digit'
    }).format(new Date(value));
  } catch {
    return 'Unknown time';
  }
}

function readableError(cause: unknown): string {
  return cause instanceof Error ? cause.message.slice(0, 240) : String(cause).slice(0, 240);
}

function errorCode(cause: unknown): string {
  if (cause instanceof Error && cause.name && cause.name !== 'Error') return cause.name;
  const message = readableError(cause);
  return message.match(/[A-Z]+(?:_[A-Z0-9]+)+/)?.[0] ?? 'CWM_UNKNOWN_ERROR';
}

function overallHealth(capabilities: CapabilityHealth[]): CapabilityHealth['status'] {
  if (capabilities.some((item) => item.status === 'unavailable' && item.capability === 'local-db')) return 'unavailable';
  if (capabilities.some((item) => item.status === 'unavailable')) return 'degraded';
  if (capabilities.some((item) => item.status === 'healthy')) return 'healthy';
  return 'unknown';
}

function healthClass(status: CapabilityHealth['status']): string {
  return `health-${status}`;
}
