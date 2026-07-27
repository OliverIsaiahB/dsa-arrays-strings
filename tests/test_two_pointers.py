from arrays_toolkit.two_pointers import (
    two_sum_sorted,
    reverse_in_place,
    remove_value,
    dedup_sorted,
)


def test_two_sum_found():
    assert two_sum_sorted([1, 2, 4, 7, 11], 9) == (1, 3)


def test_two_sum_none():
    assert two_sum_sorted([1, 2, 3], 100) is None


def test_two_sum_empty():
    assert two_sum_sorted([], 0) is None


def test_reverse_in_place():
    nums = [1, 2, 3, 4]
    reverse_in_place(nums)
    assert nums == [4, 3, 2, 1]


def test_reverse_single():
    nums = [9]
    reverse_in_place(nums)
    assert nums == [9]


def test_remove_value():
    nums = [3, 1, 3, 2, 3]
    n = remove_value(nums, 3)
    assert n == 2
    assert nums[:n] == [1, 2]


def test_dedup_sorted():
    nums = [1, 1, 2, 2, 2, 3]
    n = dedup_sorted(nums)
    assert n == 3
    assert nums[:n] == [1, 2, 3]


def test_dedup_empty():
    assert dedup_sorted([]) == 0
