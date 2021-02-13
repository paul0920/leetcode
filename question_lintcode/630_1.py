def shortestPath2(grid):
    # write your code here
    if not grid or not grid[0]:
        return -1

    n = len(grid)
    m = len(grid[0])
    dp = [[float("INF")] * m for _ in range(n)]
    dp[0][0] = 0
    DIRECTIONS = [(2, -1), (1, -2), (-1, -2), (-2, -1)]

    # The outer loop has to be column since
    # the problem's criterion is to walk from left to right
    for j in range(m):
        for i in range(n):
            if grid[i][j]:
                continue

            for dx, dy in DIRECTIONS:
                x = i + dx
                y = j + dy

                if x < 0 or x >= n or y < 0 or y >= m:
                    continue

                dp[i][j] = min(dp[i][j], dp[x][y] + 1)

    # for row in dp:
    #     print row

    return dp[n - 1][m - 1] if dp[n - 1][m - 1] != float("INF") else -1


nums = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print shortestPath2(nums)
