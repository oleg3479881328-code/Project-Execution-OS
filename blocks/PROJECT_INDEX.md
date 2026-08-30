# Blocks Index

## Purpose

This index lists reusable domain blocks embedded inside `Project-Execution-OS`.

Blocks live below the central operating system:
- the OS defines core workflow, memory, review, and handoff rules;
- blocks define domain-specific reusable assets built on top of those rules.

## Current Blocks

### Chrome Extension Block

Path:

`blocks/chrome-extension/`

Purpose:

Provide a reusable browser-extension product layer for Chrome Extension architecture, Manifest V3, ready frameworks, permissions, security/privacy, publishing, monetization, and payments.

Current status:

`candidate`

### Communication Channel Block

Path:

`blocks/communication-channel/`

Purpose:

Provide reusable routing for connected-agent communication, message transport, and coordination-path selection.

Current status:

`candidate`

### Design Block

Path:

`blocks/design/`

Purpose:

Provide a reusable website and site-building design layer for donor research, page strategy, landing/SaaS patterns, UI systems, conversion, ready site stacks, implementation handoff, AI-coded frontend design QA, and review.

Current status:

`candidate_v3`

### Documentation Block

Path:

`blocks/documentation/`

Purpose:

Turn repository analysis into reusable AI-ready documentation packages, transfer packages, and documentation-specific maintenance rules.

Current status:

`reviewed_candidate`

### Logic Block

Path:

`blocks/logic/`

Purpose:

Provide a reusable reasoning layer for logic concepts, argument structure, cause-and-effect analysis, reasoning-error detection, assumption review, contradiction checks, and decision-quality review.

Current status:

`candidate`

### Music Block

Path:

`blocks/music/`

Purpose:

Provide a reusable music-production layer covering generation, editing, real-time music, utilities, export, and rights review.

Current status:

`candidate`

### News Intelligence Block

Path:

`blocks/news-intelligence/`

Purpose:

Provide a reusable current-news intelligence workflow for collecting, deduplicating, source-checking, scoring, interpreting, packaging, and selectively preserving time-sensitive external signals.

Current status:

`candidate`

### Notion Agent Workspace Block

Path:

`blocks/notion/`

Purpose:

Provide a reusable Notion workspace layer for stable `PROJECT_ID` routing, agent-compatible project pages, shared project databases, MCP/API access design, GitHub coordination boundaries, and fresh-agent re-entry.

Current status:

`candidate`

### OSINT Block

Path:

`blocks/osint/`

Purpose:

Provide reusable open-source intelligence, public-source investigation, source verification, timeline reconstruction, due-diligence, reputation and evidence-log workflows.

Current status:

`candidate`

### Reviewer Block

Path:

`blocks/reviewer/`

Purpose:

Provide one reusable hard-review and independent-critique workflow for red-team inspection, acceptance gating, missing-evidence detection, risk review, and explicit verdicts.

Current status:

`candidate_v1`

### Server Rental Block

Path:

`blocks/server-rental/`

Purpose:

Provide reusable decision and implementation guidance for VPS, cloud/GPU rental, serverless compute, rented AI infrastructure and hybrid compute routing.

Current status:

`candidate`

### Skill Creator Block

Path:

`blocks/skill-creator/`

Purpose:

Provide one reusable workflow for creating, checking, reviewing, registering, and maintaining central skills without duplicating the underlying skill standards.

Current status:

`candidate`

### Solana Block

Path:

`blocks/solana/`

Purpose:

Provide a reusable Solana product and implementation layer for dApps, wallet flows, Anchor programs, SPL Token, payments, DeFi/NFT patterns, AI-agent actions, security, monetization, and handoff.

Current status:

`candidate`

### Telegram Block

Path:

`blocks/telegram/`

Purpose:

Provide a reusable Telegram product layer for bots, Mini Apps, Telegram Login, Gateway, Stars, business workflows, ready solutions, security, and implementation handoff.

Current status:

`candidate`

### US Law Block

Path:

`blocks/us-law/`

Purpose:

Provide a reusable United States legal-research and triage layer with source hierarchy, jurisdiction checks, deadline review, and attorney-escalation boundaries.

Current status:

`candidate`

#### Immigration Sub-Block

Path:

`blocks/us-law/immigration/`

Purpose:

Provide a narrower immigration-law path for USCIS, Form I-485, marriage-based adjustment of status, interviews, RFEs, travel risk, and policy monitoring.

Current status:

`candidate`

### US Tax and Accounting Block

Path:

`blocks/us-tax-accounting/`

Purpose:

Provide a reusable United States tax and accounting operations layer for bookkeeping, entity and tax-classification review, federal/state/local routing, deadlines, gig-economy income, payroll, contractors, information returns, sales tax, recurring close workflows, security boundaries, tool selection, and professional handoff.

Current status:

`candidate`

#### Ohio Tax and Accounting Sub-Block

Path:

`blocks/us-tax-accounting/ohio/`

Purpose:

Provide an Ohio-specific route for state tax, municipal income tax, RITA, CCA, gig-economy income, Ohio LLC and small-business workflows, payroll, unemployment tax, sales tax, deadlines, and portal selection.

Current status:

`candidate`

### Video Production Block

Path:

`blocks/video-production/`

Purpose:

Provide a reusable video-production layer for Reels, Shorts, TikTok, automated clipping, yt-dlp, ffmpeg, CapCut, AI voice/avatar workflows, multilingual factories, monetization, and implementation handoff.

Current status:

`candidate`

### YouTube Block

Path:

`blocks/youtube/`

Purpose:

Provide a reusable YouTube platform layer for channel strategy, Shorts and long-form publishing, YouTube Partner Program readiness, monetization, originality/copyright review, analytics, playlists, uploads, API automation, multilingual scaling, and channel operations.

Current status:

`candidate_v2`

## Generated Catalog

For the automatically refreshed machine-derived artifact list, use:

`indexes/BLOCK_CATALOG.generated.md`

## Maintenance Rule

Every `blocks/**/BLOCK.md` entrypoint must be discoverable from this curated index or a live router. Prefer listing current reusable blocks here even when a direct global-router route also exists.

## Final Rule

Use this curated index for human navigation and the generated catalog for machine-assisted repository discovery.