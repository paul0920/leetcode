import collections


def updateMatrix(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    if not mat:
        return [0]

    m = len(mat)
    n = len(mat[0])
    res = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                continue

            res[i][j] = bfs(i, j, mat)

    return res


def bfs(y, x, mat):
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = collections.deque([(y, x)])
    visited = {(y, x)}
    count = 0

    while queue:
        for _ in range(len(queue)):
            curr_y, curr_x = queue.popleft()

            if mat[curr_y][curr_x] == 0:
                return count

            for dy, dx in DIRECTIONS:
                next_y, next_x = curr_y + dy, curr_x + dx

                if not is_valid(next_y, next_x, mat):
                    continue

                if (next_y, next_x) in visited:
                    continue

                queue.append((next_y, next_x))
                visited.add((next_y, next_x))

        count += 1

    return count


def is_valid(y, x, mat):
    if y < 0 or y >= len(mat) or x < 0 or x >= len(mat[0]):
        return False

    return True


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print updateMatrix(mat)
