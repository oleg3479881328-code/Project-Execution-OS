"""ffprobe provider and normalization logic."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from ..errors import CapabilityFailure

Runner = Callable[..., subprocess.CompletedProcess[str]]


def _optional_float(value: Any) -> float | None:
    if value in (None, "", "N/A"):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _optional_int(value: Any) -> int | None:
    if value in (None, "", "N/A"):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def parse_fraction(value: Any) -> float | None:
    """Parse ffprobe rational strings such as ``30000/1001`` safely."""
    if value in (None, "", "N/A", "0/0"):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value)
    if "/" not in text:
        return _optional_float(text)
    numerator, denominator = text.split("/", 1)
    try:
        denominator_value = float(denominator)
        if denominator_value == 0:
            return None
        return float(numerator) / denominator_value
    except ValueError:
        return None


def _stream_duration(stream: Mapping[str, Any]) -> float | None:
    direct = _optional_float(stream.get("duration"))
    if direct is not None:
        return direct
    tags = stream.get("tags")
    if isinstance(tags, Mapping):
        return _optional_float(tags.get("DURATION"))
    return None


def _normalized_stream(stream: Mapping[str, Any]) -> dict[str, Any]:
    tags = stream.get("tags") if isinstance(stream.get("tags"), Mapping) else {}
    disposition = (
        stream.get("disposition")
        if isinstance(stream.get("disposition"), Mapping)
        else {}
    )
    return {
        "index": _optional_int(stream.get("index")),
        "codec_type": stream.get("codec_type"),
        "codec_name": stream.get("codec_name"),
        "codec_long_name": stream.get("codec_long_name"),
        "profile": stream.get("profile"),
        "codec_tag_string": stream.get("codec_tag_string"),
        "duration_seconds": _stream_duration(stream),
        "bit_rate": _optional_int(stream.get("bit_rate")),
        "width": _optional_int(stream.get("width")),
        "height": _optional_int(stream.get("height")),
        "pixel_format": stream.get("pix_fmt"),
        "sample_aspect_ratio": stream.get("sample_aspect_ratio"),
        "display_aspect_ratio": stream.get("display_aspect_ratio"),
        "average_frame_rate": stream.get("avg_frame_rate"),
        "real_frame_rate": stream.get("r_frame_rate"),
        "frame_rate_fps": parse_fraction(
            stream.get("avg_frame_rate") or stream.get("r_frame_rate")
        ),
        "sample_rate_hz": _optional_int(stream.get("sample_rate")),
        "channels": _optional_int(stream.get("channels")),
        "channel_layout": stream.get("channel_layout"),
        "language": tags.get("language"),
        "title": tags.get("title"),
        "disposition": dict(disposition),
    }


def normalize_ffprobe_payload(
    payload: Mapping[str, Any], *, actual_size_bytes: int | None = None
) -> dict[str, Any]:
    """Normalize provider-specific ffprobe JSON into a stable block payload."""
    raw_streams = payload.get("streams")
    streams: list[dict[str, Any]] = []
    if isinstance(raw_streams, Sequence) and not isinstance(raw_streams, (str, bytes)):
        streams = [
            _normalized_stream(stream)
            for stream in raw_streams
            if isinstance(stream, Mapping)
        ]

    format_data = payload.get("format")
    if not isinstance(format_data, Mapping):
        format_data = {}

    durations = [
        value
        for value in (
            _optional_float(format_data.get("duration")),
            *[stream.get("duration_seconds") for stream in streams],
        )
        if isinstance(value, (int, float))
    ]
    duration_seconds = max(durations) if durations else None

    format_size = _optional_int(format_data.get("size"))
    size_bytes = format_size if format_size is not None else actual_size_bytes

    video_streams = [item for item in streams if item.get("codec_type") == "video"]
    audio_streams = [item for item in streams if item.get("codec_type") == "audio"]
    subtitle_streams = [
        item for item in streams if item.get("codec_type") == "subtitle"
    ]

    return {
        "duration_seconds": duration_seconds,
        "size_bytes": size_bytes,
        "bit_rate": _optional_int(format_data.get("bit_rate")),
        "format_name": format_data.get("format_name"),
        "format_long_name": format_data.get("format_long_name"),
        "start_time_seconds": _optional_float(format_data.get("start_time")),
        "stream_count": len(streams),
        "video_stream_count": len(video_streams),
        "audio_stream_count": len(audio_streams),
        "subtitle_stream_count": len(subtitle_streams),
        "primary_video": video_streams[0] if video_streams else None,
        "primary_audio": audio_streams[0] if audio_streams else None,
        "streams": streams,
        "format_tags": dict(format_data.get("tags") or {})
        if isinstance(format_data.get("tags"), Mapping)
        else {},
    }


@dataclass(slots=True)
class FFprobeProvider:
    """Execute ffprobe and normalize its JSON output."""

    binary: str = "ffprobe"
    runner: Runner = subprocess.run
    provider_id: str = "ffprobe"

    def probe(self, path: Path, timeout_seconds: float) -> dict[str, Any]:
        command = [
            self.binary,
            "-v",
            "error",
            "-show_format",
            "-show_streams",
            "-of",
            "json",
            str(path),
        ]
        try:
            completed = self.runner(
                command,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                check=False,
            )
        except FileNotFoundError as exc:
            raise CapabilityFailure(
                code="ffprobe_not_found",
                message=f"ffprobe executable was not found: {self.binary}",
                details={"binary": self.binary},
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise CapabilityFailure(
                code="ffprobe_timeout",
                message=f"ffprobe exceeded the {timeout_seconds:g}s timeout",
                retryable=True,
                details={"timeout_seconds": timeout_seconds},
            ) from exc

        if completed.returncode != 0:
            stderr = (completed.stderr or "").strip()
            raise CapabilityFailure(
                code="ffprobe_failed",
                message="ffprobe could not inspect the media input",
                details={
                    "return_code": completed.returncode,
                    "stderr": stderr[-4000:],
                },
            )

        try:
            payload = json.loads(completed.stdout or "{}")
        except json.JSONDecodeError as exc:
            raise CapabilityFailure(
                code="invalid_ffprobe_output",
                message="ffprobe returned invalid JSON",
                details={"stdout_preview": (completed.stdout or "")[:1000]},
            ) from exc

        if not isinstance(payload, Mapping):
            raise CapabilityFailure(
                code="invalid_ffprobe_output",
                message="ffprobe JSON root must be an object",
            )

        return normalize_ffprobe_payload(
            payload,
            actual_size_bytes=path.stat().st_size,
        )
