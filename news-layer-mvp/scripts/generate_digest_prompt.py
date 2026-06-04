from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a ready-to-use digest prompt from article JSONL."
    )
    parser.add_argument("--input", required=True, help="Path to articles JSONL.")
    parser.add_argument(
        "--output-dir",
        default=str(ROOT / "outputs"),
        help="Directory for generated prompt file.",
    )
    return parser.parse_args()


def load_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def dedupe(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for record in records:
        key = (record.get("url") or record.get("title") or "").strip()
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(record)
    return unique


def render_prompt(records: list[dict[str, Any]]) -> str:
    lines = [
        "# News Digest Prompt",
        "",
        "You are preparing a concise evidence-first news digest.",
        "",
        "## Required Output",
        "",
        "1. Start with a short digest of the most important developments.",
        "2. Group related items by topic or event cluster.",
        "3. For each group, separate confirmed facts from uncertainty.",
        "4. Add a confidence label for each group: high, medium, or low.",
        "5. Explain why each group matters in practical terms.",
        "6. End with what to watch next.",
        "7. Finish with a source pack grouped by topic.",
        "",
        "## Article Inputs",
        "",
    ]

    for index, record in enumerate(records, start=1):
        lines.extend(
            [
                f"### Article {index}",
                f"- Title: {record.get('title') or 'Untitled'}",
                f"- URL: {record.get('url') or ''}",
                f"- Category: {record.get('category') or 'uncategorized'}",
                f"- Feed: {record.get('feed') or ''}",
                f"- Author: {record.get('author') or 'unknown'}",
                f"- Published: {record.get('published_at') or 'unknown'}",
                f"- Status: {record.get('status') or 'unknown'}",
                f"- Snippet: {record.get('content_snippet') or ''}",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    records = dedupe(load_records(Path(args.input)))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"digest_prompt_{timestamp}.md"
    output_path.write_text(render_prompt(records), encoding="utf-8", newline="\n")
    print(f"Wrote digest prompt for {len(records)} articles to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
