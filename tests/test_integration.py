"""End-to-end sanity: the patterns compose and agree with brute force."""
from arrays_toolkit.two_pointers import two_sum_sorted
from arrays_toolkit.prefix_sums import build_prefix, range_sum, count_subarrays_with_sum
from arrays_toolkit.sliding_window import max_sum_window


def brute_range_sum(nums, lo, hi):
    return sum(nums[lo:hi])


def test_prefix_matches_brute():
    nums = [4, -1, 2, 7, 0, 3]
    prefix = build_prefix(nums)
    for lo in range(len(nums) + 1):
        for hi in range(lo, len(nums) + 1):
            assert range_sum(prefix, lo, hi) == brute_range_sum(nums, lo, hi)


def test_window_matches_brute():
    nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 3
    brute = max(sum(nums[i:i + k]) for i in range(len(nums) - k + 1))
    assert max_sum_window(nums, k) == brute


def test_two_sum_sorted_consistency():
    nums = [1, 3, 4, 5, 7, 11]
    res = two_sum_sorted(nums, 9)
    assert res is not None and nums[res[0]] + nums[res[1]] == 9


def test_count_subarrays_matches_brute():
    nums = [3, 1, -2, 4, 0]
    k = 4
    brute = sum(
        1
        for i in range(len(nums))
        for j in range(i + 1, len(nums) + 1)
        if sum(nums[i:j]) == k
    )
    assert count_subarrays_with_sum(nums, k) == brute
