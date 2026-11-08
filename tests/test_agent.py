import pytest

from agents.ollama_agent import OllamaAgent, parse_response
from controller.config import load_config


def test_parse():
    result = parse_response({"done": True, "message": {"content": "5"},
                             "eval_count": 10, "prompt_eval_count": 3, "eval_duration": 500000000})
    assert result.content == "5"
    assert result.token_throughput == 20
    assert result.prompt_tokens == 3


@pytest.mark.parametrize("payload", [{}, {"done": False}, {"done": True, "message": {"content": 1}}])
def test_bad_response(payload):
    with pytest.raises((ValueError, KeyError)):
        parse_response(payload)


def test_no_answer_leak_and_timeout(config_path):
    calls = []
    def transport(url, payload=None, timeout=None):
        calls.append((url, payload, timeout))
        return {"done": True, "message": {"content": "5"}}
    config = load_config(config_path).agents[0]
    agent = OllamaAgent(config, transport)
    assert agent.respond("2+3?").content == "5"
    assert calls[0][1]["messages"][-1] == {"role": "user", "content": "2+3?"}
    assert calls[0][2] == 120
    assert calls[0][1]["stream"] is False


def test_digest_mismatch(config_path):
    config = load_config(config_path).agents[0]
    agent = OllamaAgent(config, lambda *args, **kwargs: {"models": [{"name": config.model_name,
        "digest": "wrong", "details": {"quantization_level": config.quantization}}]})
    with pytest.raises(ValueError, match="digest"):
        agent.verify_model()
