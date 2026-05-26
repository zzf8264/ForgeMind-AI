from agents.base import AgentContext, AgentResult, BaseAgent


class DocumentAgent(BaseAgent):
    name = "DocumentAgent"
    system_prompt = "Produce engineering documentation, ADRs, runbooks, and API guides from source context."

    async def run(self, context: AgentContext) -> AgentResult:
        return AgentResult(
            status="completed",
            summary="Created documentation pack from repository context and run artifacts.",
            artifacts=["architecture.md", "runbook.md", "api-reference.md"],
            token_usage=76_400,
        )

    def adr_outline(self, decision: str) -> list[str]:
        return [
            f"Decision: {decision}",
            "Context and constraints",
            "Options considered",
            "Operational impact",
            "Rollback criteria",
        ]
