import json
import os
import re
from pathlib import Path
from typing import Literal
from urllib.parse import urlparse

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict, Field, model_validator

ROOT = Path(__file__).resolve().parents[1]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class AgentConfig(StrictModel):
    agent_id: str = Field(min_length=1)
    hardware_id: str = Field(min_length=1)
    endpoint: str
    model_name: str = Field(min_length=1)
    model_digest: str = Field(min_length=1)
    quantization: str = Field(min_length=1)
    prompt_version: str = Field(min_length=1)
    system_prompt: str = Field(min_length=1)
    inference: dict = Field(default_factory=lambda: {"temperature": 0, "seed": 42})
    timeout: float = Field(default=120, gt=0)

    @model_validator(mode="after")
    def endpoint_valid(self):
        url = urlparse(self.endpoint)
        if url.scheme not in {"http", "https"} or not url.hostname or url.username or url.password:
            raise ValueError("Endpoint must be an HTTP(S) URL without credentials")
        if url.query or url.fragment or url.path not in {"", "/"}:
            raise ValueError("Endpoint must be a server origin")
        self.endpoint = self.endpoint.rstrip("/")
        return self


class ExperimentConfig(StrictModel):
    experiment_id: str = Field(pattern=r"^E(0[1-9]|1[0-2])$")
    condition: str = Field(min_length=1)
    domain: Literal["mathematics", "coding", "classification"]
    dataset_path: str
    repetitions: int = Field(default=3, ge=1)
    agents: list[AgentConfig] = Field(min_length=1, max_length=2)
    memory: Literal["none", "short-term", "long-term"] = "none"
    feedback: Literal["none", "binary", "detailed"] = "none"
    tools: list[str] = Field(default_factory=list)
    evaluation_metrics: list[Literal["exact_match", "latency", "tokens", "consistency", "failure_rate"]]
    output_directory: str

    @model_validator(mode="after")
    def independent(self):
        if len({a.agent_id for a in self.agents}) != len(self.agents):
            raise ValueError("Duplicate agent IDs")
        if len({a.endpoint for a in self.agents}) != len(self.agents):
            raise ValueError("A/B must use separate Ollama endpoints")
        return self


class Task(StrictModel):
    task_id: str
    domain: Literal["mathematics", "coding", "classification"]
    difficulty: Literal["easy", "medium", "hard"]
    input: str
    expected_output: str
    split: Literal["development", "final"]


def load_config(path):
    load_dotenv(ROOT / ".env", override=False)
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))

    def expand(value):
        if isinstance(value, str):
            def replace(match):
                key = match.group(1)
                if key not in os.environ:
                    raise ValueError(f"Missing environment variable: {key}; copy .env.example")
                return os.environ[key]
            return re.sub(r"\$\{([A-Z0-9_]+)\}", replace, value)
        if isinstance(value, list):
            return [expand(v) for v in value]
        if isinstance(value, dict):
            return {k: expand(v) for k, v in value.items()}
        return value

    return ExperimentConfig.model_validate(expand(data))


def load_tasks(config):
    tasks = [Task.model_validate(json.loads(line)) for line in
             (ROOT / config.dataset_path).read_text(encoding="utf-8").splitlines() if line.strip()]
    if not tasks or len({t.task_id for t in tasks}) != len(tasks):
        raise ValueError("Dataset empty or duplicate task IDs")
    if any(t.domain != config.domain for t in tasks):
        raise ValueError("Dataset domain mismatch")
    if (config.memory != "none" or config.feedback != "none") and any(t.split == "final" for t in tasks):
        raise ValueError("Final evaluation data cannot feed adaptation")
    return tasks
