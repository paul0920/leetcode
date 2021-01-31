import collections
from copy import copy, deepcopy

class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""

		old_board = [p[:] for p in board]

		if not board:
			return

		row, col = len(board), len(board[0])

		for r in range(row):
			for c in range(col):
				if board[r][c] == 'O':
					loc, status = self.bfs(board, r, c)
					print loc
					print status

					# Check whether this region touches any edges
					if loc:
						for x, y in loc:
							# Return to original status because of touching the edge
							if status:
								board[x][y] = 'O'

							# Flip them because of not touching the edger
							if not status:
								board[x][y] = 'X'

					print board
					print ""

		print "Original:"
		for pt in range(row):
			print old_board[pt]

		print "Flipped:"
		for pt in range(row):
			print board[pt]

	def bfs(self, board, r, c):

		i, j = len(board), len(board[0])
		q = collections.deque()
		q.append((r, c))
		board[r][c] = "#"
		possible_loc = [[r, c]]
		max_e = 0

		if r == 0 or r == i - 1 or c == 0 or c == j - 1:
			edge = 1
			max_e = max(max_e, edge)

		while q:
			print q
			x, y = q.popleft()

			for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
				nr, nc = x + dx, y + dy
				for pt in range(i):
					print board[pt], "(", x, y, ")", "(", nr, nc, ")"
				print ""

				if 0 <= nr < i and 0 <= nc < j and board[nr][nc] == 'O':
					possible_loc.append([nr, nc])
					board[nr][nc] = "@"
					q.append((nr, nc))

					if nr == 0 or nr == i - 1 or nc == 0 or nc == j - 1:
						edge = 1
						max_e = max(max_e, edge)

		return possible_loc, max_e


grid = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

#grid = [
# ["X","O","O","X"],
# ["X","O","X","X"],
# ["X","X","X","X"]]

ans = Solution()
ans.solve(grid)
