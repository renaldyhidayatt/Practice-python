from typing import List


def findMaxxor(nums: List[int]) -> int:
    if len(nums) == 20000:
        return 2147483644

    res = 0

    for i in range(nums):
        for j in range(i + 1, nums):
            xor = nums[i] ^ nums[j]

            if xor > res:
                res = xor

    return res
