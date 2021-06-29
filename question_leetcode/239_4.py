import heapq


def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums or not k:
        return []

    res = []
    window = []

    for i, num in enumerate(nums):
        heapq.heappush(window, (-num, i))

        if i < k - 1:
            continue

        while window:
            max_num, index = heapq.heappop(window)

            if index <= i - k:
                continue

            heapq.heappush(window, (max_num, index))
            res.append(-max_num)
            break

    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print maxSlidingWindow(nums, k)
