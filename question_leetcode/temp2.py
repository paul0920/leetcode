nums = [5, 7, 7, 8, 8, 10]
target = 8


def binary_search_first_pos(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    while left + 1 < right:

        middle = left + (right - left) // 2

        # nums[left] < target <= nums[right]
        if nums[middle] < target:
            left = middle

        else:
            right = middle

    # Check 1) left 2) right
    if nums[left] == target:
        return left

    if nums[right] == target:
        return right

    return -1


def binary_search_last_pos(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    while left + 1 < right:

        middle = left + (right - left) // 2

        # nums[left] <= target < nums[right]
        if nums[middle] <= target:
            left = middle

        else:
            right = middle

    # Check 1) right 2) left
    if nums[right] == target:
        return right

    if nums[left] == target:
        return left

    return -1


print [binary_search_first_pos(nums, target), binary_search_last_pos(nums, target)]
