"""The agent's state in one SQLite database (spec §11, D14, ADR-0012).

Every table of spec §11 is created here once, so later steps add methods, not migrations. The store
holds one connection, owned by the thread that opened it (the main thread): `sqlite3` refuses a call
from any other thread, which is the rule of spec §9 "Threads" enforced by the library itself.

Idempotency of `record_finding` is a database property: `UNIQUE(architecture_id, best_practice)` on
`findings`, and `insert_or_reopen_finding` decides insert / already open / reopen inside one
transaction (D13, ADR-0010).
"""

import json
import sqlite3
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

Role = Literal["user", "assistant"]
FindingStatus = Literal["open", "resolved"]

DDL = """
CREATE TABLE IF NOT EXISTS sessions (
    id          INTEGER PRIMARY KEY,
    team        TEXT NOT NULL,
    started_at  TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS messages (
    id          INTEGER PRIMARY KEY,
    session_id  INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    role        TEXT NOT NULL CHECK (role IN ('user', 'assistant')),
    text        TEXT NOT NULL,
    meta        TEXT NOT NULL,
    created_at  TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS labels (
    session_id  INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    n           INTEGER NOT NULL,
    chunk_id    TEXT NOT NULL,
    PRIMARY KEY (session_id, n)
);
CREATE TABLE IF NOT EXISTS facts (
    key         TEXT PRIMARY KEY,
    value       TEXT NOT NULL,
    updated_at  TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS feedback_rules (
    id          INTEGER PRIMARY KEY,
    rule        TEXT NOT NULL UNIQUE,
    created_at  TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS rejections (
    id                 INTEGER PRIMARY KEY,
    architecture_id    TEXT NOT NULL,
    best_practice      TEXT NOT NULL,
    reason             TEXT NOT NULL,
    architecture_hash  TEXT NOT NULL,
    created_at         TEXT NOT NULL,
    UNIQUE (architecture_id, best_practice, architecture_hash)
);
CREATE TABLE IF NOT EXISTS episodes (
    id          INTEGER PRIMARY KEY,
    session_id  INTEGER NOT NULL,
    text        TEXT NOT NULL,
    created_at  TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS findings (
    id                 INTEGER PRIMARY KEY,
    architecture_id    TEXT NOT NULL,
    pillar             TEXT NOT NULL,
    best_practice      TEXT NOT NULL,
    severity           TEXT NOT NULL,
    summary            TEXT NOT NULL,
    source_chunk_id    TEXT NOT NULL,
    status             TEXT NOT NULL CHECK (status IN ('open', 'resolved')),
    architecture_hash  TEXT NOT NULL,
    opened_at          TEXT NOT NULL,
    resolved_at        TEXT,
    reopened_count     INTEGER NOT NULL DEFAULT 0,
    UNIQUE (architecture_id, best_practice)
);
CREATE TABLE IF NOT EXISTS scores (
    id          INTEGER PRIMARY KEY,
    session_id  INTEGER NOT NULL,
    trace_id    TEXT NOT NULL,
    value       INTEGER NOT NULL,
    comment     TEXT NOT NULL,
    created_at  TEXT NOT NULL
);
"""
# episodes and scores carry a session id but no foreign key: they outlive the purge of their session.


class StoredMessage(BaseModel):
    role: Role
    text: str
    meta: dict
    created_at: datetime


class FindingRow(BaseModel):
    id: int | None
    architecture_id: str
    pillar: str
    best_practice: str
    severity: str
    summary: str
    source_chunk_id: str
    status: FindingStatus
    architecture_hash: str
    opened_at: date
    resolved_at: date | None
    reopened_count: int = 0


class RecordOutcome(BaseModel):
    status: Literal["recorded", "already_open", "reopened"]
    finding_id: int
    since: date | None  # the date the open row was opened; set for `already_open` only


