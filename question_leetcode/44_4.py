# Time complexity: O(n^2), assume len(s) = n, len(p) = n
#                    n^2 from memo
# DFS + no for loop + memo

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if s is None or p is None:
        return False

    memo = [[None] * len(p) for _ in range(len(s))]

    return check_matching(s, 0, p, 0, memo)


def check_matching(s, index_s, p, index_p, memo):
    if index_p == len(p):
        return index_s == len(s)

    if index_s == len(s):
        return is_all_stars(p, index_p)

    if memo[index_s][index_p] is not None:
        return memo[index_s][index_p]

    s_first_char = s[index_s]
    p_first_char = p[index_p]

    if p_first_char == "*":
        match = check_matching(s, index_s, p, index_p + 1, memo) or check_matching(s, index_s + 1, p, index_p, memo)

    else:
        match = is_char_matching(s_first_char, p_first_char) and check_matching(s, index_s + 1, p, index_p + 1, memo)

    memo[index_s][index_p] = match

    return match


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
