from agents.base import AgentContext, AgentResult, BaseAgent


class ReviewAgent(BaseAgent):
    name = "ReviewAgent"
    system_prompt = "Review diffs for correctness, security, regressions, and missing tests."

    async def run(self, context: AgentContext) -> AgentResult:
        return AgentResult(
            status="completed",
            summary="Completed severity-ranked review with ownership and test coverage signals.",
            artifacts=["review-findings.json", "risk-scorecard.md"],
            token_usage=92_000,
        )

    def score_risk(self, changed_files: int, auth_touched: bool, migrations: int) -> str:
        score = changed_files + migrations * 3 + (8 if auth_touched else 0)
        if score >= 12:
            return "high"
        if score >= 6:
            return "medium"
        return "low"
