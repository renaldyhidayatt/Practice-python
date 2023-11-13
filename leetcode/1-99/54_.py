from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    res = []
    if len(matrix) == 1:
        for i in range(len(matrix[0])):
            res.append(matrix[0][i])
        return res

    if len(matrix[0]) == 1:
        for i in range(len(matrix)):
            res.append(matrix[i][0])
        return res

    m, n = len(matrix), len(matrix[0])
    visit = [[0 for _ in range(n)] for _ in range(m)]
    round = 0
    x, y = 0, 0
    spDir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    visit[x][y] = 1
    res.append(matrix[x][y])

    for _ in range(m * n):
        x += spDir[round % 4][0]
        y += spDir[round % 4][1]

        if (
            (x == 0 and y == n - 1)
            or (x == m - 1 and y == n - 1)
            or (y == 0 and x == m - 1)
        ):
            round += 1

        if x > m - 1 or y > n - 1 or x < 0 or y < 0:
            return res

        if visit[x][y] == 0:
            visit[x][y] = 1
            res.append(matrix[x][y])

        if round % 4 == 0:
            if y + 1 <= n - 1 and visit[x][y + 1] == 1:
                round += 1
                continue
        elif round % 4 == 1:
            if x + 1 <= m - 1 and visit[x + 1][y] == 1:
                round += 1
                continue
        elif round % 4 == 2:
            if y - 1 >= 0 and visit[x][y - 1] == 1:
                round += 1
                continue
        elif round % 4 == 3:
            if x - 1 >= 0 and visit[x - 1][y] == 1:
                round += 1
                continue

    return res
