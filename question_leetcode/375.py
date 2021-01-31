import collections


def get_min_amount(low, high):
    if low >= high:
        return 0

    if (low, high) in memo:
        return memo[(low, high)]

    cost = float('INF')

    for k in range(low, high):
        cost_pre_k = get_min_amount(low, k - 1)
        cost_after_k = get_min_amount(k + 1, high)
        cost = min(cost, k + max(cost_pre_k, cost_after_k))

    memo[(low, high)] = cost

    return memo[(low, high)]


# memo = [[float('INF')] * (n+1) for _ in range(n+1)]
memo = collections.defaultdict(int)
n = 4

print get_min_amount(1, n)
print memo
