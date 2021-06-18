def spellchecker(wordlist, queries):
    """
    :type wordlist: List[str]
    :type queries: List[str]
    :rtype: List[str]
    """
    if not wordlist:
        return [""] * len(queries) if len(queries) else [""]

    res = []
    wordlist_set = set(wordlist)
    lower_to_origin_word = {}
    masked_to_origin_word = {}

    for word in wordlist:
        masked_word = get_masked_word(word)

        if word.lower() not in lower_to_origin_word:
            lower_to_origin_word[word.lower()] = word

        if masked_word not in masked_to_origin_word:
            masked_to_origin_word[masked_word] = word

    for word in queries:
        masked_word = get_masked_word(word)

        if word in wordlist_set:
            res.append(word)

        elif word.lower() in lower_to_origin_word:
            res.append(lower_to_origin_word[word.lower()])

        elif masked_word in masked_to_origin_word:
            res.append(masked_to_origin_word[masked_word])

        else:
            res.append("")

    return res


def get_masked_word(word):
    word_str = ""

    for char in word:
        if char.lower() in {"a", "e", "i", "o", "u"}:
            word_str += "*"
            continue

        word_str += char.lower()

    return word_str


wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
print spellchecker(wordlist, queries)
