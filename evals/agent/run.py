"""`make agent-eval`: run the agent task set and score it (spec §13). `make agent-estimate`: cost first.

Every task gets a fresh SQLite store and its own trace file under the run directory
`evals/agent/results/<YYYY-MM-DD>-<prompt version>-run<N>/`, which is never overwritten. The
confirmations are scripted per user turn (`"confirm": [true, false]`; a missing answer is no). Each
task's pass / fail is also sent as a score on its traces (Langfuse, Task 22.9).

    uv run python -m evals.agent.run --tasks t19,t22a
    uv run python -m evals.agent.run --estimate --tasks t19,t22a
"""

import argparse
import json
import time
from collections.abc import Callable
from contextlib import ExitStack
from dataclasses import asdict
from datetime import date, datetime
from pathlib import Path
from typing import Any

from evals.agent.checks import TaskRun, TaskScore, score_task
from src.agent.config import AgentConfig, load_agent_config
from src.agent.faults import parse_faults
from src.agent.mcp_client import McpTools
from src.agent.session import AgentSession, system_blocks
from src.agent.store import Store
from src.agent.tracing import Tracer, make_langfuse
from src.rag.llm import PRICES

TASKS = Path("evals/agent/tasks.jsonl")
RESULTS = Path("evals/agent/results")
# spec §16: a question task is about 4 model calls; the input grows by the tool results
EST_CALLS = 4
EST_GROWTH_TOKENS = 1_500
EST_OUTPUT_TOKENS = 1_500


def load_tasks(path: Path = TASKS) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def next_run_dir(root: Path, today: date, prompt_version: str) -> Path:
    n = 1
    while (root / f"{today.isoformat()}-{prompt_version}-run{n}").exists():
        n += 1
    return root / f"{today.isoformat()}-{prompt_version}-run{n}"


class ScriptedConfirm:
    """Answers the [y/N] questions of one user turn from the task script; no answer left is no."""

    def __init__(self) -> None:
        self.answers: list[bool] = []
        self.asked = 0

    def __call__(self, _prompt: str, _args: dict) -> bool:
        self.asked += 1
        return self.answers.pop(0) if self.answers else False


def task_config(cfg: AgentConfig, task: dict) -> AgentConfig:
    """A task may set its autonomy and tighten the limits for itself (spec §13, t24)."""
    # model_validate, not model_copy: a typo in a task's overrides must fail, not pass silently
    limits = {**cfg.limits.model_dump(), **task.get("limits", {})}
    return AgentConfig.model_validate(
        {**cfg.model_dump(), "autonomy": task["autonomy"], "limits": limits}
    )


def send_task_score(tracer: Tracer, traces: list[dict], score: TaskScore) -> None:
    """Each task's pass / fail as a Langfuse score on every trace it made (spec §12)."""
    comment = score.status + (f": {', '.join(score.failed)}" if score.failed else "")
    value = 1.0 if score.status == "passed" else 0.0
    for trace in traces:
        tracer.score(trace["trace_id"], "task_passed", value, comment)


def run_task(
    task: dict,
    make_session: Callable[[dict, Store, Tracer, ScriptedConfirm], Any],
    run_dir: Path,
    *,
    langfuse: Any = None,
) -> tuple[TaskRun, Tracer]:
    store = Store(run_dir / "db" / f"{task['id']}.db")
    trace_path = run_dir / "traces" / f"{task['id']}.jsonl"
    tracer = Tracer(trace_path, langfuse=langfuse)
    confirm = ScriptedConfirm()
    session = make_session(task, store, tracer, confirm)
    answers, results = [], []
    for i, script in enumerate(task["sessions"]):
        if i > 0:
            session.new()
        for step in script:
            if "command" in step:
                raise NotImplementedError(f"{task['id']}: commands arrive in step 24")
            confirm.answers = list(step.get("confirm", []))
            result = session.ask(step["user"])
            answers.append(result.answer)
            results.append(result)
    session.close()
    traces = [
        json.loads(line) for line in trace_path.read_text(encoding="utf-8").splitlines()
    ]
    run = TaskRun(
        task_id=task["id"],
        answers=answers,
        results=results,
        traces=traces,
        findings=store.findings(),
        confirms_asked=confirm.asked,
    )
    return run, tracer


def task_row(
    task: dict, make: Callable, run_dir: Path, *, langfuse: Any = None
) -> dict:
    """Run and score one task; an exception makes it `error` and the run goes on (final review)."""
    started = time.perf_counter()
    try:
        run, tracer = run_task(task, make, run_dir, langfuse=langfuse)
    except Exception as error:  # noqa: BLE001 - one broken task must not lose the others' results
        trace_path = run_dir / "traces" / f"{task['id']}.jsonl"
        traces = (
            [
                json.loads(line)
                for line in trace_path.read_text(encoding="utf-8").splitlines()
            ]
            if trace_path.exists()
            else []
        )
        return {
            "id": task["id"],
            "kind": task["kind"],
            "status": "error",
            "failed": [],
            "error": f"{type(error).__name__}: {error}",
            "stops": [t.get("stop") for t in traces],
            "steps": sum(t["totals"].get("steps", 0) for t in traces),
            "usd": round(sum(t["totals"].get("usd", 0.0) for t in traces), 6),
            "seconds": round(time.perf_counter() - started, 1),
            "tools": [c["name"] for t in traces for c in t.get("tool_calls", [])],
            "answers": [],
        }
    score = score_task(run, task)
    send_task_score(tracer, run.traces, score)
    return {
        "id": task["id"],
        "kind": task["kind"],
        **asdict(score),
        "stops": [r.stop for r in run.results],
        "steps": sum(t["totals"].get("steps", 0) for t in run.traces),
        "usd": round(sum(t["totals"].get("usd", 0.0) for t in run.traces), 6),
        "seconds": round(time.perf_counter() - started, 1),
        "tools": [c["name"] for c in run.tool_calls()],
        "answers": run.answers,
    }


