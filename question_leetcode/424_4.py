def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    count = {}
    res = 0
    i = 0

    # j points to the last index of the sub-string, which meets the criteria
    for j, c in enumerate(s):

        count[c] = count.get(c, 0) + 1
        max_freq = max(count.values())

        # Use "if" instead of "while" loop
        if j - i + 1 - max_freq > k:
            count[s[i]] -= 1
            i += 1

        res = max(res, j - i + 1)

    return res


s = "AABAABBA"
k = 1
print characterReplacement(s, k)
