from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[nums[0]]

    while fast != slow:
        slow = nums[slow]
        fast = nums[nums[fast]]

    walker = 0

    while walker != slow:
        walker = nums[walker]
        slow = nums[slow]

    return walker
