def maxLength(arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    if not arr:
        return 0

    res = [0] * len(arr)
    dfs(arr, 0, set(), "", res)

    return max(res)


def dfs(arr, index, visited, path, res):
    if index == len(arr):
        res[index - 1] = max(res[index - 1], len(path))
        return

    for i in range(index, len(arr)):
        if not is_unique(arr[i], visited):
            res[index - 1] = max(res[index - 1], len(path))
            continue

        # for char in list(arr[i]):
        #     visited.add(char)

        visited |= set(arr[i])
        path += arr[i]
        dfs(arr, i + 1, visited, path, res)
        path = path[:len(arr[i]) * -1]
        visited ^= set(arr[i])

        # for char in list(arr[i]):
        #     visited.remove(char)


def is_unique(word, visited):
    if len(word) != len(set(word)):
        return False

    for char in list(word):
        if char in visited:
            return False

    return True


arr = ["cha", "r", "act", "ers"]
print maxLength(arr)
