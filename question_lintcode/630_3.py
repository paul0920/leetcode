# Time complexity:
# the average case: O(sqrt(mn))
# the worst case: O(mn)

import collections


def shortestPath2(grid):
    # write your code here
    if not grid or not grid[0]:
        return -1

    n = len(grid)
    m = len(grid[0])

    # Make sure the destination is empty
    if grid[n - 1][m - 1]:
        return -1

    if n * m == 1:
        return 0

    forward_queue = collections.deque([(0, 0)])
    forward_visited = {(0, 0)}
    FORWARD_DIRECTIONS = [
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1)
    ]
    backward_queue = collections.deque([(n - 1, m - 1)])
    backward_visited = {(n - 1, m - 1)}
    BACKWARD_DIRECTIONS = [
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1)
    ]
    distance = 0

    while forward_queue and backward_queue:
        distance += 1

        if bfs(grid, forward_queue, forward_visited, backward_visited, FORWARD_DIRECTIONS):
            return distance

        distance += 1

        if bfs(grid, backward_queue, backward_visited, forward_visited, BACKWARD_DIRECTIONS):
            return distance

    return -1


def bfs(grid, queue, visited, opposite_visited, directions):
    # Remember to have the following loop to just loop through the current layer
    for _ in range(len(queue)):
        curr_x, curr_y = queue.popleft()

        for dx, dy in directions:
            x = curr_x + dx
            y = curr_y + dy

            if not is_valid(grid, x, y, visited):
                continue

            if (x, y) in opposite_visited:
                return True

            visited.add((x, y))
            queue.append((x, y))

    return False


def is_valid(grid, x, y, visited):
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
