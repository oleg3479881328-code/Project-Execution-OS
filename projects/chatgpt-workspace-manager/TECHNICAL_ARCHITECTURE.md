# ChatGPT Workspace Manager — Technical Architecture

## Status

Architecture package frozen for first implementation slice.

## Goals

1. Provide a powerful private owner-operated workspace manager for ChatGPT.
2. Keep ChatGPT-specific fragility isolated behind provider adapters.
3. Keep user data local by default.
4. Support live management and a durable local mirror without forcing full-account re-downloads on every launch.
5. Make destructive actions auditable, pausable and verifiable.
6. Keep future semantic memory and additional providers possible without rewriting the core.

## Non-goals For Initial Implementation

- Chrome Web Store publication;
- SaaS backend;
- public accounts or billing;
- remote telemetry;
- automatic cross-provider support;
- aggressive rate-limit retry or restriction bypass;
- one giant content-script architecture.

## System Layers

```text
┌──────────────────────────────────────────────────────────────┐
│                         Side Panel UI                        │
│ Workspace | Organize | Search | Bulk | Vault | Health      │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│                       Workspace Core                         │
│ models | organization | search | operations | backup       │
└──────────────────────────────┬───────────────────────────────┘
                               │ Provider contracts
┌──────────────────────────────▼───────────────────────────────┐
│                      ChatGPT Adapter                          │
│ capability router / normalizer / compatibility state        │
├───────────────────┬───────────────────┬──────────────────────┤
│ Live API Strategy │ DOM Strategy      │ Export Import        │
└─────────┬─────────┴─────────┬─────────┴──────────┬───────────┘
          │                   │                    │
          ▼                   ▼                    ▼
    ChatGPT session       ChatGPT page       Official export
          │                   │                    ZIP
          └───────────────────┴────────────────────┘
                               │ normalized data
┌──────────────────────────────▼───────────────────────────────┐
│                       Local Mirror                           │
│ IndexedDB / Dexie                                           │
│ conversations | messages | owner metadata | operations      │
│ indexes | snapshots | compatibility events                 │
└──────────────────────────────────────────────────────────────┘
```

## Canonical Contracts

### ProviderConversation

```ts
interface ProviderConversation {
  provider: 'chatgpt';
  id: string;
  title: string;
  createdAt?: number;
  updatedAt?: number;
  nativeProjectId?: string | null;
  nativeProjectTitle?: string | null;
  archived?: boolean;
  deleted?: boolean;
  currentNodeId?: string | null;
  messageCount?: number;
  contentHydrated: boolean;
  lastSyncedAt: number;
  providerRawVersion?: string;
}
```

### CanonicalMessage

```ts
interface CanonicalMessage {
  provider: 'chatgpt';
  conversationId: string;
  id: string;
  parentId?: string | null;
  index: number;
  role: 'user' | 'assistant' | 'system' | 'tool' | 'other';
  model?: string | null;
  createdAt?: number;
  textPlain: string;
  contentHtml?: string;
  contentParts?: CanonicalContentPart[];
  branchPath?: string[];
  source: 'live-api' | 'dom' | 'official-export';
  capturedAt: number;
}
```

### OwnerConversationMetadata

```ts
interface OwnerConversationMetadata {
  conversationId: string;
  folderIds: string[];
  tagIds: string[];
  favorite: boolean;
  pinned: boolean;
  note?: string;
  bookmarkIds: string[];
  customStatus?: string;
  updatedAt: number;
}
```

### OperationRecord

```ts
interface OperationRecord {
  id: string;
  type: 'archive' | 'delete' | 'rename' | 'backup' | 'tag' | 'move-local';
  status: 'planned' | 'running' | 'paused' | 'completed' | 'partial' | 'failed';
  conversationIds: string[];
  startedAt?: number;
  completedAt?: number;
  backupSnapshotId?: string;
  results: OperationItemResult[];
  stopReason?: 'user' | 'rate-limit' | 'compatibility-failure' | 'account-warning' | 'unknown';
}
```

## Database Stores

Use Dexie over IndexedDB.

Initial stores:

- `conversations`;
- `messages`;
- `ownerConversationMetadata`;
- `folders`;
- `tags`;
- `bookmarks`;
- `snapshots`;
- `operations`;
- `compatibilityChecks`;
- `searchDocuments`;
- `settings`.

Do not store an entire account as one JSON blob.

Messages and metadata must be independently upsertable to support incremental sync and migration.

## Database Versioning

Every schema change increments a local DB version and includes a migration.

Rules:

- never destroy existing local data during a normal upgrade;
- migration must be idempotent where practical;
- full DB export must be possible before risky migrations;
- expose current DB schema version in diagnostics.

## ChatGPT Adapter

### Capability interface

```ts
type Capability =
  | 'session'
  | 'list-conversations'
  | 'read-conversation'
  | 'list-projects'
  | 'archive-conversation'
  | 'delete-conversation'
  | 'rename-conversation'
  | 'dom-navigation';
```

Each capability reports:

```ts
interface CapabilityHealth {
  capability: Capability;
  status: 'healthy' | 'degraded' | 'unavailable' | 'unknown';
  strategy?: 'live-api' | 'dom' | 'official-export';
  checkedAt: number;
  message?: string;
  diagnosticCode?: string;
}
```

### Strategy routing

The adapter chooses the best available strategy per capability.

Example:

```text
list-conversations
  1. live API if healthy
  2. DOM metadata fallback if implemented
  3. local mirror only, marked stale

read-conversation
  1. live API
  2. hydrated DOM
  3. official-export/local snapshot

archive/delete
  1. live API when separately validated
  2. DOM interaction fallback
  3. unavailable rather than guessing
```

Never silently switch a destructive action to an unvalidated strategy.

