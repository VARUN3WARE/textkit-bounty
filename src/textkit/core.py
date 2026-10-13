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


def parse_duration(text):
    """Parse durations like ``"1h30m"`` into seconds."""
    total = 0
    for value, unit in re.findall(r"(\d+)([hms])", text):
        total += int(value) * _UNITS.get(unit, 0)
    return total


def word_count(text):
    """Count the words in ``text``."""
    return len(text.split(" "))


def truncate(text, limit):
    """Shorten ``text`` to at most ``limit`` characters, adding "..." if cut."""
    if len(text) <= limit:
        return text
    return text[:limit - 1] + "..."
