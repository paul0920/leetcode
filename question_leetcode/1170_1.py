import collections

queries = ["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"]
words = ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]

q = []
w = []
res = []

for s in queries:
    count = collections.Counter(s)
    # print sorted(count)[0]
    # print ""
    q.append([count[sorted(count)[0]]])

for s in words:
    count = collections.Counter(s)
    w.append([count[sorted(count)[0]]])

count = 0

for q_freq in q:

    for w_freq in w:

        if q_freq < w_freq:
            count += 1

    res.append(count)
    count = 0

print res
