def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    size = 0
    count = 0
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] >= nums[i]:
            count = 1

        else:
            count += 1

        size = max(size, count)

    return size


nums = [1, 3, 5, 4, 7]
print findLengthOfLCIS(nums)
