
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print row


n = len(matrix)
for i in range(n / 2):
    for j in range(n - n / 2):

        matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
            matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]


print ""
for row in matrix:
    print row
