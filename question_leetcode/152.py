def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    current_max = nums[0]
    current_min = nums[0]
    res_max = nums[0]

    for num in nums[1:]:
        next_max = max(num, current_max * num, current_min * num)
        next_min = min(num, current_max * num, current_min * num)
        current_max = next_max
        current_min = next_min
        res_max = max(res_max, current_max)

    return res_max


nums = [2, 3, -2, 4]
print maxProduct(nums)
