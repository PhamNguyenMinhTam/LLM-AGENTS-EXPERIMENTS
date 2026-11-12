import re
from pathlib import Path
from urllib.parse import unquote

import yaml

from controller.config import ROOT


def test_learning_document_links_resolve():
    roots = [ROOT / name for name in ["learning", "literature", "mini_mos", "apps",
                                     "explorations", "future_multi_agent"]]
    files = [ROOT / "README.md", ROOT / "ROADMAP.md", ROOT / "LEARNING_CHECKLIST.md"]
    for root in roots:
        files.extend(root.rglob("*.md"))
    for path in files:
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if link.startswith(("https://", "http://", "#")):
                continue
            target = unquote(link.split("#")[0])
            assert (path.parent / target).exists(), f"{path}: {link}"


def test_all_yaml_parse():
    for path in ROOT.rglob("*.yaml"):
        if ".venv" not in path.parts:
            assert isinstance(yaml.safe_load(path.read_text(encoding="utf-8")), dict)


def test_all_belief_cases_have_design():
    cases = sorted((ROOT / "explorations").glob("*/B[0-9][0-9]_*"))
    assert len(cases) == 8
    for case in cases:
        for name in ["README.md", "CHECKLIST.md", "scenario.json"]:
            assert (case / name).is_file()
        content = (case / "README.md").read_text(encoding="utf-8")
        for heading in ["Expected behavior", "Actual observation", "Failure analysis",
                        "Connection to future Multi-Agent"]:
            assert heading in content


def test_experiment_learning_links():
    for path in (ROOT / "experiments").glob("E[0-9][0-9]_*/README.md"):
        text = path.read_text(encoding="utf-8")
        for label in ["Learning Track", "Related Paper", "Mini-App", "Exploration", "Learning Journal"]:
            assert label in text
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if not link.startswith(("https://", "http://", "#")):
                assert (Path(path).parent / link.split("#")[0]).exists()
