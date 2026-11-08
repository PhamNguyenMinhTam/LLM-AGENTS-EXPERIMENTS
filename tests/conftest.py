import os
from pathlib import Path

import pytest

from controller.config import ROOT


@pytest.fixture(autouse=True)
def environment(monkeypatch):
    values = {"OLLAMA_ENDPOINT_A": "http://localhost:11434",
              "OLLAMA_ENDPOINT_B": "http://localhost:11435", "MODEL_NAME": "test-model:1b",
              "MODEL_DIGEST": "test-digest", "QUANTIZATION": "Q4_K_M",
              "HARDWARE_A": "test-a", "HARDWARE_B": "test-b"}
    for key, value in values.items():
        monkeypatch.setenv(key, value)


@pytest.fixture
def config_path():
    return ROOT / "experiments/E01_baseline/config.yaml"
