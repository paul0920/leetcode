import collections

S = "abbabbaaab"

# S can be sorted directly in list format
print sorted(S)

count = collections.Counter(S)


def co(other):
    return count[other]


# S needs to be sorted according to alphabet order
# in case that elements have the same count
c = sorted(sorted(S), key=co, reverse=True)

print c

half = len(c[::2]) - 1

if max([v for v in count.values()]) > half + 1:
    print ""

c[::2], c[1::2] = c[half::-1], c[:half:-1]

print "".join(c)
