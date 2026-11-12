import json

import pytest

from agents.base_agent import AgentResponse
from agents.ollama_agent import OllamaAgent
from controller.config import Task, load_config
from mini_mos.core.runtime import Runtime


def task():
    return Task(task_id="slice-1", domain="mathematics", difficulty="easy",
                input="2+3?", expected_output="5", split="development")


def test_ollama_vertical_slice(config_path):
    requests = []

    def transport(url, payload=None, timeout=None):
        requests.append(payload)
        return {"done": True, "message": {"content": "5"}}

    provider = OllamaAgent(load_config(config_path).agents[0], transport)
    result = Runtime(provider).run(task())
    assert requests[0]["messages"][-1]["content"] == "2+3?"
    assert result["assessment"] == {"score": 1.0, "success": True}
    assert result["state"] == "completed"
    assert [e["event"] for e in result["events"]] == [
        "task.started", "inference.completed", "evaluation.completed", "task.completed"]
    assert all(e["run_id"] == result["run_id"] for e in result["events"])
    json.dumps(result)


@pytest.mark.parametrize("error", [TimeoutError, ValueError, KeyError, TypeError])
def test_failed_task_has_terminal_trace(error):
    class Broken:
        def respond(self, prompt):
            raise error("Do not expose sensitive details")

    result = Runtime(Broken()).run(task())
    assert result["state"] == "failed"
    assert result["error"] == error.__name__
    assert result["assessment"] is None
    assert result["events"][-1]["event"] == "task.failed"
    assert "sensitive" not in json.dumps(result)


def test_wrong_answer_completes_without_retry():
    class Wrong:
        calls = 0

        def respond(self, prompt):
            self.calls += 1
            return AgentResponse("6")

    provider = Wrong()
    result = Runtime(provider).run(task())
    assert result["state"] == "completed"
    assert result["assessment"]["success"] is False
    assert provider.calls == 1
