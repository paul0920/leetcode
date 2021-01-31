
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

if not grid:
    print 0

count = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 1:
            if c == len(grid[r]) - 1:
                count += 1
            elif grid[r][c] != grid[r][c + 1]:
                count += 1

for c in range(len(grid[r])):
    for r in range(len(grid)):
        if grid[r][c] == 1:
            if r == len(grid) - 1:
                count += 1
                break
            elif grid[r][c] != grid[r + 1][c]:
                count += 1

print count * 2
