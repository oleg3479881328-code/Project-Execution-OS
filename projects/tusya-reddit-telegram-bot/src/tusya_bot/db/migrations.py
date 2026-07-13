from __future__ import annotations

import aiosqlite

from tusya_bot.db.schema import SCHEMA_SQL, SCHEMA_VERSION


async def migrate(connection: aiosqlite.Connection) -> None:
    row = await (await connection.execute("PRAGMA user_version;")).fetchone()
    current_version = int(row[0]) if row is not None else 0
    if current_version >= SCHEMA_VERSION:
        return

    await connection.executescript(SCHEMA_SQL)
    await connection.execute(f"PRAGMA user_version = {SCHEMA_VERSION};")
