from typing import List


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    if not candidates:
        return []

    candidates.sort()
    c, res = [], []
    find_combination_sum_2(candidates, target, 0, c, res)
    return res


def find_combination_sum_2(
    nums: List[int], target: int, index: int, c: List[int], res: List[List[int]]
) -> None:
    if target == 0:
        b = c[:]
        res.append(b)
        return

    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        if target >= nums[i]:
            c.append(nums[i])
            find_combination_sum_2(nums, target - nums[i], i + 1, c, res)
            c.pop()
