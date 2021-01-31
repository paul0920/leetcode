def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """

    if not obstacleGrid:
        return 0

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):

        if obstacleGrid[i][0]:
            break

        dp[i][0] = 1

    for j in range(n):

        if obstacleGrid[0][j]:
            break

        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):

            if obstacleGrid[i][j]:
                continue

            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print uniquePathsWithObstacles(obstacleGrid)
