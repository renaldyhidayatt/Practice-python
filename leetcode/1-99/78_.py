def subsets(nums):
    res = []
    c = []
    for k in range(len(nums) + 1):
        generate_subsets(nums, k, 0, c, res)
    return res


def generate_subsets(nums, k, start, c, res):
    if len(c) == k:
        res.append(c[:])
        return

    for i in range(start, len(nums) - (k - len(c)) + 1):
        c.append(nums[i])
        generate_subsets(nums, k, i + 1, c, res)
        c.pop()
