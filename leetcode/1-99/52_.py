from typing import List



def totalNQueens1(n: int) -> int:
    col, dia1, dia2, row, res = (
        [False] * n,
        [False] * (2 * n - 1),
        [False] * (2 * n - 1),
        [],
        [0],
    )

    def putQueen52(n, index, col, dia1, dia2, row, res):
        if index == n:
            res[0] += 1
            return

        for i in range(n):
            if not col[i] and not dia1[index + i] and not dia2[index - i + n - 1]:
                row.append(i)
                col[i] = True
                dia1[index + i] = True
                dia2[index - i + n - 1] = True
                putQueen52(n, index + 1, col, dia1, dia2, row, res)
                col[i] = False
                dia1[index + i] = False
                dia2[index - i + n - 1] = False
                row.pop()

    putQueen52(n, 0, col, dia1, dia2, row, res)
    return res[0]
