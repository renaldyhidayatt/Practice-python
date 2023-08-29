def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0

    last, finder = 0, 0

    while last < len(nums) - 1:
        while nums[finder] == nums[last]:
            finder += 1

            if finder == len(nums):
                return last + 1

        nums[last + 1] = nums[finder]

        last += 1

    return last + 1
