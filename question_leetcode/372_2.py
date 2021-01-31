def superPow(a, b):
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    num = 0

    for n in b:
        num = num * 10 + n

    return calculate(a, num)


def calculate(a, b):
    res = 1

    while b > 0:
        if b % 2 == 1:
            res = res * a % 1337

        a = a * a % 1337
        b //= 2

    return res


a = 2147483647
b = [2, 0, 0]
print superPow(a, b)
