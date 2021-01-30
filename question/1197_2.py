import collections


def minKnightMoves(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    if (x, y) == (0, 0):
        return 0

    forward_queue = collections.deque([(0, 0)])
    forward_visited = set([(0, 0)])
    backward_queue = collections.deque([(x, y)])
    backward_visited = set([(x, y)])
    distance = 0

    while forward_queue and backward_queue:
        distance += 1

        if bfs(forward_queue, forward_visited, backward_visited):
            return distance

        distance += 1

        if bfs(backward_queue, backward_visited, forward_visited):
            return distance


def bfs(queue, visited, opposite_visited):
    DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    # Use the following way to calculate 1 layer only.
    # DON'T USE "while queue:"
    for _ in range(len(queue)):
        curr_x, curr_y = queue.popleft()

        for x, y in DIRECTIONS:
            next_x, next_y = curr_x + x, curr_y + y

            if (next_x, next_y) in visited:
                continue

            if (next_x, next_y) in opposite_visited:
                return True

            queue.append((next_x, next_y))
            visited.add((next_x, next_y))

    return False


print minKnightMoves(5, 5)
