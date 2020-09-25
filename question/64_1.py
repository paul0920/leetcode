import collections

grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]

# grid = [[0]]


indegree = collections.defaultdict(int)
g_from_to = collections.defaultdict(dict)

q_visit = collections.deque()
distance = {}

# Create a graph among nodes and the next step could only move right or down
for i, y_val in enumerate(grid):
    for j, x_yal in enumerate(grid[0]):

        distance[(i, j)] = float('INF')

        if i > 0:
            indegree[(i, j)] += 1
            g_from_to[(i - 1, j)][(i, j)] = grid[i][j]

        if j > 0:
            indegree[(i, j)] += 1
            g_from_to[(i, j - 1)][(i, j)] = grid[i][j]

q_visit.append(((0, 0), grid[0][0]))
# Please remember to set node (0, 0) back to original value
distance[(0, 0)] = grid[0][0]

while q_visit:

    curr_node, curr_dis = q_visit.popleft()

    for next_node in g_from_to[curr_node]:

        next_dis = curr_dis + g_from_to[curr_node][next_node]
        distance[next_node] = min(distance[next_node], next_dis)
        indegree[next_node] -= 1

        # We already calculated all the possibilities getting to the next_node
        # and maintained the minimum value getting to "next_node"
        if not indegree[next_node]:
            q_visit.append((next_node, distance[next_node]))

# print distance
print distance[max(distance)]
