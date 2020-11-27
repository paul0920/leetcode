# Prepare the Bunnies' Escape
# ===========================
#
# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but
# once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape
# pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that
# will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling
# project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again),
# you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per
# escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's
# suspicions.
#
# You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod.
# The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out
# of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).
#
# Write a function solution(map) that generates the length of the shortest path from the prison door to the escape pod,
# where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of
# nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always
# passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width
# of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Python cases --
# Input:
# solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# Output:
#     7
#
# Input:
# solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
# Output:
#     11
#
# -- Java cases --
# Input:
# Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
# Output:
#     7
#
# Input:
# Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
# Output:
#     11

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
    map_top_2_bottom = {}
    map_bottom_2_top = {}
    zero = set()
    min_distance = float('INF')

    def check_boundry(y, x):

        if y < 0 or y >= size_y:
            return False

        if x < 0 or x >= size_x:
            return False

        return True

    def BFS_path(y, x, distance_map):

        q = collections.deque([(y, x)])
        distance_map[(y, x)] = 1
        visited = set([(y, x)])

        while q:

            curr_y, curr_x = q.popleft()

            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                next_y = curr_y + dy
                next_x = curr_x + dx

                if check_boundry(next_y, next_x):

                    if not map[next_y][next_x] and (next_y, next_x) not in visited:
                        distance_map[(next_y, next_x)] = distance_map[(curr_y, curr_x)] + 1
                        q += [(next_y, next_x)]
                        visited.add((next_y, next_x))

    def get_min_distance(y, x, distance_map):

        min_local_distance = float('INF')

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            next_y = y + dy
            next_x = x + dx

            if check_boundry(next_y, next_x):
                if not map[next_y][next_x] and (next_y, next_x) in distance_map:
                    min_local_distance = min(min_local_distance, distance_map[(next_y, next_x)])

        return min_local_distance if min_local_distance != float('INF') else 0

    BFS_path(0, 0, map_top_2_bottom)
    BFS_path(size_y - 1, size_x - 1, map_bottom_2_top)

    for y in range(size_y):
        for x in range(size_x):

            if map[y][x]:
                zero.add((y, x))

    for y, x in zero:

        pre_step = get_min_distance(y, x, map_top_2_bottom)
        post_step = get_min_distance(y, x, map_bottom_2_top)

        # print y, x, pre_step, post_step
        if not pre_step or not post_step:
            continue

        min_distance = min(min_distance, pre_step + post_step + 1)

    return min_distance


print solution(station_map)
