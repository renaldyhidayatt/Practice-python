from typing import List

def singleNumber(nums: List[int]) -> int:
    result = 0

    for i in range(len(nums)):
        result ^= nums[i]

    return result