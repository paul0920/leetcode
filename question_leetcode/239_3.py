# This is a DP solution

nums = [1,3,-1,-3,5,3,6,7]
k = 3

if not nums:
    print []

len_ = len(nums)
block_left_max = [0] * len_
block_right_max = [0] * len_
rst = []

# O(n)
for i in range(0, len_, k):

    # left: start index of current block
    # right: end index of current block

    print len_ - 1, i + k -1

    left, right = i, min(len_ - 1, i + k - 1)

    print left, right
    print ""

    # fill block_left_max from the start of block
    block_left_max[left] = nums[left]

    for j in range(left + 1, right + 1):
        block_left_max[j] = max(block_left_max[j - 1], nums[j])

    # fill block_right_max from the end of block
    block_right_max[right] = nums[right]
    for j in range(right - 1, left - 1, -1):
        block_right_max[j] = max(block_right_max[j + 1], nums[j])

# iterate through nums, O(n)
print block_left_max, "LEFT"
print block_right_max, "RIGHT"

for left in range(0, len_ - k + 1):
    right = left + k - 1

    print left, right

    # situation 1: block_right_max[left] == block_left_max[right]
    # so simply use block_right_max[left] or block_left_max[right]
    if left % k == 0:
        rst.append(block_left_max[right])

    # situation 2: find max between block_right_max and block_left_max
    else:
        rst.append(max(block_right_max[left], block_left_max[right]))

    print rst
    print ""

print rst