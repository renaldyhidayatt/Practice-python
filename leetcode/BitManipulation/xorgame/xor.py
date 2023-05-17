from typing import List


def xorGame(nums: List[int]) -> bool:
    if len(nums) % 2 == 0:
        return True

    xor = 0

    for num in nums:
        xor ^= num

    return xor == 0
