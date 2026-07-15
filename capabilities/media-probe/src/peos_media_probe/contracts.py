"""Serializable request, context, artifact, result, and error contracts."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Literal, Mapping

BlockStatus = Literal["success", "partial", "failed", "cancelled"]
ProgressReporter = Callable[[float, str], None]


def _dict(value: Mapping[str, Any] | None) -> dict[str, Any]:
    return dict(value or {})


@dataclass(frozen=True, slots=True)
class ArtifactRef:
    """Reference to an input or output artifact."""

    artifact_id: str
    kind: str
    uri: str
    mime_type: str | None = None
    size_bytes: int | None = None
    sha256: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_id": self.artifact_id,
            "kind": self.kind,
            "uri": self.uri,
            "mime_type": self.mime_type,
            "size_bytes": self.size_bytes,
            "sha256": self.sha256,
            "metadata": _dict(self.metadata),
        }


@dataclass(frozen=True, slots=True)
class BlockRequest:
    """Serializable request for one capability execution."""

    request_id: str
    input_artifacts: tuple[ArtifactRef, ...]
    parameters: Mapping[str, Any] = field(default_factory=dict)
    provider: str = "ffprobe"
    idempotency_key: str | None = None


@dataclass(slots=True)
class BlockContext:
    """Execution services supplied by the application or adapter."""

    workspace: Path
    timeout_seconds: float = 30.0
    ffprobe_path: str = "ffprobe"
    logger: Any | None = None
    progress_reporter: ProgressReporter | None = None

    def report_progress(self, fraction: float, message: str) -> None:
        if self.progress_reporter is not None:
            self.progress_reporter(max(0.0, min(1.0, fraction)), message)


@dataclass(frozen=True, slots=True)
class BlockError:
    """Structured actionable capability failure."""

    code: str
    message: str
    retryable: bool = False
    details: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "message": self.message,
            "retryable": self.retryable,
            "details": _dict(self.details),
        }


@dataclass(frozen=True, slots=True)
class BlockResult:
    """Predictable result envelope returned by every run."""

    status: BlockStatus
    output_artifacts: tuple[ArtifactRef, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)
    warnings: tuple[str, ...] = ()
    metrics: Mapping[str, Any] = field(default_factory=dict)
    error: BlockError | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "output_artifacts": [item.to_dict() for item in self.output_artifacts],
            "metadata": _dict(self.metadata),
            "warnings": list(self.warnings),
            "metrics": _dict(self.metrics),
            "error": self.error.to_dict() if self.error else None,
        }
