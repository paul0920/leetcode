import collections


def numMatchingSubseq(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: int
    """
    char_to_word = collections.defaultdict(list)
    count = 0

    for word in words:
        # Use first char as the key and word as the value
        char_to_word[word[0]].append(word)

    # Only loop through s once and process all the words in parallel
    for char in s:
        if char not in char_to_word:
            continue

        word_list = char_to_word[char]
        char_to_word.pop(char)

        for word in word_list:
            # Found the matching subsequence from a word in words
            if len(word) == 1:
                count += 1
                continue

            # Use the next char as the key and word[1:] as the value
            char_to_word[word[1]].append(word[1:])

    return count


s = "abcde"
words = ["a", "bb", "acd", "ace"]
print numMatchingSubseq(s, words)
