from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class ScheduledTask:
    id: str
    queue: str
    priority: str
    run_at: str


class TaskScheduler:
    def schedule(self, task_id: str, priority: str = "normal") -> ScheduledTask:
        queue = "agent-runs:critical" if priority == "critical" else "agent-runs:default"
        return ScheduledTask(
            id=task_id,
            queue=queue,
            priority=priority,
            run_at=datetime.now(timezone.utc).isoformat(),
        )
