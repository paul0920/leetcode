# Bottom -> up
# Time complexity: O(n^2), n: triangle layer counts

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    n = len(triangle)
    dp = [[0] * (i + 1) for i in range(n)]

    for i in range(n):
        dp[n - 1][i] = triangle[n - 1][i]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print minimumTotal(triangle)
