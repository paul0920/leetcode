def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    size = 0
    j = 0
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] >= nums[i]:
            j = i

        size = max(size, i - j + 1)

    return size


nums = [1, 3, 5, 4, 7]
print findLengthOfLCIS(nums)
