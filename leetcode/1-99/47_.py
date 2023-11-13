from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    used, p, res = [False] * len(nums), [], []
    nums.sort()
    generate_permutation_unique(nums, 0, p, res, used)
    return res


def generate_permutation_unique(
    nums: List[int], index: int, p: List[int], res: List[List[int]], used: List[bool]
) -> None:
    if index == len(nums):
        temp = p[:]
        res.append(temp)
        return

    for i in range(len(nums)):
        if not used[i]:
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            p.append(nums[i])
            generate_permutation_unique(nums, index + 1, p, res, used)
            p.pop()
            used[i] = False
