from agents.base import AgentContext, AgentResult, BaseAgent


class CodingAgent(BaseAgent):
    name = "CodingAgent"
    system_prompt = "Implement scoped code changes with tests and minimal blast radius."

    async def run(self, context: AgentContext) -> AgentResult:
        plan = self.plan(context)
        return AgentResult(
            status="completed",
            summary=f"Implemented requested change for {context.repository} using {len(plan)} execution phases.",
            artifacts=["patch.diff", "test-report.json", "pull-request.md"],
            token_usage=184_200,
        )

    def generate_patch_strategy(self, files: list[str]) -> dict:
        return {
            "edit_order": files,
            "verification": ["unit_tests", "typecheck", "focused_regression"],
            "rollback": "single PR revert",
        }
