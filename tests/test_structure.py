from controller.config import ROOT


def test_experiment_structure():
    directories = sorted(p for p in (ROOT/"experiments").glob("E[0-9][0-9]_*") if p.is_dir())
    assert len(directories) == 12
    for directory in directories:
        for name in ["README.md", "CHECKLIST.md", "EVALUATION.md", "config.yaml", "run.py", "results/.gitkeep"]:
            assert (directory/name).is_file()
        evaluation = (directory/"EVALUATION.md").read_text(encoding="utf-8")
        assert "| Tiêu chí | Định nghĩa | Công thức/cách đo | Đơn vị | Nguồn dữ liệu | Cách diễn giải |" in evaluation
