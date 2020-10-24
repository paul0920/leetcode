import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addNode(self, word):
        node = self.root

        for i, char in enumerate(word):
            node = node.children[char]

        node.isWord = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        y_size = len(board)
        x_size = len(board[0])
        trie = Trie()
        visited = set()
        res = []

        self.makeTrie(words, trie)
        node = trie.root

        for y in range(y_size):
            for x in range(x_size):
                self.dfs(board, node, visited, y, x, "", res)

        return res

    def makeTrie(self, word_list, trie):

        for each_word in word_list:
            trie.addNode(each_word)

    def checkValidPos(self, y, x, size_y, size_x):

        if y < 0 or y >= size_y or x < 0 or x >= size_x:
            return False

        return True

    def dfs(self, board, node, visited, y, x, path, res):

        if not self.checkValidPos(y, x, len(board), len(board[0])) or (y, x) in visited:
            return

        curr_char = board[y][x]

        if not curr_char in node.children:
            return

        path += curr_char
        node = node.children[curr_char]

        if node.isWord:
            res += [path]

            # Need to remove this word from trie since we already found it in the board
            node.isWord = False
            # print path, "(%s, %s)" %(y, x), visited

        # Searching through original list directly gets TLE, use trie instead
        # if path in words and not path in res:
        #     res += [path]

        visited.add((y, x))
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_y = y + dy
            next_x = x + dx

            self.dfs(board, node, visited, next_y, next_x, path, res)

        visited.remove((y, x))


board = [["b", "b", "a", "a", "b", "a"],
         ["b", "b", "a", "b", "a", "a"],
         ["b", "b", "b", "b", "b", "b"],
         ["a", "a", "a", "b", "a", "a"],
         ["a", "b", "a", "a", "b", "b"]]
words = ["abbbababaa"]
# board = [["a", "a"]]
# words = ["a"]
board = [['o', 'a', 'a', 'n'],
         ['e', 't', 'a', 'e'],
         ['i', 'h', 'k', 'r'],
         ['i', 'f', 'l', 'v']]
words = ["oath", "pea", "eat", "rain"]

obj = Solution()
print obj.findWords(board, words)
