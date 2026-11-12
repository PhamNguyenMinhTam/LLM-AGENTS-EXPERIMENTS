"""One bounded inference step; no tool execution or automatic retries."""

from datetime import datetime, timezone
from time import perf_counter
from uuid import uuid4

from agents.base_agent import BaseAgent
from controller.config import Task
from evaluation.evaluator import evaluate


class Runtime:
    def __init__(self, provider: BaseAgent):
        self.provider = provider

    def run(self, task: Task) -> dict:
        run_id = uuid4().hex
        events = []

        def event(name):
            events.append({"event": name, "run_id": run_id, "task_id": task.task_id,
                           "timestamp": datetime.now(timezone.utc).isoformat()})

        event("task.started")
        start = perf_counter()
        output, error, assessment = None, None, None
        try:
            # Expected output remains exclusively on the evaluator side.
            output = self.provider.respond(task.input).content
            event("inference.completed")
            assessment = evaluate(output, task.expected_output)
            event("evaluation.completed")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            error = type(exc).__name__
        state = "failed" if error else "completed"
        event("task." + state)
        return {"run_id": run_id, "task_id": task.task_id, "state": state,
                "output": output, "assessment": assessment, "error": error,
                "latency_s": perf_counter() - start, "events": events}
