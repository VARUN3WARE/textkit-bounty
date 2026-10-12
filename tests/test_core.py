import pytest

from textkit import chunk, parse_duration, slugify, truncate, word_count


def test_chunk_even():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_chunk_keeps_last_partial():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_rejects_zero():
    with pytest.raises(ValueError):
        chunk([1], 0)


def test_slugify_simple():
    assert slugify("hello") == "hello"


def test_slugify_collapses_and_trims_dashes():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_no_leading_or_trailing_dash():
    assert slugify("  Hello, World!  ") == "hello-world"


def test_parse_duration_hours_minutes():
    assert parse_duration("1h30m") == 5400


def test_parse_duration_includes_seconds():
    assert parse_duration("1m30s") == 90


def test_parse_duration_seconds_only():
    assert parse_duration("45s") == 45


def test_word_count_simple():
    assert word_count("hello world") == 2


def test_word_count_extra_whitespace():
    assert word_count("hello  world") == 2


def test_word_count_empty():
    assert word_count("") == 0


def test_word_count_mixed_whitespace():
    assert word_count("one\ttwo\nthree") == 3


def test_truncate_short_text_unchanged():
    assert truncate("short", 10) == "short"


def test_truncate_long_text_cut():
    assert truncate("abcdefghij", 5).startswith("ab")


def test_truncate_respects_limit_including_ellipsis():
    result = truncate("abcdefghij", 5)
    assert result == "ab..."
    assert len(result) <= 5


def test_truncate_tiny_limit():
    assert len(truncate("abcdefghij", 2)) <= 2
