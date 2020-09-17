
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [3, 3, 4]

max_area = area = 0
i, j = 0, len(height) - 1

while i < j:
    left, right = height[i], height[j]

    if left < right:
        area = (j - i) * left
        while left >= height[i]:
            i += 1
            print "left idx:", i, height[i], left

    elif left >= right:
        area = (j - i) * right

        # Need to set j > 0 in case that left == right.
        # Overall, 11_1.py is easier to understand and implement
        while height[j] <= right and j:
            j -= 1
            print "right idx:", j, height[j], right

    print ""
    if area > max_area:
        max_area = area

print max_area
