# DFS

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
    res.append(list(path))

    for i in range(index, len(nums)):
        path.append(nums[i])
        dfs(nums, i + 1, path, res)
        path.pop()


nums = [1, 2, 3]
print subsets(nums)
