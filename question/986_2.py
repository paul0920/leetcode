# A = [[3,5],[9,20]]
# B = [[4,5],[7,10],[11,12],[14,15],[16,20]]

A = [[0, 4], [7, 8], [8, 10]]
B = [[0, 7], [14, 15], [18, 20]]

ia, ib = 0, 0
res = []

while ia < len(A) and ib < len(B):
    if A[ia][0] <= B[ib][1] and B[ib][0] <= A[ia][1]:
        res.append([max(A[ia][0], B[ib][0]), min(A[ia][1], B[ib][1])])

    # This is to decide which interval we should move to
    if A[ia][1] <= B[ib][1]:
        ia += 1

    else:
        ib += 1

print res
