
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated more than once.


# nums = [0, 3, 1, 3, 4, 2]
# nums = [3, 1, 3, 4, 2]

# nums = [3, 1, 1, 4, 1, 2]
nums = [1, 3, 4, 2, 2]

low = 1
high = len(nums) - 1

while low < high:

    mid = low + (high - low) / 2
    count = 0

    # This is the core part of the search
    for i in nums:
        if i <= mid:
            count += 1

    print "L =", low, "H =", high, "Mid =", mid, "Count =", count

    if count <= mid:
        low = mid + 1
    else:
        high = mid

print low
