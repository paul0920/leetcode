# Time complexity: O(n^2), n = len(s)


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    if not s:
        return True

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if not dp[j]:
                continue

            if s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]


s = "leetcode"
wordDict = ["leet", "code"]
print wordBreak(s, wordDict)
