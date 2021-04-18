def numMatchingSubseq(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: int
    """
    word_to_count = {}

    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
            continue

        if is_subsequence(word, s):
            word_to_count[word] = 1

    return sum([n for n in word_to_count.values()])


def is_subsequence(word, s):
    if not word:
        return True

    n = len(word)
    m = len(s)

    if n > m:
        return False

    word_pointer, s_pointer = 0, 0

    while word_pointer < n and s_pointer < m:
        if word[word_pointer] == s[s_pointer]:
            word_pointer += 1

        s_pointer += 1

    return True if word_pointer == n else False


s = "abcde"
words = ["a", "bb", "acd", "ace"]
print numMatchingSubseq(s, words)
