from typing import List


def trap(height: List[int]) -> int:
    res, left, right, max_left, max_right = 0, 0, len(height) - 1, 0, 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] > max_left:
                max_left = height[left]
            else:
                res += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                res += max_right - height[right]
            right -= 1
    return res
