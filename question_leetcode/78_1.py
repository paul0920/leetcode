# BFS

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]

    nums.sort()
    i = 0
    queue = [[]]

    while i < len(queue):
        subset = queue[i]
        i += 1

        for num in nums:
            if subset and subset[-1] >= num:
                continue

            queue.append(subset + [num])

    return queue


nums = [1, 2, 3]
nums = [3, 2, 1]

print subsets(nums)
