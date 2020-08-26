import collections
import heapq

s = "loveleetcode"

count = {}
h = []
res = []

for c in s:
    count[c] = count.get(c, 0) + 1

for c in s:
    heapq.heappush(h, (count[c], c))
    print h

while h:
    res += heapq.heappop(h)[1]

print "".join(res)[::-1]



count = collections.Counter(s)

h = []
res = []

for word, fre in count.items():
    heapq.heappush(h, (fre, word))
    print h

while h:
    f, w = heapq.heappop(h)
    res.append(w * f)

print ''.join(res)[::-1]
