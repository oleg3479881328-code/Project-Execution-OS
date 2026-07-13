from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CallbackPayload:
    action: str
    subject_id: int
    page: int | None = None


def encode_callback(
    action: str,
    subject_id: int,
    *,
    page: int | None = None,
) -> str:
    if page is None:
        return f"{action}:{subject_id}"
    return f"{action}:{subject_id}:{page}"


def parse_callback(data: str) -> CallbackPayload:
    parts = data.split(":")
    if len(parts) not in {2, 3}:
        raise ValueError("Invalid callback payload")
    action = parts[0]
    subject_id = int(parts[1])
    page = int(parts[2]) if len(parts) == 3 else None
    return CallbackPayload(action=action, subject_id=subject_id, page=page)
