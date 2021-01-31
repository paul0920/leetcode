
nums = [-1, 0, 3, 5, 9, 12]
target = 9

if nums == [] or len(nums) == 0:
    print -1

left, right = 0, len(nums) - 1

# Keep in mind the relationship: <
while left < right:

    mid = (left + right)/2

    print "L:", left, "Mid:", mid, "R:", right

    if nums[mid] < target:

        # Keep in mind: mid + 1
        left = mid + 1

    else:

        # Keep in mind: mid
        right = mid

if nums[left] == target:
    print left
    exit()

# We can either use "left" or "right" to check
# the value
# if nums[right] == target:
#     print right
#     exit()

print -1
