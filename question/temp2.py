import collections

g = collections.defaultdict(list)
res = [-1.0] * len(queries)

for idx, arr in enumerate(equations):
    a, b = arr[0], arr[1]
    g[a] += [(b, values[idx])]
    g[b] += [(a, 1.0 / values[idx])]

# print g
for idx, arr in enumerate(queries):

    a, b = arr[0], arr[1]
    q = collections.deque()
    q.append((a, 1.0))
    visited = set()

    while q:

        node_a, curr_val = q.popleft()

        if not node_a or not b in g:
            break

        if node_a == b:
            res[idx] = curr_val
            break

        visited.add(node_a)

        for next_node, val in g[node_a]:

            if not next_node in visited:
                q.append((next_node, curr_val * val))

print res
