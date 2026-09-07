"""Ingest the resume (or any PDF/DOCX) into the `my_docs` PGVector collection.

Idempotent: chunks are written under stable ids (`<source>-<n>`), so re-running
overwrites the previous version instead of appending a duplicate copy. Trailing
chunks left over from a longer earlier run are swept afterwards.

    python upload_resume/ingest.py                       # ingests public/…resume.pdf
    python upload_resume/ingest.py path/to/file.pdf --source cover-letter
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from markitdown import MarkItDown

BACKEND_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = BACKEND_DIR.parent
DEFAULT_PDF = REPO_ROOT / "public" / "Anh Hoang Phuc Nguyen - resume.pdf"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# How far past the current chunk count to sweep for leftovers from a previous,
# longer run. Deleting ids that do not exist is a no-op.
SWEEP_AHEAD = 200

# Load the backend's .env before importing main, which reads it at module scope.
load_dotenv(BACKEND_DIR / ".env")
sys.path.insert(0, str(BACKEND_DIR))


def extract_text(path: Path) -> str:
    if path.suffix.lower() not in (".pdf", ".docx"):
        raise ValueError(f"Unsupported file type '{path.suffix}'. Use PDF or DOCX.")
    return MarkItDown().convert(str(path)).text_content


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", default=str(DEFAULT_PDF), help="PDF or DOCX to ingest")
    parser.add_argument("--source", default="resume", help="metadata tag and id prefix")
    parser.add_argument("--dry-run", action="store_true", help="chunk and report, but do not write")
    args = parser.parse_args()

    path = Path(args.file).expanduser()
    if not path.is_file():
        print(f"error: no such file: {path}", file=sys.stderr)
        return 1

    database_url = os.getenv("DATABASE_URL")
    openai_key = os.getenv("OPENAI_API_KEY")
    missing = [n for n, v in (("DATABASE_URL", database_url), ("OPENAI_API_KEY", openai_key)) if not v]
    if missing:
        print(f"error: missing in {BACKEND_DIR / '.env'}: {', '.join(missing)}", file=sys.stderr)
        return 1

    text = extract_text(path)
    if not text.strip():
        print(f"error: extracted no text from {path.name}", file=sys.stderr)
        return 1

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    ).split_text(text)

    print(f"{path.name}: {len(text)} chars -> {len(chunks)} chunks (source='{args.source}')")
    if args.dry_run:
        for i, chunk in enumerate(chunks):
            preview = chunk[:80].replace("\n", " ")
            print(f"  [{args.source}-{i}] {preview}...")
        return 0

    # Deferred so --dry-run needs no database, and so it runs after load_dotenv.
    # main owns the store config (collection, embedding model, URL normalisation).
    from main import vector_store as store

    ids = [f"{args.source}-{i}" for i in range(len(chunks))]
    documents = [
        Document(
            page_content=chunk,
            metadata={"source": args.source, "file": path.name, "chunk": i},
        )
        for i, chunk in enumerate(chunks)
    ]

    store.add_documents(documents, ids=ids)
    print(f"upserted {len(ids)} chunks into '{store.collection_name}'")

    stale = [f"{args.source}-{i}" for i in range(len(chunks), len(chunks) + SWEEP_AHEAD)]
    store.delete(ids=stale)
    print(f"swept ids {args.source}-{len(chunks)}..{args.source}-{len(chunks) + SWEEP_AHEAD - 1}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
