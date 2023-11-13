from typing import List


def gray_code(n: int) -> List[int]:
    l = 1 << n
    out = [0] * 1

    for i in range(l):
        out[i] = (i >> 1) ^ i

    return out
