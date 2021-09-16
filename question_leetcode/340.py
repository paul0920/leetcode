def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if not s:
        return 0

    char_to_index = {}
    start = 0
    max_len = 0

    for i, char in enumerate(s):
        char_to_index[char] = i

        if len(char_to_index) > k:
            start = min(char_to_index.values())
            del char_to_index[s[start]]
            start += 1

        max_len = max(max_len, i - start + 1)

    return max_len


s = "abacccc"
k = 2
print lengthOfLongestSubstringKDistinct(s, k)
