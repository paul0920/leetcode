# DFS: traverse. TLE
# Time complexity: O(2^n), n: triangle layer counts

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    return dfs(triangle, 0, 0, 0, float("INF"))


def dfs(triangle, x, y, path_sum, min_sum):
    if x == len(triangle):
        return min(min_sum, path_sum)

    path_sum += triangle[x][y]

    return min(dfs(triangle, x + 1, y, path_sum, min_sum),
               dfs(triangle, x + 1, y + 1, path_sum, min_sum))


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print minimumTotal(triangle)
