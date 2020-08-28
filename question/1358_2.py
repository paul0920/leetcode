
s = "aaacb"

res = i = 0
count = {c: 0 for c in 'abc'}

for j in xrange(len(s)):

    count[s[j]] += 1

    # print count.values()
    # print all(count.values())

    while all(count.values()):
        count[s[i]] -= 1
        i += 1

    # print i, j
    # print ""

    res += i

print res
