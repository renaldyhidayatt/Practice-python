from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    result = []
    length = len(nums)

    for index in range(1, length - 1):
        start, end = 0, length - 1

        if index > 1 and nums[index] == nums[index - 1]:
            start = index - 1

        while start < index and end > index:
            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
                continue

            if end < length - 1 and nums[end] == nums[end + 1]:
                end -= 1
                continue

            addNum = nums[start] + nums[end] + nums[index]

            if addNum == 0:
                result.append([nums[start], nums[index], nums[end]])
                start += 1
                end -= 1
            elif addNum > 0:
                end -= 1
            else:
                start += 1

    return result
