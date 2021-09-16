def permute(nums):
    # write your code here
    if not nums:
        return [[]]

    res = [list(nums)]
    next_nums = next_permutation(nums)

    while next_nums != nums:
        res.append(list(next_nums))
        next_nums = next_permutation(next_nums)

    return res


def next_permutation(prev_nums):
    nums = list(prev_nums)
    right = i = len(nums) - 1

    while right > 0 and nums[right - 1] >= nums[right]:
        right -= 1

    if right == 0:
        return nums[::-1]

    right -= 1

    while nums[right] >= nums[i]:
        i -= 1

    nums[right], nums[i] = nums[i], nums[right]

    return nums[:right + 1] + nums[right + 1:][::-1]


nums = [1, 2, 3]
print permute(nums)
