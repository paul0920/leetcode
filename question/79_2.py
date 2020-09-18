
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"


def show(m):
    for row in m:
        print row


show(board)

m = len(board)
n = len(board[0])
visited = set()


def dfs(y, x, idx):
    if y < 0 or y >= m or x < 0 or x >= n or (y, x) in visited or board[y][x] != word[idx]:
        return False

    elif idx == len(word) - 1:
        return True

    # Put this node into set()
    visited.add((y, x))
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):

        ny = y + dy
        nx = x + dx

        if dfs(ny, nx, idx + 1):
            return True

    # If (y, x) doesn't form a valid path, remove it from the set()
    visited.remove((y, x))

    return False


for i in range(m):
    for j in range(n):

        if board[i][j] == word[0]:
            if dfs(i, j, 0):
                print True
                exit()

print False
