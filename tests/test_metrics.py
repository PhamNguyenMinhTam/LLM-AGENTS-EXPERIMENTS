from evaluation.metrics import consistency, exact_match, latency_statistics


def test_accuracy():
    assert exact_match(" 5\n", "5") == 1
    assert exact_match("five", "5") == 0


def test_latency():
    assert latency_statistics(list(range(1, 21))) == {"mean": 10.5, "median": 10.5, "p95": 19}
    assert latency_statistics([])["p95"] is None


def test_consistency():
    assert consistency(["a", "b", "a"]) == 2/3
    assert consistency([]) is None
