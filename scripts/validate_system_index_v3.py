#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def stop(message: str) -> None:
    raise SystemExit(message)


def joined(paths):
    return "\n".join(path.read_text(encoding="utf-8") for path in paths if path.exists())


def main() -> None:
    required = [
        "indexes/system-index.json",
        "indexes/semantic-documents.jsonl",
        "indexes/BLOCK_CATALOG.generated.md",
        "indexes/KNOWLEDGE_CATALOG.generated.md",
    ]
    for item in required:
        if not (ROOT / item).exists():
            stop(f"Missing generated index artifact: {item}")

    warnings = []

    block_index = (ROOT / "blocks/PROJECT_INDEX.md").read_text(encoding="utf-8")
    for path in sorted((ROOT / "blocks").rglob("BLOCK.md")):
        folder = path.parent.relative_to(ROOT).as_posix() + "/"
        if folder not in block_index:
            warnings.append(f"Curated block index is missing: {folder}")

    knowledge_index = joined(sorted((ROOT / "knowledge-library").glob("PROJECT_INDEX*.md")))
    for path in sorted((ROOT / "knowledge-library").rglob("*.md")):
        if path.name == "README.md" or path.name.startswith("PROJECT_INDEX"):
            continue
        item = path.relative_to(ROOT).as_posix()
        if item not in knowledge_index:
            warnings.append(f"Curated knowledge index is missing: {item}")

    if warnings:
        print("Curated navigation warnings:")
        for warning in warnings:
            print(f"- {warning}")
        print("Generated indexes remain valid. Synchronize curated catalogs separately.")

    print("Generated index validation passed")


if __name__ == "__main__":
    main()
