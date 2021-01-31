nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
      # 0  1  2  3  4  5  6  7  8

left = 0
right = len(nums) - 1

while left < right:

    middle = left + (right - left) / 2

    # print left, right, middle

    if middle % 2 == 1:
        middle -= 1

    # Once middle matches middle + 1, skip these 2 elements
    if nums[middle] == nums[middle + 1]:
        left = middle + 2

    else:
        right = middle

    # print left, right, middle
    # print ""

# Now, left and right both point to the same index
print nums[left]
print nums[right]
