from dataclasses import dataclass


@dataclass
class SandboxPolicy:
    network_enabled: bool = False
    max_seconds: int = 120
    max_memory_mb: int = 2048
    writable_paths: tuple[str, ...] = ("/workspace",)


class TerminalSandbox:
    def __init__(self, policy: SandboxPolicy | None = None) -> None:
        self.policy = policy or SandboxPolicy()

    def prepare_command(self, command: list[str]) -> dict:
        return {
            "command": command,
            "network_enabled": self.policy.network_enabled,
            "timeout_seconds": self.policy.max_seconds,
            "memory_mb": self.policy.max_memory_mb,
            "audit": "enabled",
        }
