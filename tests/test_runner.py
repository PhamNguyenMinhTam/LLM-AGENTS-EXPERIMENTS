import csv
import json
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from agents.base_agent import AgentResponse
from controller.config import ROOT, load_config
from controller.experiment_runner import run_experiment
from evaluation.result_schema import RunResult


class FakeAgent:
    def __init__(self, config):
        self.config = config

    def verify_model(self):
        pass

    def respond(self, prompt):
        return AgentResponse("5" if "2 + 3" in prompt else "56", 8, 1, 20)


def temp_config(config_path, tmp_path, **changes):
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    data.update(output_directory=str(tmp_path / "output"), **changes)
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


def test_dry_run(config_path, tmp_path):
    path = temp_config(config_path, tmp_path)
    def forbidden(_):
        pytest.fail("Dry-run must not initialize agent")
    result = run_experiment(path, True, forbidden)
    assert result["planned_calls"] == 2 * 2 * load_config(config_path).repetitions
    assert not (tmp_path / "output").exists()


def test_mock_output_and_schema(config_path, tmp_path):
    result = run_experiment(temp_config(config_path, tmp_path), agent_factory=FakeAgent)
    out = Path(result["output"])
    rows = [RunResult.model_validate_json(line) for line in (out/"runs.jsonl").read_text().splitlines()]
    assert len(rows) == 2 * 2 * load_config(config_path).repetitions
    assert all(r.success and r.score == 1 and r.error_type is None for r in rows)
    assert all(r.resource_metrics["ram_peak_bytes"] is None for r in rows)
    summaries = list(csv.DictReader((out/"summary.csv").open()))
    assert len(summaries) == 2
    assert all(float(s["accuracy"]) == 1 for s in summaries)
    manifest = json.loads((out/"manifest.json").read_text(encoding="utf-8"))
    assert len(manifest["dataset_sha256"]) == 64
    assert manifest["agents"][0]["model_name"] == "test-model:1b"
    invalid = rows[0].model_dump()
    invalid["latency"] = -1
    with pytest.raises(ValidationError):
        RunResult.model_validate(invalid)
    del invalid["task_id"]
    with pytest.raises(ValidationError):
        RunResult.model_validate(invalid)


def test_api_failure_is_recorded(config_path, tmp_path):
    class Broken(FakeAgent):
        def respond(self, prompt):
            raise TimeoutError("simulated")
    result = run_experiment(temp_config(config_path, tmp_path), agent_factory=Broken)
    rows = [json.loads(line) for line in (Path(result["output"])/"runs.jsonl").read_text().splitlines()]
    assert all(r["error_type"] == "TimeoutError" and not r["success"] for r in rows)


@pytest.mark.parametrize("changes", [{"tools": ["calculator"]}, {"memory": "short-term"}, {"feedback": "detailed"}])
def test_unsupported_is_not_silently_ignored(config_path, tmp_path, changes):
    path = temp_config(config_path, tmp_path, **changes)
    assert run_experiment(path, True)["unsupported"]
    with pytest.raises(NotImplementedError):
        run_experiment(path, agent_factory=FakeAgent)


def test_final_cannot_feed_adaptation(config_path, tmp_path):
    dataset = tmp_path / "final.jsonl"
    dataset.write_text(json.dumps({"task_id": "f", "domain": "mathematics", "difficulty": "easy",
        "input": "1+1?", "expected_output": "2", "split": "final"}), encoding="utf-8")
    path = temp_config(config_path, tmp_path, memory="long-term", dataset_path=str(dataset))
    with pytest.raises(ValueError, match="Final evaluation"):
        run_experiment(path, True)
