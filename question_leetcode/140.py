def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    return dfs(s, wordDict, {})


def dfs(s, wordDict, memo):
    # memo saves all cases starting from "s" that can be broken
    if s in memo:
        return memo[s]

    partitions = []

    if not s:
        return partitions

    if s in wordDict:
        partitions.append(s)

    for i in range(1, len(s)):
        prefix = s[:i]

        if prefix not in wordDict:
            continue

        subffix = s[i:]
        sub_partitions = dfs(subffix, wordDict, memo)

        for word in sub_partitions:
            partitions.append(prefix + " " + word)

    memo[s] = partitions
    # print s, memo[s]

    return memo[s]


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print wordBreak(s, wordDict)
