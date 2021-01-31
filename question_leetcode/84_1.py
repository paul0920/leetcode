
heights = [2, 1, 5, 6, 2, 3]

stack = []
max_area = 0

for i, h in enumerate(heights):

    start = i

    # Pop the bars not the monotonic increasing
    # and calculate the area size
    while stack and stack[-1][1] > h:
        idx, val = stack.pop()
        max_area = max(max_area, val * (i - idx))
        start = idx

    stack.append((start, h))

# Calculate area of the bars which are monotonic increasing
for i, h in stack:
    max_area = max(max_area, h * (len(heights) - i))

print max_area
