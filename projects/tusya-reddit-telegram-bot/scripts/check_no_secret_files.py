from __future__ import annotations

import subprocess
from pathlib import Path

FORBIDDEN_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    ".env.development",
    "id_rsa",
    "id_dsa",
}
FORBIDDEN_SUFFIXES = {
    ".key",
    ".pem",
    ".p12",
    ".pfx",
    ".sqlite3",
    ".db",
}
ALLOWED_FILES = {
    ".env.example",
}


def main() -> int:
    project_root = Path(__file__).resolve().parent.parent
    offenders: list[str] = []

    for relative_path in _tracked_project_files(project_root):
        path = project_root / relative_path
        if not path.is_file():
            continue
        if path.name in ALLOWED_FILES:
            continue
        if path.name in FORBIDDEN_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            offenders.append(relative_path.as_posix())

    if offenders:
        print("Forbidden secret-like files detected:")
        for offender in offenders:
            print(offender)
        return 1

    print("No forbidden secret-like files detected.")
    return 0


def _tracked_project_files(project_root: Path) -> list[Path]:
    repo_root = project_root.parent.parent
    completed = subprocess.run(
        ["git", "ls-files", "projects/tusya-reddit-telegram-bot"],
        cwd=repo_root,
        capture_output=True,
        check=True,
        text=True,
    )
    tracked_paths: list[Path] = []
    prefix = Path("projects/tusya-reddit-telegram-bot")
    for line in completed.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        repo_relative = Path(line)
        tracked_paths.append(repo_relative.relative_to(prefix))
    return tracked_paths


if __name__ == "__main__":
    raise SystemExit(main())
