"""Index (src/rag/index.py) and config (src/rag/config.py): cache, tokenizer, Qdrant + BM25."""

from pathlib import Path

from src.rag.config import RagConfig, load_config
from src.rag.index import Index, embed_cached, index_text, tokenize
from src.rag.models import ChunkRecord
from tests.rag_search_fixtures import CHUNKS, fake_embed


class CountingEmbed:
    def __init__(self):
        self.texts: list[str] = []

    def __call__(self, texts: list[str]) -> list[list[float]]:
        self.texts += texts
        return fake_embed(texts)


def test_cache_second_run_embeds_nothing(tmp_path: Path):
    cache = tmp_path / "embeddings.json"
    counting = CountingEmbed()
    first = embed_cached(["alpha", "beta", "alpha"], "m", cache, counting)
    assert counting.texts == ["alpha", "beta"]  # a repeated text is embedded once

    again = CountingEmbed()
    second = embed_cached(["alpha", "beta"], "m", cache, again)
    assert again.texts == []
    assert second == first[:2]


def test_cache_key_includes_the_model(tmp_path: Path):
    cache = tmp_path / "embeddings.json"
    embed_cached(["alpha"], "model-a", cache, fake_embed)
    counting = CountingEmbed()
    embed_cached(["alpha"], "model-b", cache, counting)
    assert counting.texts == ["alpha"]  # vectors of another model are not reused


def test_tokenize_ids():
    assert tokenize("REL09-BP01.") == tokenize("rel09-bp01")
    assert "rel09" in tokenize("REL09-BP01.")
    assert "bp01" in tokenize("REL09-BP01.")


def test_index_text_has_the_contextual_header():
    c = CHUNKS[0]
    assert index_text(c) == (
        "wa-reliability title > Failure management > "
        "REL09-BP01 Identify and back up all data\n" + c.text
    )


def test_index_holds_all_chunks():
    index = Index(CHUNKS, embed_fn=fake_embed)
    assert index.count() == len(CHUNKS)
    points, _ = index.client.scroll(index.collection, limit=100, with_payload=True)
    restored = {ChunkRecord.model_validate(p.payload).chunk_id for p in points}
    assert restored == {c.chunk_id for c in CHUNKS}
    assert ChunkRecord.model_validate(points[0].payload) == CHUNKS[points[0].id]


def test_config_loads_the_pinned_values():
    cfg = load_config(Path("config/rag.yaml"))
    assert isinstance(cfg, RagConfig)
    assert cfg.embed_model == "BAAI/bge-small-en-v1.5"
    assert cfg.rerank_model == "Xenova/ms-marco-MiniLM-L-6-v2"
    assert (cfg.candidates, cfg.rrf_k, cfg.k, cfg.context_budget) == (20, 60, 5, 3000)
    assert cfg.answer_model == "claude-haiku-5-5"
    assert cfg.judge_model == "claude-sonnet-5-5"
