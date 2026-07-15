"""Runtime upload storage with path-boundary protection."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from uuid import uuid4

_SAFE_NAME = re.compile(r"[^A-Za-z0-9._-]+")
_EXECUTION_ID = re.compile(r"^[a-f0-9]{32}$")


def sanitize_filename(filename: str | None) -> str:
    name = Path(filename or "upload.bin").name
    cleaned = _SAFE_NAME.sub("_", name).strip("._")
    return cleaned[:180] or "upload.bin"


class ExecutionStorage:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def create(self, original_filename: str | None, mime_type: str | None) -> tuple[str, Path, dict[str, str | None]]:
        execution_id = uuid4().hex
        workspace = (self.root / execution_id).resolve()
        workspace.mkdir(parents=True, exist_ok=False)
        safe_name = sanitize_filename(original_filename)
        suffix = Path(safe_name).suffix[:20]
        stored_path = workspace / f"input{suffix}"
        metadata = {
            "execution_id": execution_id,
            "original_filename": safe_name,
            "stored_filename": stored_path.name,
            "mime_type": mime_type,
        }
        (workspace / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
        return execution_id, stored_path, metadata

    def resolve_file(self, execution_id: str) -> tuple[Path, dict[str, str | None]]:
        if not _EXECUTION_ID.fullmatch(execution_id):
            raise FileNotFoundError(execution_id)
        workspace = (self.root / execution_id).resolve()
        workspace.relative_to(self.root)
        metadata_path = workspace / "metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        file_path = (workspace / str(metadata["stored_filename"])).resolve()
        file_path.relative_to(workspace)
        if not file_path.is_file():
            raise FileNotFoundError(file_path)
        return file_path, metadata

    def workspace(self, execution_id: str) -> Path:
        file_path, _ = self.resolve_file(execution_id)
        return file_path.parent

    def delete(self, execution_id: str) -> bool:
        try:
            workspace = self.workspace(execution_id)
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            return False
        shutil.rmtree(workspace, ignore_errors=False)
        return True
