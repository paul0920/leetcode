
A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2

i = 0

for j in range(len(A)):

    K -= 1 - A[j]

    if K < 0:
        K += 1 - A[i]
        i += 1

print j - i + 1
