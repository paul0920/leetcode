import collections

A = [84,-37,32,40,95]
K = 167

d = collections.deque([[0, 0]])
res, cur = float('inf'), 0
for i, a in enumerate(A):
    cur += a

    print cur, d, cur - d[0][1]

    while d and cur - d[0][1] >= K:

        print cur, d[0], cur - d[0][1]
        res = min(res, i + 1 - d.popleft()[0])

    while d and cur <= d[-1][1]:
        d.pop()

    d.append([i + 1, cur])

print res if res < float('inf') else -1


