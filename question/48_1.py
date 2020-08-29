
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print row

matrix[:] = map(list, zip(*matrix[::-1]))

# matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]

print ""
for row in matrix:
    print row
