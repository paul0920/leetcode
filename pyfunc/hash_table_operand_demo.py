import collections

c1 = collections.Counter()
c2 = collections.Counter()

c1['a'] = 1
c1['b'] = 2
c2['a'] = 1
c2['b'] = 2

print c1
print c2

# "+=" works for Counter()
c1 += c2

print c1
print ""

u = collections.Counter()
u['x'] = 3
print u
# This assignment doestn' work
# u = Counter({'y': 5, 'z': 4})
# print u
print ""

l1 = collections.defaultdict(list)
l2 = collections.defaultdict(list)

l1['a'] = [1, 2, 3, 4, 5]
l1['b'] = [0, 1]
l2['b'] = [10, 20, 30]

print l1
print l2

# "+=" doesnt' work for defaultdict()
# l1 += l2

print l1
print ""

h1 = {'a': 1, 'b': 2, 'c': 3}
h2 = {'d': 4, "e": 5}

print h1
print h2

# "+=" doesnt' work for hash table
# h1 += h2

print h1
