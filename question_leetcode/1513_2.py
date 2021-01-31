def numSub(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    count = 0
    arr = s.split("0")

    for i in arr:
        count += (1 + len(i)) * len(i) // 2

    return count % (10 ** 9 + 7)


s = "0110111"
print numSub(s)
