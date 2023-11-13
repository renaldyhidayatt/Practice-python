from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    if n == 0:
        return []

    if n == 1:
        return [[1]]

    res = [[0 for _ in range(n)] for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    spDir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    round, x, y = 0, 0, 0

    for i in range(n * n):
        x += spDir[round % 4][0]
        y += spDir[round % 4][1]

        if (
            (x == 0 and y == n - 1)
            or (x == n - 1 and y == n - 1)
            or (y == 0 and x == n - 1)
        ):
            round += 1

        if x > n - 1 or y > n - 1 or x < 0 or y < 0:
            return res

        if visit[x][y] == 0:
            visit[x][y] = 1
            res[x][y] = i + 2

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directions_idx = round % 4
        next_x = x + directions[directions_idx][0]
        next_y = y + directions[directions_idx][1]

        if 0 <= next_x < n and 0 <= next_y < n and visit[next_x][next_y] == 1:
            round += 1

    return res
