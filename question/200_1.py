import collections


class Solution(object):
	def numIslands(self, grid):

		if not grid:
			return 0

		row, col = len(grid), len(grid[0])
		count = 0

		for r in range(row):
			for c in range(col):
				if grid[r][c] == '1':
					self.bfs(grid, r, c)
					print "Complete", count
					print ""
					count += 1

		return count

	def valid_node(self, grid, r, c):

		if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
			return False

		return True

	def bfs(self, grid, r, c):

		q = collections.deque()
		q.append((r, c))

		grid[r][c] = '#'

		while q:
			print q
			x, y = q.popleft()

			for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
				nr, nc = x + d[0], y + d[1]

				print grid[0], "(", x, y, ")", "(", nr, nc, ")"
				print grid[1], "(", x, y, ")", "(", nr, nc, ")"
				print grid[2], "(", x, y, ")", "(", nr, nc, ")"
				print grid[3], "(", x, y, ")", "(", nr, nc, ")"
				print ""

				if self.valid_node(grid, nr, nc) and grid[nr][nc] == '1':
					grid[nr][nc] = '@'
					q.append((nr, nc))

		return


grid = [
	["1", "1", "0", "0", "0"],
	["1", "1", "0", "0", "0"],
	["0", "0", "1", "0", "0"],
	["0", "0", "0", "1", "1"], ]

ans = Solution()
print ans.numIslands(grid)
