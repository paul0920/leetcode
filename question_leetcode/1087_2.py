def expand(s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = []
    dfs(s, 0, [], res)

    return sorted(res)


def dfs(s, index, path, res):
    if len(s) == index:
        res.append("".join(path))

        return

    if s[index] == "{":
        bracket_index = get_bracket_index(s, index)
        char_candidates = s[index + 1: bracket_index].split(",")

        for char in char_candidates:
            path.append(char)
            dfs(s, bracket_index + 1, path, res)
            path.pop()

    else:
        path.append(s[index])
        dfs(s, index + 1, path, res)
        path.pop()


def get_bracket_index(s, index):
    while s[index] != "}":
        index += 1

    return index


s = "{a,b}c{d,e}f"
print expand(s)
