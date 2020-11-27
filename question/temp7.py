import collections

station_map = [[0, 1, 1, 0],
               [0, 0, 0, 1],
               [1, 1, 0, 0],
               [1, 1, 1, 0]]
station_map = [[0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 1, 1, 1, 1, 1],
               [0, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0]]
#
station_map = [[0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0]]  # Answer 21
#
# station_map = [[0, 1, 1, 0],
#                [0, 0, 0, 1],
#                [1, 1, 0, 0],
#                [1, 1, 1, 0]]  # Answer 7
#
# station_map = [[0, 1, 0, 0, 0],
#                [0, 0, 0, 1, 0],
#                [1, 1, 1, 1, 0]]  # Answer 7
# #
# station_map = [[0, 1, 1, 1],
#                [0, 1, 0, 0],
#                [1, 0, 1, 0],
#                [1, 1, 0, 0]]  # Answer 7


def solution(map):
    if not map or not map[0]:
        return 0

    size_y = len(map)
    size_x = len(map[0])

    def BFS_path()


    q = collections.deque([(0, 0, 1, False)])
    visited = set((0, 0))
    res = []

    def check_boundry(y, x):

        if y < 0 or y >= size_y:
            return False

        if x < 0 or x >= size_x:
            return False

        return True

    while q:

        curr_y, curr_x, curr_move, wall_removed = q.popleft()

        if curr_y == size_y - 1 and curr_x == size_x - 1:
            res += [curr_move]
            # return curr_move

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            next_y = curr_y + dy
            next_x = curr_x + dx

            if check_boundry(next_y, next_x) :

                if map[next_y][next_x] == 0 and (next_y, next_x) not in visited:
                    q += [(next_y, next_x, curr_move + 1, wall_removed)]
                    visited.add((next_y, next_x))

                elif map[next_y][next_x] == 1 and not wall_removed:
                    q += [(next_y, next_x, curr_move + 1, True)]

    return min(res), res,



print solution(station_map)
