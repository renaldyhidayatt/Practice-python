def numIslands(grid):
    m = len(grid)
    if m == 0:
        return 0

    n = len(grid[0])

    if n == 0:
        return 0

    res = 0

    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not visited[i][j]:
                searchIslands(grid, visited, i, j)

                res += 1

    return res


def searchIslands(grid, visited, x, y):
    visited[x][y] = True
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for d in directions:
        nx = x + d[0]
        ny = y + d[1]

        if isInBoard(grid, nx, ny) and not visited[nx][ny] and grid[nx][ny] == "1":
            searchIslands(grid, visited, nx, ny)


def isInBoard(grid, x, y):
    m = len(grid)
    n = len(grid[0])

    return 0 <= x < m and 0 <= y < n
