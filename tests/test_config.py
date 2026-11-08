import pytest
from pydantic import ValidationError

from controller.config import AgentConfig, ExperimentConfig, ROOT, load_config, load_tasks


def test_all_configs():
    for path in (ROOT / "experiments").glob("E*/config.yaml"):
        config = load_config(path)
        assert len(load_tasks(config)) == 2


@pytest.mark.parametrize("patch", [{"repetitions": 0}, {"experiment_id": "E99"},
                                   {"memory": "invented"}, {"unknown": True}])
def test_invalid(config_path, patch):
    data = load_config(config_path).model_dump()
    data.update(patch)
    with pytest.raises(ValidationError):
        ExperimentConfig.model_validate(data)


def test_missing_environment(config_path, monkeypatch):
    monkeypatch.delenv("MODEL_NAME")
    # Không đọc .env của người dùng trong test.
    monkeypatch.setattr("controller.config.load_dotenv", lambda *a, **k: None)
    with pytest.raises(ValueError, match="Missing environment"):
        load_config(config_path)


def test_duplicate_endpoints(config_path):
    data = load_config(config_path).model_dump()
    data["agents"][1]["endpoint"] = data["agents"][0]["endpoint"]
    with pytest.raises(ValidationError, match="separate"):
        ExperimentConfig.model_validate(data)


@pytest.mark.parametrize("endpoint", ["file:///etc/passwd", "http://user:pass@localhost", "http://localhost/api/chat"])
def test_endpoint(config_path, endpoint):
    data = load_config(config_path).agents[0].model_dump()
    data["endpoint"] = endpoint
    with pytest.raises(ValidationError):
        AgentConfig.model_validate(data)
