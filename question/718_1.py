
#A = [0,0,0,0,1]
#B = [1,0,0,0,0]

A = [5,14,53,80,48]
B = [50,47,3,80,83]

j = 0
k = 0
max_count = 0

if A == B:
    print len(A)

for i in range(len(A)):

    while j < len(B):

        while i + k < len(A) and j + k < len(B):

            if A[i + k] == B[j + k]:
                max_count = max(max_count, k + 1)

                if max_count == max(len(A), len(B)):
                    print max_count

            else:
                break

            k += 1

        k = 0
        j += 1

    j = 0

print max_count