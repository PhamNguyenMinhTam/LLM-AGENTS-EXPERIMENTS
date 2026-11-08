import json
from urllib.request import Request, urlopen

from agents.base_agent import AgentResponse, BaseAgent


def request_json(url, payload=None, timeout=120):
    data = None if payload is None else json.dumps(payload).encode()
    request = Request(url, data=data, headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=timeout) as response:
        return json.load(response)


def parse_response(data):
    if data.get("done") is not True:
        raise ValueError("Incomplete Ollama response")
    content = data["message"]["content"]
    if not isinstance(content, str):
        raise ValueError("Invalid message content")
    count, duration = data.get("eval_count"), data.get("eval_duration")
    throughput = count / (duration / 1e9) if count is not None and duration else None
    return AgentResponse(content, data.get("prompt_eval_count"), count, throughput)


class OllamaAgent(BaseAgent):
    def __init__(self, config, transport=request_json):
        self.config = config
        self.transport = transport

    def verify_model(self):
        data = self.transport(self.config.endpoint + "/api/tags", timeout=self.config.timeout)
        matches = [m for m in data["models"] if m["name"] == self.config.model_name]
        if len(matches) != 1:
            raise ValueError("Configured exact model tag not found")
        model = matches[0]
        if model["digest"] != self.config.model_digest:
            raise ValueError("Model digest mismatch")
        if model["details"]["quantization_level"] != self.config.quantization:
            raise ValueError("Quantization mismatch")

    def respond(self, prompt):
        payload = {
            "model": self.config.model_name,
            "stream": False,
            "messages": [
                {"role": "system", "content": self.config.system_prompt},
                {"role": "user", "content": prompt},
            ],
            "options": self.config.inference,
        }
        return parse_response(self.transport(
            self.config.endpoint + "/api/chat", payload, timeout=self.config.timeout
        ))
