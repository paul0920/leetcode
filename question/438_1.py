import collections

s = "cbaebabacd"
p = "abc"

s_len = len(s)
p_len = len(p)

count_map = collections.Counter(p)
res = []

i = 0

for j, c in enumerate(s):

    count_map[c] -= 1

    if count_map[c] >= 0:
        p_len -= 1

    if p_len == 0:
        while i < j and count_map[s[i]] < 0:
            count_map[s[i]] += 1
            i += 1

        # Keep the same window size as p
        if j - i == len(p) - 1:
            res.append(i)

print res