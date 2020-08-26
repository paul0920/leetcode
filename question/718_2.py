
A = [0,0]
B = [0,0,0]

#A = [1,2,3,2,1]
#B = [3,2,1,4,7]

#A = [5,14,53,80,48]
#B = [50,47,3,80,83]

max_len = 0
prev = [0] * (len(B) + 1)

for i in range(len(A)):
    curr = [0] * (len(B) + 1)

    for j in range(len(B)):
        if A[i] == B[j]:

            print curr, prev, "i j =", i, j

            # keep tracking the relationships between the
            # current table and previous table
            curr[j + 1] = prev[j] + 1
            max_len = max(max_len, curr[j + 1])

            print curr, prev, "MAX_LEN:", max_len

    print ""
    prev = curr

print max_len