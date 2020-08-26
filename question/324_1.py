
# nums = [1, 2, 3, 4, 5, 6]
nums = [1, 5, 1, 1, 6, 4]

print nums[:5][::-1]

nums.sort()
size = len(nums)

idx = size / 2 - (size + 1) % 2
print idx

a = nums[idx::-1]
b = nums[:idx:-1]

print "****************"
print a
print b
print nums[::2]
print nums[1::2]
print "****************"

nums[::2], nums[1::2] = a, b

print nums

# This is a smart way to arrange index of wiggle sort
# Time complexity: O(n logn)
# Space complexity: O(1)

# 01234
# SSMLL
# nums.sort()
#
# half = len(nums[::2]) - 1
#
# nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
#
# print nums
