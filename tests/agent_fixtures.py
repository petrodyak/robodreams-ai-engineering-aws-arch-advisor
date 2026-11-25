"""Shared fakes for the agent tests: no network, no model download (plan: Global Constraints)."""

from src.agent.llm import ToolUse, Turn
from src.agent.store import Store


def turn(
    text: str = "",
    tool_uses: list[tuple[str, dict]] | None = None,
    *,
    stop: str | None = None,
    usd: float = 0.001,
    input_tokens: int = 1000,
    output_tokens: int = 100,
) -> Turn:
    """A scripted model turn; `tool_uses` are (name, input) pairs with ids toolu_1, toolu_2 …"""
    uses = [
        ToolUse(id=f"toolu_{i}", name=name, input=inp)
        for i, (name, inp) in enumerate(tool_uses or [], 1)
    ]
    content: list[dict] = [{"type": "thinking", "thinking": "", "signature": "sig"}]
    if text:
        content.append({"type": "text", "text": text})
    content += [
        {"type": "tool_use", "id": u.id, "name": u.name, "input": u.input} for u in uses
    ]
    stop_reason = stop or ("tool_use" if uses else "end_turn")
    return Turn(
        content=content,
        text=text,
        tool_uses=uses if stop_reason == "tool_use" else [],
        stop_reason=stop_reason,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_read_tokens=0,
        cache_write_tokens=0,
        cost_usd=usd,
        latency_ms=5,
        attempts=1,
    )


class FakeLLM:
    """Replays scripted turns (the last one repeats forever) and records every request."""

    def __init__(self, *turns: Turn):
        self.turns = list(turns)
        self.requests: list[dict] = []

    def call(self, system, tools, messages, *, timeout_s=None) -> Turn:
        self.requests.append(
            {
                "system": system,
                "tools": tools,
                "messages": list(messages),
                "timeout_s": timeout_s,
            }
        )
        return self.turns.pop(0) if len(self.turns) > 1 else self.turns[0]


def memory_store() -> Store:
    return Store(":memory:")
