def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return []

    #    [1, 5, 8, 4, 7, 6, 5, 3, 1]
    #              ^        ^
    # -> [1, 5, 8, 5, 7, 6, 4, 3, 1]
    #                 ^           ^
    # -> [1, 5, 8, 5, 1, 3, 4, 6, 7] (next permutation)

    i = len(nums) - 1
    j = i
    right = i

    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i == 0:
        # Be careful about the value it pointed to before that assignment
        # (your original list) will stay unchanged. Use nums[:] instead
        nums[:] = nums[::-1]

        return

    # i --> 7
    i -= 1

    while nums[i] >= nums[j]:
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]
    left = i + 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]

for _ in range(10):
    print nums
    nextPermutation(nums)
