
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [2, 4, 6]]

# matrix = [[7], [9], [6]]

matrix_demo = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [2, 4, 6]]


def show(m):
    for row in m:
        print row


res = []

while matrix:

    # Left to right
    res.extend(matrix.pop(0))

    # Top to bottom
    if matrix and matrix[0]:
        for row in matrix:
            res += [row.pop()]

    # Right to left
    if matrix:
        res.extend(matrix.pop()[::-1])

    # Bottom to top
    if matrix and matrix[0]:
        for row in matrix[::-1]:
            res += [row.pop(0)]

print res
