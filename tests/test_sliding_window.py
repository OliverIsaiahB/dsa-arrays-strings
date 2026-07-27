from arrays_toolkit.sliding_window import max_sum_window, longest_subarray_at_most


def test_basic():
    assert max_sum_window([1, 4, 2, 10, 2, 3], 3) == 14   # 2 + 10 + 2


def test_window_equals_length():
    assert max_sum_window([5, 5, 5], 3) == 15


def test_k_too_big():
    assert max_sum_window([1, 2], 5) is None


def test_k_zero():
    assert max_sum_window([1, 2], 0) is None


def test_longest_at_most():
    assert longest_subarray_at_most([1, 2, 1, 0, 1, 1], 4) == 5


def test_longest_all_fit():
    assert longest_subarray_at_most([1, 1, 1], 10) == 3


def test_longest_none_fit():
    assert longest_subarray_at_most([5, 6], 4) == 0
