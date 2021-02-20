import collections


def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    words_set = set(wordList)
    words_dict = set([beginWord])

    if endWord not in words_set:
        return 0

    queue = collections.deque([beginWord])
    layer_count = 1

    while queue:
        for _ in range(len(queue)):
            curr_word = queue.popleft()

            if curr_word == endWord:
                return layer_count

            for i in range(len(curr_word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    next_word = curr_word[: i] + char + curr_word[i + 1:]

                    if next_word in words_set and next_word not in words_dict:
                        queue.append(next_word)
                        words_dict.add(next_word)

        layer_count += 1

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print ladderLength(beginWord, endWord, wordList)
