"""A sliding window keeps a running summary of a contiguous span and slides it
one step at a time, updating incrementally instead of recomputing from scratch."""
from __future__ import annotations


def max_sum_window(nums: list[int], k: int) -> int | None:
    """Largest sum of any k consecutive elements, or None if k is invalid."""
    if k <= 0 or k > len(nums):
        return None
    window = sum(nums[:k])               # first window, computed once
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]  # add the new element, drop the old one
        best = max(best, window)
    return best


def longest_subarray_at_most(nums: list[int], limit: int) -> int:
    """Length of the longest contiguous subarray whose sum is <= limit,
    assuming non-negative values. Expand right; contract left when over."""
    left = 0
    running = 0
    best = 0
    for right in range(len(nums)):
        running += nums[right]               # expand the window to the right
        while running > limit and left <= right:
            running -= nums[left]            # contract from the left until valid
            left += 1
        best = max(best, right - left + 1)
    return best
