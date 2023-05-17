import math
from typing import List


def threeSumClosest(nums: List[int], target: int):
    n, res, diff = len(nums), 0, math.inf
    if n > 2:
        nums.sort()
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
    j, k = i + 1, n - 1
    while j < k:
        s = nums[i] + nums[j] + nums[k]
    if abs(s - target) < diff:
        res, diff = s, abs(s - target)
    if s == target:
        return res
    elif s > target:
        k -= 1
    else:
        j += 1
    return res
