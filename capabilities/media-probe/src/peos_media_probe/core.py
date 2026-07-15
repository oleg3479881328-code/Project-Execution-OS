"""Capability core for media.probe."""

from __future__ import annotations

import os
import re
import time
from pathlib import Path
from typing import Any, Protocol
from urllib.parse import unquote, urlparse
from urllib.request import url2pathname

from .contracts import (
    ArtifactRef,
    BlockContext,
    BlockError,
    BlockRequest,
    BlockResult,
)
from .errors import CapabilityFailure
from .providers import FFprobeProvider

_WINDOWS_DRIVE_PATH = re.compile(r"^[A-Za-z]:[\\/]")


class ProbeProvider(Protocol):
    provider_id: str

    def probe(self, path: Path, timeout_seconds: float) -> dict[str, Any]:
        ...


def _resolve_input_path(uri: str, workspace: Path) -> Path:
    workspace_path = workspace.expanduser().resolve()

    if _WINDOWS_DRIVE_PATH.match(uri):
        candidate = Path(uri)
    else:
        parsed = urlparse(uri)
        if parsed.scheme == "file":
            raw_path = url2pathname(unquote(parsed.path))
            if os.name == "nt" and raw_path.startswith("/") and len(raw_path) > 3:
                if raw_path[2] == ":":
                    raw_path = raw_path[1:]
            candidate = Path(raw_path)
        elif parsed.scheme:
            raise CapabilityFailure(
                code="unsupported_uri",
                message=f"media.probe supports local paths and file:// URIs, not {parsed.scheme}://",
                details={"uri": uri, "scheme": parsed.scheme},
            )
        else:
            candidate = Path(uri)

    if not candidate.is_absolute():
        candidate = workspace_path / candidate

    try:
        resolved = candidate.expanduser().resolve(strict=True)
    except FileNotFoundError as exc:
        raise CapabilityFailure(
            code="input_not_found",
            message=f"Input media file does not exist: {candidate}",
            details={"uri": uri},
        ) from exc

    if not resolved.is_file():
        raise CapabilityFailure(
            code="input_not_file",
            message=f"Input artifact is not a file: {resolved}",
            details={"uri": uri},
        )

    try:
        resolved.relative_to(workspace_path)
    except ValueError as exc:
        raise CapabilityFailure(
            code="input_outside_workspace",
            message="Input media file is outside the allowed workspace",
            details={
                "input_path": str(resolved),
                "workspace": str(workspace_path),
            },
        ) from exc

    return resolved


class MediaProbeBlock:
    """Inspect one local media artifact and return normalized metadata."""

    block_id = "media.probe"
    version = "0.1.0"

    def __init__(self, provider: ProbeProvider | None = None) -> None:
        self._provider = provider

    def run(self, request: BlockRequest, context: BlockContext) -> BlockResult:
        started = time.perf_counter()
        provider_name = request.provider or "ffprobe"

        try:
            if len(request.input_artifacts) != 1:
                raise CapabilityFailure(
                    code="invalid_request",
                    message="media.probe requires exactly one input artifact",
                    details={"input_count": len(request.input_artifacts)},
                )

            if provider_name != "ffprobe":
                raise CapabilityFailure(
                    code="unsupported_provider",
                    message=f"Unsupported media.probe provider: {provider_name}",
                    details={"supported_providers": ["ffprobe"]},
                )

            context.report_progress(0.05, "Resolving media input")
            input_artifact = request.input_artifacts[0]
            input_path = _resolve_input_path(input_artifact.uri, context.workspace)

            provider = self._provider or FFprobeProvider(binary=context.ffprobe_path)
            if provider.provider_id != provider_name:
                raise CapabilityFailure(
                    code="provider_mismatch",
                    message="Injected provider does not match the requested provider",
                    details={
                        "requested": provider_name,
                        "injected": provider.provider_id,
                    },
                )

            context.report_progress(0.2, "Running ffprobe")
            probe_metadata = provider.probe(input_path, context.timeout_seconds)
            context.report_progress(0.9, "Normalizing media metadata")

            warnings: list[str] = []
            if probe_metadata.get("video_stream_count", 0) == 0:
                warnings.append("No video stream was detected.")
            if probe_metadata.get("audio_stream_count", 0) == 0:
                warnings.append("No audio stream was detected.")

            merged_metadata = dict(input_artifact.metadata)
            merged_metadata["probe"] = probe_metadata

            output = ArtifactRef(
                artifact_id=input_artifact.artifact_id,
                kind=input_artifact.kind,
                uri=input_artifact.uri,
                mime_type=input_artifact.mime_type,
                size_bytes=probe_metadata.get("size_bytes")
                or input_artifact.size_bytes,
                sha256=input_artifact.sha256,
                metadata=merged_metadata,
            )
            elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
            context.report_progress(1.0, "Media probe complete")

            return BlockResult(
                status="success",
                output_artifacts=(output,),
                metadata={
                    "block_id": self.block_id,
                    "block_version": self.version,
                    "provider": provider_name,
                    "request_id": request.request_id,
                    "idempotency_key": request.idempotency_key,
                },
                warnings=tuple(warnings),
                metrics={"elapsed_ms": elapsed_ms},
            )
        except CapabilityFailure as exc:
            return self._failure_result(
                exc=exc,
                request=request,
                provider_name=provider_name,
                started=started,
            )
        except Exception as exc:  # defensive conversion at the capability boundary
            if context.logger is not None:
                context.logger.exception("Unexpected media.probe failure")
            failure = CapabilityFailure(
                code="internal_error",
                message="Unexpected media.probe failure",
                details={"exception_type": type(exc).__name__},
            )
            return self._failure_result(
                exc=failure,
                request=request,
                provider_name=provider_name,
                started=started,
            )

    def _failure_result(
        self,
        *,
        exc: CapabilityFailure,
        request: BlockRequest,
        provider_name: str,
        started: float,
    ) -> BlockResult:
        return BlockResult(
            status="failed",
            metadata={
                "block_id": self.block_id,
                "block_version": self.version,
                "provider": provider_name,
                "request_id": request.request_id,
                "idempotency_key": request.idempotency_key,
            },
            metrics={
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3)
            },
            error=BlockError(
                code=exc.code,
                message=exc.message,
                retryable=exc.retryable,
                details=exc.details,
            ),
        )
