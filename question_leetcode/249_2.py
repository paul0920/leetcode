import itertools

strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

f_key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]

print sorted(strings, key=f_key)

print [list(g) for _, g in itertools.groupby(sorted(strings, key=f_key), f_key)]
