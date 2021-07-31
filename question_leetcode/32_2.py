def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    stack = []
    max_count = 0

    for i in range(1, n + 1):
        if s[i - 1] == "(":
            stack.append(i - 1)
            continue

        if stack:
            prev_bracket_index = stack.pop()
            count = prev_bracket_index + 1
            dp[i] = dp[count - 1] + (i - 1) - prev_bracket_index + 1  # count - 1 = prev_bracket_index
            max_count = max(max_count, dp[i])

    return max_count


# )(())
# 01234
#  ^    dp[2] = 0
#    ^  dp[4] = dp[2] + (4 - 1) - (2) + 1 = 2
# ^     dp[1] = 0
#     ^ dp[5] = dp[1] + (5 - 1) - (1) + 1 = 4


s = ")(())"
print longestValidParentheses(s)
