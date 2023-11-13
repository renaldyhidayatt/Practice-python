from typing import List


def solveNQueens2(n: int) -> List[List[str]]:
    placements = ["".join(["Q" if i == j else "." for j in range(n)]) for i in range(n)]
    res: List[List[str]] = []

    def construct(prev: List[int]) -> None:
        if len(prev) == n:
            plan = [placements[prev[i]] for i in range(n)]
            res.append(plan)
            return

        occupied = 0
        for i in range(len(prev)):
            dist = len(prev) - i
            bit = 1 << prev[i]
            occupied |= bit | (bit << dist) | (bit >> dist)

        prev.append(-1)
        for i in range(n):
            if (occupied >> i) & 1:
                continue
            prev[-1] = i
            construct(prev[:])

    construct([])
    return res
