from typing import List


def maxLength(arr: List[str]) -> int:
    c, res = [], 0

    for s in arr:
        mask = 0

        for c in s:
            mask = mask | 1 << (ord(c) - ord("a"))

        if len(s) != bin(mask).count("1"):
            continue

        c.append(mask)

    dfs(c, 0, 0, res)

    return res


def dfs(c: List[int], index: int, mask: int, res: int):
    res = max(res, bin(mask).count("1"))

    for i in range(index, len(c)):
        if mask & c[i] == 0:
            dfs(c, i + 1, mask | c[i], res)

    return
