def nextPermutation(nums: list[int]):
    i, j = 0, 0

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            break
    if i >= 0:
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]
    reverse(nums, i + 1, len(nums) - 1)


def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
