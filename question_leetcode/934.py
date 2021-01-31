import collections


A = [[0, 1, 0],
     [0, 0, 0],
     [0, 0, 1]]

A = [[1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1]]


if not A or not A[0]:
    print 0
    exit()

y_size = len(A)
x_size = len(A[0])
island_pos = set()


def check_boundry(y, x):
    if y < 0 or y >= y_size:
        return False

    if x < 0 or x >= x_size:
        return False

    else:
        return True


def bfs_get_island(y, x):
    q = collections.deque([(y, x)])
    island_pos.add((y, x))

    while q:

        curr_y, curr_x = q.popleft()

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            next_y = curr_y + dy
            next_x = curr_x + dx

            if (next_y, next_x) in island_pos:
                continue

            if check_boundry(next_y, next_x):

                if A[next_y][next_x]:
                    q.append((next_y, next_x))
                    island_pos.add((next_y, next_x))


def bfs_count_flipped(pos_set):
    step = 0
    q = [(y, x) for y, x in pos_set]

    while q:

        next_q = []

        for curr_y, curr_x in q:
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                next_y = curr_y + dy
                next_x = curr_x + dx

                if (next_y, next_x) in pos_set:
                    continue

                if check_boundry(next_y, next_x):

                    if not A[next_y][next_x]:
                        next_q.append((next_y, next_x))
                        # island_pos keeps updating with pos_set
                        pos_set.add((next_y, next_x))

                    elif A[next_y][next_x]:
                        return step

        q = next_q
        step += 1

    return 0


for y in range(y_size):
    for x in range(x_size):

        if A[y][x] and not len(island_pos):
            bfs_get_island(y, x)

count = bfs_count_flipped(island_pos)

print count
