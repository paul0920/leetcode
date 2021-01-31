
A = [0, 6, 5, 2, 2, 5, 1, 9, 4]

L = 1
M = 2

for i in xrange(1, len(A)):
    A[i] += A[i - 1]

# print A

# A[2]: [0, 6][5] or [0][6, 5]
res = A[L + M - 1]

# A[0]: [0]
Lmax = A[L - 1]

# A[1]: [0, 6]
Mmax = A[M - 1]


for i in range(L + M, len(A)):

    # [0] vs. [6]...
    Lmax = max(Lmax, A[i - M] - A[i - L - M])
    # [0, 6] vs. [6, 5]...
    Mmax = max(Mmax, A[i - L] - A[i - L - M])
    # [0, 6][5] or [0][6, 5] vs. [6][5, 2] vs. [6, 5][2]...
    res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])

    # print res

print res
