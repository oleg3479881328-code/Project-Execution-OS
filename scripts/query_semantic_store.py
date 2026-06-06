from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = REPO_ROOT / ".local" / "semantic-index" / "semantic-index.sqlite3"


def load_sentence_transformer():
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        message = (
            "Missing semantic runtime dependency. "
            "Install it with: python -m pip install -r semantic-requirements.txt"
        )
        raise SystemExit(message) from exc
    return SentenceTransformer


def read_metadata(connection: sqlite3.Connection) -> dict[str, str]:
    rows = connection.execute("SELECT key, value FROM metadata").fetchall()
    return {key: value for key, value in rows}


def collapse_excerpt(text: str, limit: int = 220) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def encode_query_embedding(model, query: str) -> np.ndarray:
    encoder = getattr(model, "encode_query", None) or model.encode
    embedding = encoder(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True,
    )[0]
    return np.asarray(embedding, dtype=np.float32)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Query the local SQLite semantic store.")
    parser.add_argument("query")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--domain")
    parser.add_argument("--status")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    if not args.db.exists():
        raise SystemExit(f"Missing semantic store: {args.db}")

    connection = sqlite3.connect(args.db)
    try:
        metadata = read_metadata(connection)
        model_name = metadata.get("model_name")
        if not model_name:
            raise SystemExit("The semantic store is missing model metadata")

        clauses = []
        params: list[str] = []
        if args.domain:
            clauses.append("domain = ?")
            params.append(args.domain)
        if args.status:
            clauses.append("status = ?")
            params.append(args.status)
        where_clause = f"WHERE {' AND '.join(clauses)}" if clauses else ""

        rows = connection.execute(
            f"""
            SELECT path, heading, domain, status, text, embedding_dim, embedding
            FROM chunks
            {where_clause}
            """,
            params,
        ).fetchall()
    finally:
        connection.close()

    if not rows:
        print("No matching candidates found for the selected filters.")
        return 0

    SentenceTransformer = load_sentence_transformer()
    model = SentenceTransformer(model_name)
    query_embedding = encode_query_embedding(model, args.query)

    scored_rows = []
    for path, heading, domain, status, text, embedding_dim, embedding_blob in rows:
        vector = np.frombuffer(embedding_blob, dtype=np.float32, count=embedding_dim)
        score = float(np.dot(query_embedding, vector))
        scored_rows.append((score, path, heading, domain, status, text))

    scored_rows.sort(key=lambda item: item[0], reverse=True)

    print("Semantic hits are navigation leads only. Open canonical files before relying on them.")
    print()
    for rank, (score, path, heading, domain, status, text) in enumerate(scored_rows[: args.limit], start=1):
        print(f"[{rank}] score={score:.4f} path={path} heading={heading}")
        print(f"    domain={domain} status={status}")
        print(f"    excerpt={collapse_excerpt(text)}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
