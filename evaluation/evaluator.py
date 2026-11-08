from evaluation.metrics import exact_match


def evaluate(actual, expected):
    score = exact_match(actual, expected)
    return {"score": score, "success": score == 1}
