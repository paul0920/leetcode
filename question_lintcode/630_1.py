# Time complexity: O(mn)
# Space complexity: O(sqrt(mn))

import collections


def shortestPath2(grid):
    # write your code here
    if not grid or not grid[0]:
        return -1

    n = len(grid)
    m = len(grid[0])

    if grid[n - 1][m - 1]:
        return -1
    if n * m == 1:
        return 0

    forward_queue = collections.deque([(0, 0)])
    forward_visited = set([(0, 0)])
    FORWARD_DIRECTIONS = [
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1)
    ]
    distance = {(0, 0): 0}

    while forward_queue:
        curr_x, curr_y = forward_queue.popleft()
        # Check whether it is the destination here
        if (curr_x, curr_y) == (n - 1, m - 1):
            return distance[(curr_x, curr_y)]

        for dx, dy in FORWARD_DIRECTIONS:
            x = curr_x + dx
            y = curr_y + dy

            if not is_valid(x, y, grid, forward_visited):
                continue

            distance[(x, y)] = distance[(curr_x, curr_y)] + 1
            forward_visited.add((x, y))
            forward_queue.append((x, y))

    return -1


def is_valid(x, y, grid, visited):
    if x < 0 or x >= len(grid):
        return False

    if y < 0 or y >= len(grid[0]):
        return False

    if grid[x][y]:
        return False

    if (x, y) in visited:
        return False

    return True


grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print shortestPath2(grid)
