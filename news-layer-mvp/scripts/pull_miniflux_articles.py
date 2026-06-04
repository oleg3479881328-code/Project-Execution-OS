from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_PATH = ROOT / ".env"


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def parse_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def strip_html(value: str | None) -> str:
    if not value:
        return ""
    text = re.sub(r"<[^>]+>", " ", value)
    text = re.sub(r"\s+", " ", unescape(text)).strip()
    return text


def snippet(value: str | None, limit: int = 400) -> str:
    text = strip_html(value)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def parse_args() -> argparse.Namespace:
    load_env_file(DEFAULT_ENV_PATH)
    parser = argparse.ArgumentParser(
        description="Pull fresh entries from Miniflux and export normalized JSONL."
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("MINIFLUX_BASE_URL", "http://localhost:8080"),
        help="Miniflux base URL.",
    )
    parser.add_argument(
        "--auth-value",
        default=os.getenv("MINIFLUX_AUTH_VALUE", ""),
        help="Value for the X-Auth-Token header.",
    )
    parser.add_argument(
        "--output-dir",
        default=os.getenv("NEWS_OUTPUT_DIR", str(ROOT / "outputs")),
        help="Directory for generated JSONL.",
    )
    parser.add_argument(
        "--max-articles",
        type=int,
        default=int(os.getenv("NEWS_MAX_ARTICLES", "50")),
        help="Maximum number of entries to request.",
    )
    parser.add_argument(
        "--category",
        default=os.getenv("NEWS_DEFAULT_CATEGORY", "all"),
        help="Category title in Miniflux or 'all'.",
    )
    parser.add_argument(
        "--include-read",
        action="store_true",
        default=parse_bool(os.getenv("NEWS_INCLUDE_READ", "false")),
        help="Include read entries as well as unread entries.",
    )
    parser.add_argument(
        "--lookback-hours",
        type=int,
        default=int(os.getenv("NEWS_LOOKBACK_HOURS", "48")),
        help="Only include entries published within this many hours.",
    )
    return parser.parse_args()


def api_get(base_url: str, auth_value: str, endpoint: str, params: dict[str, Any] | None = None) -> Any:
    query = f"?{urlencode(params, doseq=True)}" if params else ""
    url = urljoin(base_url.rstrip("/") + "/", endpoint.lstrip("/")) + query
    headers = {"Accept": "application/json"}
    if auth_value:
        headers["X-Auth-Token"] = auth_value
    request = Request(url, headers=headers, method="GET")
    try:
        with urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Miniflux request failed: {exc.code} {body}") from exc
    except URLError as exc:
        raise RuntimeError(f"Unable to reach Miniflux at {url}: {exc}") from exc


def resolve_category_id(base_url: str, auth_value: str, category_name: str) -> int | None:
    if category_name.lower() == "all":
        return None
    categories = api_get(base_url, auth_value, "/v1/categories")
    for category in categories:
        title = str(category.get("title", "")).strip().lower()
        if title == category_name.strip().lower():
            return int(category["id"])
    raise RuntimeError(f"Category '{category_name}' was not found in Miniflux.")


def normalize_entry(entry: dict[str, Any]) -> dict[str, Any]:
    feed = entry.get("feed") or {}
    return {
        "title": entry.get("title") or "",
        "url": entry.get("url") or "",
        "author": entry.get("author") or "",
        "published_at": entry.get("published_at") or "",
        "feed": feed.get("title") or "",
        "category": feed.get("category", {}).get("title") or "uncategorized",
        "status": entry.get("status") or "unknown",
        "content_snippet": snippet(entry.get("content")),
    }


def ensure_output_dir(path_value: str) -> Path:
    path = Path(path_value)
    if not path.is_absolute():
        path = Path.cwd() / path
    path.mkdir(parents=True, exist_ok=True)
    return path


def main() -> int:
    args = parse_args()
    category_id = resolve_category_id(args.base_url, args.auth_value, args.category)
    published_after = int(
        (datetime.now(timezone.utc) - timedelta(hours=args.lookback_hours)).timestamp()
    )

    params: dict[str, Any] = {
        "direction": "desc",
        "order": "published_at",
        "limit": args.max_articles,
        "status": ["unread", "read"] if args.include_read else ["unread"],
        "published_after": published_after,
    }
    if category_id is not None:
        params["category_id"] = category_id

    payload = api_get(args.base_url, args.auth_value, "/v1/entries", params=params)
    entries = payload.get("entries", [])
    output_dir = ensure_output_dir(args.output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"articles_{timestamp}.jsonl"

    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        for entry in entries:
            handle.write(json.dumps(normalize_entry(entry), ensure_ascii=False) + "\n")

    print(f"Wrote {len(entries)} articles to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
