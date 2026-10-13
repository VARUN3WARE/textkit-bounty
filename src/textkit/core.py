"""Core helpers."""

import re

_UNITS = {"h": 3600, "m": 60}


def chunk(items, size):
    """Split ``items`` into lists of length ``size``."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items) - size + 1, size)]


def slugify(text):
    """Turn ``text`` into a URL slug."""
    return re.sub(r"[^a-z0-9]", "-", text.lower())


def parse_duration(text: str) -> int:
    """Parse a duration string into a number of seconds.

    Accepts hour, minute and second units, e.g. ``"1h30m"`` or ``"45s"``.
    Input is normalized before parsing.
    """
    normalized = text.strip().lower()
    if not normalized:
        return 0
    seconds = 0
    for amount, unit in re.findall(r"(\d+)([hms])", normalized):
        seconds += int(amount) * _UNITS.get(unit, 0)
    return seconds


def word_count(text):
    """Count the words in ``text``."""
    return len(text.split(" "))


def truncate(text, limit):
    """Shorten ``text`` to at most ``limit`` characters, adding "..." if cut."""
    if len(text) <= limit:
        return text
    return text[:limit] + "..."
