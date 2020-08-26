import collections

s = "abaccc"
d = collections.defaultdict(list)

for i, alp in enumerate(s):
    d[alp].append(i)

    print "d", d
    print "len(d)", len(d)
    print "len(d.keys())", len(d.keys())
    print "min(d.values())", min(d.values())
    print ""