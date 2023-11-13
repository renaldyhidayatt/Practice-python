from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    return [
        search_first_equal_element(nums, target),
        search_last_equal_element(nums, target),
    ]


def search_first_equal_element(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            if (mid == 0) or (nums[mid - 1] != target):
                return mid
            high = mid - 1

    return -1


def search_last_equal_element(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            if (mid == len(nums) - 1) or (nums[mid + 1] != target):
                return mid
            low = mid + 1
    return -1
