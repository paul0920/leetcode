def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    stack = [(-1, "")]  # The key is to have an index: -1 to track overall length
    max_len = 0

    for i, bracket in enumerate(s):
        if stack[-1][-1] == "(" and bracket == ")":
            stack.pop()
            max_len = max(max_len, i - stack[-1][0])
            continue

        stack.append((i, bracket))

    return max_len


s = ")()())"
print longestValidParentheses(s)
