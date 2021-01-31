

grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]


def is_valid(grid, r, c):
    m, n = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= m or c >= n:
        return False
    return True

def dfs(grid, r, c):
    grid[r][c] = '0'
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for d in directions:
        nr, nc = r + d[0], c + d[1]
        if is_valid(grid, nr, nc) and grid[nr][nc] == '1':
            dfs(grid, nr, nc)


if not grid or not grid[0]:
    print 0
    exit()

m, n = len(grid), len(grid[0])
count = 0
for i in xrange(m):
    for j in xrange(n):
        if grid[i][j] == '1':
            dfs(grid, i, j)
            count += 1

print count
