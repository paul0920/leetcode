def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if not board and word:
        return False

    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            if dfs(i, j, board, 0, word, set()):
                return True

    return False


def is_valid(y, x, board, index, word, visited):
    m = len(board)
    n = len(board[0])

    if y < 0 or m <= y:
        return False

    if x < 0 or n <= x:
        return False

    if (y, x) in visited:
        return False

    if board[y][x] != word[index]:
        return False

    return True


def dfs(y, x, board, index, word, visited):
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    if not is_valid(y, x, board, index, word, visited):
        return False

    if index == len(word) - 1:
        return True

    visited.add((y, x))

    for dy, dx in DIRECTIONS:
        if dfs(y + dy, x + dx, board, index + 1, word, visited):
            return True

    visited.remove((y, x))

    return False


board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
         ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
word = "AAAAAAAAAAAAABB"

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print exist(board, word)
