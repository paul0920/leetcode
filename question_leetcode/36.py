
board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
square = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):

        c = board[i][j]
        k = 3* (i // 3) + j // 3

        if c != ".":
            if c in row[i] or c in col[j] or c in square[k]:
                print False
                exit()

            row[i].add(c)
            col[j].add(c)
            square[k].add(c)

print True
