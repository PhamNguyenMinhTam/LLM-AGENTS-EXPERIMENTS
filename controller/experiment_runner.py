import csv
import hashlib
import json
import platform
import random
import subprocess
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

import pydantic
import yaml

from agents.ollama_agent import OllamaAgent
from controller.config import ROOT, load_config, load_tasks
from controller.task_dispatcher import dispatch
from evaluation.evaluator import evaluate
from evaluation.metrics import consistency, latency_statistics
from evaluation.result_schema import RunResult


def run_experiment(path, dry_run=False, agent_factory=OllamaAgent):
    config = load_config(path)
    tasks = load_tasks(config)
    if dry_run:
        return {"mode": "dry-run", "experiment_id": config.experiment_id,
                "condition": config.condition, "tasks": len(tasks),
                "planned_calls": len(tasks) * len(config.agents) * config.repetitions,
                "unsupported": [name for name, enabled in
                                [("tools", bool(config.tools)), ("memory", config.memory != "none"),
                                 ("feedback", config.feedback != "none")] if enabled]}
    if config.tools or config.memory != "none" or config.feedback != "none":
        raise NotImplementedError("Tools/memory/feedback are research protocols only; no runtime yet")
    for agent in config.agents:
        if any("REPLACE" in value for value in
               [agent.model_name, agent.model_digest, agent.quantization, agent.hardware_id]):
            raise ValueError("Replace environment placeholders before live execution")
    agents = [(a, agent_factory(a)) for a in config.agents]
    for _, agent in agents:
        agent.verify_model()
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    run_id = uuid4().hex
    out = ROOT / config.output_directory / run_id
    out.mkdir(parents=True, exist_ok=False)
    metadata = config.model_dump()
    metadata.update({"git_commit": commit,
                     "dataset_sha256": hashlib.sha256((ROOT / config.dataset_path).read_bytes()).hexdigest(),
                     "code_dirty": bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT))})
    (out / "manifest.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    groups = defaultdict(list)
    order = [(rep, task, a, agent) for rep in range(config.repetitions)
             for task in tasks for a, agent in agents]
    random.Random(42).shuffle(order)
    with (out / "runs.jsonl").open("x", encoding="utf-8") as handle:
        for rep, task, a, agent in order:
            start = datetime.now(timezone.utc)
            clock = time.perf_counter()
            response, error = None, None
            try:
                response = dispatch(agent, task)
                assessment = evaluate(response.content, task.expected_output)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                error = type(exc).__name__
                assessment = {"score": 0., "success": False}
            result = RunResult(
                experiment_id=config.experiment_id, run_id=run_id, condition=config.condition,
                repetition=rep, task_id=task.task_id, agent_id=a.agent_id,
                hardware_id=a.hardware_id, model_name=a.model_name, model_digest=a.model_digest,
                quantization=a.quantization, prompt_version=a.prompt_version,
                inference_config=a.inference, domain=task.domain, difficulty=task.difficulty,
                input=task.input, expected_output=task.expected_output,
                actual_output=response.content if response else None, **assessment, error_type=error,
                start_time=start, end_time=datetime.now(timezone.utc), latency=time.perf_counter()-clock,
                prompt_tokens=response.prompt_tokens if response else None,
                output_tokens=response.output_tokens if response else None,
                token_throughput=response.token_throughput if response else None,
                resource_metrics={"cpu_percent": None, "gpu_percent": None, "ram_peak_bytes": None,
                                  "vram_peak_bytes": None, "energy_joules": None,
                                  "status": "not_instrumented_on_inference_host"},
                git_commit=commit, software_versions={"python": platform.python_version(),
                    "pydantic": pydantic.__version__, "pyyaml": yaml.__version__, "ollama": "not_collected"})
            handle.write(result.model_dump_json() + "\n")
            handle.flush()
            groups[a.agent_id].append(result)
    with (out / "summary.csv").open("x", newline="", encoding="utf-8") as handle:
        fields = ["agent_id", "condition", "n", "accuracy", "failure_rate", "mean_latency_s",
                  "median_latency_s", "p95_latency_s", "consistency"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for agent_id, rows in groups.items():
            lat = latency_statistics([r.latency for r in rows])
            by_task = defaultdict(list)
            for row in rows:
                # Lỗi API không được coi là câu trả lời nhất quán.
                by_task[row.task_id].append(row.actual_output if row.error_type is None else uuid4().hex)
            writer.writerow({"agent_id": agent_id, "condition": config.condition, "n": len(rows),
                "accuracy": sum(r.score for r in rows)/len(rows),
                "failure_rate": sum(r.error_type is not None for r in rows)/len(rows),
                "mean_latency_s": lat["mean"], "median_latency_s": lat["median"],
                "p95_latency_s": lat["p95"],
                "consistency": sum(consistency(v) for v in by_task.values())/len(by_task)})
    return {"mode": "live", "output": str(out), "runs": len(order)}
