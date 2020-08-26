
A = [0,0]
B = [0,0,0]

#A = [1,2,3,2,1]
#B = [3,2,1,4,7]

#A = [5,14,53,80,48]
#B = [50,47,3,80,83]

dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:

            print dp, "(1)"

            dp[i][j] = dp[i - 1][j - 1] + 1

            print dp, "(2)"

    print ""

print [max(row) for row in dp]
print max(max(row) for row in dp)