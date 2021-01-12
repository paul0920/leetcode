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
    if b == 0:
        return 1

    num = calculate(a, b // 2)
    num = (num * num) % 1337

    if b % 2 == 1:
        num = num * a % 1337

    return num


a = 2147483647
b = [2, 0, 0]
print superPow(a, b)
