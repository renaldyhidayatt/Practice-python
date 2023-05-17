from typing import List


def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
    xors = [0] * len(arr)
    xors[0] = arr[0]
    for i in range(1, len(arr)):
        xors[i] = arr[i] ^ xors[i - 1]

    res = []
    for q in queries:
        res.append(xors[q[1]])

        if q[0] > 0:
            res[-1] ^= xors[q[0] - 1]

    return res
