def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if not s:
        return True

    char_to_word = {s[0]: s}

    for char in t:
        if char not in char_to_word:
            continue

        word = char_to_word[char]
        char_to_word.pop(char)

        if len(word) == 1:
            return True

        char_to_word[word[1]] = word[1:]

    return False


s = "abc"
t = "ahbgdc"
print isSubsequence(s, t)
