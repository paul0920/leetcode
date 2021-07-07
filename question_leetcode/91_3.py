def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(s) + 1):
        if 1 <= int(s[i - 1:i]) <= 9:  # s=226, 2-2 --> 22-6 (2 ways: 2 2-6, 22-6)
            dp[i] += dp[i - 1]

        if 10 <= int(s[i - 2:i]) <= 26:  # s=226, 22 --> 2-26 (1 way)
            dp[i] += dp[i - 2]

    return dp[-1]


s = "226"
print numDecodings(s)
