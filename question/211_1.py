import collections


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        word_len = len(word)
        self.lookup[word_len].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        word_len = len(word)

        for each_word in self.lookup[word_len]:

            i = 0

            while i < word_len and (each_word[i] == word[i] or word[i] == "."):
                i += 1

            if i == word_len:
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
