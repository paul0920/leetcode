import collections
import heapq

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.freq = 0


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.list = []

    def add(self, word):
        node = self.root

        for char in word:
            node = node.children[char]

        node.freq += 1

    def getWordFreq(self, node, word):

        if node.freq != 0:
            self.list.append((-node.freq, word))

        for char in node.children:
            self.getWordFreq(node.children[char], word + char)

    def getList(self):

        self.getWordFreq(self.root, "")

        return self.list


def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """

    node = Trie()
    res = []

    for each_word in words:
        node.add(each_word)

    heap = node.getList()
    heapq.heapify(heap)

    # Remember to heapify first and heappop to get the smallest item every time!
    for _ in range(k):
        res += [heapq.heappop(heap)[1]]

    return res


print topKFrequent(words, k)
