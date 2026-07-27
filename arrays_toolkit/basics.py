"""Array basics. An array is a contiguous block of memory, which is why
reading nums[i] is O(1): the address is base + i * element_size, one jump."""
from __future__ import annotations


def index_of(nums: list[int], target: int) -> int:
    """Return the first index of target, or -1 if absent. A plain O(n) scan."""
    for i, value in enumerate(nums):
        if value == target:
            return i
    return -1


def get_or_default(nums: list[int], i: int, default: int) -> int:
    """Safe read: return nums[i] if i is a valid index, else default."""
    if 0 <= i < len(nums):
        return nums[i]
    return default
