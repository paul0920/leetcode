nums = [1, 2, 2, 4, 5, 5]
target = 5

nums = [1, 2, 2, 4, 5, 5]
    #   0  1  2  3  4  5
target = 2

left = 0
right = len(nums) - 1

while left < right:

    middle = left + (right - left) // 2

    print left, right, middle

    if nums[middle] < target:
        left = middle + 1

    else:
        right = middle
    print left, right, middle
    print ""

if nums[left] == target:
    print left

print -1
