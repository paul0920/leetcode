
arr = [6, 2, 4]

memo = {}

def dp(i, j):
    if j <= i:
        return 0

    if (i, j) not in memo:
        res = float('inf')

        for k in range(i + 1, j + 1):
            res = min(dp(i, k - 1) + dp(k, j) + max(arr[i:k]) * max(arr[k:j + 1]), res)

        memo[(i, j)] = res

    return memo[(i, j)]


print dp(0, len(arr) - 1)
