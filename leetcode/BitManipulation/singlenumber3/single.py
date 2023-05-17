from typing import List


def singleNumberIII(nums: List[int]) -> List[int]:
    diff = 0

    for num in nums:
        diff ^= num

    diff &= -diff

    res = [0, 0]

    for num in nums:
        if (num and diff) == 0:
            res[0] ^= num
        else:
            res[1] ^= num

    return res
