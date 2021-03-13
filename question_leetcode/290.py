def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    pattern_to_count = {}
    s_to_count = {}
    s_split = s.split()

    if len(pattern) != len(s_split):
        return False

    for i in range(len(pattern)):
        pattern_key = pattern[i]
        s_key = s_split[i]

        if pattern_to_count.get(pattern_key, -1) != s_to_count.get(s_key, -1):
            return False

        pattern_to_count[pattern_key] = i
        s_to_count[s_key] = i

    return True


pattern = "aba"
s = "dog cat cat"
print wordPattern(pattern, s)
