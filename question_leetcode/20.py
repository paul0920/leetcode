def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True

    if len(s) % 2 == 1:
        return False

    bracket_mapping = {")": "(", "]": "[", "}": "{"}
    stack = []

    for bracket in s:
        if bracket in bracket_mapping.values():
            stack.append(bracket)

        elif bracket in bracket_mapping:
            if stack and stack[-1] == bracket_mapping[bracket]:
                stack.pop()
                continue

            return False

        else:
            return False

    return not stack


s = "([)]"
print isValid(s)
