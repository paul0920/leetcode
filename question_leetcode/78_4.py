def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]

    nums.sort()
    res = []
    dfs(nums, 0, [], res)

    return res


def dfs(nums, index, path, res):
    if index == len(nums):
        res.append(list(path))

        return

    path.append(nums[index])
    dfs(nums, index + 1, path, res)

    path.pop()
    dfs(nums, index + 1, path, res)


nums = [1, 2, 3]
print subsets(nums)
