# Create a game board randomly
# https://techdevguide.withgoogle.com/resources/coding-question-minesweeper/?types=coding-interview-question#!


import random

m = int(random.uniform(2, 10))
n = int(random.uniform(2, 10))
cell = m * n
mine = int(random.uniform(1, cell))

print m, n, mine, cell

board = []

for y in range(m):
    arr = []
    for x in range(n):
        arr.append('E')

    board.append(arr)

for row in board:
    print row

print "****************"

while mine and cell:

    chance = float(mine) / cell
    p = random.uniform(0, 1)

    # print mine, cell, p, chance

    if p < chance:

        y = int(random.uniform(0, m-1))
        x = int(random.uniform(0, n-1))
        # print y, x, board[y][x], m, n

        if board[y][x] == 'E':
            board[y][x] = 'M'
            mine -= 1

    cell -= 1

print "****************"

for row in board:
    print row

print mine, cell
