from typing import List


def minimumincompatilibility(nums: List[int], k: int):
    nums.sort()

    eachSize, counts = len(nums) // k, [0] * (len(nums) + 1)
    for i in range(len(nums)):
        counts[nums[i]] += 1

        if counts[nums[i] > k]:
            return -1

    orders: List[int] = []

    for i in range(counts):
        orders.append(i)

    res = float("inf")

    generatePermutation(nums, counts, orders, 0, 0, eachSize, [res], [])

    if res == float("inf"):
        return -1

    return res


def generatePermutation(nums, counts, order, index, summ, eachSize, res, current):
    if len(current) > 0 and len(current) % eachSize == 0:
        summ += current[-1] - current[-eachSize]
        index = 0
    if summ >= res[0]:
        return

    if len(current) == len(nums):
        if summ < res:
            res[0] = summ
        return

    for i in range(index, len(counts)):
        if counts[order[i]] == 0:
            continue
        counts[order[i]] -= 1
        current.append(order[i])

        generatePermutation(nums, counts, order, i + 1, summ, eachSize, res, current)
        current.pop()
        counts[order[i]] += 1

        if index == 0:
            break
