"""Pup name generator."""

import random

from words.adjectives import ADJECTIVES
from words.adverbs import ADVERBS
from words.names import NAMES


def adverb() -> str:
    return random.choice(ADVERBS)


def adjective() -> str:
    return random.choice(ADJECTIVES)


def pup() -> str:
    return random.choice(NAMES)


def generate(words: int, separator: str) -> str:
    """Generate a pup name with given number of words.

    Args:
        words: Number of words (≥1).
        separator: Separator between words.

    Returns:
        A generated pup name.

    Raises:
        ValueError: If word count is < 1.
    """
    if words < 1:
        raise ValueError("words must be >= 1")

    if words == 1:
        return pup()
    if words == 2:
        return f"{adjective()}{separator}{pup()}"

    name_parts = [adverb() for _ in range(words - 2)] + [adjective(), pup()]
    return separator.join(name_parts)
