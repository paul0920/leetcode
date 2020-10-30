import collections

n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 0]]
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

node_graph = collections.defaultdict(list)
node_level = collections.defaultdict(int)
res = []


def dfs(prev_node, curr_node, level):
    node_level[curr_node] = level

    # print "path: %s --> %s; level: %s;" % (prev_node, curr_node, level), node_level

    for next_node in node_graph[curr_node]:

        if next_node == prev_node:
            continue

        # next_node hasn't been visited
        if not next_node in node_level:
            dfs(curr_node, next_node, level + 1)

        # print "%s --> %s --> %s; level: %s;" % (prev_node, curr_node, next_node, level), node_level
        node_level[curr_node] = min(node_level[curr_node], node_level[next_node])
        # print "%s --> %s --> %s; level: %s;" % (prev_node, curr_node, next_node, level), node_level

        if node_level[next_node] == level + 1:
            res.append([curr_node, next_node])
            # print "%s --> %s --> %s; level: %s;" % (prev_node, curr_node, next_node, level), node_level, res

        # print ""

    return res


for node_a, node_b in connections:
    node_graph[node_a] += [node_b]
    node_graph[node_b] += [node_a]

# print node_graph
# initial curr_node can be started with any nodes. The result is the same
print dfs(-1, 0, 1)
# print dfs(-1, 3, 1)

print node_level
