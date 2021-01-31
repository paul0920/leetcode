
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print row

m = len(matrix)
n = len(matrix[0])

# j only loops until i
for i in range(m):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# j only loops until n / 2
for i in range(m):
    for j in range(n / 2):
        matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
        # matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]

print ""
for row in matrix:
    print row
