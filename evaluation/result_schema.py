from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class RunResult(BaseModel):
    model_config = ConfigDict(extra="forbid")
    experiment_id: str
    run_id: str
    condition: str
    repetition: int
    task_id: str
    agent_id: str
    hardware_id: str
    model_name: str
    model_digest: str
    quantization: str
    prompt_version: str
    inference_config: dict
    domain: str
    difficulty: str
    input: str
    expected_output: str
    actual_output: str | None
    score: float = Field(ge=0, le=1)
    success: bool
    error_type: str | None
    start_time: datetime
    end_time: datetime
    latency: float = Field(ge=0)
    prompt_tokens: int | None = Field(default=None, ge=0)
    output_tokens: int | None = Field(default=None, ge=0)
    token_throughput: float | None = Field(default=None, ge=0)
    resource_metrics: dict[str, Any]
    git_commit: str
    software_versions: dict
    session_id: str | None = None
    memory_config: str = "none"
    memory_snapshot_id: str | None = None
    feedback_type: str = "none"
    feedback_content: str | None = None
    iteration: int = 0
    before_score: float | None = None
    after_score: float | None = None
