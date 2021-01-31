import collections

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])
        max_count = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    count = self.bfs(grid, r, c)
                    max_count = max(max_count, count)

        return max_count

    def bfs(self, grid, r, c):

        size_r = len(grid)
        size_c = len(grid[0])
        grid[r][c] = -1
        island = 1

        q = collections.deque()
        q.append((r, c))

        while q:

            r, c = q.popleft()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):

                nr, nc = r + dx, c + dy
                if 0 <= nr < size_r and 0 <= nc < size_c and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = -1
                    island += 1

        return island

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]]

# grid = [
#     [1]]

ans = Solution()
print ans.maxAreaOfIsland(grid)
