import collections

M = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

if not M or not M[0]:
    print 0
    exit()

size = len(M)
visited = set()
count = 0


def BFS(node):
    visited.add(node)
    q = collections.deque([node])

    while q:

        curr_node = q.popleft()

        for next_node in range(size):

            if M[curr_node][next_node] == 1 and next_node not in visited:
                q += [next_node]
                visited.add(next_node)


def DFS(node):
    for next_node in range(size):

        if M[node][next_node] == 1 and next_node not in visited:
            visited.add(next_node)
            DFS(next_node)


for i in range(size):

    if i not in visited:
        # BFS(i)
        DFS(i)
        count += 1

print count
