def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1

    for i in range(1, n):
        if dp[0][i - 1] != 0 and obstacleGrid[0][i] != 1:
            dp[0][i] = 1

    for i in range(1, m):
        if dp[i - 1][0] != 0 and obstacleGrid[i][0] != 1:
            dp[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] != 1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]
