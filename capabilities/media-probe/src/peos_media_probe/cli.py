"""Command-line adapter for media.probe."""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from pathlib import Path

from .contracts import ArtifactRef, BlockContext, BlockRequest
from .core import MediaProbeBlock


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="peos-media-probe",
        description="Inspect a local media file with the media.probe capability block.",
    )
    parser.add_argument("input", help="Local media path or file:// URI")
    parser.add_argument(
        "--workspace",
        help="Allowed workspace root. Defaults to the input file's parent directory.",
    )
    parser.add_argument("--ffprobe", default="ffprobe", help="ffprobe executable")
    parser.add_argument("--timeout", type=float, default=30.0, help="Timeout in seconds")
    parser.add_argument("--request-id", help="Explicit request identifier")
    parser.add_argument("--artifact-id", help="Explicit artifact identifier")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    return parser


def _default_workspace(input_value: str) -> Path:
    if input_value.startswith("file://"):
        from urllib.parse import unquote, urlparse
        from urllib.request import url2pathname

        parsed = urlparse(input_value)
        path = Path(url2pathname(unquote(parsed.path)))
    else:
        path = Path(input_value)
    resolved = path.expanduser().resolve()
    return resolved if resolved.is_dir() else resolved.parent


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    workspace = (
        Path(args.workspace).expanduser().resolve()
        if args.workspace
        else _default_workspace(args.input)
    )
    request_id = args.request_id or f"req_{uuid.uuid4().hex}"
    artifact_id = args.artifact_id or f"art_{uuid.uuid4().hex}"

    request = BlockRequest(
        request_id=request_id,
        input_artifacts=(
            ArtifactRef(
                artifact_id=artifact_id,
                kind="media",
                uri=args.input,
            ),
        ),
    )
    context = BlockContext(
        workspace=workspace,
        timeout_seconds=args.timeout,
        ffprobe_path=args.ffprobe,
    )
    result = MediaProbeBlock().run(request, context)
    json.dump(
        result.to_dict(),
        sys.stdout,
        ensure_ascii=False,
        indent=2 if args.pretty else None,
        sort_keys=args.pretty,
    )
    sys.stdout.write("\n")
    return 0 if result.status == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