def _session_factory(
    cfg: AgentConfig,
    llm: Any,
    index: Any,
    rag_cfg: Any,
    run_id: str | None = None,
    mcp_for: Callable[[str], Any] = lambda _team: None,
):
    def make(
        task: dict, store: Store, tracer: Tracer, confirm: ScriptedConfirm
    ) -> AgentSession:
        if task.get("overlay"):
            raise NotImplementedError(f"{task['id']}: the overlay arrives in step 24")
        return AgentSession(
            task_config(cfg, task),
            llm=llm,
            index=index,
            store=store,
            tracer=tracer,
            team=task.get("team", "data-platform"),
            confirm=confirm,
            faults=parse_faults(task["faults"]),
            rag_cfg=rag_cfg,
            # the backoff of injected faults never waits in an eval (§7)
            sleep=lambda _: None,
            run_id=run_id,
            mcp=mcp_for(task.get("team", "data-platform")),
        )

    return make


def estimate(
    tasks: list[dict], cfg: AgentConfig, llm: Any, make_tools: Callable[[], list[dict]]
) -> float:
    """Count the first request of each user turn (free endpoint) and extrapolate (spec §16)."""
    price_in, price_out = PRICES[cfg.model]
    system, tools = system_blocks(cfg, "data-platform"), make_tools()
    total = 0.0
    for task in tasks:
        turns = [s for sess in task["sessions"] for s in sess if "user" in s]
        cost = 0.0
        for step in turns:
            first = llm.count_tokens(
                system, tools, [{"role": "user", "content": step["user"]}]
            )
            calls_in = sum(first + i * EST_GROWTH_TOKENS for i in range(EST_CALLS))
            cost += (calls_in * price_in + EST_OUTPUT_TOKENS * price_out) / 1_000_000
        print(f"  {task['id']:6s} {len(turns)} turn(s)  ≈ ${cost:.4f}")
        total += cost
    print(f"estimate for {len(tasks)} task(s): ≈ ${total:.4f}")
    return total


def main(argv: list[str] | None = None) -> int:
    from dotenv import load_dotenv

    from src.agent.llm import ToolUseLLM
    from src.agent.search_tool import build_agent_index
    from src.rag.config import load_config

    p = argparse.ArgumentParser(description="Run the agent task set (spec §13).")
    p.add_argument("--tasks", help="comma-separated task ids (default: all)")
    p.add_argument(
        "--estimate", action="store_true", help="print the cost estimate, run nothing"
    )
    p.add_argument("--fixed-rag", action="store_true", help="ablation (Task 25.2)")
    p.add_argument("--no-memory", action="store_true", help="ablation (Task 25.2)")
    args = p.parse_args(argv)
    if args.fixed_rag or args.no_memory:
        raise SystemExit("not yet: the ablations arrive in Task 25.2")

    load_dotenv()  # ANTHROPIC_API_KEY
    cfg = load_agent_config()
    tasks = load_tasks()
    if args.tasks:
        wanted = args.tasks.split(",")
        tasks = [t for t in tasks if t["id"] in wanted]
        missing = set(wanted) - {t["id"] for t in tasks}
        if missing:
            raise SystemExit(f"unknown task ids: {', '.join(sorted(missing))}")
    llm = ToolUseLLM(cfg.model, cfg.effort, cfg.max_tokens_per_call)
    rag_cfg = load_config()
    index = build_agent_index(rag_cfg, overlay=False)
    with ExitStack() as stack:
        servers: dict[str, McpTools] = {}

        def mcp_for(team: str) -> McpTools:
            """One MCP server per team, started on first use and closed at the end of the run."""
            if team not in servers:
                servers[team] = stack.enter_context(McpTools(team))
            return servers[team]

        return _run(args, cfg, llm, index, rag_cfg, tasks, mcp_for)


def _run(args, cfg, llm, index, rag_cfg, tasks, mcp_for) -> int:
    make = _session_factory(cfg, llm, index, rag_cfg, mcp_for=mcp_for)

    if args.estimate:
        probe = make(
            {"id": "probe", "autonomy": cfg.autonomy, "faults": ""},
            Store(":memory:"),
            Tracer(Path("/dev/null")),
            ScriptedConfirm(),
        )
        estimate(tasks, cfg, llm, lambda: probe.tools)
        return 0

    run_dir = next_run_dir(RESULTS, datetime.now().date(), cfg.prompt_version)
    run_dir.mkdir(parents=True)
    make = _session_factory(
        cfg, llm, index, rag_cfg, run_id=run_dir.name, mcp_for=mcp_for
    )
    langfuse = make_langfuse()
    rows = []
    for task in tasks:
        row = task_row(task, make, run_dir, langfuse=langfuse)
        rows.append(row)
        failed = ",".join(row.get("failed", [])) or row.get("error", "-")[:30]
        print(
            f"{task['id']:6s} {row['status']:8s} {failed:30s} steps {row['steps']:2d}  ${row['usd']:.4f}"
        )
    passed = sum(r["status"] == "passed" for r in rows)
    summary = {
        "prompt_version": cfg.prompt_version,
        "tools_version": cfg.tools_version,
        "model": cfg.model,
        "effort": cfg.effort,
        "tasks": rows,
        "passed": passed,
        "invalid": sum(r["status"] == "invalid" for r in rows),
        "errors": sum(r["status"] == "error" for r in rows),
        "total": len(rows),
        "usd": round(sum(r["usd"] for r in rows), 6),
    }
    (run_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"passed {passed}/{len(rows)} · ${summary['usd']:.4f} · {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
