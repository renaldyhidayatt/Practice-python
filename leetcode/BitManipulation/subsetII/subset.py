def subsetsWithDup(nums: list) -> list:
    c, res = [], []
    nums.sort()

    for k in range(len(nums) + 1):
        generateSubsetsWithDup(nums, k, 0, c, res)

    return res


def generateSubsetsWithDup(nums: list, k: int, start: int, c: list, res: list):
    if len(c) == k:
        b = c.copy()
        res.append(b)
        return

    for i in range(start, len(nums) - (k - len(c)) + 1):
        if i > start and nums[i] == nums[i - 1]:
            continue
        c.append(nums[i])
        generateSubsetsWithDup(nums, k, i + 1, c, res)
        c.pop()
