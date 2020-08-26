
A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2

count = 0
start = 0
res = 0

for idx, n in enumerate(A):

    if n == 0:
        count += 1

    if count > K:

        if A[start] == 0:
            count -= 1

        start += 1

    res = max(res, idx - start + 1)

print res
