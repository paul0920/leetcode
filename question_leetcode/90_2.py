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
        subset, pool = queue.popleft()
        # print id(subset)
        res.append(subset)

        for i in range(len(pool)):
            if i > 0 and pool[i - 1] == pool[i]:
                continue

            queue.append((subset + [pool[i]], pool[i + 1:]))

    return res


nums = [1, 2, 3]
nums = [1, 3, 2, 1]

print subsetsWithDup(nums)
