# board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#          [6, 0, 0, 1, 9, 5, 0, 0, 0],
#          [0, 9, 8, 0, 0, 0, 0, 6, 0],
#          [8, 0, 0, 0, 6, 0, 0, 0, 3],
#          [4, 0, 0, 8, 0, 3, 0, 0, 1],
#          [7, 0, 0, 0, 2, 0, 0, 0, 6],
#          [0, 6, 0, 0, 0, 0, 2, 8, 0],
#          [0, 0, 0, 4, 1, 9, 0, 0, 5],
#          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
		 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
		 [".", "9", "8", ".", ".", ".", ".", "6", "."],
		 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
		 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
		 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
		 [".", "6", ".", ".", ".", ".", "2", "8", "."],
		 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
		 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def print_board(board):
	for n in range(len(board)):
		print board[n]

	print ""


def checker(row, col, n):
	for y in range(9):
		if board[y][col] == n:
			return False

	for x in range(9):
		if board[row][x] == n:
			return False

	x0 = (col / 3) * 3
	y0 = (row / 3) * 3

	for y in range(3):
		for x in range(3):
			if board[y0 + y][x0 + x] == n:
				return False

	return True


def solve():
	for r in range(9):
		for c in range(9):
			if board[r][c] == ".":
				for n in range(1, 10):
					if checker(r, c, str(n)):

						print "n is possible @ board[r][c]:", str(n), "[", r, "]", "[", c, "]"
						board[r][c] = str(n)

						if solve():
							print "n is solved @ board[r][c]:", str(n), "[", r, "]", "[", c, "]"
							print_board(board)
							return True

						print "Redo to the last step", str(n), "[", r, "]", "[", c, "]"
						board[r][c] = "."

					print "n is impossible @ board[r][c]:", str(n), "[", r, "]", "[", c, "]"
					print_board(board)

				print "1~10 are not working @ board[r][c]:", str(n), "[", r, "]", "[", c, "]"
				return False

	print "Returning......"
	return True


solve()

print "Final Result"
print_board(board)
# print checker(0, 2, str(1))
