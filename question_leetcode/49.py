def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagram_to_word = {}

    for word in strs:
        key = "".join(sorted(word))

        if key in anagram_to_word:
            anagram_to_word[key].append(word)
            continue

        anagram_to_word[key] = [word]

    return anagram_to_word.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(strs)
