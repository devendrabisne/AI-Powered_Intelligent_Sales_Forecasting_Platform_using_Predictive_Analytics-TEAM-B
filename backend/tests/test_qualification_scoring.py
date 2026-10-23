
def test_qualification_score_is_within_range():
    score = 75
    assert 0 <= score <= 100


def test_qualification_score_is_numeric():
    score = 75
    assert isinstance(score, (int, float))


def test_qualification_score_lower_boundary():
    score = 0
    assert 0 <= score <= 100


def test_qualification_score_upper_boundary():
    score = 100
    assert 0 <= score <= 100


def test_qualification_score_is_not_negative():
    score = 50
    assert score >= 0


def test_qualification_score_does_not_exceed_100():
    score = 90
    assert score <= 100
    
