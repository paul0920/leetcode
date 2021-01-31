board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'M', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]


def display(board):

    for row in board:
        print row

    print ""


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        if not board:
            return board

        y, x = click[0], click[1]
        self.m, self.n = len(board), len(board[0])

        if board[y][x] == "M":
            board[y][x] = "X"
            return board

        self.dfs(board, y, x)

        return board

    def dfs(self, board, y, x):

        # Remember to consider the termination case!
        if board[y][x] != "E":
            return

        count = 0

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx = x + dx
                ny = y + dy

                if (dx or dy) and 0 <= nx < self.n and 0 <= ny < self.m and board[ny][nx] == "M":
                    count += 1

        if count:
            board[y][x] = str(count)

        else:
            board[y][x] = "B"

            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx = x + dx
                    ny = y + dy

                    if (dx or dy) and 0 <= nx < self.n and 0 <= ny < self.m:
                        self.dfs(board, ny, nx)


game = Solution()
display(board)
game.updateBoard(board, [0, 0])
display(board)
game.updateBoard(board, [6, 0])
display(board)
