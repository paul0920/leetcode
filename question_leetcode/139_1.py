# Time complexity: O(nL), n = len(s), L = max_length
# It may be stack overflow. Use DP instead.

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    max_length = get_max_length(wordDict)

    return is_possible(s, 0, max_length, wordDict, {})


def get_max_length(wordDict):
    max_length = 0

    for word in wordDict:
        max_length = max(max_length, len(word))

    return max_length


def is_possible(s, index, max_length, wordDict, memo):
    if index in memo:
        return memo[index]

    if len(s) == index:
        return True

    memo[index] = False

    for i in range(index, len(s)):
        if i - index + 1 > max_length:
            break

        word = s[index: i + 1]

        if word not in wordDict:
            continue

        if is_possible(s, i + 1, max_length, wordDict, memo):
            memo[index] = True

    return memo[index]


s = "leetcode"
wordDict = ["leet", "code"]
print wordBreak(s, wordDict)
