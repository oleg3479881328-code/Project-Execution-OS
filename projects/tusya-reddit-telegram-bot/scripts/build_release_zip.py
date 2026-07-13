from __future__ import annotations

import zipfile
from pathlib import Path

VERSION = "v0.1.0-alpha"
ARTIFACT_NAME = f"tusya-reddit-telegram-bot-{VERSION}.zip"
EXCLUDED_NAMES = {
    ".env",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "__pycache__",
    "data",
    "logs",
    "backups",
}
EXCLUDED_SUFFIXES = {".sqlite3", ".db", ".pyc"}


def main() -> int:
    project_root = Path(__file__).resolve().parent.parent
    dist_dir = project_root / "dist"
    dist_dir.mkdir(parents=True, exist_ok=True)
    artifact_path = dist_dir / ARTIFACT_NAME

    with zipfile.ZipFile(artifact_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in project_root.rglob("*"):
            relative = path.relative_to(project_root)
            if _should_exclude(relative):
                continue
            if path.is_file():
                archive.write(path, arcname=relative.as_posix())

    print(artifact_path.as_posix())
    return 0


def _should_exclude(relative: Path) -> bool:
    if any(part in EXCLUDED_NAMES for part in relative.parts):
        return True
    if relative.name in EXCLUDED_NAMES:
        return True
    if relative.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    return False


if __name__ == "__main__":
    raise SystemExit(main())
