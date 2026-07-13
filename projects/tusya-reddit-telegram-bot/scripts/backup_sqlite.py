from __future__ import annotations

import argparse
import sqlite3
from datetime import UTC, datetime
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database-path", default="data/tusya.sqlite3")
    parser.add_argument("--backup-dir", default="backups")
    args = parser.parse_args()

    database_path = Path(args.database_path)
    backup_dir = Path(args.backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    backup_path = backup_dir / f"tusya-backup-{timestamp}.sqlite3"

    source = sqlite3.connect(database_path)
    destination = sqlite3.connect(backup_path)
    try:
        source.backup(destination)
    finally:
        destination.close()
        source.close()

    print(backup_path.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
