import collections


def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not nums:
        return 0

    sum_to_count = collections.defaultdict(int)
    sum_to_count[0] = 1  # sum = 0 is counted once
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        pre_sum = current_sum - k

        if pre_sum in sum_to_count:
            count += sum_to_count[pre_sum]

        sum_to_count[current_sum] += 1

    return count


nums = [0, 3, -3, 3]
k = 3
# 0
# 0, [0] --> 0: 2

# 0, [3]
# 0, [0, 3] --> count = 2

# 0
# 0, [3, -3]
# 0, [0, 3, -3] --> 0: 3

# 0, [3]
# 0, [3, -3, 3]
# 0, [0, 3, -3, 3] --> count = 2 + 3

print subarraySum(nums, k)
