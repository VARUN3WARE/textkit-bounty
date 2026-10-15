import pytest

from textkit import chunk, parse_duration, slugify, truncate, word_count


def test_chunk_even():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_chunk_rejects_zero():
    with pytest.raises(ValueError):
        chunk([1], 0)


def test_slugify_simple():
    assert slugify("hello") == "hello"


def test_slugify_complex():
    assert slugify("Hello, World!") == "hello-world"


def test_parse_duration_hours_minutes():
    assert parse_duration("1h30m") == 5400


def test_word_count_simple():
    assert word_count("hello world") == 2


def test_truncate_short_text_unchanged():
    assert truncate("short", 10) == "short"


def test_truncate_long_text_cut():
    assert truncate("abcdefghij", 5).startswith("ab")
