def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 2:
        return x

    left = 1
    right = x

    while left + 1 < right:
        mid = (left + right) // 2
        square_num = mid * mid

        if square_num < x:
            left = mid

        elif square_num == x:
            left = mid  # check last position of target

        else:
            right = mid

    if right * right <= x:  # check last position of target

        return right

    if left * left <= x:
        return left


x = 4
print mySqrt(x)
x = 2
print mySqrt(x)
