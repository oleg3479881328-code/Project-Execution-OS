"""Capability catalog assembled from the central registry, manifests, and entry points."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from importlib import metadata
from pathlib import Path
from typing import Any

import yaml


_DESCRIPTIONS = {
    "media.download": ("Скачивание медиа", "Получает разрешённый источник и создаёт локальный media artifact."),
    "media.probe": ("Анализ медиа", "Показывает длительность, кодеки, разрешение, FPS, аудио и потоки файла."),
    "media.extract_audio": ("Извлечение аудио", "Создаёт нормализованный аудиофайл из видео или другого медиа."),
    "media.transcribe": ("Транскрибация", "Преобразует речь в текст с сегментами и тайм-кодами."),
    "media.clip": ("Нарезка видео", "Вырезает один или несколько точных фрагментов из исходного файла."),
    "media.generate_captions": ("Генерация субтитров", "Создаёт SRT, VTT или ASS из transcript artifact."),
    "media.render_vertical": ("Вертикальный рендер", "Собирает ролик под Reels, Shorts и TikTok."),
}


@dataclass(slots=True)
class CatalogBlock:
    block_id: str
    title: str
    description: str
    status: str
    version: str
    provider: str
    inputs: str
    outputs: str
    implementation_location: str
    limitations: str
    installed: bool
    interactive: bool
    manifest: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def find_repo_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__)).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "capability-library" / "REGISTRY.md").exists():
            return candidate
    raise RuntimeError("Project Execution OS repository root was not found")


def parse_registry(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if not cells or all(set(cell) <= {"-", ":"} for cell in cells):
            continue
        if cells[0] == "Block ID":
            headers = cells
            continue
        if headers and len(cells) >= len(headers):
            rows.append(dict(zip(headers, cells, strict=False)))
    return rows


def _load_manifests(repo_root: Path) -> dict[str, dict[str, Any]]:
    manifests: dict[str, dict[str, Any]] = {}
    capability_root = repo_root / "capabilities"
    if not capability_root.exists():
        return manifests
    for path in capability_root.glob("*/manifest.yaml"):
        try:
            payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError):
            continue
        block_id = payload.get("block_id")
        if isinstance(block_id, str):
            manifests[block_id] = payload
    return manifests


def discover_installed_capabilities() -> set[str]:
    installed: set[str] = set()
    try:
        entry_points = metadata.entry_points(group="project_execution_os.capabilities")
    except TypeError:
        entry_points = metadata.entry_points().select(group="project_execution_os.capabilities")
    for entry_point in entry_points:
        try:
            factory = entry_point.load()
            block = factory()
            block_id = getattr(block, "block_id", None)
            if isinstance(block_id, str):
                installed.add(block_id)
        except Exception:
            continue
    return installed


def build_catalog(repo_root: Path | None = None) -> list[CatalogBlock]:
    root = repo_root or find_repo_root()
    rows = parse_registry(root / "capability-library" / "REGISTRY.md")
    manifests = _load_manifests(root)
    installed = discover_installed_capabilities()
    result: list[CatalogBlock] = []

    for row in rows:
        block_id = row.get("Block ID", "")
        if not block_id:
            continue
        title, description = _DESCRIPTIONS.get(block_id, (block_id, "Reusable capability block."))
        manifest = manifests.get(block_id)
        providers = row.get("Initial providers", "—")
        if manifest and manifest.get("providers"):
            providers = ", ".join(str(value) for value in manifest["providers"])
        version = str((manifest or {}).get("version") or row.get("Version") or "—")
        status = str((manifest or {}).get("status") or row.get("Status") or "idea")
        is_installed = block_id in installed
        result.append(
            CatalogBlock(
                block_id=block_id,
                title=title,
                description=description,
                status=status,
                version=version,
                provider=providers,
                inputs=row.get("Inputs", "—"),
                outputs=row.get("Outputs", "—"),
                implementation_location=row.get("Implementation location", "not created"),
                limitations=row.get("Known limitations", "—"),
                installed=is_installed,
                interactive=is_installed and block_id == "media.probe",
                manifest=manifest,
            )
        )
    return result


def block_detail(block_id: str, repo_root: Path | None = None) -> dict[str, Any] | None:
    root = repo_root or find_repo_root()
    for block in build_catalog(root):
        if block.block_id != block_id:
            continue
        payload = block.to_dict()
        validation_path = root / "capabilities" / "media-probe" / "VALIDATION.md"
        validation = validation_path.read_text(encoding="utf-8") if validation_path.exists() else ""
        payload["tests"] = {
            "local": "6 passed" if "6 passed" in validation else "not recorded",
            "github_ci": "success" if "media.probe tests — success" in validation else "not recorded",
            "integrity_ci": "success" if "Validate Project OS Integrity — success" in validation else "not recorded",
            "windows": "pending" if "native Windows" in validation else "unknown",
            "application_integration": "pending" if "not yet been integrated" in validation else "unknown",
        }
        payload["contract"] = {
            "operation": "local media artifact → normalized media metadata",
            "request": ["request_id", "input_artifacts", "parameters", "provider", "idempotency_key"],
            "result": ["status", "output_artifacts", "metadata", "warnings", "metrics", "error"],
            "permissions": ["workspace read-only", "ffprobe subprocess", "no network", "no secrets"],
        }
        payload["usage"] = {
            "cli": "peos-media-probe input.mp4 --pretty",
            "python": "create_block().run(BlockRequest(...), BlockContext(workspace=...))",
        }
        return payload
    return None
