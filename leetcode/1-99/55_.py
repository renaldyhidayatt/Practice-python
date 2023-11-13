from typing import List


def canJump(nums: List[int]) -> bool:
    n = len(nums)

    if n == 0:
        return False

    if n == 1:
        return True

    max_jump = 0

    for i, v in enumerate(nums):
        if i > max_jump:
            return False

        max_jump = max(max_jump, i + v)

    return True
