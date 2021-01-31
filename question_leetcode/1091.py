import collections

grid = [[0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]]


if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1]:
    print -1
    exit()

size_y = len(grid)
size_x = len(grid[0])
q = collections.deque([(0, 0, 1)])
visited = set((0, 0))


def check_boundry_valid(y, x):
    if y < 0 or y >= size_y:
        return False

    if x < 0 or x >= size_x:
        return False

    else:
        return True


# Empty cells are saved in q
while q:

    curr_y, curr_x, curr_len = q.popleft()

    if curr_y == size_y - 1 and curr_x == size_x - 1:
        print curr_len
        exit()

    for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:

        next_y = curr_y + dy
        next_x = curr_x + dx

        if check_boundry_valid(next_y, next_x):

            if not grid[next_y][next_x] and (next_y, next_x) not in visited:

                # This is the key point to find the shortest path:
                # record the current distance with next step together
                q.append((next_y, next_x, curr_len + 1))
                visited.add((next_y, next_x))

print -1
