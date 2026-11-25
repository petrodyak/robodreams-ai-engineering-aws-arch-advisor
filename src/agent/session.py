"""AgentSession: the composition root that the chat (`cli.py`) and the eval runner share (spec §6.1).

One session = one row in `sessions`; its labels, messages and findings context live as long as it.
What the first request carries (spec §6.1): the system prompt with today and the team, the tool
definitions, then the history of this session and the question. The memory block and the history
window with its summary arrive in Task 24.3; the MCP tools in Task 23.3 (`mcp=None` until then).

`system` and `tools` are built once per session and sent unchanged on every call, so the prompt-cache
prefix stays stable (spec §6).
"""

import time
from collections.abc import Callable
from datetime import date
from pathlib import Path
from typing import Any

from src.agent.config import AgentConfig
from src.agent.faults import Fault, apply_faults
from src.agent.findings import Confirm, FindingContext, make_record_finding
from src.agent.loop import TurnResult, run_turn
from src.agent.search_tool import SearchArgs, SearchTool, best_practice_ids
from src.agent.store import Store
from src.agent.tools import ToolEntry, load_descriptions, tool_spec
from src.agent.tracing import Tracer
from src.rag.config import RagConfig, load_config
from src.rag.index import Index

PROMPTS_DIR = Path("prompts")


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
        self.mcp = mcp  # Task 23.3
        self.rag_cfg = rag_cfg or load_config()
        self.supersedes = supersedes or {}
        self.sleep = sleep
        self.on_tool = on_tool
        self.run_id = run_id
        # cfg.today is frozen for the prompt and the editions (§10); purge, finding dates and
        # episodes use the real date (final review, finding 4)
        self.today_fn = today_fn
        self.known_bp = best_practice_ids(index.chunks)
        self.system = system_blocks(cfg, team)
        self.descriptions = load_descriptions(cfg.tools_version)
        self.blocked_docs: set[str] = set()  # filled from the overlay (24.2)
        store.purge_sessions(today_fn())
        self._start()

    def _start(self) -> None:
        self.session_id = self.store.new_session(self.team)
        # architectures read in this session, id -> hash; filled by the get_architecture wrapper
        # (23.3) and fresh per session: "read in this session" (spec §8; final review, finding 5)
        self.arch_hashes: dict[str, str] = {}
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
        )
        local = {
            "search_corpus": ToolEntry(
                fn=self.search_tool.search,
                args_model=SearchArgs,
                read_only=True,
                finish=self.search_tool.label,
            ),
            "record_finding": make_record_finding(self.findings_ctx),
        }
        self.registry = apply_faults(local, self.faults, sleep=self.sleep)
        self.tools = [
            tool_spec(name, entry.args_model, self.descriptions)
            for name, entry in self.registry.items()
        ]

    def _messages(self, question: str) -> list[dict]:
        """This session's earlier questions and answers as text, then the question (§11)."""
        history = [
            {"role": m.role, "content": m.text}
            for m in self.store.history(self.session_id)
        ]
        return [*history, {"role": "user", "content": question}]

    def ask(self, question: str) -> TurnResult:
        self.search_tool.new_request()
        messages = self._messages(question)
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

            result = run_turn(
                self.llm,
                self.system,
                self.tools,
                messages,
                self.registry,
                self.cfg.limits,
                critic_retries=self.cfg.critic_retries,
                on_event=on_event,
            )
            trace.end(result)
        self.last_trace_id = trace.trace_id
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
            },
        )
        return result

    def _episode(self) -> str:
        """A deterministic summary of the session, no model call (§11; refined in Task 24.3)."""
        recorded = [
            f.best_practice
            for f in self.store.findings()
            if f.opened_at == self.findings_ctx.today
        ]
        text = f"Session {self.session_id}: {len(self.questions)} question(s); first: {self.questions[0][:80]}"
        if recorded:
            text += f"; findings open from today: {', '.join(recorded)}"
        return text

    def _end(self) -> None:
        if self.questions:
            self.store.add_episode(self.session_id, self._episode())

    def new(self) -> None:
        self._end()
        self._start()

    def close(self) -> None:
        self._end()
        self.questions = []
