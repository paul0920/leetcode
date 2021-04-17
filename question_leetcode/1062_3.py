def longestRepeatingSubstring(S):
    """
    :type S: str
    :rtype: int
    """
    if not S:
        return 0

    string_to_count = {}

    for i in range(len(S)):
        for j in range(i, len(S)):
            sub_string = S[i:j + 1]

            if sub_string in string_to_count:
                string_to_count[sub_string] += 1
                continue

            string_to_count[sub_string] = 1

    max_len = 0

    for string, count in string_to_count.items():
        if count == 1:
            continue

        max_len = max(max_len, len(string))

    return max_len


S = "abbaba"
print longestRepeatingSubstring(S)
