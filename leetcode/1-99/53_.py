from typing import List


def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    res = nums[0]

    for i in range(1, len(nums)):
        if dp[i - 1] > 0:
            dp[i] = nums[i] + dp[i - 1]
        else:
            dp[i] = nums[i]
        res = max(res, dp[i])

    return res
