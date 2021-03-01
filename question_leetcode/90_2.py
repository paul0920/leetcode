# BFS

import collections


def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]

    # Need to sort the array first for handling duplicate cases
    nums.sort()
    queue = collections.deque([([], nums)])
    res = []

    while queue:
        subset, candidates = queue.popleft()
        # print id(subset)
        res.append(subset)

        for i, num in enumerate(candidates):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue

            subset.append(num)
            queue.append((list(subset), candidates[i + 1:]))
            subset.pop()

    return res


nums = [1, 2, 3]
nums = [1, 2, 2]
print subsetsWithDup(nums)
