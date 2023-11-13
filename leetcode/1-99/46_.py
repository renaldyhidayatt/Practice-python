from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []

    def generate_permutation(
        nums: List[int],
        index: int,
        p: List[int],
        res: List[List[int]],
        used: List[bool],
    ):
        if index == len(nums):
            temp = p[:]
            res.append(temp)
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                p.append(nums[i])
                generate_permutation(nums, index + 1, p, res, used)
                p.pop()
                used[i] = False

    used = [False] * len(nums)

    p, res = [], []
    generate_permutation(nums, 0, p, res, used)
    return res
