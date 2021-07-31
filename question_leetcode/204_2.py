def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return 0
    # n = 0, 0
    # n = 1, 0
    # n = 2, 0
    # n = 3, 1

    prime = [True] * n
    prime[0] = False
    prime[1] = False

    for num in range(2, int(n ** 0.5) + 1):  # num loops to sqrt(n)
        if not prime[num]:
            continue

        for next_num in range(num ** 2, n, num):  # start from num^2
            prime[next_num] = False

    return sum(prime)


n = 5000000
print countPrimes(n)
