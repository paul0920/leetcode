
# nums = [1, 2, 3, 4, 5, 6]
nums = [1, 5, 1, 1, 6, 4]

def findMed(nums):
    left, right = -2 ** 31, 2 ** 31
    half_count = float(len(nums)) / 2

    while left <= right:

        mid = (left + right) / 2
        count = 0

        for n in nums:

            if n <= mid:
                count += 1

        if count <= half_count:
            left = mid + 1

        elif count > half_count:
            right = mid - 1

    return left


def partition(nums, pos):
    j = 0

    for i, v in enumerate(nums):
        if v <= pos:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1


median = findMed(nums)

# Do partition twice with using v <= median, v <= median - 1
# to first partition L vs. M & S and then partition against
# M vs. S
# LLMSS -> MSSLL -> SSMLL
partition(nums, median)
partition(nums, median - 1)

half = len(nums[::2]) - 1
nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
