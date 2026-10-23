"""HW 1 entry point: one Run (model × prompt version × sampling) over the Working Set.

Usage:
    uv run python main.py --model claude --prompt v1 --sampling t0
    uv run python main.py ... --estimate     # input tokens and their cost; no paid call
    uv run python main.py ... --only 049-amazon-simple-storage-service.pdf
    uv run python main.py --model qwen2.5-7b --sampling t05
    uv run python main.py --sampling t05 --gold   # the 10 Golden Set documents only

Writes results/runs/jsonl/<run_id>.jsonl (contract items 11-12) and its readable mirror
results/runs/md/<run_id>.md. Documents already in the JSONL are skipped, so a run
interrupted halfway is resumed by running the same command again.
A document with no answer (network, rate limit, billing) gets no record (contract item 15):
the command then exits non-zero, and running it again retries just those documents. If
the same error comes back, it is permanent: metrics count the document as failed (item 18).
"""

import argparse
from collections import Counter

from dotenv import load_dotenv

from src.extract import pipeline
from src.extract.llm import ClaudeClient, OllamaClient
from src.extract.llm.claude import cost_usd

# Short model names, as they appear in run ids (contract item 11).
MODELS = {"claude": ClaudeClient, "qwen2.5-7b": OllamaClient}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--model", choices=sorted(MODELS), default="claude")
    parser.add_argument(
        "--prompt", default="v1", help="prompt version: prompts/extract_<v>.txt"
    )
    parser.add_argument(
        "--sampling", default="t0", help="a key of config/sampling.yaml"
    )
    parser.add_argument("--only", nargs="+", metavar="FILE", help="manifest file names")
    parser.add_argument(
        "--gold",
        action="store_true",
        help="the Golden Set documents only; the run id gets the __gold suffix",
    )
    parser.add_argument(
        "--estimate", action="store_true", help="count input tokens only (Claude)"
    )
    args = parser.parse_args()

    load_dotenv()  # ANTHROPIC_API_KEY, OLLAMA_HOST from .env
    prompt = pipeline.load_prompt(args.prompt)
    sampling = pipeline.load_sampling(args.sampling)
    docs = pipeline.load_manifest()
    if args.only:
        unknown = set(args.only) - {d.file for d in docs}
        if unknown:
            parser.error(f"not in data/raw/manifest.csv: {sorted(unknown)}")
        docs = [d for d in docs if d.file in args.only]
    if args.gold:
        docs = [d for d in docs if d.gold]
    if args.estimate and args.model != "claude":
        parser.error("--estimate counts Claude tokens; a local model costs $0")
    client = MODELS[args.model]()
    run_id = pipeline.make_run_id(
        args.model, prompt.version, sampling.name, gold=args.gold
    )

    if args.estimate:
        estimate(client, docs, prompt)
        return

    out_path = pipeline.RUNS_DIR / f"{run_id}.jsonl"
    md_path = pipeline.RUNS_MD_DIR / f"{run_id}.md"
    print(f"Run {run_id}: {len(docs)} document(s) -> {out_path} (readable: {md_path})")
    result = pipeline.run(client, docs, prompt, sampling, out_path, md_path=md_path)
    records, lost = result.records, result.lost

    statuses = Counter(r.status.value for r in records)
    # paid tokens include those of documents that ended without a record (finding F10)
    tokens_in = sum(r.usage.input_tokens for r in records) + lost.input_tokens
    tokens_out = sum(r.usage.output_tokens for r in records) + lost.output_tokens
    print(
        f"Done: {len(records)} new record(s) {dict(statuses)}; "
        f"in {tokens_in:,} / out {tokens_out:,} tokens"
        + (
            f" ≈ ${cost_usd(tokens_in, tokens_out):.2f}"
            if args.model == "claude"
            else ""
        )
    )
    if lost.input_tokens or lost.output_tokens:
        print(
            f"  of which lost (paid, no record): in {lost.input_tokens:,} / "
            f"out {lost.output_tokens:,} tokens"
        )
    missing = pipeline.missing_files(docs, out_path)
    if missing:
        print(f"{len(missing)} document(s) still without a record: {missing}")
        raise SystemExit(
            "run the same command again to retry them; if the same error comes back, "
            "it is permanent and metrics count the document as failed"
        )


def estimate(client: ClaudeClient, docs: list[pipeline.Document], prompt) -> None:
    """The input side of the cost, measured; the output side is known only after a run."""
    total = 0
    for doc in docs:
        messages = [
            {"role": "user", "content": prompt.user_message(doc.service, doc.text())}
        ]
        n = client.count_input_tokens(prompt.system, messages)
        total += n
        print(f"{doc.file}: {n:,} input tokens")
    print(
        f"Total: {total:,} input tokens ≈ ${cost_usd(total, 0):.2f} for the first answers "
        "(output tokens and repair calls come on top)"
    )


if __name__ == "__main__":
    main()
