# Time complexity: O(mn x logmn)

def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0

    points = []
    longest_path = {}
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            points.append((matrix[i][j], (i, j)))

    points.sort()

    for point in points:
        location = point[1]
        longest_path[location] = 1

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = location[0] + dx
            y = location[1] + dy
            prev_location = (x, y)

            if x < 0 or x >= n or y < 0 or y >= m:
                continue

            # Here is the key part by using DP concept
            if prev_location in longest_path and matrix[x][y] < point[0]:
                longest_path[location] = max(longest_path[location],
                                             longest_path[prev_location] + 1)

    return max(longest_path.values())


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print longestIncreasingPath(matrix)
