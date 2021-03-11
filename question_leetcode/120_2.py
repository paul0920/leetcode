# DFS: divide & conquer. TLE
# Time complexity: O(2^n), n: triangle layer counts

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    return dfs(triangle, 0, 0)


def dfs(triangle, x, y):
    if x == len(triangle):
        return 0

    left = dfs(triangle, x + 1, y)
    right = dfs(triangle, x + 1, y + 1)

    return triangle[x][y] + min(left, right)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print minimumTotal(triangle)
