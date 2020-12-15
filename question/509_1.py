def fib(N):
    """
    :type N: int
    :rtype: int
    """
    if N <= 1:
        return N

    return fib(N - 1) + fib(N - 2)


for i in range(10):
    print fib(i)
