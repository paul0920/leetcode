# Time complexity: O(V + E). Walk through all nodes and edges by BFS.
# O(len(wordList)) for DFS
import collections


def findLadders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    words_set = set(wordList)
    words_set.add(beginWord)

    if endWord not in words_set:
        return []

    indexes = build_index(words_set)
    distance = bfs(endWord, indexes)

    res = []
    dfs(beginWord, endWord, indexes, distance, [beginWord], res)

    return res


def build_index(words_set):
    indexes = {}

    for word in words_set:
        for i in range(len(word)):
            key = word[: i] + "?" + word[i + 1:]

            if key not in indexes:
                indexes[key] = {word}

            else:
                indexes[key].add(word)

    return indexes


def bfs(endWord, indexes):
    distance = {endWord: 0}
    queue = collections.deque([endWord])

    while queue:
        curr_word = queue.popleft()

        for next_word in get_the_next_words(curr_word, indexes):
            if next_word not in distance:
                distance[next_word] = distance[curr_word] + 1
                queue.append(next_word)

    return distance


def get_the_next_words(word, indexes):
    words = set()

    for i in range(len(word)):
        key = word[: i] + "?" + word[i + 1:]

        for w in indexes[key]:
            words.add(w)

    return list(words)


def dfs(beginWord, endWord, indexes, distance, path, res):
    if beginWord == endWord:
        res.append(list(path))

        return

    for next_word in get_the_next_words(beginWord, indexes):
        # This is to handle the case that there is no path getting to endWord
        if next_word not in distance:
            continue

        if distance[next_word] != distance[beginWord] - 1:
            continue

        path.append(next_word)
        dfs(next_word, endWord, indexes, distance, path, res)
        path.pop()


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot", "dog"]

print findLadders(beginWord, endWord, wordList)
