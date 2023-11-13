from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    if not candidates:
        return []
    c, res = [], []
    candidates.sort()
    find_combination_sum(candidates, target, 0, c, res)
    return res


def find_combination_sum(
    nums: List[int], target: int, index: int, c: List[int], res: List[List[int]]
) -> None:
    if target <= 0:
        if target == 0:
            b = c[:]
            res.append(b)
        return

    for i in range(index, len(nums)):
        if nums[i] > target:
            break
        c.append(nums[i])
        find_combination_sum(nums, target - nums[i], i, c, res)
        c.pop()
