
A = [[1,2,3],[4,5,6],[7,8,9]]
#A = [[1,2,3],[4,5,6]]

# This only works for a square matrix
for i in range(len(A)):
    for j in range(i+1, len(A[0])):
        A[i][j], A[j][i] = A[j][i], A[i][j]
print A
print ""

A = [[1,2,3],[4,5,6]]
print [[A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print ""

A = [[1,2,3],[4,5,6]]
print [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
print ""

A = [[1,2,3],[4,5,6]]
ans = [[] for i in range(len(A[0]))]
print ans
for i in range(len(A)):
    for j in range(len(A[0])):
        ans[j].append(A[i][j])
print ans
print ""

A = [[1,2,3],[4,5,6]]
print map(list, zip(*A))
print ""

# This gets tuple results so we need map()
# to turn them to list
A = [[1,2,3],[4,5,6]]
print zip(*A)