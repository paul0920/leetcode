def expand(s):
    """
    :type s: str
    :rtype: List[str]
    """
    if not s:
        return []

    res = []
    dfs(0, s, [], res)

    return sorted(res)


def get_char_to_expand(index, s):
    stack = []
    close_bracket_index = None

    for i in range(index, len(s)):
        char = s[i]

        if char == ",":
            continue

        elif char == "}":
            close_bracket_index = i

            return stack, close_bracket_index

        stack.append(char)


def dfs(index, s, path, res):
    if index == len(s):
        res.append("".join(path))

    elif s[index] == "{":
        stack, close_bracket_index = get_char_to_expand(index + 1, s)

        for char in stack:
            path.append(char)
            dfs(close_bracket_index + 1, s, path, res)
            path.pop()

    else:
        path.append(s[index])
        dfs(index + 1, s, path, res)
        path.pop()


s = "{a,b}c{d,e}f"
print expand(s)
