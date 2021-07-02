import collections
import heapq


class WordCount(object):
    def __init__(self, count=0, word=""):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word

        return self.count < other.count


def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    if not words:
        return []

    word_count = collections.Counter(words)
    word_heap = []
    res = []

    for word in word_count:
        heapq.heappush(word_heap, WordCount(word_count[word], word))

        if len(word_heap) > k:
            heapq.heappop(word_heap)

    for _ in range(k):
        word_obj = heapq.heappop(word_heap)
        res.append(word_obj.word)

    return res[::-1]


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print topKFrequent(words, k)
