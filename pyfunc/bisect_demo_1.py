import bisect

A = [[[-1, 0], [3, -1], [4, 5]]]

print A[0]


# [3] always be the smallest one comparing to any [3, x]
print bisect.bisect(A[0], [3])
print bisect.bisect(A[0], [3, -2])
print bisect.bisect(A[0], [3, -1])
# print bisect.bisect_left(A[0], [3, -1])
print bisect.bisect(A[0], [3, 0])
print bisect.bisect(A[0], [3, 1])

print ""

print bisect.bisect(A[0], [0])
print bisect.bisect(A[0], [1])
print bisect.bisect(A[0], [2])
print bisect.bisect(A[0], [3])
print bisect.bisect(A[0], [4])
print bisect.bisect(A[0], [5])

print ""

print bisect.bisect_left(A[0], [0])
print bisect.bisect_left(A[0], [1])
print bisect.bisect_left(A[0], [2])
print bisect.bisect_left(A[0], [3])
print bisect.bisect_left(A[0], [4])
print bisect.bisect_left(A[0], [5])
