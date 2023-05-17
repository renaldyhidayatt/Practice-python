from typing import List


def totalHammingDistance(nums: List[int]) -> int:
    total, n = 0, len(nums)
    for i in range(32):
        bit_count = 0
        for j in range(n):
            bit_count += (nums[j] >> i) & 1
        total += bit_count * (n - bit_count)
    return total
