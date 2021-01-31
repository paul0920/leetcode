import collections

board = [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]
# board = [[-1, 4, 4, 4, 4, 4, 4, -1],
#          [-1, -1, -1, -1, -1, -1, -1, -1]]


if not board or not board[0]:
    print -1
    exit()

size_y = len(board)
size_x = len(board[0])
visited = {1: 0}
q = collections.deque([1])

while q:

    current_pos = q.popleft()

    for step in range(current_pos + 1, current_pos + 7):

        next_step = step
        # Mapping between each square and matrix index is one of the key parts
        y = -(((next_step - 1) / size_x) + 1)
        x = (next_step - 1) % size_x
        transfer_step = board[y][x if y % 2 != 0 else -(x + 1)]

        if transfer_step > 0:
            next_step = transfer_step

        if next_step not in visited:
            visited[next_step] = visited[current_pos] + 1
            q.append(next_step)

        if next_step == size_y * size_x:
            print visited[current_pos] + 1
            exit()

print -1
