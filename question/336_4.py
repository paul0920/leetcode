from collections import defaultdict

words = ["abb", "a", "lls","s", "cat"]
words = ["abb", "a"]
words = ["bba", "a"]


class Trie:
    def __init__(self):
        self.paths = defaultdict(Trie)
        self.wordEndIndex = -1
        self.palindromesBelow = []

    def addWord(self, word, index):

        node = self

        # Insert each alphabet reversely
        for j, char in enumerate(reversed(word)):

            if isPalindrome(word[0:len(word) - j]):
                node.palindromesBelow.append(index)

            node = node.paths[char]
        node.wordEndIndex = index


def isPalindrome(word):
    return word == word[::-1]

def makeTrie(words):

    node = Trie()
    for i, word in enumerate(words):
        node.addWord(word, i)

    return node

def getPalindromesForWord(node, word):

    output = []

    while word:

        if node.wordEndIndex >= 0:
            if isPalindrome(word):
                output += [node.wordEndIndex]

        if not word[0] in node.paths:
            return output

        node = node.paths[word[0]]
        word = word[1:]

    if node.wordEndIndex >= 0:
        output.append(node.wordEndIndex)

    output += node.palindromesBelow

    print output, node.palindromesBelow

    return output

def palindromePairs(words):

    trie = makeTrie(words)
    res = []

    for i, word in enumerate(words):

        candidates = getPalindromesForWord(trie, word)
        res += [[i, c] for c in candidates if i != c]

    return res


print palindromePairs(words)
