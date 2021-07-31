def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    char_to_start_index = {}
    start = 0
    max_len = 0

    for i, char in enumerate(s):
        if char in char_to_start_index:
            start = max(start, char_to_start_index[char])

        max_len = max(max_len, i - start + 1)
        char_to_start_index[char] = i + 1

    return max_len


s = 'tmmzuxt'
print lengthOfLongestSubstring(s)
