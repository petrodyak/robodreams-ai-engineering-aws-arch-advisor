"""AgentSession: the composition root that the chat (`cli.py`) and the eval runner share (spec §6.1).

One session = one row in `sessions`; its labels, messages and findings context live as long as it.
What the first request carries (spec §6.1): the system prompt with today and the team, the tool
definitions, then the history of this session and the question. The memory block and the history
window with its summary arrive in Task 24.3; the MCP tools in Task 23.3 (`mcp=None` until then).

`system` and `tools` are built once per session and sent unchanged on every call, so the prompt-cache
prefix stays stable (spec §6).
"""

import json
import time
from collections.abc import Callable
from datetime import date
from pathlib import Path
from typing import Any

from src.agent.config import AgentConfig
from src.agent.context import build_messages, episode_text, make_remember, memory_block
from src.agent.critic import critic
from src.agent.faults import Fault, apply_faults
from src.agent.findings import (
    BP_PATTERN,
    Confirm,
    FindingContext,
    make_record_finding,
    normalize_bp,
)
from src.agent.loop import CallRecord, TurnResult, run_turn
from src.agent.search_tool import (
    OVERLAY_DOC,
    SearchArgs,
    SearchTool,
    best_practice_ids,
    load_supersedes,
)
from src.agent.store import Store
from src.agent.tools import ToolEntry, load_descriptions, tool_spec
from src.agent.tracing import Tracer
from src.rag.config import RagConfig, load_config
from src.rag.index import Index

PROMPTS_DIR = Path("prompts")


def service_stopped(calls: list) -> bool:
    """A tool's service was unavailable or its budget used up: the only reasons a review may leave a
    pillar "not covered" (D25; step 24 review M7). An argument error is not one of them."""
    reasons = (
        "ERROR: service unavailable",
        "ERROR: MCP server unavailable",
        "budget for this tool is used up",
        "ERROR: the quota service returned an unexpected format",  # the schema fault (review M5)
        "ERROR: the registry service returned an unexpected format",
    )
    return any(c.outcome.is_error and c.outcome.text.startswith(reasons) for c in calls)


def rejection_note(rows: list[dict]) -> str:
    """`Rejected by the user for this version: REL01-BP01 (<reason>)`, or "" (spec §6.1)."""
    if not rows:
        return ""
    items = "; ".join(f"{r['best_practice']} ({r['reason']})" for r in rows)
    return f"Rejected by the user for this version: {items}"


def system_blocks(
    cfg: AgentConfig, team: str, prompts_dir: Path = PROMPTS_DIR
) -> list[dict]:
    path = prompts_dir / f"agent_system_{cfg.prompt_version}.txt"
    text = path.read_text(encoding="utf-8")
    text = text.replace("{today}", cfg.today.isoformat()).replace("{team}", team)
    return [{"type": "text", "text": text}]


