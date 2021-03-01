def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]

    nums.sort()
    queue = [[]]

    for num in nums:
        for i in range(len(queue)):
            subset = queue[i] + [num]
            queue.append(subset)

    return queue


nums = [1, 2, 3]
print subsets(nums)
