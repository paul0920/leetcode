# Time complexity: O(n^2)

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):

            if nums[j] < nums[i]:
                dp[i] = max(dp[j] + 1, dp[i])

            # if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
            #     dp[i] = dp[j] + 1

    # print dp
    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print lengthOfLIS(nums)
