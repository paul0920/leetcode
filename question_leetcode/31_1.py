
nums = [1, 3, 5, 2]
nums = [0, 1, 2, 5, 3, 4]
nums = [0, 1, 2, 5, 4, 3]
# nums = [0, 1, 3, 2, 4, 5]
# nums = [0, 1, 3, 2, 5, 4]
# nums = [0, 1, 3, 4, 2, 5]


i = j = len(nums) - 1

# Remember to include "="!!!
while i > 0 and nums[i - 1] >= nums[i]:
    i -= 1

if i == 0:
    nums.reverse()

    print nums
    exit()

k = i - 1

# Remember to include "="!!!
# Find the next value > nums[k]
while nums[k] >= nums[j]:
    j -= 1

nums[k], nums[j] = nums[j], nums[k]

left = i
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

print nums
