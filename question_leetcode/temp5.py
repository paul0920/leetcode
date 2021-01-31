def binarySearch_first_b(nums, target):
    # write your code here
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    while left + 1 < right:

        middle = left + (right - left) // 2

        if nums[middle] < target:
            left = middle

        elif nums[middle] == target:
            right = middle

        else:
            right = middle

    if nums[left] == target:
        return left

    if nums[right] == target:
        return right

    return -1
