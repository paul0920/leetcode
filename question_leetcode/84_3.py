def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    if not heights:
        return 0

    max_area = 0

    for i in range(len(heights)):
        min_height = float("INF")

        for j in range(i, len(heights)):
            min_height = min(min_height, heights[j])
            max_area = max(max_area, min_height * (j - i + 1))

    return max_area


heights = [2, 1, 5, 6, 2, 3]
print largestRectangleArea(heights)
