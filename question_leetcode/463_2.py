
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

if not grid:
    print 0

land = 0
rept = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):

        if grid[r][c]:
            land += 1

            if r != 0 and grid[r - 1][c]:
                rept += 1

            if c != 0 and grid[r][c - 1]:
                rept += 1

print 4 * land - 2 * rept
