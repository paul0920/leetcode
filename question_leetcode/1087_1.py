def expand(s):
    """
    :type s: str
    :rtype: List[str]
    """
    if not s:
        return []

    s_list = convert_to_list(s)
    res = []
    dfs(s_list, 0, [], res)

    return sorted(res)


def convert_to_list(s):
    res = []
    stack = []
    flag = 0

    for char in s:
        if char == "{":
            flag = 1

        elif char == "}":
            res.append(list(stack))
            stack = []
            flag = 0

        elif char.isalpha():
            if flag == 1:
                stack.append(char)

            else:
                res.append([char])

    return res


def dfs(s_list, index, path, res):
    if len(path) == len(s_list):
        res.append("".join(path))

        return

    for i in range(index, len(s_list)):
        char = s_list[i]

        for j in range(len(char)):
            path.append(char[j])
            dfs(s_list, i + 1, path, res)
            path.pop()


s = "{a,b}c{d,e}f"
print expand(s)
