def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    if not text1 or not text2:
        return 0

    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1

            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

    return dp[m % 2][n]


text1 = "abcde"
text2 = "ace"
print longestCommonSubsequence(text1, text2)
