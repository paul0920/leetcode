def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    if not heights:
        return 0

    height_list = [0] + heights + [0]  # Need to add 0s to cover all cases in "heights" (stack is not empty)
    stack = []
    max_area = 0

    for i, height in enumerate(height_list):
        while stack and height_list[stack[-1]] > height:
            min_height = height_list[stack.pop()]
            width = (i - 1) - stack[-1]  # This is the longest width for the current min_height
            max_area = max(max_area, min_height * width)

        stack.append(i)  # Maintain indices of monotonic increasing heights

        # temp = []
        # for j in stack:
        #     temp.append(height_list[j])
        # print temp
        # print stack
        # print max_area
        # print ""

    return max_area


heights = [2, 1, 5, 6, 2, 3]
heights = [1, 3, 2, 3, 5]
print largestRectangleArea(heights)
