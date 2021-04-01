# Time complexity: O(2^n), assume len(s) = n, len(p) = n
# DFS + no for loop

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if s is None or p is None:
        return False

    return check_matching(s, 0, p, 0)


def check_matching(s, index_s, p, index_p):
    if index_p == len(p):
        return index_s == len(s)

    if index_s == len(s):
        return is_all_stars(p, index_p)

    s_first_char = s[index_s]
    p_first_char = p[index_p]

    if p_first_char == "*":
        return check_matching(s, index_s, p, index_p + 1) or check_matching(s, index_s + 1, p, index_p)

    else:
        return is_char_matching(s_first_char, p_first_char) and check_matching(s, index_s + 1, p, index_p + 1)


def is_all_stars(p, index_p):
    for i in range(index_p, len(p)):
        if p[i] != "*":
            return False

    return True


def is_char_matching(s_first_char, p_first_char):
    return s_first_char == p_first_char or p_first_char == "?"


s = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba"
p = "a*******b"
s = "adceb"
p = "*a*b"
print isMatch(s, p)
