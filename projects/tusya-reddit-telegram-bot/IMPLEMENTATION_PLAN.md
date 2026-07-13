# Implementation Plan

## Phase 0 — repository and safety baseline

- Create Python package and lock dependencies.
- Add `.env.example` with names only, no values.
- Add `.gitignore` for secrets, DB files and local logs.
- Add structured logging and root project log files.
- Add CI for lint/typecheck/tests.
- Add owner-chat authorization middleware/helper.

Exit criteria: package starts, tests run, secrets cannot be committed accidentally.

## Phase 1 — persistence and CRUD

- Implement SQLite schema and migrations.
- Implement repositories for resources, keywords, posts, drafts, settings and delivery events.
- Implement resource URL normalization.
- Implement resource CRUD and keyword CRUD services.
- Add Telegram menu and CRUD conversations.

Tests:

- normalization of subreddit/new/search URLs;
- removal of transient parameters;
- duplicate resource prevention;
- duplicate keyword prevention;
- edit/toggle/delete persistence;
- unauthorized chat rejection.

Exit criteria: owner can manage both databases fully inside Telegram.

## Phase 2 — Reddit monitoring core

- Define Reddit client protocol and response schema.
- Implement newest-post fetch adapter.
- Implement matcher modes.
- Implement baseline transaction.
- Implement deduplication and per-resource error isolation.
- Implement scheduler with no overlapping cycles.
- Add `/status` and `Check now`.

Tests:

- baseline sends zero old notifications;
- later unseen matching post is selected;
- nonmatching post is stored but not delivered;
- duplicate poll produces no duplicate;
- one failed resource does not block others;
- retry/backoff policy.

Exit criteria: deterministic monitoring works against mocked Reddit responses.

## Phase 3 — Telegram feed delivery

- Render new-post cards.
- Add open-in-bot, open-Reddit and ignore actions.
- Add safe Telegram text chunking.
- Persist delivery events and post status.
- Implement feed pagination.

Tests:

- message rendering and escaping;
- callback ownership and stale callback handling;
- notification delivered once;
- long post chunking;
- link construction.

Exit criteria: a new matching fixture appears once in Telegram and can be opened.

## Phase 4 — DeepSeek drafts

- Implement DeepSeek client behind protocol.
- Add prompt versioning.
- Add configurable language, tone and length.
- Add create, regenerate and refine flows.
- Persist every accepted generated draft.
- Ensure no Reddit publishing code exists.

Tests:

- structured request construction;
- API failure shown safely;
- draft persistence;
- regenerate creates a new draft record or revision according to chosen repository design;
- no secret logging.

Exit criteria: owner can create and refine a saved draft from a post.

## Phase 5 — live acceptance and deployment

- Build Docker image.
- Configure persistent SQLite volume.
- Enter secrets only through deployment environment.
- Run controlled Telegram acceptance.
- Add one test Reddit resource and one keyword.
- Verify baseline.
- Verify exactly one new matching fixture/post delivery.
- Verify restart persistence.
- Verify GPT draft.
- Verify unauthorized Telegram account cannot access data.

Exit criteria: live bot works on phone continuously with no blockers.

## Required executor report

```text
EXECUTION REPORT

Status:
Version:
Branch:
PR URL:
Commit SHA:
Deployment URL/Host:
Telegram CRUD: Passed / Failed
Resource Normalization: Passed / Failed
Keyword Matching: Passed / Failed
Baseline: Passed / Failed
New Post Delivery: Passed / Failed
Duplicate Suppression: Passed / Failed
Full Post View: Passed / Failed
GPT Draft: Passed / Failed
Persistence After Restart: Passed / Failed
Owner Authorization: Passed / Failed
Secret Exposure Check: Passed / Failed
Automatic Reddit Publishing Present: No / Yes
Tests:
Validation Not Performed:
Blockers:
Ready For Review: Yes / No
```

## Executor boundaries

The executor may choose implementation details inside the approved modules, but must not:

- add automatic Reddit publishing;
- expose secrets;
- change single-owner MVP into SaaS;
- add a web admin panel;
- silently replace keyword matching with AI-only filtering;
- merge automatically.
