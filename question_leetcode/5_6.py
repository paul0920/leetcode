def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s

    max_len = 0
    start = 0

    for i, char in enumerate(s):
        start_1, len_1 = is_valid_palindrome(i, i, s)

        if len_1 > max_len:
            start = start_1
            max_len = len_1

        start_2, len_2 = is_valid_palindrome(i, i + 1, s)

        if len_2 > max_len:
            start = start_2
            max_len = len_2

    return s[start:start + max_len]


def is_valid_palindrome(start, end, s):
    while 0 <= start and end < len(s):
        if s[start] != s[end]:
            break

        start -= 1
        end += 1

    return start + 1, end - 1 - start


s = "babad"
print longestPalindrome(s)
