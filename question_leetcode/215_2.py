# Bubble sort algorithm
# Time complexity: O( k(n - (k+1)/2) ); if k = n, O( n(n-1)/2 )
#   Best case: O(n)
#   Worst case: O(n^2)
# Space complexity: O(1)

# If j+1 > j, just swap and so on

# nums = [3, 2, 1, 5, 6, 4]
# k = 2

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4


for i in range(k):
    for j in range(len(nums) - 1 - i):

        print i, j

        if nums[j] > nums[j+1]:

            print nums
            nums[j], nums[j+1] = nums[j+1], nums[j]
            print nums
            print ""

print "the Kth largest:", nums[len(nums)-k]
