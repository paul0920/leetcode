def shortestPath2(grid):
    # write your code here
    if not grid or not grid[0]:
        return -1

    n = len(grid)
    m = len(grid[0])
    dp = [[float("INF")] * 3 for _ in range(n)]
    dp[0][0] = 0
    DIRECTIONS = [(2, -1), (1, -2), (-1, -2), (-2, -1)]

    # The index has to be started with 1 instead of 0
    # due to the usage of rotational array
    for j in range(1, m):
        for i in range(n):

            # Need to initialize and clean up the previous old data
            dp[i][j % 3] = float("INF")

            if grid[i][j]:
                continue

            for dx, dy in DIRECTIONS:
                x = i + dx
                y = j + dy

                if x < 0 or x >= n or y < 0 or y >= m:
                    continue

                dp[i][j % 3] = min(dp[i][j % 3], dp[x][y % 3] + 1)

    # for row in dp:
    #     print row

    return dp[n - 1][(m - 1) % 3] if dp[n - 1][(m - 1) % 3] != float("INF") else -1


nums = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print shortestPath2(nums)
