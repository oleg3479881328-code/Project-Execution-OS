"""Project Execution OS capability block: media.probe."""

from .contracts import (
    ArtifactRef,
    BlockContext,
    BlockError,
    BlockRequest,
    BlockResult,
)
from .core import MediaProbeBlock

__all__ = [
    "ArtifactRef",
    "BlockContext",
    "BlockError",
    "BlockRequest",
    "BlockResult",
    "MediaProbeBlock",
    "create_block",
]

__version__ = "0.1.0"


def create_block() -> MediaProbeBlock:
    """Create the default ffprobe-backed capability block."""
    return MediaProbeBlock()
