
A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]


# Only need to check the 1st elements of both A & B array
for x in [A[0], B[0]]:

    if all(x in d for d in zip(A, B)):
        print len(A) - max(A.count(x), B.count(x))

print -1