class AgentSession:
    def __init__(
        self,
        cfg: AgentConfig,
        *,
        llm: Any,
        index: Index,
        store: Store,
        tracer: Tracer,
        team: str,
        confirm: Confirm,
        faults: list[Fault] | None = None,
        mcp: Any = None,
        rag_cfg: RagConfig | None = None,
        supersedes: dict[str, str] | None = None,
        sleep: Callable[[float], None] = time.sleep,
        on_tool: Callable[[Any], None] = lambda _: None,
        run_id: str | None = None,
        candidates_path: Path = Path("evals/agent/feedback_candidates.jsonl"),
        ablation: str | None = None,  # "fixed_rag" or "no_memory" (spec §13, Task 25.2)
        today_fn: Callable[[], date] = date.today,
    ):
        self.cfg = cfg
        self.llm = llm
        self.index = index
        self.store = store
        self.tracer = tracer
        self.team = team
        self.confirm = confirm
        self.faults = faults or []
        self.mcp = (
            mcp  # McpTools (src/agent/mcp_client.py), or None for local tools only
        )
        self.rag_cfg = rag_cfg or load_config()
        # real edition metadata, always on (§10); a superseded edition and the planted overlay chunk
        # are never the source of a finding (§8)
        self.supersedes = load_supersedes() if supersedes is None else supersedes
        self.sleep = sleep
        self.on_tool = on_tool
        self.run_id = run_id
        self.candidates_path = candidates_path
        if ablation not in (None, "fixed_rag", "no_memory"):
            raise ValueError(f"unknown ablation {ablation!r}")
        self.ablation = ablation
        self.last_trace_id: str | None = None
        self.last_result: TurnResult | None = None
        self.last_question = ""
        # cfg.today is frozen for the prompt and the editions (§10); purge, finding dates and
        # episodes use the real date (final review, finding 4)
        self.today_fn = today_fn
        self.blocked_docs: set[str] = set(self.supersedes) | {OVERLAY_DOC}
        # ids of current documents only: not of the planted chunk or a superseded edition (review M9)
        self.known_bp = best_practice_ids(
            [c for c in index.chunks if c.doc_id not in self.blocked_docs]
        )
        self.system = system_blocks(cfg, team)
        self.descriptions = load_descriptions(cfg.tools_version)
        self._question = ""  # the user's message of the current turn (D24)
        self._fixed_context = (
            ""  # --fixed-rag: the chunks of the one search of this request
        )
        self._rejected_now: list[
            str
        ] = []  # /reject since the last answer, for its meta
        store.purge_sessions(today_fn())
        self._start()

    def _start(self) -> None:
        self.session_id = self.store.new_session(self.team)
        # architectures read in this session, id -> hash; filled by the get_architecture wrapper
        # (23.3) and fresh per session: "read in this session" (spec §8; final review, finding 5)
        self.arch_hashes: dict[str, str] = {}
        self.last_arch: str | None = (
            None  # the architecture read last; `/reject` applies to it
        )
        # feedback rates an answer of this session only (review M4)
        self.last_trace_id: str | None = None
        self.last_result: TurnResult | None = None
        self.last_question = ""
        self.questions: list[str] = []
        self.search_tool = SearchTool(
            self.index,
            self.store,
            self.session_id,
            k=self.cfg.k,
            rag_cfg=self.rag_cfg,
            relevance_threshold=self.cfg.relevance_threshold,
            supersedes=self.supersedes,
        )
        self.findings_ctx = FindingContext(
            store=self.store,
            session_id=self.session_id,
            autonomy=self.cfg.autonomy,
            confirm=self.confirm,
            known_bp=self.known_bp,
            arch_hashes=self.arch_hashes,  # a fresh dict per session (finding 5)
            blocked_docs=self.blocked_docs,
            today=self.today_fn(),
            faults=self.faults,
            rejected=self._rejection,
        )
        local = {
            "search_corpus": ToolEntry(
                fn=self.search_tool.search,
                args_model=SearchArgs,
                read_only=True,
                finish=self.search_tool.label,
            ),
            "record_finding": make_record_finding(self.findings_ctx),
            # gated in code (D24): saves only what the user typed in this turn
            "remember": make_remember(
                self.store, self.cfg.autonomy, lambda: self._question
            ),
        }
        if self.ablation == "fixed_rag":  # the search is not the model's decision (§13)
            local.pop("search_corpus")
        self.tools = [
            tool_spec(name, entry.args_model, self.descriptions)
            for name, entry in local.items()
        ]
        if self.mcp is not None:  # the three registry tools of the MCP server (step 23)
            local.update(
                self.mcp.entries(
                    self.faults,
                    arch_hashes=self.arch_hashes,
                    timeout=self.cfg.limits.tool_timeout_s,
                    on_architecture=self._architecture_read,
                )
            )
            self.tools += self.mcp.specs()
        self.registry = apply_faults(local, self.faults, sleep=self.sleep)

    def _messages(self, question: str) -> list[dict]:
        """memory block → summary of the dropped history → recent history → question (§6.1, §11)."""
        if self.ablation == "no_memory":  # no memory block and no history (§13)
            return [{"role": "user", "content": question}]
        if (
            self._fixed_context
        ):  # --fixed-rag: the one search's chunks before the question (§13)
            question = f"{self._fixed_context}\n\n{question}"
        memory = memory_block(self.store.facts(), self.rules(), self.store.episodes())
        history = self.store.history(self.session_id)
        return build_messages(memory, history, question, self.cfg.history_budget_tokens)

    def rules(self) -> list[str]:
        """Feedback rules for the form of answers, from `/down <comment>` (§11)."""
        return self.store.rules()

    # feedback (Task 24.4, spec §6.1, §11) ------------------------------------------------------

    def _architecture_read(self, architecture_id: str, architecture_hash: str) -> str:
        """Called when get_architecture returned a version: remember it, attach its rejections."""
        self.last_arch = architecture_id
        return rejection_note(self.store.rejections(architecture_id, architecture_hash))

    def _rejection(
        self, architecture_id: str, architecture_hash: str, bp: str
    ) -> dict | None:
        rows = self.store.rejections(architecture_id, architecture_hash)
        return next((r for r in rows if r["best_practice"] == bp), None)

    def _take_rejected(self) -> list[str]:
        taken, self._rejected_now = self._rejected_now, []
        return taken

    def rejected_bp(self) -> set[str]:
        """Best practices rejected for the versions of the architectures read in this session."""
        return {
            r["best_practice"]
            for arch, h in self.arch_hashes.items()
            for r in self.store.rejections(arch, h)
        }

    def _score(self, value: int, comment: str) -> str | None:
        if self.last_trace_id is None:
            return "nothing to rate yet: ask a question first"
        self.store.add_score(self.session_id, self.last_trace_id, value, comment)
        self.tracer.score(
            self.last_trace_id, "user_feedback", float(value), comment or None
        )
        return None

    def feedback_up(self) -> str:
        return self._score(1, "") or "noted: score 1 for the last answer"

    def feedback_down(self, comment: str) -> str:
        """Score 0; a comment becomes a rule for later answers and a task candidate (§11)."""
        refused = self._score(0, comment)
        if refused:
            return refused
        if not comment:
            return "noted: score 0 for the last answer"
        self.store.add_rule(comment)
        self.candidates_path.parent.mkdir(parents=True, exist_ok=True)
        with self.candidates_path.open("a", encoding="utf-8") as f:
            row = {
                "question": self.last_question,
                "answer": self.last_result.answer,
                "comment": comment,
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return f"noted: later answers follow: {comment}"

    def resolve(self, bp: str) -> str:
        """Mark the open finding of `bp` on the architecture read last resolved (findings-resolve)."""
        if self.last_arch is None:
            return "review an architecture first"
        row = self.store.find_finding(self.last_arch, normalize_bp(bp))
        if (
            row is None
            or row.status != "open"
            or not self.store.resolve_finding(row.id, self.today_fn())
        ):
            return f"no open finding {normalize_bp(bp)} on {self.last_arch}"
        return f"resolved {row.best_practice} on {self.last_arch}"

    def reject(self, bp: str, reason: str) -> str:
        """`/reject <BP> <reason>` for the architecture read last, for its current version only."""
        if self.last_arch is None or self.last_arch not in self.arch_hashes:
            return "review an architecture first"
        best_practice = normalize_bp(bp)
        if (
            not BP_PATTERN.fullmatch(best_practice)
            or best_practice not in self.known_bp
        ):
            return f"not a Well-Architected best-practice id of the corpus: {bp} (e.g. REL09-BP01)"
        arch, arch_hash = self.last_arch, self.arch_hashes[self.last_arch]
        self.store.add_rejection(
            arch, best_practice, reason, arch_hash, self.today_fn()
        )
        open_row = self.store.find_finding(arch, best_practice)
        if open_row is not None and open_row.status == "open":
            self.store.resolve_finding(
                open_row.id, self.today_fn()
            )  # the reason is in the rejection
        self._rejected_now.append(best_practice)  # for the history summary (§11)
        return f"noted: {best_practice} will not be raised again for this version of {arch}"

    def forget(self, key: str) -> bool:
        """`/forget <key>`: delete one fact (D24)."""
        return self.store.delete_fact(key)

    def ask(self, question: str) -> TurnResult:
        self._question = question  # what `remember` checks a value against (D24)
        self.search_tool.new_request()
        meta = {
            "model": self.cfg.model,
            "run_id": self.run_id,
            "prompt_version": self.cfg.prompt_version,
            "faults": [f"{f.kind}:{f.tool}" if f.tool else f.kind for f in self.faults],
        }
        with self.tracer.request(self.session_id, question, meta) as trace:

            def on_event(kind: str, data: dict) -> None:
                if kind == "model_call":
                    trace.model_call(data["turn"])
                elif kind == "tool_call":
                    trace.tool_call(data["record"])
                    self.on_tool(data["record"])
                elif kind == "critic":
                    trace.critic(data["problems"])

            self._fixed_context = ""
            if self.ablation == "fixed_rag":
                # one search with the raw question, before the loop, traced like a tool call so
                # the trace keeps its labels and retrieved chunks (step 25 review, I7)
                args = SearchArgs(
                    query=question[:200], doc_types=None, published_from=None
                )
                outcome = self.search_tool.label(self.search_tool.search(args))
                trace.tool_call(
                    CallRecord(
                        step=0,
                        name="search_corpus",
                        input=args.model_dump(mode="json"),
                        outcome=outcome,
                        ms=0,
                    )
                )
                self._fixed_context = outcome.text
            messages = self._messages(question)

            # the texts a number may come from (spec §10, check 3): this request's tool results,
            # the history and the question (the string messages), the memory block, the system prompt
            texts = [m["content"] for m in messages if isinstance(m["content"], str)]

            def check(answer: str, state: Any) -> list[str]:
                # a search counts only if it found something relevant: an honest "not found"
                # after an empty or all-low search needs no citation (review I5)
                ok_searches = [
                    c
                    for c in state.calls
                    if c.name == "search_corpus"
                    and not c.outcome.is_error
                    and (c.outcome.data or {}).get("labels")
                    and (
                        self.cfg.relevance_threshold is None
                        or 'relevance="high"' in c.outcome.text
                    )
                ]
                return critic(
                    answer,
                    label_map=self.store.label_map(self.session_id),
                    searched=bool(ok_searches),
                    number_sources=[c.outcome.text for c in state.calls]
                    + texts
                    + [self.system[0]["text"]],
                    rejected_bp=self.rejected_bp(),
                    tools_failed=service_stopped(state.calls),
                )

            result = run_turn(
                self.llm,
                self.system,
                self.tools,
                messages,
                self.registry,
                self.cfg.limits,
                critic=check,
                critic_retries=self.cfg.critic_retries,
                on_event=on_event,
            )
            trace.end(result)
        self.last_trace_id = trace.trace_id
        self.last_result = result
        self.last_question = question
        self.questions.append(question)
        self.store.add_message(self.session_id, "user", question, {})
        self.store.add_message(
            self.session_id,
            "assistant",
            result.answer,
            {
                "stop": result.stop,
                "trace_id": trace.trace_id,
                "partial": result.partial,
                # turn metadata for the history summary and the episode (§11)
                "architectures": sorted(
                    {
                        c.input.get("architecture_id")
                        for c in result.state.calls
                        if c.name == "get_architecture" and not c.outcome.is_error
                    }
                ),
                "rejected": self._take_rejected(),
                "recorded": [
                    normalize_bp(c.input.get("best_practice") or "")
                    for c in result.state.calls
                    if c.name == "record_finding"
                    and (c.outcome.data or {}).get("status") in ("recorded", "reopened")
                ],
            },
        )
        return result

    def _episode(self) -> str:
        """A deterministic summary of the session, no model call (§11)."""
        metas = [
            m.meta for m in self.store.history(self.session_id) if m.role == "assistant"
        ]
        return episode_text(self.session_id, self.questions, metas)

    def _end(self) -> None:
        if self.questions:
            self.store.add_episode(self.session_id, self._episode())

    def new(self) -> None:
        self._end()
        self._start()

    def close(self) -> None:
        self._end()
        self.questions = []
