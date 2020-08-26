
matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]

if not matrix or not matrix[0]:
    print 0

m = len(matrix)
n = len(matrix[0])
max_area = 0

for idx, row in enumerate(matrix):

    for j in range(n):

        matrix[idx][j] = int(matrix[idx][j])

        if idx > 0 and matrix[idx][j]:
            matrix[idx][j] += matrix[idx - 1][j]

    stack = []

    for j, h in enumerate(row):

        start = j
        while stack and stack[-1][1] > h:
            j_pre, val = stack.pop()
            max_area = max(max_area, min((j - j_pre), val) ** 2)
            start = j_pre

        stack.append((start, h))

        # print stack, max_area
    # print ""

    for j, h in stack:
        # print j, h, max_area
        max_area = max(max_area, min(n - j, h) ** 2)

print max_area
