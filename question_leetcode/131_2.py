import collections


def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    if not s:
        return [[""]]

    palindrome_set = collections.defaultdict(list)
    i = 0

    while i < len(s):
        get_palindrome_indexes(i, i, s, palindrome_set)
        get_palindrome_indexes(i, i + 1, s, palindrome_set)
        i += 1

    res = []
    dfs(s, 0, palindrome_set, [], res)

    return res


def get_palindrome_indexes(left, right, s, palindrome_set):
    while 0 <= left and right < len(s):
        if s[left] != s[right]:
            break

        palindrome_set[left].append(right)
        left -= 1
        right += 1


def dfs(s, index, palindrome_set, path, res):
    # Check whether the index is out of the boundary
    if index == len(s):
        res.append(list(path))
        # print res
        return

    for i in palindrome_set[index]:
        # i + 1 is the boundary of palindrome sub array
        next_index = i + 1
        path.append(s[index: next_index])
        dfs(s, next_index, palindrome_set, path, res)
        path.pop()


s = "aab"
print partition(s)
