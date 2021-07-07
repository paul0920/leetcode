import collections


def reorganizeString(s):
    """
    :type s: str
    :rtype: str
    """
    if not s or len(s) == 1:
        return s

    char_to_count = collections.Counter(s)
    # key (optional) - key function where the iterables are passed
    # and comparison is performed based on its return value
    max_freq_char = max(char_to_count.keys(), key=lambda x: char_to_count[x])
    max_count = char_to_count[max_freq_char]
    res = [max_freq_char] * max_count
    i = 0

    for char, count in char_to_count.items():
        if char == max_freq_char:
            continue

        for _ in range(count):
            res[i % max_count] += char
            i += 1

    string = "".join(res)

    return string if i >= max_count - 1 else ""


s = "aaab"
s = "aab"
print reorganizeString(s)
