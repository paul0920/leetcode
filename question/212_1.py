class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        y_size = len(board)
        x_size = len(board[0])
        visited = set()
        res = []

        for y in range(y_size):
            for x in range(x_size):
                self.dfs(board, set(words), visited, y, x, "", res)

        return res

    def checkValidPos(self, y, x, size_y, size_x):

        if y < 0 or y >= size_y or x < 0 or x >= size_x:
            return False

        return True

    def dfs(self, board, words, visited, y, x, path, res):

        if not self.checkValidPos(y, x, len(board), len(board[0])) or (y, x) in visited:
            return

        path += board[y][x]

        if path in words and not path in res:
            res += [path]

        visited.add((y, x))
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_y = y + dy
            next_x = x + dx

            self.dfs(board, words, visited, next_y, next_x, path, res)

        visited.remove((y, x))


board = [["b", "b", "a", "a", "b", "a"], ["b", "b", "a", "b", "a", "a"], ["b", "b", "b", "b", "b", "b"],
         ["a", "a", "a", "b", "a", "a"], ["a", "b", "a", "a", "b", "b"]]
words = ["abbbababaa"]


obj = Solution()
print obj.findWords(board, words)
