import collections

x = 300
y = 0

x = 97
y = 133

x = 5
y = 5

box = collections.defaultdict(list)
box[(0, 0)] = [[(0, 0)], 0]
q = collections.deque()

step = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
q.append((0, 0))

while q:

    curr_x, curr_y = q.popleft()

    if curr_x == x and curr_y == y:
        # print box[(curr_x, curr_y)][0]
        print box[(curr_x, curr_y)][1]
        # for k, v in box.items():
        #     print k, v
        exit()

    for dx, dy in step:

        next_x = curr_x + dx
        next_y = curr_y + dy

        if not (next_x, next_y) in box:
            box[(next_x, next_y)] = [box[(curr_x, curr_y)][0] + [(next_x, next_y)]]
            box[(next_x, next_y)] += [box[(curr_x, curr_y)][1] + 1]
            q.append((next_x, next_y))

        # This if-statement is always False since using BFS already gives us the shortest path
        # elif box[(next_x, next_y)] > box[(curr_x, curr_y)] + 1:
        #     box[(next_x, next_y)] = box[(curr_x, curr_y)] + 1
