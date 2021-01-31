# Selection sort algorithm
# Time complexity: O(n^2)
#   Best case: same
#   Worst case: same
# Space complexity: O(1)

# Find the index of the largest value in the current section
# and swap

nums = [3, 2, 1, 5, 6, 4]
k = 4

# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4


for i in range(len(nums), len(nums)-k, -1):

    idx_max_v = 0

    # search the max value in this section nums[0: i]
    for j in range(i):

        print "i:", i, "j:", j, nums

        if nums[j] > nums[idx_max_v]:
            idx_max_v = j

            print "current index of the max value", idx_max_v

    print "Find the largest value and do swap.", "Swapping index:", idx_max_v, "->", i-1
    # put the largest value in this section to the last of this section
    nums[idx_max_v], nums[i-1] = nums[i-1], nums[idx_max_v]

    print nums
    print ""

print "the Kth largest:", nums[len(nums)-k]
