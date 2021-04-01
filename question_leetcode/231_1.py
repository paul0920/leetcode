# Time complexity: O(logn)

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 0:
        return False

    while n % 2 == 0:
        n /= 2

    return n == 1


n = 33554431
print isPowerOfTwo(n)
