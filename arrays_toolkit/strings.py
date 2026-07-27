"""Strings in Python are immutable sequences. That changes how you build and
mutate them: concatenation in a loop is O(n^2); join over a list is O(n)."""
from __future__ import annotations

from collections import Counter


def reverse_words(sentence: str) -> str:
    """Reverse the order of words, collapsing extra whitespace."""
    return " ".join(reversed(sentence.split()))


def char_frequency(s: str) -> dict[str, int]:
    """Count occurrences of each character — the basis of many string problems."""
    return dict(Counter(s))


def is_anagram(a: str, b: str) -> bool:
    """Two strings are anagrams iff they have identical character counts."""
    return Counter(a) == Counter(b)


def build_repeated(ch: str, n: int) -> str:
    """Build ch repeated n times via a list + join — O(n), not O(n^2)."""
    parts = []
    for _ in range(n):
        parts.append(ch)        # appending to a list is amortized O(1)
    return "".join(parts)       # one join is O(n); '+=' in the loop would be O(n^2)
