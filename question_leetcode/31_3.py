def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # [1, 5, 8, 4, 7, 6, 5, 4, 3, 1, 1]
    #           ^
    # [1, 5, 8, 4, 7, 6, 5, 4, 3, 1, 1]
    #                    ^
    # [1, 5, 8, 5, 7, 6, 4, 4, 3, 1, 1]
    # [1, 5, 8, 5, 1, 1, 3, 4, 4, 6, 7] (next permutation)
    #              ^^^^^^^^^^^^^^^^

    if not nums:
        return []

    right = j = len(nums) - 1

    while right > 0 and nums[right - 1] >= nums[right]:  # Need to use ">="
        right -= 1

    if right == 0:
        # Be careful about the value it pointed to before that assignment
        # (your original list) will stay unchanged. Use nums[:] instead
        nums[:] = nums[::-1]

        return

    right -= 1

    while nums[right] >= nums[j]:  # Need to use ">="
        j -= 1

    nums[right], nums[j] = nums[j], nums[right]
    nums[right + 1:] = nums[right + 1:][::-1]


nums = [1, 5, 8, 4, 7, 6, 5, 4, 3, 1, 1]

for _ in range(10):
    print nums
    nextPermutation(nums)
