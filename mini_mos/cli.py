"""Run one task through the existing Ollama adapter or an explicit fixture."""

import argparse
import json
from pathlib import Path

from agents.base_agent import AgentResponse, BaseAgent
from agents.ollama_agent import OllamaAgent
from controller.config import load_config, load_tasks
from mini_mos.core.runtime import Runtime


class FixtureProvider(BaseAgent):
    def __init__(self, response):
        self.response = response

    def respond(self, prompt):
        return AgentResponse(self.response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--agent", type=int, default=0)
    parser.add_argument("--mock-response", help="Fixture text; never a model measurement")
    parser.add_argument("--trace", type=Path, required=True)
    args = parser.parse_args()
    config = load_config(args.config)
    if config.tools or config.memory != "none" or config.feedback != "none":
        parser.error("Tools/memory/feedback are not implemented in this slice")
    if not 0 <= args.agent < len(config.agents):
        parser.error("Agent index out of range")
    selected = config.agents[args.agent]
    if args.mock_response is None:
        if any("REPLACE" in v for v in [selected.model_name, selected.model_digest,
                                        selected.quantization, selected.hardware_id]):
            parser.error("Replace model/hardware placeholders before live execution")
        provider = OllamaAgent(selected)
        provider.verify_model()
    else:
        provider = FixtureProvider(args.mock_response)
    result = Runtime(provider).run(load_tasks(config)[0])
    result.update({"mode": "mock" if args.mock_response is not None else "live",
                   "agent_id": selected.agent_id, "model_name": selected.model_name})
    args.trace.parent.mkdir(parents=True, exist_ok=True)
    with args.trace.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False))
    return 1 if result["state"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
