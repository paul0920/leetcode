import collections


def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums or not k:
        return []

    queue = collections.deque()  # using queue is the key to maintain a window
    res = []

    for i, num in enumerate(nums):
        if queue and i >= queue[0] + k:  # remove the leftmost in the window
            queue.popleft()

        while queue and nums[queue[-1]] <= num:  # maintain the window being monotonic decreasing
            last_index = queue[-1]
            last_num = nums[last_index]

            if last_num <= num:
                queue.pop()

        queue.append(i)

        if i >= k - 1:  # start appending the max number of the existing window
            max_num_index = queue[0]
            res.append(nums[max_num_index])

    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print maxSlidingWindow(nums, k)
