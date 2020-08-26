import collections

grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]


def is_valid(grid, r, c):
    m, n = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= m or c >= n:
        return False
    return True

def bfs(grid, r, c):
    queue = collections.deque()
    queue.append((r, c))
    grid[r][c] = '0'
    while queue:
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        r, c = queue.popleft()
        # grid[r][c] = '0'
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                queue.append((nr, nc))

                # Need to assign grid[nr][nc] to '0' immediately!!!
                # Otherwise, BFS possibly visits this node again later.
                # This is a common mistake!!!
                grid[nr][nc] = '0'


if not grid or not grid[0]:
    print 0
    exit()

m, n = len(grid), len(grid[0])
count = 0
for i in xrange(m):
    for j in xrange(n):
        if grid[i][j] == '1':
            bfs(grid, i, j)
            count += 1

print count
