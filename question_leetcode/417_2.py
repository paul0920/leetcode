import collections

matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]


if not matrix or not matrix[0]:
    print []
    exit()

m, n = len(matrix), len(matrix[0])

def bfs(reachable_ocean):

    q = collections.deque(reachable_ocean)

    while q:

        i, j = q.popleft()

        for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            next_i = i + di
            next_j = j + dj

            if 0 <= next_i < m and 0 <= next_j < n and (next_i, next_j) not in reachable_ocean and matrix[next_i][next_j] >= matrix[i][j]:
                q.append((next_i, next_j))
                reachable_ocean.add((next_i, next_j))

    return reachable_ocean


pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
atlantic = set([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n - 1)])

print list(bfs(pacific) & bfs(atlantic))
