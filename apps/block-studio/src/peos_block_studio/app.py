"""FastAPI application adapter for the local Block Studio."""
from __future__ import annotations

import asyncio
import mimetypes
import shutil
import time
from datetime import datetime, timezone
from functools import lru_cache
from importlib import metadata
from pathlib import Path
from typing import Annotated, Any, Callable
from uuid import uuid4

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from peos_media_probe import ArtifactRef, BlockContext, BlockRequest

from .catalog import block_detail, build_catalog, find_repo_root
from .storage import ExecutionStorage

MAX_UPLOAD_MB = 2048
CHUNK_SIZE = 1024 * 1024
BlockLoader = Callable[[str], Any]


@lru_cache(maxsize=16)
def load_capability(block_id: str) -> Any:
    try:
        points = metadata.entry_points(group="project_execution_os.capabilities")
    except TypeError:
        points = metadata.entry_points().select(group="project_execution_os.capabilities")
    for point in points:
        factory = point.load()
        block = factory()
        if getattr(block, "block_id", None) == block_id:
            return block
    raise LookupError(f"Capability is not installed: {block_id}")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def create_app(
    *,
    repo_root: Path | None = None,
    runtime_root: Path | None = None,
    block_loader: BlockLoader | None = None,
) -> FastAPI:
    root = (repo_root or find_repo_root()).resolve()
    runtime = (runtime_root or root / "apps" / "block-studio" / "runtime").resolve()
    storage = ExecutionStorage(runtime)
    loader = block_loader or load_capability
    static_root = Path(__file__).resolve().parent / "static"

    app = FastAPI(title="Project Execution OS — Block Studio", version="0.1.0")
    app.state.repo_root = root
    app.state.storage = storage
    app.state.block_loader = loader
    app.mount("/assets", StaticFiles(directory=static_root), name="assets")

    @app.get("/", include_in_schema=False)
    def index() -> FileResponse:
        return FileResponse(static_root / "index.html")

    @app.get("/api/health")
    def health() -> dict[str, Any]:
        ffprobe_path = shutil.which("ffprobe")
        catalog = build_catalog(root)
        return {
            "status": "ready" if ffprobe_path else "degraded",
            "studio_version": "0.1.0",
            "local_only": True,
            "ffprobe": {"available": bool(ffprobe_path), "path": ffprobe_path},
            "installed_blocks": [block.block_id for block in catalog if block.installed],
            "interactive_blocks": [block.block_id for block in catalog if block.interactive],
        }

    @app.get("/api/blocks")
    def blocks() -> list[dict[str, Any]]:
        return [block.to_dict() for block in build_catalog(root)]

    @app.get("/api/blocks/{block_id}")
    def block(block_id: str) -> dict[str, Any]:
        payload = block_detail(block_id, root)
        if payload is None:
            raise HTTPException(status_code=404, detail="Capability block not found")
        return payload

    @app.post("/api/blocks/media.probe/run")
    async def run_media_probe(
        file: Annotated[UploadFile, File(...)],
        timeout_seconds: Annotated[float, Form()] = 30.0,
    ) -> dict[str, Any]:
        if timeout_seconds <= 0 or timeout_seconds > 600:
            raise HTTPException(status_code=400, detail="Timeout must be between 0 and 600 seconds")

        execution_id, stored_path, stored_metadata = storage.create(file.filename, file.content_type)
        logs: list[dict[str, Any]] = []
        started = time.perf_counter()

        def log(level: str, message: str, **details: Any) -> None:
            logs.append({"time": _now(), "level": level, "message": message, "details": details})

        try:
            log("info", "Upload started", filename=stored_metadata["original_filename"])
            size_bytes = 0
            with stored_path.open("wb") as destination:
                while chunk := await file.read(CHUNK_SIZE):
                    size_bytes += len(chunk)
                    if size_bytes > MAX_UPLOAD_MB * 1024 * 1024:
                        raise HTTPException(status_code=413, detail=f"File exceeds {MAX_UPLOAD_MB} MB limit")
                    destination.write(chunk)
            await file.close()
            log("info", "Upload stored locally", size_bytes=size_bytes, workspace=str(stored_path.parent))

            def progress(fraction: float, message: str) -> None:
                log("progress", message, percent=round(fraction * 100, 1))

            try:
                capability = loader("media.probe")
            except Exception as exc:
                log("error", "Capability loading failed", exception_type=type(exc).__name__)
                raise HTTPException(status_code=503, detail="media.probe capability is not installed") from exc

            request = BlockRequest(
                request_id=f"studio_{uuid4().hex}",
                input_artifacts=(
                    ArtifactRef(
                        artifact_id=f"upload_{execution_id}",
                        kind="video" if (file.content_type or "").startswith("video/") else "audio" if (file.content_type or "").startswith("audio/") else "media",
                        uri=stored_path.as_uri(),
                        mime_type=file.content_type,
                        size_bytes=size_bytes,
                        metadata={"original_filename": stored_metadata["original_filename"], "source": "block-studio"},
                    ),
                ),
            )
            context = BlockContext(
                workspace=stored_path.parent,
                timeout_seconds=timeout_seconds,
                progress_reporter=progress,
            )
            result = await asyncio.to_thread(capability.run, request, context)
            result_payload = result.to_dict()
            log("info" if result.status == "success" else "error", "Capability execution finished", status=result.status)
            elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
            return {
                "execution_id": execution_id,
                "filename": stored_metadata["original_filename"],
                "mime_type": file.content_type or mimetypes.guess_type(str(stored_path))[0] or "application/octet-stream",
                "size_bytes": size_bytes,
                "preview_url": f"/api/executions/{execution_id}/file",
                "result": result_payload,
                "logs": logs,
                "studio_metrics": {"total_elapsed_ms": elapsed_ms},
            }
        except HTTPException:
            storage.delete(execution_id)
            raise
        except Exception as exc:
            log("error", "Unhandled studio adapter failure", exception_type=type(exc).__name__)
            storage.delete(execution_id)
            raise HTTPException(status_code=500, detail="Block Studio could not process the file") from exc

    @app.get("/api/executions/{execution_id}/file")
    def execution_file(execution_id: str) -> FileResponse:
        try:
            file_path, metadata_payload = storage.resolve_file(execution_id)
        except (FileNotFoundError, ValueError):
            raise HTTPException(status_code=404, detail="Execution file not found") from None
        media_type = metadata_payload.get("mime_type") or mimetypes.guess_type(file_path.name)[0]
        return FileResponse(file_path, media_type=media_type, filename=str(metadata_payload.get("original_filename") or file_path.name), content_disposition_type="inline")

    @app.delete("/api/executions/{execution_id}")
    def delete_execution(execution_id: str) -> dict[str, bool]:
        if not storage.delete(execution_id):
            raise HTTPException(status_code=404, detail="Execution not found")
        return {"deleted": True}

    return app


app = create_app()
