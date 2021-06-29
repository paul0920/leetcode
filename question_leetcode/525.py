def findMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    count_to_index = {0: -1}
    count = 0
    max_len = 0

    for i, num in enumerate(nums):
        if num == 0:
            count -= 1

        else:
            count += 1

        if count not in count_to_index:
            count_to_index[count] = i

        else:
            max_len = max(max_len, i - count_to_index[count])

    return max_len


nums = [0, 1, 0]
print findMaxLength(nums)