class Store:
    def __init__(self, path: Path | str, *, busy_timeout_s: float = 10.0) -> None:
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        # `timeout` is SQLite's busy timeout: how long a write waits for a lock (spec §9 "Threads")
        self._conn = sqlite3.connect(str(path), timeout=busy_timeout_s)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA foreign_keys = ON")
        self._conn.executescript(DDL)

    def close(self) -> None:
        self._conn.close()

    # sessions and messages -------------------------------------------------------------------

    def new_session(self, team: str, *, started_at: datetime | None = None) -> int:
        started = (started_at or datetime.now()).isoformat(timespec="seconds")
        with self._conn:
            cur = self._conn.execute(
                "INSERT INTO sessions (team, started_at) VALUES (?, ?)", (team, started)
            )
        return int(cur.lastrowid)

    def add_message(self, session_id: int, role: Role, text: str, meta: dict) -> None:
        with self._conn:
            self._conn.execute(
                "INSERT INTO messages (session_id, role, text, meta, created_at) VALUES (?, ?, ?, ?, ?)",
                (session_id, role, text, json.dumps(meta), datetime.now().isoformat()),
            )

    def history(self, session_id: int) -> list[StoredMessage]:
        rows = self._conn.execute(
            "SELECT role, text, meta, created_at FROM messages WHERE session_id = ? ORDER BY id",
            (session_id,),
        ).fetchall()
        return [
            StoredMessage(
                role=r["role"],
                text=r["text"],
                meta=json.loads(r["meta"]),
                created_at=datetime.fromisoformat(r["created_at"]),
            )
            for r in rows
        ]

    def purge_sessions(self, today: date, days: int = 30) -> int:
        """Delete sessions started more than `days` ago, with their messages and labels.

        Episodes, scores and findings stay: they have no foreign key to `sessions`.
        """
        cutoff = datetime.combine(today - timedelta(days=days), datetime.min.time())
        with self._conn:
            cur = self._conn.execute(
                "DELETE FROM sessions WHERE started_at < ?",
                (cutoff.isoformat(timespec="seconds"),),
            )
        return cur.rowcount

    # session labels (spec §10) -----------------------------------------------------------------

    def add_labels(self, session_id: int, labels: dict[str, str]) -> None:
        """Store `{"S6": chunk_id, …}`; a label always means one chunk inside one session."""
        with self._conn:
            self._conn.executemany(
                "INSERT INTO labels (session_id, n, chunk_id) VALUES (?, ?, ?)",
                [
                    (session_id, _label_number(label), chunk_id)
                    for label, chunk_id in labels.items()
                ],
            )

    def label_map(self, session_id: int) -> dict[str, str]:
        rows = self._conn.execute(
            "SELECT n, chunk_id FROM labels WHERE session_id = ? ORDER BY n",
            (session_id,),
        ).fetchall()
        return {f"S{r['n']}": r["chunk_id"] for r in rows}

    def next_label(self, session_id: int) -> int:
        row = self._conn.execute(
            "SELECT MAX(n) AS n FROM labels WHERE session_id = ?", (session_id,)
        ).fetchone()
        return (row["n"] or 0) + 1

    # episodes (spec §11; the deterministic summary text is built in Task 24.3) -----------------

    def add_episode(
        self, session_id: int, text: str, created_at: datetime | None = None
    ) -> None:
        created = (created_at or datetime.now()).isoformat()
        with self._conn:
            self._conn.execute(
                "INSERT INTO episodes (session_id, text, created_at) VALUES (?, ?, ?)",
                (session_id, text, created),
            )

    def episodes(self) -> list[str]:
        rows = self._conn.execute("SELECT text FROM episodes ORDER BY id").fetchall()
        return [r["text"] for r in rows]

    # findings registry (D13, ADR-0010) ---------------------------------------------------------

    def insert_or_reopen_finding(self, f: FindingRow) -> RecordOutcome:
        """Insert a new finding, report an open one, or reopen a resolved one, in one transaction.

        An open row keeps its date; only its architecture hash follows the version it was seen on
        again (spec §11 edge cases). A resolved row is reopened with the new evidence.
        """
        with self._conn:
            row = self._conn.execute(
                "SELECT id, status, opened_at FROM findings "
                "WHERE architecture_id = ? AND best_practice = ?",
                (f.architecture_id, f.best_practice),
            ).fetchone()
            if row is None:
                cur = self._conn.execute(
                    "INSERT INTO findings (architecture_id, pillar, best_practice, severity, summary, "
                    "source_chunk_id, status, architecture_hash, opened_at, resolved_at, reopened_count) "
                    "VALUES (?, ?, ?, ?, ?, ?, 'open', ?, ?, NULL, 0)",
                    (
                        f.architecture_id,
                        f.pillar,
                        f.best_practice,
                        f.severity,
                        f.summary,
                        f.source_chunk_id,
                        f.architecture_hash,
                        f.opened_at.isoformat(),
                    ),
                )
                return RecordOutcome(
                    status="recorded", finding_id=int(cur.lastrowid), since=None
                )
            if row["status"] == "open":
                self._conn.execute(
                    "UPDATE findings SET architecture_hash = ? WHERE id = ?",
                    (f.architecture_hash, row["id"]),
                )
                return RecordOutcome(
                    status="already_open",
                    finding_id=row["id"],
                    since=date.fromisoformat(row["opened_at"]),
                )
            self._conn.execute(
                "UPDATE findings SET status = 'open', resolved_at = NULL, "
                "reopened_count = reopened_count + 1, architecture_hash = ?, severity = ?, "
                "summary = ?, source_chunk_id = ? WHERE id = ?",
                (
                    f.architecture_hash,
                    f.severity,
                    f.summary,
                    f.source_chunk_id,
                    row["id"],
                ),
            )
            return RecordOutcome(status="reopened", finding_id=row["id"], since=None)

    def resolve_finding(self, finding_id: int, today: date) -> bool:
        with self._conn:
            cur = self._conn.execute(
                "UPDATE findings SET status = 'resolved', resolved_at = ? "
                "WHERE id = ? AND status = 'open'",
                (today.isoformat(), finding_id),
            )
        return cur.rowcount == 1

    def findings(self, status: FindingStatus | None = None) -> list[FindingRow]:
        sql = "SELECT * FROM findings"
        params: tuple = ()
        if status is not None:
            sql += " WHERE status = ?"
            params = (status,)
        rows = self._conn.execute(sql + " ORDER BY id", params).fetchall()
        return [FindingRow(**dict(r)) for r in rows]

    def find_finding(
        self, architecture_id: str, best_practice: str
    ) -> FindingRow | None:
        """The row of one idempotency key, if any (record_finding checks it before asking)."""
        row = self._conn.execute(
            "SELECT * FROM findings WHERE architecture_id = ? AND best_practice = ?",
            (architecture_id, best_practice),
        ).fetchone()
        return FindingRow(**dict(row)) if row else None


def _label_number(label: str) -> int:
    """`"S12"` or `"[S12]"` → 12."""
    return int(label.strip("[]").removeprefix("S"))
