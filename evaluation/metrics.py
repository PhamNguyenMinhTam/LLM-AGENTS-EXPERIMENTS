import math
from collections import Counter
from statistics import mean, median


def exact_match(actual, expected):
    return float(actual.strip() == expected.strip())


def latency_statistics(values):
    if not values:
        return {"mean": None, "median": None, "p95": None}
    ordered = sorted(values)
    return {"mean": mean(values), "median": median(values),
            "p95": ordered[math.ceil(.95 * len(values)) - 1]}


def consistency(outputs):
    return max(Counter(outputs).values()) / len(outputs) if outputs else None
