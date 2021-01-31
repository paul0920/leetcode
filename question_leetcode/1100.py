
S = "abcdde"; K = 2

res, i = 0, 0
cur = set()

for j in range(len(S)):

    while S[j] in cur:
        cur.remove(S[i])
        i += 1
        print i,

    cur.add(S[j])
    res += j - i + 1 >= K

    print ""
    print "S[j]:", S[j], "   ", cur
    print "res:", res
    print ""

print res
