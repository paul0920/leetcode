import collections


def shortestPath(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not grid or not grid[0]:
        return -1

    m = len(grid)
    n = len(grid[0])
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = collections.deque()
    queue.append((0, 0, 0))
    visited = collections.defaultdict()
    visited[(0, 0)] = 0
    step = 0

    while queue:

        for _ in range(len(queue)):
            y, x, obstacle_count = queue.popleft()

            if (y, x) == (m - 1, n - 1):
                return step

            for dy, dx in DIRECTIONS:
                next_y = y + dy
                next_x = x + dx
                next_obstacle_count = obstacle_count

                if not is_valid(next_y, next_x, grid, next_obstacle_count, k):
                    continue

                if grid[next_y][next_x] == 1:
                    next_obstacle_count += 1

                if not is_obstacle_count_smaller(next_y, next_x, visited, next_obstacle_count):
                    continue

                visited[(next_y, next_x)] = next_obstacle_count
                queue.append((next_y, next_x, next_obstacle_count))

        step += 1

    return -1


def is_valid(y, x, grid, obstacle_count, k):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return False

    if obstacle_count > k:
        return False

    return True


def is_obstacle_count_smaller(y, x, visited, obstacle_count):
    if (y, x) in visited and obstacle_count < visited[(y, x)]:
        return True

    if (y, x) not in visited:
        return True

    return False


grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
k = 0
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
k = 1
print shortestPath(grid, k)
