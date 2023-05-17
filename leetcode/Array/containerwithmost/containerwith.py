from typing import List


def maxArea(height: List[int]) -> int:
    max, start, end = 0, 0, len(height) - 1

    while start < end:
        width = end - start

        high = 0
        if height[start] < height[end]:
            high = height[start]
            start++
        else:
            high = height[end]

        temp = width * high

        if temp > max:
            max = temp

    return max
