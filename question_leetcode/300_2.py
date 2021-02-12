# Time complexity: O(n logn)

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    sub = []

    for num in nums:
        index = find_highr_index(sub, num)

        if len(sub) == index:
            sub.append(num)

        else:
            sub[index] = num

    return len(sub)


def find_highr_index(nums, target):
    if not nums:
        return 0

    left = 0
    right = len(nums) - 1

    while left + 1 < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid

        elif nums[mid] == target:
            right = mid

        else:
            right = mid

    if nums[left] >= target:
        return left

    if nums[right] >= target:
        return right

    return len(nums)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print lengthOfLIS(nums)
