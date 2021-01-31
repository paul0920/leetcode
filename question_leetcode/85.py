
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

if not matrix or not matrix[0]:
    print 0

m = len(matrix)
n = len(matrix[0])
max_area = 0

for idx, row in enumerate(matrix):

    for j in range(n):

        row[j] = int(row[j])

        if idx > 0 and row[j] == 1:
            row[j] += int(matrix[idx - 1][j])

    print row

    stack = []

    for j, h in enumerate(row):

        start = j
        while stack and stack[-1][1] > h:
            j_pre, val = stack.pop()
            max_area = max(max_area, val * (j - j_pre))
            start = j_pre

        stack.append((start, h))
        print stack, max_area

    print ""

    # No need to use enumerate(stack). I made this mistake several times!
    for j, h in stack:
        # Use (n - j) instead of (len(stack) - j)
        # I also made this mistake several times!
        max_area = max(max_area, h * (n - j))

print max_area
