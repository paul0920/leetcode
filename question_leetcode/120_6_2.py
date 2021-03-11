# Top -> down
# Time complexity: O(n^2), n: triangle layer counts
# Space complexity: O(n)

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    n = len(triangle)
    dp = [[0] * n, [0] * n]
    # dp = [[0] * (i + 1) for i in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        dp[i % 2][0] = triangle[i][0] + dp[(i - 1) % 2][0]
        dp[i % 2][i] = triangle[i][i] + dp[(i - 1) % 2][i - 1]

        for j in range(1, i):
            dp[i % 2][j] = triangle[i][j] + min(dp[(i - 1) % 2][j - 1], dp[(i - 1) % 2][j])

    return min(dp[(n - 1) % 2])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print minimumTotal(triangle)
