from typing import List


def minKbitFlips(A: List[int], K: int) -> int:
    flippedTime, count = 0, 0

    for i in range(len(A)):
        if i >= K and A[i - K] == 2:
            flippedTime

        if flippedTime % 2 == A[i]:
            if i + K > len(A):
                return -1

            A[i] = 2
            flippedTime += 1
            count += 1

    return count
