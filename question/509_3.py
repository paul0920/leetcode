def fib(N):
    """
    :type N: int
    :rtype: int
    """
    if N <= 1:
        return N

    cache = {0: 0, 1: 1}

    for i in range(2, N + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[N]


for i in range(10):
    print fib(i)
