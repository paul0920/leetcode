import collections
import heapq

n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2

p_findmax = [0] * n
g = collections.defaultdict(list)

for idx, (a, b) in enumerate(edges):
    g[a] += [(b, idx)]
    g[b] += [(a, idx)]

print g

p_findmax[start] = 1
# Use negative probability for min heap sorting
q = [(-p_findmax[start], start)]

while q:
    (prob, node) = heapq.heappop(q)

    if node == end:
        print -prob
        exit()

    for neighbor, idx in g[node]:

        curr_pro = -prob * succProb[idx]
        if p_findmax[neighbor] < curr_pro:
            p_findmax[neighbor] = curr_pro
            heapq.heappush(q, (-curr_pro, neighbor))

    # print p_findmax

print 0.0
