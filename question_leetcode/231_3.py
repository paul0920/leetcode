# Time complexity: O(1)

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 0:
        return False

    return n & -n == n


n = 33554431
print isPowerOfTwo(n)
