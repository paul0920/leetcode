import collections

n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
labels = "abaedcd"


def dfs(node, parent):
    # Counter() has "+=" operand
    count = collections.Counter(labels[node])

    for child in g[node]:
        if child != parent:
            count += dfs(child, node)

    res[node] = count[labels[node]]

    return count


g = collections.defaultdict(list)
visited = set()
res = [0] * n

# The following way is to create a relationship map among nodes
for a, b in edges:
    g[a] += [b]
    g[b] += [a]

dfs(0, -1)

print res
