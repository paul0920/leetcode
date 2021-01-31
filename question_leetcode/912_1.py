def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    if not nums:
        return nums

    quick_sort(nums, 0, len(nums) - 1)

    return nums


def quick_sort(nums, start, end):
    if start >= end:
        return

    left = start
    right = end
    pivot = nums[(left + right) / 2]

    while left <= right:

        while left <= right and nums[left] < pivot:
            left += 1

        while left <= right and nums[right] > pivot:
            right -= 1

        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    quick_sort(nums, start, right)
    quick_sort(nums, left, end)


nums = [5, 1, 1, 2, 0, 0]
print sortArray(nums)
