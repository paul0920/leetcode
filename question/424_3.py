def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    counter = {}
    res = 0
    # j points to the position right after the last index of
    # the sub-string, which meets the criteria
    j = 0
    max_freq = 0

    for i in range(len(s)):

        # (j - 1) - i + 1 - max_freq
        # the last index - the first index + 1 = sub-string length
        # Make sure "<=" instead of "<" since j can move with max_freq
        # at the same time
        while j < len(s) and j - i - max_freq <= k:
            c = s[j]
            counter[c] = counter.get(c, 0) + 1
            max_freq = max(max_freq, counter[c])
            j += 1

        if j - i - max_freq > k:
            res = max(res, j - 1 - i)

        else:
            res = max(res, j - i)

        counter[s[i]] -= 1
        max_freq = max(counter.values())

    return res


s = "AABAABBA"
k = 1
print characterReplacement(s, k)
