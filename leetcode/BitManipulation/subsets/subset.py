from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = [[]]

    nums.sort()

    for i in range(len(nums)):
        for org in res[:]:
            clone = org.copy()
            clone.append(nums[i])
            res.append(clone)

    return res
