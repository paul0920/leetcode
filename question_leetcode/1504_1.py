
mat = [[1, 0, 1],
       [1, 1, 0],
       [1, 1, 0]]

mat = [[1, 1, 1],
       [1, 0, 1],
       [1, 1, 1]]


if not mat:
    print 0

row = len(mat)
col = len(mat[0])
count = 0

# Treat mat[top][left] as origin and see
# how many rectangles between
# mat[top][left] and mat[bottom][right]
for top in range(row):

    for left in range(col):

        bottom = row

        for right in range(left, col):

            scan = top

            while scan < bottom and mat[scan][right]:
                scan += 1

            bottom = scan
            count += bottom - top

            if bottom == top:
                break

print count
