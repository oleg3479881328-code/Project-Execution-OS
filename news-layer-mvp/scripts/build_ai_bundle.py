from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a grouped Markdown analysis bundle from article JSONL."
    )
    parser.add_argument("--input", required=True, help="Path to articles JSONL.")
    parser.add_argument(
        "--output-dir",
        default=str(ROOT / "outputs"),
        help="Directory for generated Markdown bundle.",
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
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
    result: list[dict[str, Any]] = []
    for record in records:
        key = (record.get("url") or record.get("title") or "").strip()
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(record)
    return result


def render_bundle(records: list[dict[str, Any]]) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[(record.get("category") or "uncategorized").lower()].append(record)

    lines = [
        "# AI News Bundle",
        "",
        "## Instructions For Analysis",
        "",
        "1. What happened",
        "2. What is confirmed",
        "3. What is uncertain",
        "4. Why it matters",
        "5. Practical meaning",
        "6. Confidence",
        "7. What to watch next",
        "8. Source pack",
        "",
        "## Articles",
        "",
    ]

    for category in sorted(grouped):
        lines.append(f"### {category}")
        lines.append("")
        for article in grouped[category]:
            lines.append(f"#### {article.get('title') or 'Untitled'}")
            lines.append(f"- URL: {article.get('url') or ''}")
            lines.append(f"- Feed: {article.get('feed') or ''}")
            lines.append(f"- Author: {article.get('author') or 'unknown'}")
            lines.append(f"- Published: {article.get('published_at') or 'unknown'}")
            lines.append(f"- Status: {article.get('status') or 'unknown'}")
            lines.append(f"- Snippet: {article.get('content_snippet') or ''}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    unique_records = dedupe(load_jsonl(input_path))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"ai_bundle_{timestamp}.md"
    output_path.write_text(render_bundle(unique_records), encoding="utf-8", newline="\n")

    print(f"Wrote AI bundle with {len(unique_records)} unique articles to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
