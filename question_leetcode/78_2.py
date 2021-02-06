def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]

    queue = [[]]
    subset = []

    # Sort nums first
    for num in sorted(nums):
        for i in range(len(queue)):
            # Remember to do deep copy
            subset = queue[i][:]
            subset.append(num)
            queue.append(subset)

    return queue


nums = [1, 2, 3]
nums = [3, 2, 1]

print subsets(nums)
