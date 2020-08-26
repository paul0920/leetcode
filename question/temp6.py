import collections

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]

g = collections.defaultdict(dict)
for (x, y), v in zip(equations, values):
    g[x][y] = v
    g[y][x] = 1 / v

print g



for idx, (a, b) in enumerate(equations):
    print idx, a, b
