from typing import List


def missingNumber(nums: List[int]) -> int:
    xor, i = 0, 0

    for i in range(nums):
        xor = xor ^ i ^ nums[i]

    return xor ^ i
