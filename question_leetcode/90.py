def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # Remember to handle empty list
    if not nums:
        return [nums]

    # Need to sort the array first for handling duplicate cases
    nums.sort()
    subset = []
    res = []

    dfs(nums, 0, subset, res)

    return res


def dfs(nums, idx, subset, res):
    # Remember to do deep copy (subset[:])
    res += [subset[:]]

    for i in range(idx, len(nums)):

        # The key statement to skip duplicate cases
        if i > idx and nums[i] == nums[i - 1]:
            continue

        subset += [nums[i]]
        dfs(nums, i + 1, subset, res)
        subset.pop()


nums = [1, 2, 2]
print subsetsWithDup(nums)
