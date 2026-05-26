from dataclasses import dataclass
from typing import Any


@dataclass
class ToolDefinition:
    name: str
    description: str
    risk_level: str
    timeout_seconds: int


class ToolRegistry:
    def __init__(self) -> None:
        self._tools = {
            "terminal.run": ToolDefinition("terminal.run", "Execute a command inside a governed sandbox.", "high", 120),
            "github.read_file": ToolDefinition("github.read_file", "Read repository files through the GitHub integration.", "low", 30),
            "github.open_pr": ToolDefinition("github.open_pr", "Open a pull request with generated patches and evidence.", "medium", 60),
            "rag.search": ToolDefinition("rag.search", "Retrieve repository context from Qdrant.", "low", 15),
        }

    def list_tools(self) -> list[ToolDefinition]:
        return list(self._tools.values())

    def describe(self, name: str) -> ToolDefinition:
        return self._tools[name]

    def audit_call(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        tool = self.describe(name)
        return {"tool": tool.name, "risk_level": tool.risk_level, "arguments": arguments, "policy": "recorded"}
