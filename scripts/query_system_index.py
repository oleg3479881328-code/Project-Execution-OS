#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "indexes/semantic-documents.jsonl"


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[\w-]+", text.lower(), flags=re.UNICODE))


def main() -> None:
    parser = argparse.ArgumentParser(description="Search semantic-ready repository chunks with lexical ranking")
    parser.add_argument("query")
    parser.add_argument("--domain")
    parser.add_argument("--status")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    wanted = tokens(args.query)
    rows = []
    with CORPUS.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            if args.domain and row.get("domain") != args.domain:
                continue
            if args.status and row.get("status") != args.status:
                continue
            haystack = " ".join([
                row.get("source_path", ""),
                row.get("heading", ""),
                row.get("text", ""),
            ])
            overlap = wanted & tokens(haystack)
            if not overlap:
                continue
            score = len(overlap) / max(len(wanted), 1)
            rows.append((score, row))

    rows.sort(key=lambda item: (-item[0], item[1].get("source_path", "")))
    for score, row in rows[: args.limit]:
        print(f"[{score:.2f}] {row.get('source_path')} :: {row.get('heading')}")
        text = row.get("text", "").replace("\n", " ")
        print(text[:500])
        print()


if __name__ == "__main__":
    main()
