
grid = [[4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]]

grid = [[2, 7, 6, 9],
        [9, 5, 1, 6],
        [4, 3, 8, 8],
        [1, 4, 10, 1]]

m = len(grid)
n = len(grid[0])
res = []
count = 0
magic_num = set()
check_num = set()

for val in range(1, 10):
    check_num.add(val)

# grid_trans = map(list, zip(*grid))

for i in range(m - 2):
    for j in range(n - 2):

        magic_num = set()

        for x in range(i, i + 3):
            for y in range(j, j + 3):
                magic_num.add(grid[x][y])

        if magic_num != check_num:
            continue

        res += [sum(grid[x][j:j + 3]) for x in range(i, i + 3)]
        res += [sum([row[y] for row in grid[i:i + 3]]) for y in range(j, j + 3)]
        # res += [sum(grid_trans[y][i:i+3]) for y in range(j, j+3)]

        if sum([grid[i][j], grid[i + 2][j + 2]]) == sum([grid[i][j + 2], grid[i + 2][j]]) and len(set(res)) == 1:
            count += 1

        res = []

print count
