# media.probe Capability Block

## Purpose

Inspect one authorized local media file with `ffprobe` and return normalized metadata through the Project Execution OS capability contract.

## Status

`candidate` — implementation and local tests exist. Real cross-application validation is still required before promotion to `validated`.

## Block Identity

```text
block_id: media.probe
version: 0.1.0
provider: ffprobe
```

## Responsibility

This block performs one technical operation:

```text
local media artifact -> normalized media metadata
```

It does not download files, transcode media, cut clips, transcribe audio, publish content, or contain application UI and business logic.

## Inputs

Exactly one `ArtifactRef` with:

- a local path or `file://` URI;
- an artifact identifier;
- a media kind;
- optional MIME type, size, hash, and metadata.

The resolved file must remain inside `BlockContext.workspace`.

## Outputs

The result envelope contains the original artifact enriched under:

```text
artifact.metadata.probe
```

Normalized metadata includes:

- duration;
- file size and bit rate;
- container format;
- stream counts;
- normalized video, audio, and subtitle stream records;
- primary video and audio summaries;
- frame rate, dimensions, sample rate, channels, language, and disposition when available.

## Python Usage

```python
from pathlib import Path
from peos_media_probe import ArtifactRef, BlockContext, BlockRequest, create_block

path = Path("input.mp4").resolve()
result = create_block().run(
    BlockRequest(
        request_id="req-1",
        input_artifacts=(
            ArtifactRef(
                artifact_id="media-1",
                kind="video",
                uri=path.as_uri(),
            ),
        ),
    ),
    BlockContext(workspace=path.parent),
)
```

## CLI Usage

```bash
peos-media-probe input.mp4 --pretty
```

or:

```bash
python -m peos_media_probe.cli input.mp4 --pretty
```

The CLI returns exit code `0` for success and `1` for a structured capability failure.

## Dependencies

Python dependencies: none.

Runtime dependency:

```text
ffprobe
```

`ffprobe` must be installed and available on `PATH`, or supplied through `BlockContext.ffprobe_path` / `--ffprobe`.

## Safety Boundary

- no network access;
- read-only access to one file inside the configured workspace;
- no destructive operations;
- no secrets;
- no DRM or access-control bypass;
- no hidden downstream execution.

## Verification

```bash
python -m pip install -e '.[dev]'
pytest
peos-media-probe path/to/media.mp4 --pretty
```

## Known Limitations

- only local paths and `file://` URIs are accepted;
- only the `ffprobe` provider exists in v0.1.0;
- container and codec metadata are normalized on a best-effort basis because source formats vary;
- Windows path behavior is implemented but still requires a native Windows smoke test;
- the block has not yet been integrated into two real applications.

## Promotion Requirement

Promote to `validated` only after successful integration into a real workflow, with artifact evidence and any required contract corrections recorded in the central registry.
