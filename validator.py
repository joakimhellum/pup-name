"""Pup name validation logic."""

from words.adverbs import ADVERBS
from words.adjectives import ADJECTIVES
from words.names import NAMES


def validate(name: str, separator: str = "-") -> bool:
    """Validate a pup name based on word list structure.

    Args:
        name: Name string to validate.
        separator: Word separator used in name.

    Returns:
        True if name format and words are valid, False otherwise.
    """
    parts = name.split(separator)

    if not 1 <= len(parts) <= 10:
        return False
    if len(parts) == 1:
        return parts[0] in NAMES
    if len(parts) == 2:
        return parts[0] in ADJECTIVES and parts[1] in NAMES

    *adverbs, adjective, noun = parts
    return (
        all(word in ADVERBS for word in adverbs)
        and adjective in ADJECTIVES
        and noun in NAMES
    )
