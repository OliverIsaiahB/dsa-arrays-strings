"""A prefix-sum array stores cumulative totals so any range sum becomes a single
subtraction: precompute once in O(n), then answer each query in O(1)."""
from __future__ import annotations


def build_prefix(nums: list[int]) -> list[int]:
    """prefix[i] = sum of nums[0:i]. Length is len(nums) + 1; prefix[0] = 0."""
    prefix = [0] * (len(nums) + 1)
    for i, value in enumerate(nums):
        prefix[i + 1] = prefix[i] + value
    return prefix


def range_sum(prefix: list[int], lo: int, hi: int) -> int:
    """Sum of nums[lo:hi] (hi exclusive) using a precomputed prefix array."""
    return prefix[hi] - prefix[lo]


def count_subarrays_with_sum(nums: list[int], k: int) -> int:
    """Count contiguous subarrays summing to exactly k, in one O(n) pass.
    A subarray (i, j] sums to k iff running[j] - running[i] == k."""
    counts: dict[int, int] = {0: 1}      # one empty prefix (sum 0) seen so far
    running = 0
    total = 0
    for value in nums:
        running += value
        total += counts.get(running - k, 0)   # prefixes that make a k-sum end here
        counts[running] = counts.get(running, 0) + 1
    return total
