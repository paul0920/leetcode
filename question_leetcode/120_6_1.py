# Top -> down
# Time complexity: O(n^2), n: triangle layer counts

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    n = len(triangle)
    # dp = [[0] * n, [0] * n]
    dp = [[0] * (i + 1) for i in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        dp[i][0] = triangle[i][0] + dp[i - 1][0]
        dp[i][i] = triangle[i][i] + dp[i - 1][i - 1]

        for j in range(1, i):
            dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])

    return min(dp[n - 1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print minimumTotal(triangle)
