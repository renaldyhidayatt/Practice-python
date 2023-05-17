from typing import List


def combinationSum(candidates: List[int], target: int) -> List[int]:
    if len(candidates) == 0:
        return []
    c, res = [], []

    candidates.sort()

    findCombinationSum(candidates, target, 0, c, res)

    return res


def findCombinationSum(
    nums: List[int], target: int, index: int, c: List[int], res: List[int]
):
    if target <= 0:
        if target == 0:
            res.append(c[:])
            return

        for i in range(index, len(nums)):
            if nums[i] > target:
                break

            c.append(nums[i])

            findCombinationSum(nums, target - nums[i], i, c, res)

            c.pop()
