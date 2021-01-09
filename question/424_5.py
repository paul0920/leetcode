import collections


def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    count = collections.defaultdict(int)
    max_freq = 0
    # res = j - i, which is the length of the sub-string - 1
    res = 0

    # j points to the last index of the sub-string, which meets the criteria
    for j, c in enumerate(s):

        count[c] += 1
        max_freq = max(max_freq, count[c])

        if res + 1 - max_freq > k:
            count[s[j - res]] -= 1

        else:
            res += 1

    return res


s = "AABAABBA"
k = 1
print characterReplacement(s, k)
