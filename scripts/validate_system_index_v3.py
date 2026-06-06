from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_PATH = REPO_ROOT / "indexes" / "semantic-documents.jsonl"
REQUIRED_FIELDS = {"id", "path", "heading", "domain", "status", "content_hash", "text"}


def main() -> int:
    if not CORPUS_PATH.exists():
        raise SystemExit(f"Missing corpus: {CORPUS_PATH}")

    domain_counts: Counter[str] = Counter()
    line_count = 0
    with CORPUS_PATH.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            line_count += 1
            record = json.loads(line)
            missing = REQUIRED_FIELDS - record.keys()
            if missing:
                raise SystemExit(f"Line {line_number} is missing fields: {sorted(missing)}")
            if not record["text"].strip():
                raise SystemExit(f"Line {line_number} has empty text")
            source_path = REPO_ROOT / record["path"]
            if not source_path.exists():
                raise SystemExit(f"Line {line_number} points to missing file: {record['path']}")
            domain_counts[record["domain"]] += 1

    if line_count == 0:
        raise SystemExit("The structural corpus is empty")

    print(f"Validated {line_count} records in {CORPUS_PATH}")
    for domain, count in sorted(domain_counts.items()):
        print(f"{domain}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
