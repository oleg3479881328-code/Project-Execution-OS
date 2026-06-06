#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def fail(message: str) -> None:
    raise SystemExit(message)


def main() -> None:
    required = [
        ROOT / "indexes/system-index.json",
        ROOT / "indexes/semantic-documents.jsonl",
        ROOT / "indexes/BLOCK_CATALOG.generated.md",
        ROOT / "indexes/KNOWLEDGE_CATALOG.generated.md",
    ]
    for path in required:
        if not path.exists():
            fail(f"Missing generated index artifact: {rel(path)}")

    block_index = (ROOT / "blocks/PROJECT_INDEX.md").read_text(encoding="utf-8")
    for path in sorted((ROOT / "blocks").rglob("BLOCK.md")):
        folder = rel(path.parent) + "/"
        if folder not in block_index:
            fail(f"Curated block index is missing: {folder}")

    knowledge_index = (ROOT / "knowledge-library/PROJECT_INDEX.md").read_text(encoding="utf-8")
    for path in sorted((ROOT / "knowledge-library").rglob("*.md")):
        if path.name in {"README.md", "PROJECT_INDEX.md"}:
            continue
        item = rel(path)
        if item not in knowledge_index:
            fail(f"Curated knowledge index is missing: {item}")

    print("Structural index validation passed")


if __name__ == "__main__":
    main()
