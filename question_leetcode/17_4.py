def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []

    KEYBOARD = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    res = []
    dfs(digits, 0, [], res, KEYBOARD)

    return res


def dfs(digits, index, path, res, KEYBOARD):
    if index == len(digits):
        res.append("".join(path))

        return

    for char in KEYBOARD[digits[index]]:
        path.append(char)
        dfs(digits, index + 1, path, res, KEYBOARD)
        path.pop()


digits = "23"
print letterCombinations(digits)
