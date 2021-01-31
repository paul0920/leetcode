import collections

n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
labels = "abaedcd"


def dfs(node):
    # Counter() has "+=" operand
    count = collections.Counter()

    if not node in visited:
        count[labels[node]] = 1
        visited.add(node)

        for child in g[node]:
            count += dfs(child)

        res[node] = count[labels[node]]

    return count


g = collections.defaultdict(list)
visited = set()
res = [0] * n

# The following way is to create a relationship map among nodes
for a, b in edges:
    g[a] += [b]
    g[b] += [a]

dfs(0)

print res
