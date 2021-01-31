
mat = [[0, 0, 1, 1],
       [0, 1, 1, 1],
       [0, 0, 1, 1]]

mat = [[1, 1, 1],
       [1, 0, 1],
       [1, 1, 1]]

m = len(mat)
n = len(mat[0])
j = 0
count = 0

for idx, row in enumerate(mat):

    # Compress the 2D array into 1D array starting from the 2nd row.
    # The requirement is "1" has to be continuous vertically
    for j in range(len(row)):
        if idx > 0 and row[j] == 1:
            row[j] += mat[idx - 1][j]

    # Start bar_count from this row
    bar_count = 0
    stack = [-1]

    # j: row index, h: bar height
    for j, h in enumerate(row):
        bar_overlapping = 0

        while stack[-1] >= 0 and row[stack[-1]] >= h:
            pre_j = stack.pop()

            # Calculate the previous index with non-monotonic bar height
            bar_overlapping += row[pre_j] * (pre_j - stack[-1])

        bar_count += h * (j - stack[-1]) - bar_overlapping
        count += bar_count
        stack.append(j)

print count
