# Project Execution OS — Block Studio

A local browser application for touching, viewing, and verifying reusable capability blocks.

## What version 0.1.0 provides

- capability library generated from the central registry and manifests;
- fully interactive `media.probe` screen;
- drag-and-drop upload;
- local video/audio preview;
- owner-friendly metadata cards;
- stream table, raw JSON, execution log, contract, tests, and usage tabs;
- owner/developer display modes;
- environment health indicator;
- no upload to external services.

## Windows start

Double-click at the repository root:

```text
START_BLOCK_STUDIO.bat
```

The launcher creates `.venv-block-studio`, installs the local capability and application packages, starts the server, and opens:

```text
http://127.0.0.1:8015
```

Runtime requirement:

```text
ffprobe
```

## Manual start

```bash
python -m venv .venv-block-studio
.venv-block-studio/Scripts/python -m pip install -e capabilities/media-probe -e "apps/block-studio[dev]"
.venv-block-studio/Scripts/python -m peos_block_studio
```

Linux/macOS uses `bin/python` instead of `Scripts/python`.

## Safety

- binds to `127.0.0.1` by default;
- stores temporary uploads under `apps/block-studio/runtime/`;
- does not use network APIs;
- executes the original capability package instead of duplicating probing logic;
- allows deletion of each temporary execution from the UI.
