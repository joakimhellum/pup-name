from validator import validate


def test_valid_one_word():
    assert validate("pup")


def test_valid_two_words():
    assert validate("actual-pup")


def test_valid_three_words():
    assert validate("actually-actual-pup")


def test_invalid_word():
    assert not validate("fake-pup")


def test_invalid_too_many_parts():
    name = "-".join(["quickly"] * 11)
    assert not validate(name)


def test_valid_max_parts():
    name = "-".join(["quickly"] * 8 + ["actual", "pup"])
    assert validate(name)
