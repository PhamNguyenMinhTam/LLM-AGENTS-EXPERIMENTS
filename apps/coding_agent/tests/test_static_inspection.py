from apps.coding_agent.app import inspect_code


def test_untrusted_code_is_never_executed(tmp_path):
    target = tmp_path / "should-not-exist"
    code = f"from pathlib import Path\nPath({str(target)!r}).write_text('bad')"
    result = inspect_code(code)
    assert result["syntax_valid"]
    assert result["execution"] == "blocked_no_sandbox"
    assert result["unit_tests"] == "not_run"
    assert not target.exists()


def test_syntax_error_is_reported():
    result = inspect_code("def broken(:")
    assert not result["syntax_valid"]
    assert result["syntax_error"]["line"] == 1
