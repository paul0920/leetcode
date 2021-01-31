class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        nums.sort()
        res = []
        self.dfs(nums, set(), [], res)

        return res

    def dfs(self, nums, visited, permutation, res):
        if len(permutation) == len(nums):
            res += [permutation[:]]

            return

        for i in range(len(nums)):
            if i in visited:
                continue

            # Here is the key point:
            # if this is not the path with nums[i - 1],
            # skip this path (this is a repeated path)
            if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                continue

            permutation.append(nums[i])
            visited.add(i)
            self.dfs(nums, visited, permutation, res)
            visited.remove(i)
            permutation.pop()


nums = [1, 1, 2]
obj = Solution()
print obj.permuteUnique(nums)
