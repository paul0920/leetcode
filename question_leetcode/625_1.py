def smallestFactorization(a):
    """
    :type a: int
    :rtype: int
    """
    if a < 10:
        return a

    res = []
    calculate_factors(res, [], a, 2)

    if not res:
        return 0

    smallest = float("INF")

    for nums in res:

        b_num = ""
        for num in sorted(nums):
            b_num += str(num)

        smallest = min(smallest, int(b_num))

    return smallest if smallest < 2 ** 31 else 0


def calculate_factors(res, path, n, factor):
    if len(path) > 0:
        if n <= 10:
            res.append(path + [n])

    while factor * factor <= n:
        if n % factor == 0:
            path.append(factor)
            calculate_factors(res, path, n // factor, factor)
            path.pop()

        factor += 1


a = 48
print smallestFactorization(a)
