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
REVIEW_FACTOR = (
    2.5  # a measured six-pillar review against the question estimate (step 22)
)


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
        self.yes = (
            0  # the questions answered yes: the only writes with permission (review I5)
        )

    def __call__(self, _prompt: str, _args: dict) -> bool:
        self.asked += 1
        answer = self.answers.pop(0) if self.answers else False
        self.yes += answer
        return answer


def task_config(cfg: AgentConfig, task: dict) -> AgentConfig:
    """A task may set its autonomy and tighten the limits for itself (spec §13, t24)."""
    # model_validate, not model_copy: a typo in a task's overrides must fail, not pass silently
    limits = {**cfg.limits.model_dump(), **task.get("limits", {})}
    return AgentConfig.model_validate(
        {**cfg.model_dump(), "autonomy": task["autonomy"], "limits": limits}
    )


def run_command(session: Any, command: str) -> str:
    """A scripted chat command between two questions of a task (spec §13, t18b / t29 / t30)."""
    if command.startswith("resolve "):  # `make findings-resolve` for one best practice
        return session.resolve(command.removeprefix("resolve ").strip())
    name, _, rest = command.removeprefix("/").partition(" ")
    if name == "up":
        return session.feedback_up()
    if name == "down":
        return session.feedback_down(rest.strip())
    if name == "reject":
        bp, _, reason = rest.strip().partition(" ")
        return session.reject(bp, reason.strip())
    raise ValueError(f"unknown task command {command!r}")


TOOL_CHECKS = (
    "tools_called",
    "tools_not_called",
    "tool_count",
    "distinct_args",
    "arg_contains",
)
MCP_TOOLS = ("list_architectures", "get_architecture", "get_service_quota")


def _rate(values: list[float]) -> dict:
    return {
        "mean": round(sum(values) / len(values), 4) if values else None,
        "min": round(min(values), 4) if values else None,
        "max": round(max(values), 4) if values else None,
    }


def aggregate(runs: list[list[dict]]) -> dict:
    """Metrics over one or more runs of the task set (lesson 11 `aggregate`, spec §13).

    The pass rate leaves `invalid` tasks out of the denominator (the thing they test did not happen).
    `unconfirmed_actions` counts findings written beyond the [y/N] questions asked (target 0).
    """
    rates = []
    for rows in runs:
        valid = [r for r in rows if r["status"] != "invalid"]
        rates.append(
            sum(r["status"] == "passed" for r in valid) / len(valid) if valid else 0.0
        )
    rows = [r for run in runs for r in run]
    valid = [r for r in rows if r["status"] != "invalid"]
    # "the share of tasks with the required tools called": over the tasks that require tools (their
    # `tools_called` checks), MCP ones separately; an error row is not a pass (review I4)
    required = [r for r in valid if r.get("required") and r["status"] != "error"]
    tools_ok = [
        r.get("status") == "passed" or "tools_called" not in r.get("failed", [])
        for r in required
    ]
    mcp = [
        ok
        for r, ok in zip(required, tools_ok, strict=True)
        if set(r["required"]) & set(MCP_TOOLS)
    ]
    ignoring_tools = []  # for the ablations: a pass if only tool checks failed (review I7)
    for run_rows in runs:
        v = [r for r in run_rows if r["status"] != "invalid"]
        ok = [
            r["status"] == "passed" or set(r.get("failed", [])) <= set(TOOL_CHECKS)
            for r in v
        ]
        ignoring_tools.append(sum(ok) / len(ok) if ok else 0.0)
    stops: dict[str, int] = {}
    for r in rows:
        for s in r.get("stops", []):
            stops[s] = stops.get(s, 0) + 1
    n = len(rows) or 1
    return {
        "runs": len(runs),
        "pass_rate": _rate(rates),
        "tools_ok": round(sum(tools_ok) / len(tools_ok), 4) if tools_ok else None,
        "tools_ok_mcp": round(sum(mcp) / len(mcp), 4) if mcp else None,
        "pass_rate_ignoring_tool_checks": _rate(ignoring_tools),
        "unconfirmed_actions": sum(
            max(0, r.get("writes", 0) - r.get("confirmed_yes", r.get("confirms", 0)))
            for r in rows
        ),
        "steps_per_task": round(sum(r["steps"] for r in rows) / n, 2),
        "usd_per_task": round(sum(r["usd"] for r in rows) / n, 6),
        "seconds_per_task": round(sum(r["seconds"] for r in rows) / n, 1),
        "usd": round(sum(r["usd"] for r in rows), 6),
        "stops": stops,
        "invalid": sum(r["status"] == "invalid" for r in rows),
        "errors": sum(r["status"] == "error" for r in rows),
    }


def stability(runs: list[list[dict]]) -> dict[str, float]:
    """The share of runs in which each task passed (lesson 9 / 11 `stability`)."""
    ids = [r["id"] for r in runs[0]]
    if any([r["id"] for r in run] != ids for run in runs):
        raise ValueError("stability needs runs of the same tasks (review M4)")
    return {
        tid: sum(r["status"] == "passed" for run in runs for r in run if r["id"] == tid)
        / len(runs)
        for tid in ids
    }


