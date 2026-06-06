#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def stop(message: str) -> None:
    raise SystemExit(message)


def text(paths):
    return "\n".join(p.read_text(encoding="utf-8") for p in paths if p.exists())


def main() -> None:
    required = [
        "indexes/system-index.json",
        "indexes/semantic-documents.jsonl",
        "indexes/BLOCK_CATALOG.generated.md",
        "indexes/KNOWLEDGE_CATALOG.generated.md",
    ]
    for item in required:
        if not (ROOT / item).exists():
            stop(f"Missing index artifact: {item}")

    block_index = (ROOT / "blocks/PROJECT_INDEX.md").read_text(encoding="utf-8")
    for path in sorted((ROOT / "blocks").rglob("BLOCK.md")):
        folder = path.parent.relative_to(ROOT).as_posix() + "/"
        if folder not in block_index:
            stop(f"Missing block catalog entry: {folder}")

    knowledge_index = text(sorted((ROOT / "knowledge-library").glob("PROJECT_INDEX*.md")))
    for path in sorted((ROOT / "knowledge-library").rglob("*.md")):
        if path.name == "README.md" or path.name.startswith("PROJECT_INDEX"):
            continue
        item = path.relative_to(ROOT).as_posix()
        if item not in knowledge_index:
            stop(f"Missing knowledge catalog entry: {item}")

    print("Index validation passed")


if __name__ == "__main__":
    main()
