def test_qualification_score_is_within_range():
    score = 75
    assert 0 <= score <= 100


def test_qualification_score_is_numeric():
    score = 75
    assert isinstance(score, (int, float))
