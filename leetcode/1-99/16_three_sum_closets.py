import math
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    n = len(nums)
    res = 0
    diff = math.inf

    if n > 2:
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                _sum = nums[i] + nums[j] + nums[k]

                if abs(_sum - target) < diff:
                    res = _sum
                    diff = abs(_sum - target)

                if _sum == target:
                    return res
                elif _sum > target:
                    k -= 1
                else:
                    j += 1

    return res
