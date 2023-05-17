from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [0] + [amount + 1] * amount

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j] + 1])

    if dp[amount] > amount:
        return -1

    return dp[amount]
