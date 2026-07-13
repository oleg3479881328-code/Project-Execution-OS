from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

from tusya_bot.bot.application import run_bot


def main() -> None:
    parser = argparse.ArgumentParser(prog="tusya-bot")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("run")
    health_parser = subparsers.add_parser("healthcheck")
    health_parser.add_argument(
        "--database-path",
        default="data/tusya.sqlite3",
    )

    args = parser.parse_args()
    if args.command in {None, "run"}:
        run_bot()
        return
    if args.command == "healthcheck":
        run_healthcheck(Path(args.database_path))
        return


def run_healthcheck(database_path: Path) -> None:
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON;")
        cursor = connection.execute("PRAGMA journal_mode = WAL;")
        journal_mode = str(cursor.fetchone()[0]).lower()
        if journal_mode != "wal":
            raise SystemExit("SQLite journal mode is not WAL")
        connection.execute("SELECT 1;").fetchone()
    finally:
        connection.close()


if __name__ == "__main__":
    main()
