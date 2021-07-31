def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    char_to_start_index = {}
    left = 0
    right = 0
    max_len = 0

    while right < len(s):
        char = s[right]

        if char in char_to_start_index:
            start = char_to_start_index[char]
            left = max(left, start + 1)

        max_len = max(max_len, right - left + 1)
        char_to_start_index[char] = right
        right += 1

    return max_len


s = "pwwkew"
print lengthOfLongestSubstring(s)
