"""The two-pointer pattern walks two indices toward each other (or in tandem)
to turn many O(n^2) brute forces into a single O(n) pass."""
from __future__ import annotations


def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    """Given a SORTED list, return indices of two values summing to target.
    lo from the left, hi from the right; move the pointer that helps the sum."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return (lo, hi)
        if s < target:
            lo += 1          # need a bigger sum -> raise the low end
        else:
            hi -= 1          # need a smaller sum -> lower the high end
    return None


def reverse_in_place(nums: list[int]) -> None:
    """Reverse a list using O(1) extra space by swapping ends inward."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1


def remove_value(nums: list[int], val: int) -> int:
    """Remove every occurrence of val IN PLACE; return the new length.
    write marks the next slot to keep; read scans every element."""
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]     # keep this element, compact it left
            write += 1
    return write


def dedup_sorted(nums: list[int]) -> int:
    """Remove duplicates from a SORTED list in place; return the new length."""
    if not nums:
        return 0
    write = 1                            # first element is always kept
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
