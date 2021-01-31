def fib(N):
    """
    :type N: int
    :rtype: int
    """
    cache = {0: 0, 1: 1}

    return memo(N, cache)


def memo(n, cache):
    if n in cache:
        return cache[n]

    cache[n] = memo(n - 1, cache) + memo(n - 2, cache)

    return cache[n]


for i in range(10):
    print fib(i)
