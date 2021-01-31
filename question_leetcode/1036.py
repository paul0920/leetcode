import collections


def isEscapePossible(blocked, source, target):
    """
    :type blocked: List[List[int]]
    :type source: List[int]
    :type target: List[int]
    :rtype: bool
    """
    if not blocked:
        return True

    blocked_cell = {(x, y) for x, y in blocked}
    x_src, y_src = source[0], source[1]
    x_tar, y_tar = target[0], target[1]

    # Need clarification on the assumptions
    # if (x_src, y_src) in blocked_cell or (x_tar, y_tar) in blocked_cell:
    #     return False

    forward_queue = collections.deque([(x_src, y_src)])
    forward_visited = set([(x_src, y_src)])
    backward_queue = collections.deque([(x_tar, y_tar)])
    backward_visited = set([(x_tar, y_tar)])
    # The maximum layer is defined by 0 <= blocked.length <= 200
    max_count = 19900
    count = 0

    while forward_queue and backward_queue:
        count += 1

        if bfs(forward_queue, forward_visited, backward_visited, blocked_cell):
            return True

        count += 1

        if bfs(backward_queue, backward_visited, forward_visited, blocked_cell):
            return True

        # To successfully escape, both sides need to move more than max_count steps
        if len(forward_visited) > max_count and len(backward_visited) > max_count:
            return True

    return False


def bfs(queue, visited, opposite_visited, blocked_cell):
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for _ in range(len(queue)):
        curr_x, curr_y = queue.popleft()

        for x, y in DIRECTIONS:
            next_x, next_y = curr_x + x, curr_y + y

            if not is_valid(next_x, next_y, visited, blocked_cell):
                continue

            if (next_x, next_y) in opposite_visited:
                return True

            visited.add((next_x, next_y))
            queue.append((next_x, next_y))

    return False


def is_valid(x, y, visited, blocked_cell):
    if (x, y) in visited:
        return False

    if (x, y) in blocked_cell:
        return False

    if x < 0 or 10 ** 6 <= x or y < 0 or 10 ** 6 <= y:
        return False

    return True


blocked = [[5, 20], [10, 10], [15, 10], [10, 30], [15, 30], [20, 30]]
source = [10, 20]
target = [20, 30]
print isEscapePossible(blocked, source, target)
