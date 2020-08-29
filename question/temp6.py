import collections

A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]


s = "paper"
t = "title"

h_s = collections.defaultdict(list)
h_t = collections.defaultdict(list)

for idx, c in enumerate(s):
    h_s[c].append(idx)

for idx, c in enumerate(t):
    h_t[c].append(idx)

print h_s
print h_t

print sorted([arr for arr in h_s.values()])
print sorted([arr for arr in h_t.values()])