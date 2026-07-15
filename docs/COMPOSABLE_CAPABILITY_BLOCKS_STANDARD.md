# Composable Capability Blocks Standard

## Purpose

This standard defines how `Project Execution OS` builds reusable executable capabilities that can be composed into multiple applications without repeatedly redesigning or rewriting the same functionality.

Examples include:

- video download;
- media probing;
- audio extraction;
- transcription;
- video clipping;
- subtitle generation;
- voice synthesis;
- publishing adapters;
- document parsing;
- notification delivery.

The goal is not to create a collection of copy-paste snippets. The goal is to create versioned, testable, contract-driven capability packages that an application can install, configure, and compose.

## Source Trail

Donor patterns reviewed:

- Python Packaging User Guide — plugin discovery and package entry points: `https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/`
- n8n node architecture and lifecycle: `https://docs.n8n.io/integrations/creating-nodes/overview/`
- Temporal Activity model: `https://docs.temporal.io/activities`
- OpenAPI Specification: `https://spec.openapis.org/oas/latest.html`
- Existing local architecture: `docs/HARNESS_ENGINEERING_STANDARD.md`
- Existing local domain-block construction: `skills/orchestration/domain-block-creation/SKILL.md`

Captured for `Project Execution OS` on: `2026-07-15`.

## Status

`candidate_v1`

This is the system-wide default for new functionality that is likely to be reused across two or more projects.

It must be validated on the first real media capability chain:

```text
media.download
-> media.probe
-> media.extract_audio
-> media.transcribe
-> media.clip
```

## Core Decision

All reusable system functionality should be evaluated as a potential capability block before it is implemented directly inside an application.

Use this rule:

```text
Do not build the same capability separately inside multiple applications.
Build it once behind a stable contract, validate it, version it, and compose it.
```

This does not mean every helper function becomes a block.

A capability deserves a block when it has at least one of these properties:

- it will likely be reused in multiple applications;
- it wraps a substantial external tool, model, API, or workflow;
- it has meaningful configuration, failure modes, permissions, or resource costs;
- it needs independent testing or versioning;
- replacing its underlying provider should not require rewriting the application;
- it produces reusable artifacts consumed by later stages.

## Two Different Meanings Of Block

`Project Execution OS` must distinguish two block types.

### Domain Block

Location:

```text
blocks/<domain>/
```

Purpose:

- reusable knowledge;
- research;
- decision rules;
- tool selection;
- patterns;
- review guidance;
- implementation handoff.

A domain block helps decide what to build and how to evaluate it.

### Capability Block

Implementation location:

```text
capabilities/<capability-id>/
```

or in a dedicated capability-library repository when code volume justifies separation.

Purpose:

- executable reusable functionality;
- stable input and output contracts;
- provider adapters;
- tests;
- examples;
- versioned releases.

A capability block performs one bounded action.

### Workflow

A workflow composes capability blocks without absorbing their internal implementation.

Example:

```text
DownloadVideo
-> ProbeMedia
-> ExtractAudio
-> TranscribeAudio
-> SelectSegments
-> CutVideo
-> BurnCaptions
```

The workflow owns sequencing and business decisions.

The capability block owns one technical operation.

### Application Adapter

An adapter connects a generic capability to a particular application surface.

Examples:

- FastAPI endpoint;
- Telegram command;
- desktop button;
- background worker;
- n8n node;
- Temporal Activity;
- CLI command;
- scheduled job.

Application-specific UI and business logic must not be placed inside the reusable core block.

## Core Architectural Model

```text
Application UI / Bot / API
        |
Application Adapter
        |
Workflow Orchestrator
        |
Capability Contract
        |
Capability Core
        |
Provider Adapter
        |
ffmpeg / yt-dlp / Whisper / cloud API / local model
```

Each layer may be replaced independently when its contract remains compatible.

## Default Implementation Strategy

Use a package-first model, not a microservice-first model.

Default progression:

```text
Python package
-> CLI adapter
-> in-process application adapter
-> HTTP or worker service only when isolation or scaling requires it
```

Do not create one server per block by default.

Promote a block to a service only when at least one is true:

- it needs a different machine, GPU, operating system, or dependency environment;
- it must scale independently;
- it processes long-running jobs outside the application process;
- it needs strong permission or failure isolation;
- several non-Python consumers need network access;
- deployment evidence shows that in-process packaging is inadequate.

## Standard Block Identity

Every capability block must have a stable identifier:

```text
<domain>.<action>
```

Examples:

```text
media.download
media.probe
media.extract_audio
media.transcribe
media.clip
media.render_vertical
media.generate_captions
voice.synthesize
notify.telegram_send
storage.put_object
```

The identifier remains stable even when the default provider changes.

Provider implementations use a second identifier:

```text
media.transcribe.whisper_cpp
media.transcribe.faster_whisper
media.transcribe.openai_api
```

Applications depend on the capability contract, not directly on one provider, unless a deliberate lock-in decision is recorded.

