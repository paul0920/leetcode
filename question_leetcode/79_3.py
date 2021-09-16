# This implementation gets TLE
import collections


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
            if not is_valid(i, j, board, set(), word[0]):
                continue

            if bfs(i, j, board, word):
                return True

    return False


def is_valid(i, j, board, visited, char):
    m = len(board)
    n = len(board[0])

    if i < 0 or m <= i:
        return False

    if j < 0 or n <= j:
        return False

    if (i, j) in visited:
        return False

    if board[i][j] != char:
        return False

    return True


def bfs(i, j, board, word):
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = {(i, j)}
    queue = collections.deque([(i, j, visited)])
    index = 0

    while queue:
        for _ in range(len(queue)):
            curr_y, curr_x, curr_visited = queue.popleft()

            if index == len(word) - 1 and board[curr_y][curr_x] == word[index]:
                return True

            for dy, dx in DIRECTIONS:
                next_y = curr_y + dy
                next_x = curr_x + dx

                if not is_valid(next_y, next_x, board, curr_visited, word[index + 1]):
                    continue

                next_visited = curr_visited.copy()
                next_visited.add((next_y, next_x))
                queue.append((next_y, next_x, next_visited))

        index += 1

    return False


board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
         ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
word = "AAAAAAAAAAAAABB"
print exist(board, word)
