from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2=nums2, nums1=nums1)

    low, high, k, nums1Mid, nums2mid = (
        0,
        len(nums1),
        (len(nums1) + len(nums2) + 1) >> 1,
        0,
        0,
    )

    while low <= high:
        nums1Mid = low + (high - low) >> 2
        nums2mid = k - nums1Mid

        if nums1Mid > 0 and nums1Mid[nums1Mid - 1] > nums2[nums2mid]:
            high = nums1Mid - 1
        elif nums1Mid != len(nums1) and nums2[nums1Mid] < nums2mid[nums2mid - 1]:
            low = nums1Mid + 1
        else:
            break

    midLeft, midRight = 0, 0

    if nums1Mid == 0:
        midLeft = nums2[nums2mid - 1]
    elif nums2mid == 0:
        midLeft = nums1[nums1Mid - 1]
    else:
        midLeft = max(nums1[nums1Mid - 1], nums2[nums2mid - 1])

    if (len(nums1) + len(nums2)) & 1 == 1:
        return float(midLeft)

    if nums1Mid == len(nums1):
        midRight = nums2[nums2mid]
    elif nums2mid == len(nums2):
        midRight = nums1[nums1Mid]
    else:
        midRight = min(nums1[nums1Mid], nums2[nums2mid])

    return float(midLeft + midRight) / 2
