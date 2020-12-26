# Get TLE

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.count = 0
        self.res = []
        self.dfs(n, k, set(), [])

        return "".join(map(str, self.res))

    def dfs(self, n, k, visited, permutation):

        if len(permutation) == n:
            self.count += 1

            if self.count == k:
                self.res = permutation[:]
                return

        for i in range(1, n + 1):

            if i in visited:
                continue

            permutation += [i]
            visited.add(i)
            self.dfs(n, k, visited, permutation)
            visited.remove(i)
            permutation.pop()


n = 4
k = 9

obj = Solution()
print obj.getPermutation(n, k)
