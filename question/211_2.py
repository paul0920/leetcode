import collections


class TrieNode(object):

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.res = False

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root

        for c in word:
            node = node.children[c]

        node.is_word = True

    def dfs(self, node, word):

        if not word:

            if node.is_word:
                self.res = True

        elif word[0] in node.children:

            self.dfs(node.children[word[0]], word[1:])

        elif word[0] == ".":

            for next_node in node.children.values():
                self.dfs(next_node, word[1:])

        return

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False
        self.dfs(node, word)

        return self.res

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
