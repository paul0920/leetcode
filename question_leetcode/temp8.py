def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    size = len(nums)
    dp = [[0] * size for _ in range(size)]

    # Remember such template
    for length in range(3, size + 1):
        for i in range(size - length + 1):
            j = i + length - 1

            # i < k < j
            for k in range(i + 1, j):
                # dp[i][j] is the max number between i and j
                # but doesn't include i and j
                dp[i][j] = max(
                    dp[i][j],
                    dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                )

    # size includes 2 ones at boundaries
    return dp[0][size - 1]


nums = [3, 1, 5, 8]
print maxCoins(nums)
