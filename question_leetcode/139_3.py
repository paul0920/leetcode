# Time complexity: O(nL), n = len(s), L = max_length


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
    max_length = max([len(word) for word in wordDict]) if wordDict else 0

    for i in range(1, n + 1):
        for length in range(1, max_length + 1):
            # print i, length
            if i < length:
                break

            if not dp[i - length]:
                continue

            if s[i - length: i] in wordDict:
                dp[i] = True
                break

    return dp[n]


s = "leetcode"
wordDict = ["leet", "code"]
print wordBreak(s, wordDict)
