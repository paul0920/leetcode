import collections

n = 15
headID = 0
manager =   [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
informTime = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

g = collections.defaultdict(list)
q = collections.deque()

for sub, mg in enumerate(manager):

    if mg != -1:
        g[mg] += [sub]

print g

q.append(headID)

while q:

    node = q.popleft()

    for next_node in g[node]:
        informTime[next_node] = informTime[node] + informTime[next_node]
        q.append(next_node)

print max(informTime)
