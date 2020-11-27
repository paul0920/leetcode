def cord(src):
    return src / 8, src % 8

def sht_pth(sx, sy, board):
    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]:
          nx, ny = x + i[0], y + i[1]
          if 0 <= nx <= 7 and 0 <= ny <= 7:
              if board[nx][ny] is None:
                  board[nx][ny] = board[x][y] + 1
                  arr.append((nx, ny)) 

def answer(src, dest):
    board = [[None for i in range(8)] for i in range(8)]
    sx, sy = cord(src)
    dx, dy = cord(dest)
    board[sx][sy] = 0
    sht_pth(sx, sy, board)
    show(board)
    return board[dx][dy]


def show(board):

    for row in board:
        print row

print answer(19, 36)
# Answer 1

print answer(0, 1)
# Answer 3
