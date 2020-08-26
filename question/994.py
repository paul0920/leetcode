
grid = [[2,1,1],[1,1,0],[0,1,1]]

row, col = len(grid), len(grid[0])

# 'rotting' and 'fresh' are hashtables
rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}

print "[rotting]:", rotting, "[fresh]:", fresh

timer = 0
while fresh:
    if not rotting:
        print -1
    rotting = {(i + di, j + dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if
               (i + di, j + dj) in fresh}

    # keep removing rotting from fresh until there is no fresh
    fresh -= rotting
    timer += 1

print timer