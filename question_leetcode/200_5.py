import collections


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])
    visited = set()
    count = 0

    for i in range(m):
        for j in range(n):
            if not is_valid(i, j, visited, grid):
                continue

            visited.add((i, j))
            bfs(i, j, visited, grid)
            count += 1

    return count


def is_valid(y, x, visited, grid):
    if (y, x) in visited:
        return False

    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return False

    if grid[y][x] == "0":
        return False

    return True


def bfs(y, x, visited, grid):
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = collections.deque()
    queue.append((y, x))

    while queue:
        curr_y, curr_x = queue.popleft()

        for dy, dx in DIRECTIONS:
            next_y, next_x = curr_y + dy, curr_x + dx

            if not is_valid(next_y, next_x, visited, grid):
                continue

            visited.add((next_y, next_x))
            queue.append((next_y, next_x))


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print numIslands(grid)
