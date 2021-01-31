# 1. You must do this in-place without making a copy of the array.
# 2. Minimize the total number of operations.

nums = [0, 1, 0, 3, 12]

left, right = 0, 0

while right < len(nums):

    if nums[right] != 0:
        nums[left] = nums[right]
        left += 1

    right += 1

while left < len(nums):
    nums[left] = 0
    left += 1

print nums
