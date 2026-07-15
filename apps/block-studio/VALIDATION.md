# Block Studio Validation Record

Date: 2026-07-15
Version: `0.1.0 candidate`

## Local environment

```text
Python 3.13.5
FastAPI 0.128.2
Uvicorn 0.48.0
pytest 9.0.2
ffprobe 7.1.3
Node syntax checker available
```

## Package and automated tests

Commands:

```bash
python -m pip install -e capabilities/media-probe -e "apps/block-studio[dev]"
cd apps/block-studio
pytest -q
node --check src/peos_block_studio/static/app.js
```

Result:

```text
5 passed in 1.55s
JavaScript syntax check passed
```

Coverage includes:

- registry and manifest discovery;
- Python entry-point discovery for `media.probe`;
- health and capability-library APIs;
- real `ffprobe` execution through the Block Studio upload endpoint;
- generated WAV input with duration and sample-rate verification;
- local preview endpoint;
- temporary execution deletion;
- filename sanitization and execution-path protection.

## Real MP4 integration smoke test

A real local test MP4 was generated with:

```text
video: H.264, 320x240
audio: AAC, 44100 Hz
duration: 0.8 seconds
```

The running Block Studio server returned:

```text
health: ready
ffprobe: available
execution status: success
duration: 0.8
video: 320 x 240, h264
audio: aac, 44100 Hz
temporary execution deletion: success
```

The HTTP path was verified end to end:

```text
GET  /
GET  /api/health
POST /api/blocks/media.probe/run
DELETE /api/executions/<execution-id>
```

## Visual QA

The owner-mode layout was rendered in headless Chromium as a static visual fixture and inspected at 1440 pixels width.

Verified visually:

- library sidebar;
- readiness/status badges;
- file selection and preview area;
- result cards;
- owner/developer mode control;
- responsive dark interface hierarchy.

Direct headless-browser navigation to the local HTTP server was blocked by the execution environment policy with `ERR_BLOCKED_BY_ADMINISTRATOR`. Functional server and upload behavior were therefore verified separately through real HTTP requests, while the interface was rendered as a static browser fixture. No bypass was invented.

## Portable artifact

A portable ZIP was generated for owner testing:

```text
Block-Studio-v0.1.0-portable.zip
```

It contains the Windows launcher, Block Studio application, capability package, registry, and first-start instructions.

## Promotion boundary

Block Studio remains `candidate 0.1.0` until:

- GitHub Actions passes on Linux and Windows;
- the owner opens it on the target Windows computer;
- a real user-owned media file is processed successfully.
