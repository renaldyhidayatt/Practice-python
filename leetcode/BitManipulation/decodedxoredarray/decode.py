from typing import List


def decode(encoded: List[int], first: int) -> List[int]:
    arr = [first] + [0] * len(encoded)

    for i, val in enumerate(encoded):
        arr[i + 1] = arr[i] ^ val

    return arr
