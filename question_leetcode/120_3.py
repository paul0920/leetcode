# DFS: divide & conquer + memo
# Time complexity: O(n^2), n: triangle layer counts

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    return dfs(triangle, 0, 0, {})


def dfs(triangle, x, y, memo):
    if x == len(triangle):
        return 0

    if (x, y) in memo:
        return memo[(x, y)]

    left = dfs(triangle, x + 1, y, memo)
    right = dfs(triangle, x + 1, y + 1, memo)

    memo[(x, y)] = triangle[x][y] + min(left, right)

    return memo[(x, y)]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print minimumTotal(triangle)
