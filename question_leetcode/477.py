def totalHammingDistance(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    bit_status = [[0, 0] for _ in range(32)]
    res = 0

    # 4:  0100
    # 14: 1110
    # 2:  0010
    # --> 2x1 + 1x2 + 1x2 + 3x0 = 6
    # [[3, 0], [1, 2], [1, 2], [2, 1], [3, 0]........

    for num in nums:
        for each_bit in bit_status:
            each_bit[num % 2] += 1
            num /= 2

    for count_zero, count_one in bit_status:
        res += count_zero * count_one

    return res


nums = [4, 14, 2]
print totalHammingDistance(nums)
