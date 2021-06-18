def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []

    nums = sorted(nums)
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        two_sum(i + 1, len(nums) - 1, nums, 0 - nums[i], res)

    return res


def two_sum(left, right, nums, target, res):
    last_pair = None

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            if (nums[left], nums[right]) != last_pair:
                res.append([-target, nums[left], nums[right]])

            last_pair = (nums[left], nums[right])
            left += 1
            right -= 1

        elif curr_sum > target:
            right -= 1

        else:
            left += 1


nums = [-1, 0, 1, 2, -1, -4]
print threeSum(nums)
