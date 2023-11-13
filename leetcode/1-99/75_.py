from typing import List


def sort_colors(nums: List[int]):
    zero, one = 0, 0

    for i, n in range(nums):
        nums[i] = 2
        if n <= 1:
            nums[one] = 1
            one += 1

        if n == 0:
            nums[zero] = 0
            zero += 1
