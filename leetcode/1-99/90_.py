from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    c = []
    nums.sort()

    def generateSubsetsWithDup(
        nums: List[int], k: int, start: int, c: List[int], res: List[List[int]]
    ):
        if len(c) == k:
            res.append(list(c))
            return

        for i in range(start, len(nums) - (k - len(c)) + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue

            c.append(nums[i])
            generateSubsetsWithDup(nums=nums, k=k, start=i + 1, c=c, res=res)
            c.pop()

    for k in range(len(nums) + 1):
        generateSubsetsWithDup(nums, k, 0, c, res)

    return res
