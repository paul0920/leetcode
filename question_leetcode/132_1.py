def minCut(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dp = [float("INF")] * (n + 1)
    dp[0] = -1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            # if s[i - 1: j - 1] == s[j - 1: i - 1: -1]:
            if s[i - 1: j] == s[i - 1: j][:: -1]:
                dp[j] = min(dp[j], dp[i - 1] + 1)

    return dp[n]


s = "aab"
print minCut(s)
