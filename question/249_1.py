import collections

strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

box = collections.defaultdict(list)

for s in strings:

    key = ()

    for c in s:
        # "," turns it into a tuple
        key += (ord(c) - ord(s[0])) % 26,

    # "," turns s into an element of the list
    box[key] += s,

print box.values()
