class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        # Do sort() to simplify the question
        nums.sort()

        dist = {}
        ans = set()

        # Loop up to nums[:-2] since there is only 1 combination left
        for i in range(len(nums) - 2):

            # Once the values become positive, there is no need to
            # search anymore
            if nums[i] > 0:
                break

            target = 0 - nums[i]

            # Since we sort the array in the beginning so that we can
            # ignore those repeating values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):

                if target - nums[j] in dist:

                    # The items we added are in tuples!
                    ans.add((nums[i], nums[j], target - nums[j]))

                dist[nums[j]] = j

            dist = {}

        # Use map function to map the tuple set to array list.
        # This is a very useful technique.
        return map(list, ans)

# Overall, this question is an extension of 2 Sum!

print Solution().threeSum([-1, 0, 1, 2, -1, -4])