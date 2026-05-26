import asyncio
from datetime import datetime, timezone
from uuid import uuid4

from app.models.schemas import TaskRequest


class AgentRuntime:
    def __init__(self) -> None:
        self._runs: list[dict] = [
            {
                "id": "run_7f92",
                "agent": "RepoAnalyzerAgent",
                "status": "completed",
                "repository": "github.com/acme/payments",
                "tokens": 1284300,
                "duration_ms": 18420,
            },
            {
                "id": "run_8b11",
                "agent": "CodingAgent",
                "status": "running",
                "repository": "github.com/acme/platform",
                "tokens": 840210,
                "duration_ms": 9440,
            },
        ]

    def catalog(self) -> list[dict]:
        return [
            {"name": "CodingAgent", "capabilities": ["plan", "edit", "test", "open_pr"], "concurrency": 1200},
            {"name": "ReviewAgent", "capabilities": ["diff_review", "risk_scoring", "test_gap_detection"], "concurrency": 900},
            {"name": "RepoAnalyzerAgent", "capabilities": ["long_context_indexing", "dependency_graph", "ownership_map"], "concurrency": 600},
            {"name": "DevOpsAgent", "capabilities": ["terraform", "kubernetes", "incident_triage"], "concurrency": 450},
            {"name": "DocumentAgent", "capabilities": ["adr", "runbook", "api_docs"], "concurrency": 700},
        ]

    async def dispatch(self, payload: TaskRequest) -> dict:
        run = {
            "id": f"run_{uuid4().hex[:10]}",
            "agent": payload.agent,
            "status": "queued",
            "repository": payload.repository,
            "objective": payload.objective,
            "priority": payload.priority,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "queue": "redis:agent-runs:critical" if payload.priority == "critical" else "redis:agent-runs:default",
        }
        self._runs.insert(0, run)
        return run

    def recent_runs(self) -> list[dict]:
        return self._runs[:25]

    async def stream_run(self, run_id: str):
        phases = [
            ("queued", "Task accepted by distributed scheduler"),
            ("indexing", "Repository context loaded into Qdrant collection"),
            ("planning", "Multi-agent planner decomposed objective into 7 steps"),
            ("executing", "Sandbox terminal executed tests and static analysis"),
            ("streaming", "Tool calls and code edits are being emitted"),
            ("completed", "Run completed with policy checks and usage ledger update"),
        ]
        for index, (phase, message) in enumerate(phases):
            await asyncio.sleep(0.4)
            yield {
                "run_id": run_id,
                "sequence": index,
                "phase": phase,
                "message": message,
                "tokens": 18200 * (index + 1),
            }