## Minimum Capability Contract

Every non-trivial block must expose one conceptual operation.

Recommended Python shape:

```python
class CapabilityBlock(Protocol):
    block_id: str
    version: str

    def run(self, request: BlockRequest, context: BlockContext) -> BlockResult:
        ...
```

### BlockRequest

Must contain only serializable configuration and artifact references.

Typical fields:

```text
request_id
input_artifacts
parameters
provider
idempotency_key
```

### BlockContext

Carries execution services without embedding application business logic:

```text
workspace
logger
progress reporter
cancellation signal
secrets provider
artifact store
timeout / deadline
```

### BlockResult

Must use a predictable result envelope:

```text
status: success | partial | failed | cancelled
output_artifacts
metadata
warnings
metrics
error
```

Errors must be structured and actionable. Do not return only a free-text exception string.

## Artifact Contract

Blocks should exchange artifact references plus structured metadata rather than hidden process state.

Example media artifact:

```json
{
  "artifact_id": "art_123",
  "kind": "video",
  "uri": "file:///workspace/input.mp4",
  "mime_type": "video/mp4",
  "size_bytes": 123456,
  "sha256": "...",
  "metadata": {
    "duration_seconds": 92.4,
    "width": 1920,
    "height": 1080
  }
}
```

The first implementation may use local files, but the contract must not assume that every future artifact lives on the same machine.

## Recommended Package Structure

```text
capabilities/<capability-id>/
├── BLOCK.md
├── pyproject.toml
├── manifest.yaml
├── src/
│   └── <package_name>/
│       ├── __init__.py
│       ├── contracts.py
│       ├── core.py
│       ├── errors.py
│       └── providers/
├── tests/
│   ├── unit/
│   ├── contract/
│   └── smoke/
├── examples/
└── CHANGELOG.md
```

Add optional directories only when justified:

```text
adapters/
fixtures/
benchmarks/
docker/
schemas/
```

## Required Manifest

Each block must include machine-readable metadata.

Example:

```yaml
block_id: media.transcribe
version: 0.1.0
status: candidate
runtime: python
python: ">=3.12"
entry_point: capability_media_transcribe:create_block
inputs:
  - audio
outputs:
  - transcript
permissions:
  network: optional
  filesystem: workspace-only
  gpu: optional
providers:
  - whisper_cpp
  - faster_whisper
idempotent: true
```

The manifest is used by the registry, installers, tests, and future workflow builders.

## Discovery And Installation

For Python-first blocks, prefer standard package metadata and entry points rather than hard-coded imports.

Recommended entry-point group:

```toml
[project.entry-points."project_execution_os.capabilities"]
media_transcribe = "capability_media_transcribe:create_block"
```

Applications may then discover installed capability blocks through package metadata.

Do not copy the source folder manually into each application as the normal integration method.

Preferred integration:

```text
install versioned package
-> discover or import block
-> configure provider
-> call stable contract
```

## Invocation Adapters

Every validated block should support at least:

1. Python in-process invocation.
2. CLI invocation for testing, debugging, and manual use.

Optional adapters:

- HTTP with OpenAPI description;
- queue worker;
- Temporal Activity;
- n8n node;
- MCP tool;
- desktop bridge.

Adapters must remain thin. They translate transport inputs to the core contract and translate the result back.

## Composition Rules

### One Block, One Technical Responsibility

Good:

```text
media.download
media.transcribe
media.clip
```

Bad:

```text
media.make_complete_reel_and_publish_everywhere
```

Large business outcomes belong in workflows composed from smaller blocks.

### Explicit Inputs And Outputs

A block must not depend on undocumented files, global variables, current working directory, chat history, or ambient application state.

### Provider Independence

The core contract should allow the provider to change when practical.

Example:

```text
media.transcribe
  -> whisper.cpp locally
  -> faster-whisper on GPU
  -> cloud API when local execution is unavailable
```

### Idempotency

Blocks that may be retried should avoid creating duplicate irreversible effects.

For deterministic file-producing operations, use an idempotency key or content-derived output path when practical.

### No Hidden Orchestration

A block may perform the internal steps required for its one action, but it must not secretly trigger unrelated downstream capabilities.

`media.transcribe` must not publish a video or send a Telegram message.

### No UI In The Core

The core block must not contain Telegram messages, web-page components, desktop dialogs, or app-specific labels.

### No Embedded Secrets

Credentials come through the secrets provider or environment-specific adapter.

The block repository must never contain production secrets.

## Permissions And Safety

Each block must declare:

- filesystem access;
- network access;
- subprocess use;
- GPU requirement;
- credentials used;
- destructive behavior;
- external publication or communication effects;
- legal or rights constraints.

Use least privilege.

Media download blocks must not be designed to bypass access controls, DRM, private authentication boundaries, or copyright restrictions.

## Testing Standard

A block is not reusable merely because it worked once.

### Candidate

