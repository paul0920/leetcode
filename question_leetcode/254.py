def getFactors(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    if n <= 1:
        return []

    res = []
    calculate_factors(res, [], n, 2)

    return res


def calculate_factors(res, path, n, factor):
    # To prevent from adding the case of number itself
    if len(path) > 0:
        res.append(path + [n])

    while factor * factor <= n:
        if n % factor == 0:
            path.append(factor)
            calculate_factors(res, path, n // factor, factor)
            path.pop()

        factor += 1


n = 32
print getFactors(n)
