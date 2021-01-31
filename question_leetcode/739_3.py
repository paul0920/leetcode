
T = [73, 74, 75, 71, 69, 72, 76, 73]

# 102 is the upper bound of the temperature
nxt = [float('inf')] * 102
res = [0] * len(T)

for i in range(len(T) - 1, -1, -1):

    warmer_index = min(nxt[t] for t in range(T[i] + 1, 102))

    print "index:", i, T[i]
    print [nxt[t] for t in range(min(T), 102)]
    print "warmer_index:", warmer_index

    if warmer_index < float('inf'):
        res[i] = warmer_index - i

    nxt[T[i]] = i

    print res
    print ""

print res
