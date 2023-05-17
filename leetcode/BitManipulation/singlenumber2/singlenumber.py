def singleNumberII(nums: list) -> int:
    ones, twos = 0, 0

    for i in range(len(nums)):
        ones = (ones ^ nums[i]) & ~twos
        twos = (twos ^ nums[i]) & ~ones

    return ones
