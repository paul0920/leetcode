import bisect

queries = ["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"]
words = ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]

f = sorted([w.count(min(w)) for w in words])
# print f

print [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]
