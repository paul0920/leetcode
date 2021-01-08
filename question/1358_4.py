def numberOfSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    i = 0
    res = 0
    hash_map = {c: 0 for c in "abc"}

    for j in range(len(s)):

        hash_map[s[j]] += 1

        while hash_map["a"] and hash_map["b"] and hash_map["c"]:
            hash_map[s[i]] -= 1
            i += 1

        res += i

    return res


s = "abccabc"
print numberOfSubstrings(s)
