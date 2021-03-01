def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    res = []
    dfs(s, 0, [], res)

    return res


def dfs(s, index, path, res):
    if index == len(s):
        res.append(list(path))

        return

    for i in range(index + 1, len(s) + 1):
        sub_string = s[index: i]

        if not is_palindrome(sub_string):
            continue

        path.append(sub_string)
        dfs(s, i, path, res)
        path.pop()


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1

        else:
            return False

    return True


s = "aab"
print partition(s)
