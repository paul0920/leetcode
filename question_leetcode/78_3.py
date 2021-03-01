# BFS

import collections


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]

    nums.sort()
    queue = collections.deque([[]])
    res = []

    while queue:
        subset = queue.popleft()
        res.append(subset)

        for num in nums:
            if subset and subset[-1] >= num:
                continue

            subset.append(num)
            queue.append(list(subset))
            subset.pop()

    return res


nums = [1, 2, 3]
print subsets(nums)
