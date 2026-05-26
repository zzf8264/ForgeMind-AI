class AutonomousCodingWorkflow:
    def build_plan(self, objective: str, repository: str) -> list[dict]:
        return [
            {"phase": "context", "action": f"Index and retrieve relevant files from {repository}"},
            {"phase": "plan", "action": f"Decompose objective: {objective}"},
            {"phase": "edit", "action": "Generate minimal patch and update tests"},
            {"phase": "verify", "action": "Run focused test, typecheck, and static analysis commands"},
            {"phase": "handoff", "action": "Prepare PR summary, risk notes, and rollback instructions"},
        ]
