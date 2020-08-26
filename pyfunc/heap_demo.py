import heapq

x = [9, 8, 7, 6, 5, 4]
res = []

for n in x:
    heapq.heappush(res, n)
    print res

print ""

heapq.heapify(x)
print x
print ""


a, b = [], []

while res:
    a.append(heapq.heappop(res))
    b.append(heapq.heappop(x))

print "a:", a
print "b:", b
print ""


a = [9, 8, 7, 6, 5, 4]

while a:
    print heapq.heappop(a), a
