
matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]


if not matrix or not matrix[0]:
    print []
    exit()

y_size = len(matrix)
x_size = len(matrix[0])
pacific = set()
atlantic = set()


def check_valid(height, y, x, visited):
    if y < 0 or y >= y_size:
        return False

    if x < 0 or x >= x_size:
        return False

    if height <= matrix[y][x] and (y, x) not in visited:
        return True

    else:
        return False


def dfs_search(y, x, visited):
    visited.add((y, x))
    curr_height = matrix[y][x]

    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_y = y + dy
        next_x = x + dx

        if check_valid(curr_height, next_y, next_x, visited):
            dfs_search(next_y, next_x, visited)


pacific_reachable = [(i, 0) for i in range(y_size)] + [(0, i) for i in range(x_size)]
atlantic_reachable = [(y_size - 1, i) for i in range(x_size)] + [(i, x_size - 1) for i in range(y_size)]

for y, x in pacific_reachable:
    dfs_search(y, x, pacific)

for y, x in atlantic_reachable:
    dfs_search(y, x, atlantic)

print list(pacific & atlantic)
