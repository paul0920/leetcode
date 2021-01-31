# Recursion (Top Down)

def numTrees(n, memo={0: 1, 1: 1}):

    if n in memo:
        return memo[n]

    if n == 0:
        return 1

    res = 0
    for root in range(0, n):
        # numTrees(left) x numTrees(right)
        res += numTrees(root) * numTrees(n - 1 - root)

    memo[n] = res

    return res

n = 19
n = 3

print numTrees(n)
