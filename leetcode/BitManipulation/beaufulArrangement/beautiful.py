from typing import List


def countArrangement(N: int) -> int:
    if N == 0:
        return 0

    nums, used, p, res = list(range(1, N + 1)), [False] * N, [], []

    for i in range(nums):
        nums[i] = i + 1

    generatePermutation(nums, 0, p, res, used)

    return len(res)


def generatePermutation(
    nums: List[int], index: int, p: List[int], res: List[List[int]], used: List[bool]
):
    if index == len(nums):
        temp = p.copy()

        res.append(temp)

        return

    for i in range(len(nums)):
        if not used[i]:
            if not (
                checkDivisible(nums[i], len(p) + 1)
                or checkDivisible(len(p) + 1, nums[i])
            ):
                continue
            used[i] = True
            p.append(nums[i])
            generatePermutation(nums, index + 1, p, res, used)
            p.pop()
            used[i] = False

    return


def checkDivisible(num: int, d: int) -> bool:
    tmp = num / d

    if tmp * d == num:
        return True

    return False
