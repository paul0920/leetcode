def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) < 3:
        return 0

    max_height_from_left = []
    max_height = 0
    water = 0

    for each_height in height:
        max_height = max(max_height, each_height)
        max_height_from_left.append(max_height)

    max_height = 0

    for i in range(len(height) - 1, -1, -1):
        each_height = height[i]
        max_height = max(max_height, each_height)
        wall_height = min(max_height_from_left[i], max_height)
        water += wall_height - each_height

    return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print trap(height)
