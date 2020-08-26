import collections

n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2

g, dq = collections.defaultdict(list), collections.deque([start])

for i, (a, b) in enumerate(edges):
    g[a].append([b, i])
    g[b].append([a, i])

p = [0.0] * n
p[start] = 1.0

print g
print ""

while dq:

    print dq, p
    cur = dq.popleft()

    for neighbor, i in g[cur]:
        print cur, p[cur], "    ", neighbor, p[neighbor], succProb[i]
        if p[cur] * succProb[i] > p[neighbor]:

            # The probability of each node will be maximized
            p[neighbor] = p[cur] * succProb[i]
            dq.append(neighbor)
    print ""

print p[end]