## Sync Engine

### Metadata sync

Goal: fast refresh of workspace state.

Expected behavior:

- fetch conversation pages;
- normalize metadata;
- upsert conversations;
- detect new, changed, archived and missing records;
- preserve owner metadata regardless of platform changes;
- mark missing provider conversations as `providerMissing` until verified rather than deleting local data immediately.

### Content hydration

Hydrate conversation content when:

- user opens preview;
- conversation enters full-text index and content is absent/stale;
- user requests backup/export;
- destructive operation requires pre-action snapshot;
- user explicitly requests full local indexing.

Use cache freshness metadata to avoid unnecessary re-fetching.

## Search Architecture

### Phase 1

- title search;
- local full-text search;
- filters by time, native project, owner folder, tag, archive state;
- saved searches / smart collections.

Use MiniSearch or equivalent local index over canonical local documents.

### Phase 2

Hybrid local recall:

```text
keyword / BM25 score
+
local vector similarity
+
metadata filters
```

Use local embeddings only; no remote AI backend by default.

## Bulk Operation Engine

### Mandatory state machine

```text
DRAFT
-> PLAN
-> OPTIONAL / REQUIRED SNAPSHOT
-> CONFIRM
-> RUNNING
-> PAUSED / COMPLETED / PARTIAL / FAILED
```

### Item execution

For each item:

1. verify capability health;
2. verify target still exists and current state is compatible with the action;
3. execute one action;
4. verify resulting state;
5. log result;
6. delay according to configured safe pacing;
7. continue only if health remains acceptable.

### Stop conditions

Pause immediately on:

- HTTP 429 or explicit rate-limit signal;
- account warning or suspicious-activity signal;
- auth/session loss;
- repeated verification failure;
- compatibility failure suggesting endpoint/DOM drift;
- explicit user pause/cancel.

Do not implement retry loops intended to defeat platform throttling.

## Snapshot Safety

Destructive actions should offer a pre-action local snapshot.

For delete, default behavior should strongly prefer snapshot when content is available.

A snapshot records:

- canonical conversation metadata;
- canonical messages currently available;
- owner metadata;
- snapshot timestamp;
- source and completeness state.

The manager must distinguish:

- complete snapshot;
- metadata-only snapshot;
- partial snapshot.

## Side Panel Information Architecture

Primary tabs:

1. `Workspace`
2. `Organize`
3. `Search`
4. `Bulk`
5. `Vault`
6. `Health`

Later tabs / surfaces:

- `Memory`;
- `Prompts`;
- current-conversation `Navigator` overlay or subpanel.

Header always shows:

- extension version;
- ChatGPT adapter status;
- sync state;
- local DB status.

## Compatibility Harness

Run non-destructive health probes on startup and on demand.

Do not run destructive probes automatically.

Minimum checks:

- current ChatGPT tab detected;
- authenticated session discoverable;
- conversation list readable;
- one known conversation can be read when safe;
- project list capability state;
- DOM anchor selectors used by navigator;
- IndexedDB open/migrate/read/write;
- search index available.

Destructive capabilities become `healthy` only after their implementation has a current validated contract and real user-triggered operation succeeds.

## Diagnostics

Provide an exportable local diagnostics report containing no conversation content by default.

Include:

- extension version;
- DB schema version;
- adapter version;
- capability health;
- endpoint/selector diagnostic codes;
- recent operation result counts;
- timestamps;
- sanitized errors.

## Permissions Baseline

Because this is owner-operated and unpacked, permissions may be wider than a public-store extension when genuinely useful, but they should still remain understandable.

Initial target:

- `storage`;
- `sidePanel`;
- `activeTab`;
- `scripting` if required;
- host access limited initially to ChatGPT domains.

Do not add unrelated website access before a provider capability exists.

## Local-First Rule

Default runtime has:

- no telemetry;
- no analytics;
- no extension vendor backend;
- no remote conversation storage;
- no model-provider API keys.

External libraries/models must be pinned or vendored where practical.

## Test Strategy

### Unit

- canonical normalization;
- owner metadata merges;
- DB migrations;
- search indexing;
- operation state machine;
- snapshot completeness flags.

### Adapter fixture tests

Maintain sanitized fixtures for known ChatGPT response and DOM shapes.

Test:

- list normalization;
- conversation tree normalization;
- archive/delete request construction without sending requests;
- selector fallbacks;
- compatibility classification.

### Browser integration

Use an unpacked build against a real owner ChatGPT session for acceptance testing.

Destructive tests use deliberately disposable test conversations only.

## First Implementation Slice

Build a vertical slice that proves the architecture rather than all features.

Required:

1. WXT project shell;
2. owner Side Panel shell;
3. Dexie DB and schema versioning;
4. ChatGPTAdapter capability framework;
5. metadata list sync;
6. Workspace conversation list;
7. on-demand preview for one conversation;
8. owner favorites + notes;
9. title/local metadata search;
10. Health panel;
11. diagnostics export;
12. no destructive actions yet.

Acceptance criteria:

- extension loads unpacked;
- Side Panel opens and shows dynamic version;
- current ChatGPT session can be detected;
- metadata sync populates local DB;
- reopening Side Panel reads cached data without refetching everything;
- preview hydrates only the selected conversation;
- favorites/notes survive reload;
- Health panel reports capability state correctly;
- adapter failure does not break local workspace browsing;
- no external server traffic from our code.

## Second Slice

After Slice 1 passes real-browser review:

- archive queue;
- delete queue;
- pre-action snapshot;
- result verification;
- pause/resume;
- operation history.

## Architecture Decision

Proceed with this modular private-owner architecture. Do not fork a donor as the main application. Donor code may enter only capability-by-capability behind our contracts.
