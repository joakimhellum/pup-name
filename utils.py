"""Utility functions for generating pup names."""

import uuid

from generator import generate

def generate_with_uuid(
    words: int = 2, separator: str = "-", used: set[str] | None = None
) -> str:
    """Generate a unique pup name with a short UUID suffix.

    Args:
        words: Number of base words in name.
        separator: Word separator.
        used: Set of previously generated names.

    Returns:
        Unique name with UUID suffix.

    Raises:
        RuntimeError: If a unique name can't be generated.
    """
    if used is None:
        used = set()

    for _ in range(1000):
        base = generate(words, separator)
        suffix = uuid.uuid4().hex[:4]
        full = f"{base}{separator}{suffix}"
        if full not in used:
            used.add(full)
            return full

    raise RuntimeError("Unable to find unique name with UUID.")


def unique(used: set[str], words: int = 2, separator: str = "-") -> str:
    """Generate a unique pup name.

    Args:
        used: Set of previously generated names.
        words: Number of base words in name.
        separator: Word separator.

    Returns:
        A unique name.

    Raises:
        RuntimeError: If no unique name can be found.
    """
    for _ in range(1000):
        name = generate(words, separator)
        if name not in used:
            used.add(name)
            return name

    raise RuntimeError(
        "Unable to find a unique name after 1000 attempts. "
        "Try increasing the number of words, reducing the count, "
        "or using '--uuid' for uniqueness."
    )
