# We save paths instead of nodes while using BFS.
# However, it saves many unnecessary paths and wastes space
# Use BFS + DFS instead to get the optimum solution
import collections


def findLadders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    words_set = set(wordList)

    if endWord not in words_set:
        return []

    words_dict = {beginWord: [[beginWord]]}

    while words_dict:
        next_words_dict = collections.defaultdict(list)

        for word in words_dict:
            if word == endWord:
                return words_dict[word]

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[: i] + char + word[i + 1:]

                    if next_word in words_set:
                        for pre_list in words_dict[word]:
                            new_list = pre_list + [next_word]
                            next_words_dict[next_word].append(new_list)

        words_set -= set(next_words_dict.keys())
        words_dict = next_words_dict

    return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print findLadders(beginWord, endWord, wordList)
