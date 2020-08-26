
grid = [[4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]]

grid = [[2, 7, 6, 9],
        [9, 5, 1, 6],
        [4, 3, 8, 8],
        [1, 4, 10, 1]]


def isMagic(i, j):
    s = "".join(str(grid[i + x / 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
    return s in "43816729" * 2 or s in "43816729"[::-1] * 2


print sum(isMagic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2) if grid[i + 1][j + 1] == 5)
