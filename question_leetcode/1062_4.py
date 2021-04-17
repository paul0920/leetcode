def longestRepeatingSubstring(S):
    """
    :type S: str
    :rtype: int
    """
    if not S:
        return 0

    n = len(S)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    max_len = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if S[i - 1] != S[j - 1]:
                dp[i][j] = 0
                continue

            #
            # We need to make sure the distance between i and j are
            # greater than the length of previous substring.
            # For example, assuming S is "mississipi, the answer will be 3 instead of 4 as issi with overlapping
            # character i is not a qualified answer.
            #
            # if j - i > dp[i - 1][j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_len = max(max_len, dp[i][j])

    return max_len


S = "abbaba"
S = "mississipi"
print longestRepeatingSubstring(S)
