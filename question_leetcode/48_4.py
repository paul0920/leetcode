def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    if not matrix:
        return matrix

    # rotate_n90(matrix)
    # rotate_p90(matrix)
    rotate_p90(matrix)


def rotate_p90(matrix):
    n = len(matrix)

    for i in range(n):  # transpose the matrix --> matrix[0][1] to matrix[1][0]
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):  # reverse the column at any given row
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


def rotate_n90(matrix):
    n = len(matrix)

    for i in range(n):  # transpose the matrix --> matrix[0][1] to matrix[1][0]
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n // 2):
        for j in range(n):  # reverse the row at any given column
            matrix[i][j], matrix[-i - 1][j] = matrix[-i - 1][j], matrix[i][j]


def display(matrix):
    for row in matrix:
        print row

    print ""


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
display(matrix)
rotate_n90(matrix)
display(matrix)
rotate_p90(matrix)
display(matrix)
