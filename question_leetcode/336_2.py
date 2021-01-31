
words = ["abcd", "dcba", "lls", "s", "sssll"]


word_hash_table = {}
res = []


def findPrefix(word):
    word_list = []

    for i in range(len(word)):

        if word[i:] == word[i:][::-1]:
            word_list += [word[:i]]

    return word_list


def findSuffix(word):
    word_list = []

    for i in range(len(word)):

        # Check i + 1, which is different from prefix part
        if word[:i + 1] == word[:i + 1][::-1]:
            word_list += [word[i + 1:]]

    return word_list


for i, word in enumerate(words):
    word_hash_table[word] = i

for idx, word in enumerate(words):

    palindrome_word = word[::-1]

    if palindrome_word in word_hash_table:

        another_idx = word_hash_table[palindrome_word]

        # To handle the edge case of only one-alphabet word
        if idx != another_idx:
            res += [[idx, another_idx]]

    for prefix_word in findPrefix(word):

        prefix_palindrome_word = prefix_word[::-1]

        if prefix_palindrome_word in word_hash_table:
            res += [[idx, word_hash_table[prefix_palindrome_word]]]

    for suffix_word in findSuffix(word):

        suffix_palindrome_word = suffix_word[::-1]

        if suffix_palindrome_word in word_hash_table:

            # Be careful about the order, which is different from prefix part
            res += [[word_hash_table[suffix_palindrome_word], idx]]

print res
