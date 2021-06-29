import collections


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    s_size = len(s)
    t_size = len(t)
    left = 0
    left_min = 0
    right_min = s_size - 1

    if not s or t_size > s_size:
        return ""

    char_to_count = collections.Counter(t)

    for right, char in enumerate(s):
        char_to_count[char] -= 1

        if char_to_count[char] > -1:
            t_size -= 1

        if t_size:  # t_size = 0 --> found all character in t
            continue

        while left < right:
            starting_char = s[left]

            if char_to_count[starting_char] >= 0:  # not the 1st character
                break

            char_to_count[starting_char] += 1  # search the 1st character in the next window
            left += 1

        if right - left < right_min - left_min:
            left_min = left
            right_min = right

    if t_size:
        return ""

    return s[left_min:right_min + 1]


s = "cabwefgewcwaefgcf"
t = "cae"

s = "ADOBECODEBANC"
t = "ABC"

# s = "abcdefghijk"
# t = "h"

print minWindow(s, t)
