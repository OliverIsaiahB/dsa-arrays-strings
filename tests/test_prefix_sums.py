from arrays_toolkit.prefix_sums import (
    build_prefix,
    range_sum,
    count_subarrays_with_sum,
)


def test_build():
    assert build_prefix([1, 2, 3]) == [0, 1, 3, 6]


def test_range_sum_middle():
    prefix = build_prefix([1, 2, 3, 4])
    assert range_sum(prefix, 1, 3) == 5      # 2 + 3


def test_range_sum_full():
    prefix = build_prefix([1, 2, 3, 4])
    assert range_sum(prefix, 0, 4) == 10


def test_range_sum_empty_range():
    prefix = build_prefix([1, 2, 3])
    assert range_sum(prefix, 2, 2) == 0


def test_count_subarrays_basic():
    assert count_subarrays_with_sum([1, 1, 1], 2) == 2


def test_count_subarrays_with_negatives():
    assert count_subarrays_with_sum([1, -1, 0], 0) == 3


def test_count_subarrays_none():
    assert count_subarrays_with_sum([1, 2, 3], 100) == 0
