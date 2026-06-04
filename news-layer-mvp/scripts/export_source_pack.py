from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export a deduplicated URL-only source pack from article JSONL."
    )
    parser.add_argument("--input", required=True, help="Path to articles JSONL.")
    parser.add_argument(
        "--output-dir",
        default=str(ROOT / "outputs"),
        help="Directory for exported source pack.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    seen: set[str] = set()
    urls: list[str] = []

    with input_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            url = (record.get("url") or "").strip()
            if not url or url in seen:
                continue
            seen.add(url)
            urls.append(url)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"source_pack_{timestamp}.txt"
    output_path.write_text("\n".join(urls) + ("\n" if urls else ""), encoding="utf-8", newline="\n")

    print(f"Wrote {len(urls)} source URLs to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
