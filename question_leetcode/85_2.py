def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    row = [0] * n
    max_area = 0

    for i in range(m):
        for j in range(n):
            if int(matrix[i][j]) == 0:  # Remember to reset the row[j] due to this bar @ j is discontinued
                row[j] = 0
                continue

            row[j] += int(matrix[i][j])

        max_area_unit_row = get_max_area(row)
        max_area = max(max_area, max_area_unit_row)

    return max_area


def get_max_area(row):
    n = len(row)
    max_area = 0

    for i in range(n):
        min_height = float("INF")

        for j in range(i, n):
            min_height = min(min_height, row[j])
            max_area = max(max_area, min_height * (j - i + 1))

    return max_area


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print maximalRectangle(matrix)
