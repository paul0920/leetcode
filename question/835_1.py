import collections


A = [[0, 1], [1, 1]]
B = [[1, 1], [1, 0]]

N = len(A)
scaling = 2 * N - 1
LA = [i / N * scaling + i % N for i in xrange(N * N) if A[i / N][i % N]]
LB = [i / N * scaling + i % N for i in xrange(N * N) if B[i / N][i % N]]
c = collections.Counter(i - j for i in LA for j in LB)

print max(c.values() or [0])
