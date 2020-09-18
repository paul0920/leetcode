
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"


def show(m):

    for row in m:
        print row

show(board)

m = len(board)
n = len(board[0])
q = []

for i in range(m):
    for j in range(n):
        if board[i][j] == word[0]:
            q.append((i, j))

for r, c in q:

    stack = []
    visited = set()
    stack.append((r, c, 0, False))

    while stack:

        # Use stack.pop() to keep checking the latest possible nodes through right to left of the array
        # This is the key to do iterative DFS!
        y, x, i, backtrack = stack.pop()

        # Check whether we already get to this node once. If yes, remove the node in visited() set
        if backtrack:
            visited.remove((y, x))

        # If getting to this node the first time, backtrack the node
        else:

            stack.append((y, x, i, True))
            visited.add((y, x))

            if i == len(word) - 1:
                print True
                exit()

            for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):

                next_y = y + dy
                next_x = x + dx

                if 0 <= next_y < m and 0 <= next_x < n and not (next_y, next_x) in visited and board[next_y][next_x] == word[i + 1]:
                    stack.append((next_y, next_x, i + 1, False))

print False
