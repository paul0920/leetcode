
def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """

    word_lookup = set(words)
    res = []

    for each_word in words:

        if dfs(each_word, word_lookup):
            res += [each_word]

    return res

def dfs(word, table):

    # Make sure the range can separate a word into 2 parts: 1 to len(word) - 1
    for i in range(1, len(word)):

        prefix = word[:i]
        suffix = word[i:]

        if prefix in table and suffix in table:
            # print prefix, suffix
            return True

        if prefix in table and dfs(suffix, table):
            return True

    return False


words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

print findAllConcatenatedWordsInADict(words)
