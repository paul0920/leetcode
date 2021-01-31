import collections


grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]


if not grid or not grid[0]:
    print 0
    exit()

m = len(grid)
n = len(grid[0])
visited = set()
island_count = 0


def check_valid(y, x):
    if y < 0 or y >= m or x < 0 or x >= n:
        return False

    if (y, x) in visited:
        return False

    # Value check needs to be after the boundary check
    # Also, be careful about the input element type is string not int
    if grid[y][x] == "0":
        return False

    return True


def bfs(y, x):
    visited.add((y, x))
    q = collections.deque()
    q.append((y, x))

    while q:

        curr_y, curr_x = q.popleft()

        for dy, dx in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            next_y = curr_y + dy
            next_x = curr_x + dx

            if check_valid(next_y, next_x):
                q.append((next_y, next_x))
                visited.add((next_y, next_x))


for y in range(m):
    for x in range(n):

        if check_valid(y, x):
            bfs(y, x)
            island_count += 1

print island_count
