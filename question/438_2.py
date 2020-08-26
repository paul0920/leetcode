import collections

s = "cbaebabacd"
p = "abc"

a = []
l = len(p)
cs = collections.Counter(s[:l - 1])
cp = collections.Counter(p)

i = 0

while i + l <= len(s):

    print "cs", cs
    print i, l, s[i + l - 1]

    cs[s[i + l - 1]] += 1

    if cs == cp:
        a.append(i)
        print a

    cs[s[i]] -= 1
    print "cs", cs

    if cs[s[i]] == 0:
        del cs[s[i]]

    print "cs", cs

    i += 1
    print ""

print a