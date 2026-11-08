import argparse
import json

from agents.ollama_agent import OllamaAgent
from controller.config import load_config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    config = load_config(parser.parse_args().config)
    for agent in config.agents:
        OllamaAgent(agent).verify_model()
        print(json.dumps({"agent_id": agent.agent_id, "verified": True}))


if __name__ == "__main__":
    main()
