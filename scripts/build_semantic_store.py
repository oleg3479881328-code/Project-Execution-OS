from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO_ROOT / "indexes" / "semantic-documents.jsonl"
DEFAULT_OUTPUT = REPO_ROOT / ".local" / "semantic-index" / "semantic-index.sqlite3"
DEFAULT_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


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


def load_records(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing structural corpus: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def encode_documents(model, records: list[dict[str, str]], batch_size: int) -> np.ndarray:
    texts = [f"{record['heading']}\n\n{record['text']}" for record in records]
    encoder = getattr(model, "encode_document", None) or model.encode
    embeddings = encoder(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
        convert_to_numpy=True,
    )
    return np.asarray(embeddings, dtype=np.float32)


def initialize_database(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS chunks (
            id TEXT PRIMARY KEY,
            path TEXT NOT NULL,
            heading TEXT NOT NULL,
            domain TEXT NOT NULL,
            status TEXT NOT NULL,
            content_hash TEXT NOT NULL,
            text TEXT NOT NULL,
            embedding_dim INTEGER NOT NULL,
            embedding BLOB NOT NULL
        );
        DELETE FROM metadata;
        DELETE FROM chunks;
        """
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the local SQLite semantic store.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--batch-size", type=int, default=32)
    args = parser.parse_args()

    SentenceTransformer = load_sentence_transformer()
    records = load_records(args.input)
    if not records:
        raise SystemExit("Structural corpus is empty")

    model = SentenceTransformer(args.model)
    embeddings = encode_documents(model, records, args.batch_size)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp_output = args.output.with_suffix(args.output.suffix + ".tmp")
    if temp_output.exists():
        temp_output.unlink()

    connection = sqlite3.connect(temp_output)
    try:
        initialize_database(connection)
        rows = [
            (
                record["id"],
                record["path"],
                record["heading"],
                record["domain"],
                record["status"],
                record["content_hash"],
                record["text"],
                int(embedding.shape[0]),
                embedding.tobytes(),
            )
            for record, embedding in zip(records, embeddings, strict=True)
        ]
        connection.executemany(
            """
            INSERT INTO chunks (
                id, path, heading, domain, status, content_hash, text, embedding_dim, embedding
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )
        built_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        metadata_rows = [
            ("model_name", args.model),
            ("chunk_count", str(len(rows))),
            ("embedding_dim", str(int(embeddings.shape[1]))),
            ("built_at", built_at),
            ("source_corpus", str(args.input)),
        ]
        connection.executemany("INSERT INTO metadata (key, value) VALUES (?, ?)", metadata_rows)
        connection.commit()
    finally:
        connection.close()

    temp_output.replace(args.output)
    print(f"Built semantic store with {len(records)} chunks at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
