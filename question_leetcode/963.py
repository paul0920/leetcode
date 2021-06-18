def minAreaFreeRect(points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    if not points:
        return 0

    m = len(points)
    points_set = {(x, y) for x, y in points}
    res = float("INF")

    for i in range(m - 2):
        x0, y0 = points[i]

        for j in range(i + 1, m - 1):
            x1, y1 = points[j]

            for k in range(j + 1, m):
                x2, y2 = points[k]
                dx1, dy1 = x1 - x0, y1 - y0
                dx2, dy2 = x2 - x0, y2 - y0

                if dx1 * dx2 != -dy1 * dy2:  # Check dx1/dy1 * dx2/dy2 = -1
                    continue

                new_x = x2 + x1 - x0  # Find the possible x through (x1 + x2) / 2 = (x0 + new_x) / 2
                new_y = y2 + y1 - y0  # Find the possible y through (y1 + y2) / 2 = (y0 + new_y) / 2

                if (new_x, new_y) not in points_set:
                    continue

                res = min(res, (dx1 ** 2 + dy1 ** 2) ** 0.5 * (dx2 ** 2 + dy2 ** 2) ** 0.5)

    return res if res != float("INF") else 0


points = [[1, 2], [2, 1], [1, 0], [0, 1]]
print minAreaFreeRect(points)
