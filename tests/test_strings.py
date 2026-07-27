from arrays_toolkit.strings import (
    reverse_words,
    char_frequency,
    is_anagram,
    build_repeated,
)


def test_reverse_words():
    assert reverse_words("the  quick brown") == "brown quick the"


def test_reverse_words_empty():
    assert reverse_words("   ") == ""


def test_char_frequency():
    assert char_frequency("aab") == {"a": 2, "b": 1}


def test_is_anagram_true():
    assert is_anagram("listen", "silent") is True


def test_is_anagram_false():
    assert is_anagram("abc", "abd") is False


def test_build_repeated():
    assert build_repeated("x", 3) == "xxx"
