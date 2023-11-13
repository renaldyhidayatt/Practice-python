from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0:
        return False

    m, low, high = len(matrix[0]), 0, len(matrix[0]) * len(matrix) - 1

    while low <= high:
        mid = low + (high - low) >> 1

        if matrix[mid / m][mid % m] == target:
            return True
        elif matrix[mid / m][mid % m] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False