def write_metrics(run_dirs: list[Path]) -> int:
    """`--aggregate`: metrics and stability over several runs, written next to the first run."""
    runs = [
        json.loads((d / "summary.json").read_text(encoding="utf-8"))["tasks"]
        for d in run_dirs
    ]
    out = {
        "runs": [d.name for d in run_dirs],
        "metrics": aggregate(runs),
        "stability": stability(runs),
    }
    target = run_dirs[0].parent / f"metrics-{'+'.join(d.name for d in run_dirs)}.json"
    target.write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(out["metrics"], indent=2))
    print(f"wrote {target}")
    return 0


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
    answers, results, command_outputs = [], [], []
    for i, script in enumerate(task["sessions"]):
        if i > 0:
            session.new()
        for step in script:
            if "command" in step:
                command_outputs.append(run_command(session, step["command"]))
                continue
            confirm.answers = list(step.get("confirm", []))
            result = session.ask(step["user"])
            answers.append(result.answer)
            results.append(result)
    session.close()
    lines = (
        trace_path.read_text(encoding="utf-8").splitlines()
        if trace_path.exists()
        else []
    )
    traces = [json.loads(line) for line in lines]
    run = TaskRun(
        task_id=task["id"],
        answers=answers,
        results=results,
        traces=traces,
        findings=store.findings(),
        confirms_asked=confirm.asked,
        facts=store.facts(),
        command_outputs=command_outputs,
        confirmed_yes=confirm.yes,
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
    try:
        score = score_task(run, task)
    except Exception as error:  # noqa: BLE001 - a broken check must not lose the run (review I6)
        return {
            "id": task["id"],
            "kind": task["kind"],
            "status": "error",
            "failed": [],
            "error": f"check failed: {type(error).__name__}: {error}",
            "stops": [r.stop for r in run.results],
            "steps": sum(t["totals"].get("steps", 0) for t in run.traces),
            "usd": round(sum(t["totals"].get("usd", 0.0) for t in run.traces), 6),
            "seconds": round(time.perf_counter() - started, 1),
            "tools": [c["name"] for c in run.tool_calls()],
            "answers": run.answers,
        }
    send_task_score(tracer, run.traces, score)
    # a write is a recorded or reopened finding, or one committed before a dropped connection
    writes = sum(
        1
        for c in run.tool_calls()
        if c["name"] == "record_finding"
        and (
            (c.get("data") or {}).get("status") in ("recorded", "reopened")
            or c.get("result", "").startswith("ERROR: connection lost after the write")
        )
    )
    return {
        "writes": writes,
        "confirms": run.confirms_asked,
        "confirmed_yes": run.confirmed_yes,
        "required": sorted(
            {
                t
                for c in task["checks"]
                if c["type"] == "tools_called"
                for t in c["tools"]
            }
        ),
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
    run_dir: Path | None = None,
    ablation: str | None = None,
):
    def make(
        task: dict, store: Store, tracer: Tracer, confirm: ScriptedConfirm
    ) -> AgentSession:
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
            # an eval's /down rows stay in its run directory, never in the repo's file (review I1)
            candidates_path=(run_dir or Path(".")) / "feedback_candidates.jsonl",
            mcp=mcp_for(task.get("team", "data-platform")),
            ablation=ablation,
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
            # a review sends six pillar searches: measured about 2.5x a question (step 22)
            factor = REVIEW_FACTOR if step["user"].lower().startswith("review") else 1.0
            cost += (
                factor
                * (calls_in * price_in + EST_OUTPUT_TOKENS * price_out)
                / 1_000_000
            )
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
    p.add_argument(
        "--fixed-rag", action="store_true", help="ablation: one search, no search tool"
    )
    p.add_argument(
        "--no-memory", action="store_true", help="ablation: no memory block, no history"
    )
    p.add_argument(
        "--aggregate", nargs="+", metavar="RUN_DIR", help="metrics over these run dirs"
    )
    args = p.parse_args(argv)
    if args.aggregate:
        return write_metrics([Path(d) for d in args.aggregate])
    if args.fixed_rag and args.no_memory:
        raise SystemExit("one ablation at a time")
    args.ablation = (
        "fixed_rag" if args.fixed_rag else "no_memory" if args.no_memory else None
    )

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
    # the injection chunk is in every eval task, the brief's "corpus with problems" (spec §10)
    index = build_agent_index(rag_cfg, overlay=True)
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

    label = cfg.prompt_version + (
        f"-{args.ablation.replace('_', '-')}" if args.ablation else ""
    )
    run_dir = next_run_dir(RESULTS, datetime.now().date(), label)
    run_dir.mkdir(parents=True)
    make = _session_factory(
        cfg,
        llm,
        index,
        rag_cfg,
        run_id=run_dir.name,
        mcp_for=mcp_for,
        run_dir=run_dir,
        ablation=args.ablation,
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
        "ablation": args.ablation,
        "max_tokens_per_call": cfg.max_tokens_per_call,  # review M8: v3-run2 had 4000, run3 8000
        "limits": cfg.limits.model_dump(),
        "metrics": aggregate([rows]),
    }
    (run_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"passed {passed}/{len(rows)} · ${summary['usd']:.4f} · {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