Required:

- unit tests for core parsing and configuration;
- one contract test;
- one local smoke test;
- documented known limitations.

### Validated

Required:

- several representative fixtures;
- expected failure tests;
- retry or idempotency check when relevant;
- cross-application integration in at least one real project;
- output artifact verification.

### Production

Required when business-critical:

- regression suite;
- version compatibility policy;
- performance or cost evidence;
- security and permission review;
- rollback or provider fallback;
- operational logging.

## Verification Output

Each run should make it possible to answer:

```text
Which block and version ran?
Which provider ran?
What inputs were used?
What artifacts were produced?
How long did it take?
What did it cost when applicable?
What warnings or failures occurred?
Can the operation be safely retried?
```

## Versioning

Use semantic versioning for capability contracts.

- Patch: bug fix without contract change.
- Minor: backward-compatible capability addition.
- Major: incompatible request, result, or behavior contract change.

Provider upgrades do not automatically require a major block version, but output changes that break consumers do.

Applications must pin compatible versions. Do not depend on an unreviewed moving branch.

## Block Registry

All reusable capability blocks must be listed in:

```text
capability-library/REGISTRY.md
```

Registry fields:

```text
block_id
version
status
owner
implementation location
providers
input kinds
output kinds
validated projects
known limitations
```

Statuses:

```text
idea
candidate
validated
production
deprecated
retired
```

A domain block may recommend a capability, but the registry is the source of truth for whether executable code actually exists and has been validated.

## Existing Solution First

Before creating a capability block:

1. check existing local capability blocks;
2. check the relevant Project Execution OS domain block;
3. check official tools and SDKs;
4. check mature open-source wrappers and plugins;
5. select a provider strategy;
6. create custom code only for the missing contract, adapter, or orchestration layer.

Do not reimplement ffmpeg, yt-dlp, Whisper, cloud SDKs, or other mature engines. Wrap them behind our contract.

## First Media Capability Set

### 1. `media.download`

Responsibility:

- accept an authorized source URL or source descriptor;
- download media through an approved provider;
- return a media artifact and metadata;
- expose progress and structured errors.

Initial provider candidates:

- yt-dlp for supported public or authorized sources;
- direct HTTP download for direct media URLs.

### 2. `media.probe`

Responsibility:

- inspect a media artifact;
- return normalized stream, codec, duration, resolution, frame-rate, and audio metadata.

Initial provider:

- ffprobe.

### 3. `media.extract_audio`

Responsibility:

- produce a normalized audio artifact suitable for transcription.

Initial provider:

- ffmpeg.

### 4. `media.transcribe`

Responsibility:

- transcribe an audio or video artifact;
- produce text, segments, timestamps, language, and confidence metadata when available.

Initial provider candidates:

- whisper.cpp for lightweight local execution;
- faster-whisper for GPU or higher-throughput execution;
- cloud provider adapter only when required.

### 5. `media.clip`

Responsibility:

- cut one or more time ranges from a media artifact;
- support stream-copy when safe and re-encode when necessary;
- return exact output timing and encoding metadata.

Initial provider:

- ffmpeg.

## Example Application Composition

A QuizLight import workflow may use:

```text
media.download
-> media.probe
-> media.extract_audio
-> media.transcribe
-> phrase selection logic owned by QuizLight
-> media.clip
```

A Reels factory may use the same blocks but provide different selection, caption, voice, layout, and publishing workflows.

The shared technical blocks remain unchanged.

## Promotion Rule

Do not call a capability block ready merely because its specification exists.

Use these meanings precisely:

- `idea`: only the need is recorded;
- `candidate`: code exists and basic tests pass;
- `validated`: used successfully in at least one real application workflow;
- `production`: operational evidence, regression tests, and maintenance ownership exist.

## Relationship To Other Standards

Use:

- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` before selecting providers or writing wrappers;
- `docs/HARNESS_ENGINEERING_STANDARD.md` when a block runs as an agent tool, worker, or operational workflow;
- `skills/orchestration/domain-block-creation/SKILL.md` for reusable knowledge domains;
- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md` when providers have variable API cost;
- `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` when agent behavior is part of the workflow;
- the relevant domain block for business and domain decisions;
- the capability registry for executable readiness.

## Fail Conditions

The architecture fails if:

- applications copy and fork block code instead of depending on a versioned package;
- a block combines unrelated business outcomes;
- inputs and outputs are undocumented;
- the block depends on ambient state or one application's database schema;
- provider-specific details leak through the generic contract without necessity;
- there are no contract or smoke tests;
- errors are unstructured;
- secrets are embedded;
- a block is called reusable before another consumer can integrate it;
- a specification is mistaken for implemented and validated code;
- a microservice is created without evidence that a package is insufficient.

## Final Rule

Build capabilities once, behind stable contracts.

Compose applications from validated blocks and project-specific workflows.

Keep domain knowledge, executable capability, orchestration, and application UI as separate layers.