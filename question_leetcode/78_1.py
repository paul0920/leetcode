def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]

    i = 0
    queue = [[]]

    while i < len(queue):
        subset = queue[i]
        i += 1

        # No need to sort
        for num in nums:
            if subset and subset[-1] >= num:
                continue

            queue.append(subset + [num])

    return queue


nums = [1, 2, 3]
nums = [3, 2, 1]

print subsets(nums)
