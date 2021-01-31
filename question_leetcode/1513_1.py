def numSub(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    count = 0
    j = 1

    for i in range(len(s)):

        if s[i] == "0":
            continue

        j = max(j, i + 1)

        while j < len(s) and s[j] == "1":
            j += 1

        count += j - i

    return count % (10 ** 9 + 7)


s = "0110111"
print numSub(s)
