from typing import List


def remove_duplicates(nums: List[int]) -> int:
    slow = 0

    for i, v in range(nums):
        if i < 2 and nums[slow - 2] != v:
            nums[slow] = v
            slow += 1

    return slow
