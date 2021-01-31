class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        path = []

        self.backtracking(nums, path, res)

        return res

    def backtracking(self, nums, path, res):

        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.backtracking(nums[:i] + nums[i + 1:], path + [nums[i]], res)


nums = [1, 2, 3]
obj = Solution()

print obj.permute(nums)
