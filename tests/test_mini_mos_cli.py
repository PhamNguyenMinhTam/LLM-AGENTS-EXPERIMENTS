import json
import sys

import pytest

from mini_mos.cli import main


def invoke(monkeypatch, config_path, trace, *extra):
    monkeypatch.setattr(sys, "argv", ["mini-mos", "--config", str(config_path),
                                      "--trace", str(trace), *extra])
    return main()


def test_mock_trace_and_no_overwrite(monkeypatch, config_path, tmp_path):
    path = tmp_path / "trace.json"
    assert invoke(monkeypatch, config_path, path, "--mock-response", "fixture text") == 0
    result = json.loads(path.read_text())
    assert result["mode"] == "mock"
    assert result["output"] == "fixture text"
    with pytest.raises(FileExistsError):
        invoke(monkeypatch, config_path, path, "--mock-response", "overwrite")
    assert json.loads(path.read_text())["output"] == "fixture text"


def test_bad_agent_index(monkeypatch, config_path, tmp_path):
    with pytest.raises(SystemExit) as exc:
        invoke(monkeypatch, config_path, tmp_path / "trace.json", "--agent", "-1")
    assert exc.value.code == 2


def test_live_placeholder_rejected_before_network(monkeypatch, config_path, tmp_path):
    monkeypatch.setenv("MODEL_NAME", "REPLACE_WITH_INSTALLED_TAG")
    with pytest.raises(SystemExit) as exc:
        invoke(monkeypatch, config_path, tmp_path / "trace.json")
    assert exc.value.code == 2
    assert not (tmp_path / "trace.json").exists()
