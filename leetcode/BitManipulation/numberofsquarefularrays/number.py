import math
from typing import List


def numSquarefulPerms(A: List[int]) -> int:
    if len(A) == 0:
        return 0

    used, p, res = [False] * len(A), [], []
    A.sort()

    return len(res)


def generatePermutation(
    nums: List[int], index: int, p: List[int], res: List[List[int]], used: List[bool]
):
    if index == len(nums):
        checkSquareful = True
        for i in range(len(p) - 1):
            if not checkSquare(p[i] + p[i + 1]):
                checkSquareful = False
                break
        if checkSquareful:
            res.append(p.copy())
        return
    
    for i in range(len(nums)):
        if not used[i]:
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            if len(p) > 0 and not checkSquare(nums[i] + p[-1]):
                continue
            used[i] = True
            p.append(nums[i])
            generatePermutation(nums, index + 1, p, res, used)
            p.pop()
            used[i] = False


def checkSquare(num: int) -> bool:
    tmp = int(math.sqrt(num))

    if tmp * tmp == num:
        return True
    
    return False