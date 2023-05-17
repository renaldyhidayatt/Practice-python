from typing import List


def subArrayBitwiseOrs(A: List[int]) -> int:
    res, t = set(), set()

    for num in A:
        r = set()

        r.add(num)

        for n in t:
            r.add(num | n)

        t = r

        for n in t:
            res.add(n)

    return len(res)
