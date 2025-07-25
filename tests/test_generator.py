from generator import generate


def test_generate_one_word():
    name = generate(1, "-")
    assert isinstance(name, str)
    assert "-" not in name


def test_generate_two_words():
    name = generate(2, "-")
    parts = name.split("-")
    assert len(parts) == 2


def test_generate_three_words():
    name = generate(3, "-")
    parts = name.split("-")
    assert len(parts) == 3


def test_generate_invalid_word_count():
    import pytest

    with pytest.raises(ValueError):
        generate(0, "-")
