from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0
    start = 0
    end = len(height) - 1

    while start < end:
        width = end - start
        h = min(height[start], height[end])
        area = width * h

        if area > max_area:
            max_area = area

        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return max_area
