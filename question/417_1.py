import collections

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
res = []


def check_valid(height, y, x, visited, reach_ocean):
    if y < 0 or x < 0:
        reach_ocean["pacific"] = True
        return False

    if y >= y_size or x >= x_size:
        reach_ocean["atlantic"] = True
        return False

    if height >= matrix[y][x] and (y, x) not in visited:
        return True

    else:
        return False


def bfs_search(y, x):
    q = collections.deque([(y, x)])
    visited = {(y, x)}
    reach_ocean = {"pacific": False, "atlantic": False}

    while q:

        curr_y, curr_x = q.popleft()
        curr_height = matrix[curr_y][curr_x]

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_y = curr_y + dy
            next_x = curr_x + dx

            if check_valid(curr_height, next_y, next_x, visited, reach_ocean):
                q.append((next_y, next_x))
                visited.add((next_y, next_x))

            if reach_ocean["pacific"] and reach_ocean["atlantic"]:
                return True

    return False


for y in range(y_size):
    for x in range(x_size):

        if bfs_search(y, x):
            res += [[y, x]]

print res
