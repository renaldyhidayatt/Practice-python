from typing import List


def removeElement(nums: List[int], val: int) -> int:
    if len(nums) == 0:
        return 0

    j = 0

    for i in range(nums):
        if nums[i] != val:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return j
