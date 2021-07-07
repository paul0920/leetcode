def shortestToChar(s, c):
    """
    :type s: str
    :type c: str
    :rtype: List[int]
    """
    # The key thing is to do one pass from left to right and the other pass from right to left
    n = len(s)
    dp = [0 if char == c else n for char in s]

    for i in range(1, n):  # start from index = 1
        dp[i] = min(dp[i], dp[i - 1] + 1)

    for i in range(n - 2, -1, -1):  # start from index = -2
        dp[i] = min(dp[i], dp[i + 1] + 1)

    return dp


s = "loveleetcode"
c = "e"
print shortestToChar(s, c)
