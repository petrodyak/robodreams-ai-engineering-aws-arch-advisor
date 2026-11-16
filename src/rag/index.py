"""The search index: chunk vectors in Qdrant plus a BM25 index over the same texts (spec §5).

Adapted from the lesson-7 `embed` / `build_index` and the lesson-8 `Retriever`:
- Both indexes read `index_text(chunk)`: the Contextual Header ("<title> > <section path>") on the
  first line, then the chunk text. The header gives a short chunk ("Implementation guidance ...")
  the context of the best practice it belongs to.
- Vectors are cached on disk by sha256(model + "\n" + text), so a re-run embeds only new or changed
  chunks, and a model change misses every key (vectors of two models are not comparable).
- The embedder and the reranker are passed in as functions. Unit tests pass fakes, so they need no
  model download; `default_embed_fn` / `default_rerank_fn` are the real fastembed ones.
"""

import hashlib
import json
import re
from collections.abc import Callable
from pathlib import Path

from qdrant_client import QdrantClient, models
from rank_bm25 import BM25Okapi

from src.rag.ingest.chunk import header
from src.rag.models import ChunkRecord

EmbedFn = Callable[[list[str]], list[list[float]]]
RerankFn = Callable[[str, list[str]], list[float]]

MODELS_DIR = Path(".cache/models")
EMBED_CACHE = Path(".cache/embeddings.json")


def load_chunks(path: Path) -> list[ChunkRecord]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [ChunkRecord.model_validate_json(line) for line in lines if line]


def index_text(chunk: ChunkRecord) -> str:
    """What both indexes see: the Contextual Header, a newline, the chunk text."""
    return header(chunk.title, chunk.section_path) + "\n" + chunk.text


def tokenize(text: str) -> list[str]:
    """Lower-case word tokens. "REL09-BP01." and "rel09-bp01" both give ["rel09", "bp01"]."""
    return re.findall(r"\w+", text.lower())


def embed_cached(
    texts: list[str], model: str, cache_path: Path, embed_fn: EmbedFn
) -> list[list[float]]:
    """Vectors for texts in input order; only texts missing from the cache reach embed_fn."""
    keys = [hashlib.sha256(f"{model}\n{t}".encode()).hexdigest() for t in texts]
    cache = (
        json.loads(cache_path.read_text(encoding="utf-8"))
        if cache_path.exists()
        else {}
    )
    missing = {k: t for k, t in zip(keys, texts, strict=True) if k not in cache}
    if missing:
        vectors = embed_fn(list(missing.values()))
        cache.update(
            (k, [round(float(x), 6) for x in v])
            for k, v in zip(missing, vectors, strict=True)
        )
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(cache), encoding="utf-8")
    return [cache[k] for k in keys]


def default_embed_fn(model: str, cache_path: Path = EMBED_CACHE) -> EmbedFn:
    """The real embedder: fastembed, loaded on the first cache miss, behind the disk cache."""
    loaded = None

    def raw(texts: list[str]) -> list[list[float]]:
        nonlocal loaded
        if loaded is None:
            from fastembed import TextEmbedding

            loaded = TextEmbedding(model, cache_dir=str(MODELS_DIR))
        return [v.tolist() for v in loaded.embed(texts)]

    return lambda texts: embed_cached(texts, model, cache_path, raw)


def default_rerank_fn(model: str) -> RerankFn:
    """The real reranker: fastembed's cross-encoder, one relevance score per document.

    Checked against fastembed 0.9.1: `TextCrossEncoder` lives in `fastembed.rerank.cross_encoder`,
    `rerank(query, documents, batch_size=64)` yields one float per document in input order.
    """
    from fastembed.rerank.cross_encoder import TextCrossEncoder

    encoder = TextCrossEncoder(model, cache_dir=str(MODELS_DIR))
    return lambda query, docs: [float(s) for s in encoder.rerank(query, docs)]


class Index:
    """Qdrant `:memory:` collection (cosine, payload = the chunk) and BM25 over the same chunks.

    Point id i is the position of the chunk in `chunks`, so a hit maps back to its ChunkRecord
    without parsing the payload.
    """

    collection = "rag"

    def __init__(
        self,
        chunks: list[ChunkRecord],
        *,
        embed_fn: EmbedFn,
        rerank_fn: RerankFn | None = None,
    ):
        if not chunks:
            raise ValueError("Index needs at least one chunk")
        self.chunks = chunks
        self.embed_fn = embed_fn
        self.rerank_fn = rerank_fn
        texts = [index_text(c) for c in chunks]
        vectors = embed_fn(texts)

        self.client = QdrantClient(":memory:")
        self.client.create_collection(
            self.collection,
            vectors_config=models.VectorParams(
                size=len(vectors[0]), distance=models.Distance.COSINE
            ),
        )
        points = [
            models.PointStruct(id=i, vector=v, payload=c.model_dump(mode="json"))
            for i, (c, v) in enumerate(zip(chunks, vectors, strict=True))
        ]
        for start in range(0, len(points), 512):
            self.client.upsert(self.collection, points=points[start : start + 512])

        self.bm25 = BM25Okapi([tokenize(t) for t in texts])

    def count(self) -> int:
        return self.client.count(self.collection).count


def main() -> None:
    """`make index`: build both indexes from the committed chunks and print their sizes."""
    import time

    from src.rag.config import load_config

    cfg = load_config()
    embed_fn = default_embed_fn(cfg.embed_model)
    for path in (Path("data/rag/chunks.jsonl"), Path("data/rag/chunks_fixed.jsonl")):
        start = time.perf_counter()
        index = Index(load_chunks(path), embed_fn=embed_fn)
        took = time.perf_counter() - start
        print(
            f"{path}: {index.count()} points, BM25 over {len(index.chunks)} texts, {took:.0f} s"
        )


if __name__ == "__main__":
    main()
