"""`make agent`: the chat with the reviewer (spec §3); also `agent-ask`, `findings`, `findings-resolve`.

The `[y/N]` question before a finding is written is asked here, by code, never by the model (§8). An
empty answer, EOF or Ctrl-C at that prompt counts as no; EOF or Ctrl-C at the chat prompt ends the
session cleanly, with its episode saved (Review Focus 5).
"""

import argparse
import os
import sys
from datetime import datetime
from typing import Any, TextIO

LATER = "available from step 24"
COMMANDS = ("new", "quit", "up", "down", "reject", "forget")
HELP = "/up /down <comment> /reject <BP> <reason> /forget <key> /new /quit"


def parse_command(line: str) -> tuple[str, str] | None:
    """`/down shorter please` → ("down", "shorter please"); a question → None."""
    if not line.startswith("/"):
        return None
    name, _, rest = line[1:].partition(" ")
    return (name.lower(), rest.strip())


def console_confirm(stream_in: TextIO = sys.stdin, out: TextIO = sys.stdout):
    def confirm(prompt: str, _args: dict) -> bool:
        out.write(f"{prompt} [y/N] ")
        out.flush()
        try:
            answer = stream_in.readline()
        except (EOFError, KeyboardInterrupt):
            out.write("\n")
            return False
        return answer.strip().lower() in ("y", "yes")

    return confirm


def _short(value: Any, n: int = 60) -> str:
    text = str(value)
    return text if len(text) <= n else text[: n - 1] + "…"


def format_labels(labels: list[str]) -> str:
    """`["S21", "S22", "S23", "S17"]` → `[S21]–[S23], [S17]`: runs of consecutive labels collapsed."""
    numbers = [int(label.removeprefix("S")) for label in labels]
    runs: list[list[int]] = []
    for n in numbers:
        if runs and n == runs[-1][-1] + 1:
            runs[-1].append(n)
        else:
            runs.append([n])
    return ", ".join(
        f"[S{r[0]}]–[S{r[-1]}]" if len(r) > 1 else f"[S{r[0]}]" for r in runs
    )


def print_result(result: Any, out: TextIO) -> None:
    for c in result.state.calls:
        args = ", ".join(_short(v, 40) for v in c.input.values() if v is not None)
        labels = (c.outcome.data or {}).get("labels")
        if labels:
            got = format_labels(list(labels))
        else:
            got = _short(c.outcome.text.splitlines()[0] if c.outcome.text else "")
        out.write(f"  {c.name}({args}) → {got}\n")
    out.write(f"{result.answer}\n")
    state = result.state
    out.write(f"  ({result.stop} · {state.steps} model calls · ${state.usd:.4f})\n")


def run_chat(
    session: Any, stream_in: TextIO = sys.stdin, out: TextIO = sys.stdout
) -> int:
    out.write(f"team: {session.team} · session {session.session_id} · {HELP}\n")
    while True:
        out.write("> ")
        out.flush()
        try:
            line = stream_in.readline()
        except (EOFError, KeyboardInterrupt):
            line = ""
        if not line:  # EOF
            out.write("\n")
            break
        line = line.strip()
        if not line:
            continue
        command = parse_command(line)
        if command is None:
            try:
                print_result(session.ask(line), out)
            except (
                KeyboardInterrupt
            ):  # Ctrl-C while the model works ends the chat cleanly
                out.write("\n")
                break
            except Exception as error:  # noqa: BLE001 - one failed request never ends the chat
                out.write(f"error: {type(error).__name__}: {error}\n")
            continue
        name, _ = command
        if name == "quit":
            break
        if name == "new":
            session.new()
            out.write(f"new session {session.session_id}\n")
        elif name in COMMANDS:
            out.write(f"/{name}: {LATER}\n")
        else:
            out.write(f"unknown command /{name}; commands: {HELP}\n")
    session.close()
    return 0


def _build_session(args: argparse.Namespace, out: TextIO):
    from dotenv import load_dotenv

    from src.agent.config import load_agent_config
    from src.agent.faults import parse_faults
    from src.agent.llm import ToolUseLLM
    from src.agent.search_tool import build_agent_index
    from src.agent.session import AgentSession
    from src.agent.store import Store
    from src.agent.tracing import Tracer, make_langfuse
    from src.rag.config import load_config

    load_dotenv()  # ANTHROPIC_API_KEY (and the Langfuse keys, Task 22.9)
    cfg = load_agent_config()
    rag_cfg = load_config()
    team = os.environ.get("TEAM", "data-platform")
    store = Store(cfg.db_path, busy_timeout_s=cfg.limits.tool_timeout_s)
    tracer = Tracer(
        cfg.traces_dir / f"{datetime.now():%Y-%m-%d}.jsonl", langfuse=make_langfuse()
    )
    confirm = (lambda *_: False) if args.yes_never else console_confirm(sys.stdin, out)
    return AgentSession(
        cfg,
        llm=ToolUseLLM(cfg.model, cfg.effort, cfg.max_tokens_per_call),
        index=build_agent_index(rag_cfg, overlay=False),
        store=store,
        tracer=tracer,
        team=team,
        confirm=confirm,
        faults=parse_faults(args.faults or os.environ.get("FAULTS", "")),
        rag_cfg=rag_cfg,
    )


def _findings(resolve: int | None, out: TextIO) -> int:
    from src.agent.config import load_agent_config
    from src.agent.store import Store

    cfg = load_agent_config()
    store = Store(cfg.db_path)
    if resolve is not None:
        ok = store.resolve_finding(resolve, datetime.now().date())
        out.write(
            f"finding {resolve}: {'resolved' if ok else 'no open finding with this id'}\n"
        )
        return 0 if ok else 1
    rows = store.findings()
    if not rows:
        out.write("the findings registry is empty\n")
    out.writelines(
        f"#{f.id} {f.status:8s} {f.architecture_id} {f.best_practice} "
        f"[{f.severity} · {f.pillar}] opened {f.opened_at}"
        f"{f' resolved {f.resolved_at}' if f.resolved_at else ''}"
        f"{f' reopened ×{f.reopened_count}' if f.reopened_count else ''}: {f.summary}\n"
        for f in rows
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ask", help="one question, then exit (make agent-ask Q=…)")
    p.add_argument("--yes-never", action="store_true", help="answer no to every [y/N]")
    p.add_argument("--faults", help="FAULTS spec, e.g. 503:search_corpus")
    p.add_argument(
        "--findings", action="store_true", help="print the findings registry"
    )
    p.add_argument("--resolve", type=int, help="mark one finding resolved")
    args = p.parse_args(argv)
    out = sys.stdout
    if args.findings or args.resolve is not None:
        return _findings(args.resolve, out)
    session = _build_session(args, out)
    if args.ask:
        print_result(session.ask(args.ask), out)
        session.close()
        return 0
    return run_chat(session, sys.stdin, out)


if __name__ == "__main__":
    sys.exit(main())
