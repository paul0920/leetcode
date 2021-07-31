def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) < 3:
        return 0

    left = 0
    right = len(height) - 1
    h_left_max = 0
    h_right_max = 0
    water = 0

    while left < right:
        # find the next higher walls of both ends
        h_left_max = max(h_left_max, height[left])
        h_right_max = max(h_right_max, height[right])

        # check whether the left or right wall is higher to trap water at current index
        if h_left_max <= h_right_max:
            water += h_left_max - height[left]
            left += 1

        else:
            water += h_right_max - height[right]
            right -= 1

    return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print trap(height)
