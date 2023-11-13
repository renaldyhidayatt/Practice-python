from typing import List


def first_missing_positive(nums: List[int]) -> int:
    num_map = {v: v for v in nums}
    for index in range(1, len(nums) + 1):
        if index not in num_map:
            return index
    return len(nums) + 1
