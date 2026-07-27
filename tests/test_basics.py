from arrays_toolkit.basics import index_of, get_or_default


def test_index_found():
    assert index_of([10, 20, 30], 20) == 1


def test_index_absent():
    assert index_of([1, 2, 3], 99) == -1


def test_index_empty():
    assert index_of([], 1) == -1


def test_get_or_default_in_range():
    assert get_or_default([5, 6, 7], 0) == 5


def test_get_or_default_out_of_range():
    assert get_or_default([5, 6, 7], 10, -1) == -1
