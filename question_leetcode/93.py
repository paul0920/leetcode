def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    if not s or len(s) > 3 * 4:
        return []

    res = []
    dfs(0, s, [], res)

    return res


def dfs(index, s, path, res):
    if index == len(s) and len(path) == 4:
        res.append(".".join(path))

        return

    if len(path) > 4:
        return

    address_info = get_address(index, s)

    for i, address in address_info:
        path.append(address)
        dfs(i + 1, s, path, res)
        path.pop()


def get_address(index, s):
    string = ""
    stack = []

    for i in range(index, index + 3):
        if i == len(s):
            break

        string += s[i]

        if int(string) > 255:
            break

        if len(string) > 1 and string[0] == "0":
            break

        stack.append((i, string))

    return stack


s = "25525511135"
print restoreIpAddresses(s)
s = "0000"
print restoreIpAddresses(s)
s = "1111"
print restoreIpAddresses(s)
s = "010010"
print restoreIpAddresses(s)
s = "101023"
print restoreIpAddresses(s)
