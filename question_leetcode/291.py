def wordPatternMatch(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    return is_matched(pattern, s, {}, set())


def is_matched(pattern, string, mapping, used):
    # Check pattern status
    if not pattern:
        return not string

    char = pattern[0]

    # Check whether we visited this character
    if char in mapping:
        word = mapping[char]

        if not string.startswith(word):
            return False

        return is_matched(pattern[1:], string[len(word):], mapping, used)

    # Start checking all the possibilities of string
    for length in range(len(string)):
        word = string[:length + 1]

        if word in used:
            continue

        mapping[char] = word
        used.add(word)
        if is_matched(pattern[1:], string[length + 1:], mapping, used):
            return True

        used.remove(word)
        del mapping[char]

    return False


pattern = "abab"
s = "redblueredblue"
print wordPatternMatch(pattern, s)
