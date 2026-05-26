from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class AgentContext:
    run_id: str
    repository: str
    objective: str
    metadata: dict = field(default_factory=dict)


@dataclass
class AgentResult:
    status: str
    summary: str
    artifacts: list[str] = field(default_factory=list)
    token_usage: int = 0
    completed_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class BaseAgent(ABC):
    name = "BaseAgent"
    system_prompt = "You are a ForgeMind AI enterprise agent."

    @abstractmethod
    async def run(self, context: AgentContext) -> AgentResult:
        raise NotImplementedError

    def plan(self, context: AgentContext) -> list[str]:
        return [
            f"Load policy and repository context for {context.repository}",
            "Select tools and sandbox constraints",
            "Execute task and collect evidence",
            "Write audit-safe run summary",
        ]
