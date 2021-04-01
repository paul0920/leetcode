# Time complexity: O(n^2), assume len(s) = n, len(p) = n
# For loop

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if s is None or p is None:
        return False

    size_s = len(s)
    size_p = len(p)
    dp = [[False] * (size_p + 1) for _ in range(size_s + 1)]
    dp[0][0] = True

    for j in range(1, size_p + 1):
        dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"

    for i in range(1, size_s + 1):
        for j in range(1, size_p + 1):
            if p[j - 1] == "*":
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

            else:
                dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == "?")

    return dp[size_s][size_p]


s = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba"
p = "a*******b"
s = "adceb"
p = "*a*b"
print isMatch(s, p)
