import collections


s = "QQWE"

count = collections.Counter(s)
res = n = len(s)
i = 0

for j, c in enumerate(s):
    count[c] -= 1

    print [n / 4 >= count[c] for c in 'QWER']
    # print all([n / 4 >= count[c] for c in 'QWER'])


    while i < n and all(n / 4 >= count[c] for c in 'QWER'):
        res = min(res, j - i + 1)
        count[s[i]] += 1
        i += 1

print res
