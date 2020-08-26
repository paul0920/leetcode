import collections


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]


g = collections.defaultdict(list)
res = [-1.0] * len(queries)

for idx, (a, b) in enumerate(equations):
    g[a] += [(b, values[idx])]
    g[b] += [(a, 1.0 / values[idx])]

# print g

for idx, (a, b) in enumerate(queries):

    q = collections.deque()
    q.append((a, 1.0))
    visited = set()

    visited.add(a)

    while q:

        node_a, curr_val = q.popleft()

        if not node_a or not b in g:
            res[idx] = -1.0
            break

        if node_a == b:
            res[idx] = curr_val
            break

        # Add node_a(next_node) into visited right before appending it to q
        # to prevent duplicate visits later
        # visited.add(node_a)

        for next_node, val in g[node_a]:

            if not next_node in visited:
                visited.add(next_node)
                q.append((next_node, curr_val * val))

print res
