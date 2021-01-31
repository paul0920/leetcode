# Insertion sort algorithm
# Average time complexity: O(n^2)
#   Best case: O(n) (if already sorted)
#   Worst case: O(n^2)
# Space complexity: O(1)

# Move elements of nums[0...i-1], that are greater than key,
# to one position ahead of their current position

nums = [3, 2, 1, 5, 6, 4]
# k = 2


# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4

for i in range(1, len(nums)):

    key = nums[i]
    j = i - 1

    # Ascending order: > key
    # Descending order: < key
    while j >= 0 and nums[j] > key:

        print "i:", "[", i, "]", "key:", key, " ", "j:", "[", j, "]", nums[j], nums
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = key

    print "Shift completed"
    print nums
    print ""


print "the sorted array:", nums
