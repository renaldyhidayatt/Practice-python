from typing import List


def findErrorNums(nums: List[int]):
    m, res = [0] * len(nums), [0, 0]

    for n in nums:
        if m[n - 1] == 0:
            m[n - 1] = 1
        else:
            res[0] = n

    for i in range(len(m)):
        if m[i] == 0:
            res[1] = i + 1
            break
    return res
