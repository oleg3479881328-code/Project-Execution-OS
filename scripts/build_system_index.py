from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "indexes" / "semantic-documents.jsonl"
TEXT_EXTENSIONS = {".md", ".txt", ".html", ".yml", ".yaml"}
ALLOWED_PREFIXES = (
    "docs/",
    "blocks/",
    "workflow-templates/",
    "knowledge-library/",
    "project-library/",
    "news-layer-mvp/sources/",
    "START_HERE.md",
    "PROJECT.md",
    "PROJECT_INDEX.md",
    "README.md",
    "AGENTS.md",
    "SYSTEM_CONTEXT_MANIFEST.md",
)


def should_index(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return False
    relative = path.relative_to(REPO_ROOT).as_posix()
    return relative.startswith(ALLOWED_PREFIXES)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").replace("\r\n", "\n")


def clean_text(text: str) -> str:
    text = re.sub(r"`{3,}.*?`{3,}", " ", text, flags=re.S)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def infer_domain(path_text: str, text: str) -> str:
    lowered = f"{path_text}\n{text}".lower()
    if any(term in lowered for term in ("uscis", "immigration", "visa", "green card", "marriage interview")):
        return "us-law"
    if any(term in lowered for term in ("telegram", "bot", "messaging")):
        return "messaging"
    if any(term in lowered for term in ("video", "audio", "music")):
        return "media"
    if path_text.startswith("workflow-templates/"):
        return "workflow"
    if path_text.startswith("blocks/"):
        return "blocks"
    if path_text.startswith("knowledge-library/"):
        return "knowledge"
    if path_text.startswith("project-library/"):
        return "project-memory"
    return "project-os"


def infer_status(path_text: str) -> str:
    if path_text.startswith("knowledge-library/") or path_text.startswith("news-layer-mvp/sources/"):
        return "reference"
    if path_text.startswith("indexes/"):
        return "generated"
    return "active"


def split_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_heading = "Document"
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("#"):
            if current_lines:
                sections.append((current_heading, "\n".join(current_lines).strip()))
                current_lines = []
            current_heading = line.lstrip("#").strip() or "Document"
            continue
        current_lines.append(line)
    if current_lines:
        sections.append((current_heading, "\n".join(current_lines).strip()))
    return [(heading, body) for heading, body in sections if clean_text(body)]


def chunk_text(text: str, limit: int = 900) -> list[str]:
    chunks: list[str] = []
    paragraphs = [clean_text(part) for part in re.split(r"\n\s*\n", text) if clean_text(part)]
    current = ""
    for paragraph in paragraphs:
        candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= limit:
            current = candidate
            continue
        if current:
            chunks.append(current)
        while len(paragraph) > limit:
            chunks.append(paragraph[:limit].strip())
            paragraph = paragraph[limit - 120 :].strip()
        current = paragraph
    if current:
        chunks.append(current)
    return chunks


def build_records() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file() or not should_index(path):
            continue
        relative = path.relative_to(REPO_ROOT).as_posix()
        text = read_text(path)
        if not clean_text(text):
            continue
        for section_index, (heading, body) in enumerate(split_sections(text), start=1):
            for chunk_index, chunk in enumerate(chunk_text(body), start=1):
                content_hash = hashlib.sha256(chunk.encode("utf-8")).hexdigest()
                records.append(
                    {
                        "id": f"{relative}#{section_index}-{chunk_index}",
                        "path": relative,
                        "heading": heading,
                        "domain": infer_domain(relative, chunk),
                        "status": infer_status(relative),
                        "content_hash": content_hash,
                        "text": chunk,
                    }
                )
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the structural corpus for semantic retrieval.")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    records = build_records()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {len(records)} records to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
