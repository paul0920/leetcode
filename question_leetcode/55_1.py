
nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    if len(nums) == 1:
        return True

    for idx in range(len(nums)):

        if idx == len(nums) - 1 or nums[idx] == 0:
            return False
            # break

        for next_step in range(1, nums[idx] + 1):

            if canJump(nums[next_step:]):
                return True

    # return False


print canJump(nums)
